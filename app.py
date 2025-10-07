import importlib
from flask import Flask, render_template, request, session, redirect, url_for
from dados.simulados import SIMULADOS_DISPONIVEIS
import os
import uuid

# Define a chave secreta para usar as sessões
# Isso é obrigatório para usar 'session'
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', str(uuid.uuid4()))

# --- ROTAS PRINCIPAIS ---

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('home.html')

# Rota para o índice de simulados (lista de opções)
@app.route('/simulados')
def simulados():
    # Envia a lista de índice para o template (simulados.html)
    return render_template('simulados.html', simulados_disponiveis=SIMULADOS_DISPONIVEIS)

# Rota dinâmica para fazer um simulado específico
@app.route('/simulado/<int:id_do_simulado>', methods=['GET'])
def fazer_simulado(id_do_simulado):
    # 1. Encontra o simulado no índice (dados/simulados.py)
    simulado_info = next((s for s in SIMULADOS_DISPONIVEIS if s["id"] == id_do_simulado), None)

    if simulado_info is None:
        return "Simulado não encontrado!", 404

    try:
        # 2. IMPORTA O MÓDULO CORRETO DINAMICAMENTE
        # Ex: importa o módulo 'dados.simulado_1'
        modulo_simulado = importlib.import_module(f"dados.{simulado_info['arquivo']}")
        
        # 3. Pega os dados brutos (DADOS_SIMULADO) de dentro do módulo
        simulado_data = modulo_simulado.DADOS_SIMULADO
        
    except ImportError:
        return f"Erro: Arquivo de dados para o simulado {id_do_simulado} não encontrado.", 500
    except AttributeError:
        return f"Erro: Variável DADOS_SIMULADO não encontrada no arquivo {simulado_info['arquivo']}.py.", 500

    # Por enquanto, apenas exibimos o título e as questões para teste
    return render_template('fazer_simulado.html', simulado=simulado_data)

# Rota de materiais
@app.route('/materiais')
def materiais():
    return render_template('materiais.html')

# Rota de links
@app.route('/links')
def links():
    return render_template('links.html')

# Rota de histórico
@app.route('/historico')
def historico():
    # Futuramente, você passará o histórico salvo aqui
    return render_template('historico.html')

if __name__ == '__main__':
    app.run(debug=True)