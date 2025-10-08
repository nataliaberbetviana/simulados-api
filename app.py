import random
import importlib
from flask import Flask, render_template, request, session, redirect, url_for
from dados.simulados import SIMULADOS_DISPONIVEIS
from dados.simulado_logica import verificar_resposta, calcular_pontuacao, gerar_questoes_nao_pontuadas
from flask_sqlalchemy import SQLAlchemy
import os
import uuid
from typing import Union, List
from datetime import datetime

app = Flask(__name__)

# --- CONFIGURAÇÃO DO BANCO DE DADOS (SQLite) ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.secret_key = os.environ.get('SECRET_KEY', str(uuid.uuid4()))

# --- MODELO DO BANCO DE DADOS ---
class ResultadoSimulado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    simulado_id = db.Column(db.Integer, nullable=False)
    titulo = db.Column(db.String(100), nullable=False)
    percentual = db.Column(db.Float, nullable=False)
    acertos = db.Column(db.Integer, nullable=False)
    total_questoes = db.Column(db.Integer, nullable=False)
    tempo_gasto_segundos = db.Column(db.Integer, nullable=False)
    data_conclusao = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Resultado(Simulado ID: {self.simulado_id}, Pontuação: {self.percentual}%)"

# --- FUNÇÕES AUXILIARES ---

def formatar_tempo(total_segundos):
    """Formata segundos totais no formato H:MM:SS."""
    if total_segundos < 0:
        total_segundos = 0
        
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60

    return f"{horas:01d}:{minutos:02d}:{segundos:02d}"

def carregar_dados_simulado(id_do_simulado):
    """Carrega dinamicamente os dados completos de um simulado a partir do seu arquivo."""
    simulado_info = next((s for s in SIMULADOS_DISPONIVEIS if s["id"] == id_do_simulado), None)
    if simulado_info is None:
        return None, "Simulado não encontrado!"
    try:
        modulo_simulado = importlib.import_module(f"dados.{simulado_info['arquivo']}")
        return modulo_simulado.DADOS_SIMULADO, None
    except (ImportError, AttributeError):
        return None, f"Erro ao carregar dados do arquivo {simulado_info['arquivo']}.py."
        
def pegar_resposta_do_form(questao_data, questao_index) -> Union[str, List[str], None]:
    """Determina o tipo de resposta (única ou múltipla) e extrai do formulário."""
    if questao_data.get('tipo') == 'multipla_resposta':
        campo_nome = f'resposta_{questao_index}'
        return request.form.getlist(campo_nome)
    else:
        return request.form.get('resposta')

def embaralhar_opcoes(questao):
    """Embaralha as opções de uma questão mantendo a resposta correta rastreável."""
    questao_embaralhada = questao.copy()
    opcoes = questao['opcoes'].copy()
    random.shuffle(opcoes)
    questao_embaralhada['opcoes'] = opcoes
    return questao_embaralhada

def embaralhar_questoes(simulado_data):
    """Embaralha a ordem das questões do simulado."""
    simulado_embaralhado = simulado_data.copy()
    questoes = simulado_data['questoes'].copy()
    random.shuffle(questoes)
    simulado_embaralhado['questoes'] = questoes
    return simulado_embaralhado

def inicializar_simulado_embaralhado(id_do_simulado):
    """Carrega o simulado, embaralha questões e opções, e salva na sessão."""
    simulado_data, erro = carregar_dados_simulado(id_do_simulado)
    if erro:
        return None, erro
    
    # Embaralha a ordem das questões
    simulado_embaralhado = embaralhar_questoes(simulado_data)
    
    # Embaralha as opções de cada questão
    for i in range(len(simulado_embaralhado['questoes'])):
        simulado_embaralhado['questoes'][i] = embaralhar_opcoes(simulado_embaralhado['questoes'][i])
    
    # Salva o simulado embaralhado na sessão
    simulado_key = f'simulado_{id_do_simulado}_data'
    session[simulado_key] = simulado_embaralhado
    
    return simulado_embaralhado, None


# --- ROTAS PRINCIPAIS ---

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/simulados')
def simulados():
    return render_template('simulados.html', simulados_disponiveis=SIMULADOS_DISPONIVEIS)

@app.route('/simulado/<int:id_do_simulado>', methods=['GET'])
def fazer_simulado(id_do_simulado):
    simulado_key = f'simulado_{id_do_simulado}_progresso'
    simulado_data_key = f'simulado_{id_do_simulado}_data'
    
    if simulado_key not in session:
        # Primeira vez acessando, inicializa e embaralha
        simulado_embaralhado, erro = inicializar_simulado_embaralhado(id_do_simulado)
        if erro:
            return erro, 404
        
        # Gera as questões não pontuadas aleatoriamente
        total_questoes = len(simulado_embaralhado['questoes'])
        questoes_nao_pontuadas = gerar_questoes_nao_pontuadas(total_questoes, 15)
        
        session[simulado_key] = {
            'acertos': {},
            'questao_atual': 0,
            'tempo_gasto': 0,
            'questoes_nao_pontuadas': list(questoes_nao_pontuadas)
        }
    else:
        # Usa o simulado embaralhado já salvo na sessão
        simulado_embaralhado = session.get(simulado_data_key)
        if not simulado_embaralhado:
            simulado_embaralhado, erro = inicializar_simulado_embaralhado(id_do_simulado)
            if erro:
                return erro, 404
        
    progresso = session[simulado_key]
    questao_index = progresso['questao_atual']
    
    if questao_index >= len(simulado_embaralhado['questoes']):
        return redirect(url_for('finalizar_simulado', id_do_simulado=id_do_simulado))

    questao_data = simulado_embaralhado['questoes'][questao_index]
    tempo_gasto_previamente = progresso.get('tempo_gasto', 0)
    
    # Verifica se a questão atual é pontuada
    questao_pontuada = questao_index not in progresso['questoes_nao_pontuadas']
    
    return render_template('fazer_simulado.html', 
                           simulado=simulado_embaralhado,
                           questao=questao_data,
                           questao_index=questao_index,
                           total_questoes=len(simulado_embaralhado['questoes']),
                           id_simulado=id_do_simulado,
                           tempo_gasto_previamente=tempo_gasto_previamente,
                           questao_pontuada=questao_pontuada)


@app.route('/processar_simulado/<int:id_do_simulado>', methods=['POST'])
def processar_simulado(id_do_simulado):
    simulado_data_key = f'simulado_{id_do_simulado}_data'
    simulado_data = session.get(simulado_data_key)
    
    if not simulado_data:
        return "Erro: Simulado não encontrado na sessão", 404
    
    simulado_key = f'simulado_{id_do_simulado}_progresso'
    progresso = session.get(simulado_key, {
        'acertos': {},
        'questao_atual': 0,
        'tempo_gasto': 0,
        'questoes_nao_pontuadas': []
    })
    
    # Verifica se já viu a explicação
    ja_respondeu = request.form.get('ja_respondeu')
    
    if ja_respondeu == 'true':
        progresso['questao_atual'] += 1
        session[simulado_key] = progresso
        
        if progresso['questao_atual'] >= len(simulado_data['questoes']):
            return redirect(url_for('finalizar_simulado', id_do_simulado=id_do_simulado))
        else:
            return redirect(url_for('fazer_simulado', id_do_simulado=id_do_simulado))
    
    questao_index = progresso['questao_atual']
    questao_data = simulado_data['questoes'][questao_index]
    resposta_usuario_raw = pegar_resposta_do_form(questao_data, questao_index)
    
    try:
        tempo_total_gasto = int(request.form.get('tempo_decorrido', 0))
    except ValueError:
        tempo_total_gasto = progresso.get('tempo_gasto', 0)
    
    if not resposta_usuario_raw or (isinstance(resposta_usuario_raw, list) and not resposta_usuario_raw):
        return redirect(url_for('fazer_simulado', id_do_simulado=id_do_simulado))
    
    acertou = verificar_resposta(simulado_data, questao_index, resposta_usuario_raw)
    
    progresso['acertos'][str(questao_index)] = acertou
    progresso['tempo_gasto'] = tempo_total_gasto
    session[simulado_key] = progresso
    
    if isinstance(resposta_usuario_raw, list):
        resposta_formatada = ', '.join(resposta_usuario_raw)
    else:
        resposta_formatada = resposta_usuario_raw
    
    # Verifica se a questão é pontuada
    questao_pontuada = questao_index not in progresso['questoes_nao_pontuadas']
    
    return render_template('explicacao.html',
                          questao=questao_data,
                          questao_numero=questao_index + 1,
                          total_questoes=len(simulado_data['questoes']),
                          acertou=acertou,
                          resposta_usuario=resposta_formatada,
                          id_simulado=id_do_simulado,
                          questao_index=questao_index,
                          tempo_decorrido=tempo_total_gasto,
                          questao_pontuada=questao_pontuada)


@app.route('/finalizar_simulado/<int:id_do_simulado>')
def finalizar_simulado(id_do_simulado):
    simulado_data_key = f'simulado_{id_do_simulado}_data'
    simulado_data = session.get(simulado_data_key)
    
    simulado_info = next((s for s in SIMULADOS_DISPONIVEIS if s["id"] == id_do_simulado), None)

    simulado_key = f'simulado_{id_do_simulado}_progresso'
    progresso = session.pop(simulado_key, None)
    session.pop(simulado_data_key, None)
    
    if progresso is None:
        return redirect(url_for('simulados'))

    # Converte lista para set
    questoes_nao_pontuadas = set(progresso.get('questoes_nao_pontuadas', []))
    
    # Calcula pontuação considerando apenas questões pontuadas
    percentual, acertos, total_pontuadas = calcular_pontuacao(
        progresso['acertos'],
        questoes_nao_pontuadas
    )
    
    tempo_final_segundos = progresso.get('tempo_gasto', 0)
    tempo_final_formatado = formatar_tempo(tempo_final_segundos)
    
    novo_resultado = ResultadoSimulado(
        simulado_id=id_do_simulado,
        titulo=simulado_info['titulo'] if simulado_info else "Simulado Desconhecido",
        percentual=percentual,
        acertos=acertos,
        total_questoes=total_pontuadas,
        tempo_gasto_segundos=tempo_final_segundos
    )
    
    try:
        db.session.add(novo_resultado)
        db.session.commit()
    except Exception as e:
        print(f"Erro ao salvar resultado no DB: {e}")
        db.session.rollback()

    return render_template('resultado.html',
                           percentual=percentual,
                           acertos=acertos,
                           total=total_pontuadas,
                           tempo_final_formatado=tempo_final_formatado)

@app.route('/materiais')
def materiais():
    return render_template('materiais.html')

@app.route('/links')
def links():
    return render_template('links.html')

@app.route('/historico')
def historico():
    with app.app_context():
        resultados = ResultadoSimulado.query.order_by(ResultadoSimulado.data_conclusao.desc()).all()
    
    maior_nota = 0.0
    media_pontuacao = 0.0
    media_tempo_gasto = "00:00:00"
    
    if resultados:
        pontuacoes = [r.percentual for r in resultados]
        tempos_gasto = [r.tempo_gasto_segundos for r in resultados]
        
        maior_nota = round(max(pontuacoes), 1)
        media_pontuacao = round(sum(pontuacoes) / len(pontuacoes), 1)
        
        total_segundos_acumulados = sum(tempos_gasto)
        media_segundos = round(total_segundos_acumulados / len(resultados))
        media_tempo_gasto = formatar_tempo(media_segundos)

    historico_formatado = [{
        'titulo': r.titulo,
        'percentual': r.percentual,
        'acertos': r.acertos,
        'total': r.total_questoes,
        'tempo_formatado': formatar_tempo(r.tempo_gasto_segundos),
        'data': r.data_conclusao.strftime('%d/%m/%Y %H:%M')
    } for r in resultados]
    
    return render_template('historico.html', 
                           historico=historico_formatado,
                           maior_nota=maior_nota,
                           media_pontuacao=media_pontuacao,
                           media_tempo_gasto=media_tempo_gasto)


@app.route('/resetar-historico')
def resetar_historico():
    """Apaga todas as tabelas e as recria (reset completo do histórico)."""
    try:
        with app.app_context():
            db.drop_all()
            db.create_all()
        return redirect(url_for('historico'))
    except Exception as e:
        return f"Erro ao resetar o banco de dados: {e}", 500


if __name__ == '__main__':
    if not os.path.exists('site.db'):
        with app.app_context():
            db.create_all()
            print("Banco de dados 'site.db' criado com sucesso!")

    if 'SECRET_KEY' not in os.environ:
        print("AVISO: Usando chave secreta aleatória para desenvolvimento.")
    
    app.run(debug=True)