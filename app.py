import importlib
from flask import Flask, render_template, request, session, redirect, url_for
from dados.simulados import SIMULADOS_DISPONIVEIS
from dados.simulado_logica import verificar_resposta, calcular_pontuacao
from flask_sqlalchemy import SQLAlchemy
import os
import uuid
from typing import Union, List
from datetime import datetime

# Define a chave secreta para usar as sessões
app = Flask(__name__)

# --- CONFIGURAÇÃO DO BANCO DE DADOS (SQLite) ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a chave secreta para as sessões (obrigatório para usar 'session')
app.secret_key = os.environ.get('SECRET_KEY', str(uuid.uuid4()))

# --- MODELO DO BANCO DE DADOS ---
# Tabela para salvar o histórico de resultados de cada simulado
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
    """
    Formata segundos totais no formato H:MM:SS.
    """
    if total_segundos < 0:
        total_segundos = 0
        
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60

    return f"{horas:01d}:{minutos:02d}:{segundos:02d}"

def carregar_dados_simulado(id_do_simulado):
    """
    Carrega dinamicamente os dados completos de um simulado a partir do seu arquivo.
    """
    simulado_info = next((s for s in SIMULADOS_DISPONIVEIS if s["id"] == id_do_simulado), None)
    if simulado_info is None:
        return None, "Simulado não encontrado!"
    try:
        # Importa o módulo (ex: dados.simulado_1)
        modulo_simulado = importlib.import_module(f"dados.{simulado_info['arquivo']}")
        # Retorna os dados brutos (DADOS_SIMULADO)
        return modulo_simulado.DADOS_SIMULADO, None
    except (ImportError, AttributeError):
        return None, f"Erro ao carregar dados do arquivo {simulado_info['arquivo']}.py."
        
def pegar_resposta_do_form(questao_data, questao_index) -> Union[str, List[str], None]:
    """
    Determina o tipo de resposta (única ou múltipla) e extrai do formulário.
    """
    if questao_data.get('tipo') == 'multipla_resposta':
        # Se for checkbox, o nome do campo é dinâmico (ex: resposta_0)
        campo_nome = f'resposta_{questao_index}'
        # request.form.getlist é usado para capturar todos os valores de um checkbox
        return request.form.getlist(campo_nome)
    else:
        # Se for radio, o nome do campo é 'resposta'
        return request.form.get('resposta')


# --- ROTAS PRINCIPAIS ---

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('home.html')

# Rota para o índice de simulados (lista de opções)
@app.route('/simulados')
def simulados():
    return render_template('simulados.html', simulados_disponiveis=SIMULADOS_DISPONIVEIS)

# Rota dinâmica para fazer um simulado específico
@app.route('/simulado/<int:id_do_simulado>', methods=['GET'])
def fazer_simulado(id_do_simulado):
    simulado_data, erro = carregar_dados_simulado(id_do_simulado)
    if erro:
        return erro, 404
    # 1. Gerenciamento de sessão e estado (inicia o simulado)
    simulado_key = f'simulado_{id_do_simulado}_progresso'
    if simulado_key not in session:
        # Inicializa a sessão, incluindo o tempo gasto
        session[simulado_key] = {'acertos': {}, 'questao_atual': 0, 'tempo_gasto': 0}
        
    progresso = session[simulado_key]
    
    # Obtém o índice da questão atual
    questao_index = progresso['questao_atual']
    
    # 2. Verifica se o simulado já terminou
    if questao_index >= len(simulado_data['questoes']):
        return redirect(url_for('finalizar_simulado', id_do_simulado=id_do_simulado))

    # 3. Exibe a questão atual
    questao_data = simulado_data['questoes'][questao_index]
    
    # 4. Envia o tempo gasto acumulado para o template
    tempo_gasto_previamente = progresso.get('tempo_gasto', 0)
    
    return render_template('fazer_simulado.html', 
                           simulado=simulado_data,
                           questao=questao_data,
                           questao_index=questao_index,
                           total_questoes=len(simulado_data['questoes']),
                           id_simulado=id_do_simulado,
                           tempo_gasto_previamente=tempo_gasto_previamente)

# Rota para processar a resposta do usuário (POST)
@app.route('/processar_simulado/<int:id_do_simulado>', methods=['POST'])
def processar_simulado(id_do_simulado):
    simulado_data, erro = carregar_dados_simulado(id_do_simulado)
    if erro:
        return erro, 404
    simulado_key = f'simulado_{id_do_simulado}_progresso'
    progresso = session.get(simulado_key, {'acertos': {}, 'questao_atual': 0, 'tempo_gasto': 0})
    
    questao_index = progresso['questao_atual']
    
    # NOVO: Usa a função auxiliar para pegar a resposta correta (string ou lista)
    questao_data = simulado_data['questoes'][questao_index]
    resposta_usuario_raw = pegar_resposta_do_form(questao_data, questao_index)
    
    try:
        tempo_total_gasto = int(request.form.get('tempo_decorrido', 0))
    except ValueError:
        tempo_total_gasto = progresso.get('tempo_gasto', 0) # Usa o valor anterior se falhar

    # Verifica se o usuário selecionou alguma coisa (obrigatório)
    if not resposta_usuario_raw or (isinstance(resposta_usuario_raw, list) and not resposta_usuario_raw):
        return redirect(url_for('fazer_simulado', id_do_simulado=id_do_simulado))

    # Executa a Lógica de Verificação (agora compatível com listas)
    acertou = verificar_resposta(simulado_data, questao_index, resposta_usuario_raw)
    
    progresso['acertos'][str(questao_index)] = acertou
    progresso['questao_atual'] += 1 
    progresso['tempo_gasto'] = tempo_total_gasto
    session[simulado_key] = progresso

    if progresso['questao_atual'] >= len(simulado_data['questoes']):
        return redirect(url_for('finalizar_simulado', id_do_simulado=id_do_simulado))
    else:
        return redirect(url_for('fazer_simulado', id_do_simulado=id_do_simulado))

# Rota para a tela final (resultado)
@app.route('/finalizar_simulado/<int:id_do_simulado>')
def finalizar_simulado(id_do_simulado):
    simulado_data, erro = carregar_dados_simulado(id_do_simulado)
    simulado_info = next((s for s in SIMULADOS_DISPONIVEIS if s["id"] == id_do_simulado), None)

    simulado_key = f'simulado_{id_do_simulado}_progresso'
    progresso = session.pop(simulado_key, None) 
    if progresso is None:
        return redirect(url_for('simulados'))

    percentual, acertos = calcular_pontuacao(progresso['acertos'])
    tempo_final_segundos = progresso.get('tempo_gasto', 0)
    tempo_final_formatado = formatar_tempo(tempo_final_segundos)
    
    # --- SALVAR NO BANCO DE DADOS ---
    novo_resultado = ResultadoSimulado(
        simulado_id=id_do_simulado,
        titulo=simulado_info['titulo'] if simulado_info else "Simulado Desconhecido",
        percentual=percentual,
        acertos=acertos,
        total_questoes=len(progresso['acertos']),
        tempo_gasto_segundos=tempo_final_segundos
    )
    
    try:
        db.session.add(novo_resultado)
        db.session.commit()
    except Exception as e:
        # Em caso de erro (ex: banco não criado), imprime no console
        print(f"Erro ao salvar resultado no DB: {e}")
        db.session.rollback()

    return render_template('resultado.html',
                           percentual=percentual,
                           acertos=acertos,
                           total=len(progresso['acertos']),
                           tempo_final_formatado=tempo_final_formatado)


# Rota de materiais
@app.route('/materiais')
def materiais():
    return render_template('materiais.html')

# Rota de links
@app.route('/links')
def links():
    return render_template('links.html')

# Rota de histórico (busca no banco de dados)
@app.route('/historico')
def historico():
    # Busca todos os resultados salvos, ordenados por data de conclusão
    with app.app_context():
        resultados = ResultadoSimulado.query.order_by(ResultadoSimulado.data_conclusao.desc()).all()
    
    # --- CÁLCULO DE DESEMPENHO GERAL ---
    maior_nota = 0.0
    media_pontuacao = 0.0
    
    if resultados:
        pontuacoes = [r.percentual for r in resultados]
        maior_nota = round(max(pontuacoes), 1)
        media_pontuacao = round(sum(pontuacoes) / len(pontuacoes), 1)
    # ------------------------------------

    # Formata o tempo de cada resultado antes de enviar para o template
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
                           media_pontuacao=media_pontuacao)


# ROTA DE ADMINISTRAÇÃO PARA RESETAR O BANCO DE DADOS
@app.route('/resetar-historico')
def resetar_historico():
    """Apaga todas as tabelas e as recria (reset completo do histórico)."""
    try:
        with app.app_context():
            db.drop_all()
            db.create_all()
        return redirect(url_for('historico')) # Redireciona de volta para a página de histórico limpa
    except Exception as e:
        return f"Erro ao resetar o banco de dados: {e}", 500


# --- EXECUÇÃO PRINCIPAL ---

if __name__ == '__main__':
    # Cria o contexto de aplicação e o banco de dados se não existir
    if not os.path.exists('site.db'):
        with app.app_context():
            db.create_all()
            print("Banco de dados 'site.db' criado com sucesso!")

    if 'SECRET_KEY' not in os.environ:
        print("AVISO: Usando chave secreta aleatória para desenvolvimento.")
    
    app.run(debug=True)