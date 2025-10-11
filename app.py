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
        
def pegar_resposta_do_form(questao_data, questao_index_sequencial) -> Union[str, List[str], None]:
    """Determina o tipo de resposta (única ou múltipla) e extrai do formulário.
    Usa o índice sequencial para nomear o campo no caso de múltipla resposta."""
    if questao_data.get('multipla_escolha'):
        campo_nome = f'resposta_{questao_index_sequencial}'
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

def inicializar_simulado_embaralhado(id_do_simulado):
    """Carrega o simulado, embaralha os índices das questões e salva o MAPA na sessão."""
    simulado_data_completo, erro = carregar_dados_simulado(id_do_simulado)
    if erro:
        return None, erro
    
    indices_originais = list(range(len(simulado_data_completo['questoes'])))
    random.shuffle(indices_originais)
    
    simulado_map_key = f'simulado_{id_do_simulado}_data_map'
    session[simulado_map_key] = {
        'titulo': simulado_data_completo['titulo'],
        'ordem_questoes': indices_originais,
    }
    session.modified = True
    
    print(f"DEBUG: Simulado {id_do_simulado} (DATA MAP) inicializado e salvo na sessão. (TAMANHO REDUZIDO)")
    
    return simulado_data_completo, None


# --- ROTAS PRINCIPAIS ---
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/simulados')
def simulados():
    return render_template('simulados.html', simulados_disponiveis=SIMULADOS_DISPONIVEIS)

@app.route('/materiais')
def materiais():
    return render_template('materiais.html')

@app.route('/servicos_aws')
def servicos_aws():
    return render_template('servicos_aws.html')

@app.route('/ec2')
def ec2():
    return render_template('ec2.html')

@app.route('/s3')
def s3():
    return render_template('s3.html')

@app.route('/vpc')
def vpc():
    return render_template('vpc.html')

@app.route('/iam')
def iam():
    return render_template('iam.html')

@app.route('/cloud_trail')
def cloud_trail():
    return render_template('cloud_trail.html')

@app.route('/config')
def config():
    return render_template('config.html')

@app.route('/trusted_advisor')
def trusted_advisor():
    return render_template('trusted_advisor.html')

@app.route('/praticas_recomendadas')
def praticas_recomendadas():
    return render_template('praticas_recomendadas.html')

@app.route('/conformidade')
def conformidade():
    return render_template('conformidade.html')

@app.route('/recursos_seguranca')
def recursos_seguranca():
    return render_template('recursos_seguranca.html')

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

@app.route('/simulado/<int:id_do_simulado>', methods=['GET'])
def fazer_simulado(id_do_simulado):
    simulado_key = f'simulado_{id_do_simulado}_progresso'
    simulado_map_key = f'simulado_{id_do_simulado}_data_map'
    
    simulado_data_completo, erro_data = carregar_dados_simulado(id_do_simulado)
    if erro_data:
        return erro_data, 404

    simulado_map = session.get(simulado_map_key)
    
    if not simulado_map:
        _, erro = inicializar_simulado_embaralhado(id_do_simulado)
        if erro:
            return erro, 404
        simulado_map = session.get(simulado_map_key)

    if simulado_key not in session:
        total_questoes = len(simulado_map['ordem_questoes'])
        questoes_nao_pontuadas = gerar_questoes_nao_pontuadas(total_questoes, 15)
        
        session[simulado_key] = {
            'acertos': {},
            'questao_atual': 0,
            'tempo_gasto': 0,
            'questoes_nao_pontuadas': list(questoes_nao_pontuadas)
        }
        session.modified = True
        print(f"DEBUG: Progresso do Simulado {id_do_simulado} (PROGRESSO) inicializado.")
    
    progresso = session[simulado_key]
    questao_index_sequencial = progresso['questao_atual']
    
    if questao_index_sequencial >= len(simulado_map['ordem_questoes']):
        return redirect(url_for('finalizar_simulado', id_do_simulado=id_do_simulado))

    indice_original_da_questao = simulado_map['ordem_questoes'][questao_index_sequencial]
    questao_data_original = simulado_data_completo['questoes'][indice_original_da_questao]
    questao_data_embaralhada = embaralhar_opcoes(questao_data_original)
    
    tempo_gasto_previamente = progresso.get('tempo_gasto', 0)
    questao_pontuada = questao_index_sequencial not in progresso['questoes_nao_pontuadas']

    print(f"DEBUG: Carregando Questão {questao_index_sequencial + 1} (Original Index: {indice_original_da_questao}). Tempo acumulado: {tempo_gasto_previamente}s")
    
    return render_template('fazer_simulado.html', 
                           simulado={'titulo': simulado_map['titulo']},
                           questao=questao_data_embaralhada,
                           questao_index=questao_index_sequencial,
                           total_questoes=len(simulado_map['ordem_questoes']),
                           id_simulado=id_do_simulado,
                           tempo_gasto_previamente=tempo_gasto_previamente,
                           questao_pontuada=questao_pontuada)


@app.route('/processar_simulado/<int:id_do_simulado>', methods=['POST'])
def processar_simulado(id_do_simulado):
    simulado_map_key = f'simulado_{id_do_simulado}_data_map'
    simulado_map = session.get(simulado_map_key)
    
    if not simulado_map:
        _, erro = inicializar_simulado_embaralhado(id_do_simulado)
        if erro:
            return f"Erro: Simulado não encontrado na sessão. {erro}", 404
        simulado_map = session.get(simulado_map_key)
    
    simulado_data_completo, erro_data = carregar_dados_simulado(id_do_simulado)
    if erro_data:
        return erro_data, 404
    
    simulado_key = f'simulado_{id_do_simulado}_progresso'
    progresso = session.get(simulado_key, {
        'acertos': {},
        'questao_atual': 0,
        'tempo_gasto': 0,
        'questoes_nao_pontuadas': []
    })
    
    ja_respondeu = request.form.get('ja_respondeu')
    
    if ja_respondeu == 'true':
        progresso['questao_atual'] += 1
        
        session[simulado_key] = progresso
        session.modified = True
        
        print(f"DEBUG: AVANÇANDO. Novo índice: {progresso['questao_atual']}. Tempo total salvo: {progresso['tempo_gasto']}s")
        
        if progresso['questao_atual'] >= len(simulado_map['ordem_questoes']):
            return redirect(url_for('finalizar_simulado', id_do_simulado=id_do_simulado))
        else:
            return redirect(url_for('fazer_simulado', id_do_simulado=id_do_simulado))
    
    questao_index_sequencial = progresso['questao_atual']
    indice_original_da_questao = simulado_map['ordem_questoes'][questao_index_sequencial]
    questao_data_original = simulado_data_completo['questoes'][indice_original_da_questao]
    
    resposta_usuario_raw = pegar_resposta_do_form(questao_data_original, questao_index_sequencial)
    
    try:
        tempo_total_gasto = int(request.form.get('tempo_decorrido', 0))
    except ValueError:
        tempo_total_gasto = progresso.get('tempo_gasto', 0)
    
    if not resposta_usuario_raw or (isinstance(resposta_usuario_raw, list) and not resposta_usuario_raw):
        return redirect(url_for('fazer_simulado', id_do_simulado=id_do_simulado))
    
    acertou = verificar_resposta(simulado_data_completo, indice_original_da_questao, resposta_usuario_raw)
    
    progresso['acertos'][str(questao_index_sequencial)] = acertou
    progresso['tempo_gasto'] = tempo_total_gasto
    session[simulado_key] = progresso
    session.modified = True
    
    print(f"DEBUG: RESPOSTA PROCESSADA (Questão {questao_index_sequencial + 1}). Tempo total salvo: {tempo_total_gasto}s")
    
    if isinstance(resposta_usuario_raw, list):
        resposta_formatada = ', '.join(resposta_usuario_raw)
    else:
        resposta_formatada = resposta_usuario_raw
    
    questao_pontuada = questao_index_sequencial not in progresso['questoes_nao_pontuadas']
    
    return render_template('explicacao.html',
                          questao=questao_data_original,
                          questao_numero=questao_index_sequencial + 1,
                          total_questoes=len(simulado_map['ordem_questoes']),
                          acertou=acertou,
                          resposta_usuario=resposta_formatada,
                          id_simulado=id_do_simulado,
                          questao_index=questao_index_sequencial,
                          tempo_decorrido=tempo_total_gasto,
                          questao_pontuada=questao_pontuada)


@app.route('/finalizar_simulado/<int:id_do_simulado>')
def finalizar_simulado(id_do_simulado):
    simulado_map_key = f'simulado_{id_do_simulado}_data_map'
    simulado_map = session.get(simulado_map_key)
    
    simulado_info = next((s for s in SIMULADOS_DISPONIVEIS if s["id"] == id_do_simulado), None)

    simulado_key = f'simulado_{id_do_simulado}_progresso'
    progresso = session.pop(simulado_key, None)
    session.pop(simulado_map_key, None)
    
    if progresso is None:
        return redirect(url_for('simulados'))

    questoes_nao_pontuadas = set(progresso.get('questoes_nao_pontuadas', []))
    
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

    print(f"DEBUG: Simulado {id_do_simulado} FINALIZADO. Pontuação: {percentual}%. Tempo total: {tempo_final_segundos}s")
    
    return render_template('resultado.html',
                           percentual=percentual,
                           acertos=acertos,
                           total=total_pontuadas,
                           tempo_final_formatado=tempo_final_formatado)


if __name__ == '__main__':
    if not os.path.exists('site.db'):
        with app.app_context():
            db.create_all()
            print("Banco de dados 'site.db' criado com sucesso!")

    if 'SECRET_KEY' not in os.environ:
        print("AVISO: Usando chave secreta aleatória para desenvolvimento.")
    
    app.run(debug=True)