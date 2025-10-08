# Arquivo: dados/simulado_logica.py
# Contém as funções de LÓGICA de verificação e cálculo de pontuação do simulado.
import collections
import random

def normalizar_resposta(resposta):
    """Garante que a resposta seja sempre uma lista para fácil comparação."""
    if isinstance(resposta, str):
        return [resposta]
    elif resposta is None:
        return []
    return resposta


def gerar_questoes_nao_pontuadas(total_questoes, quantidade_nao_pontuadas=15):
    """
    Gera aleatoriamente os índices das questões que NÃO serão pontuadas.
    
    Args:
        total_questoes (int): Total de questões do simulado (ex: 65)
        quantidade_nao_pontuadas (int): Quantas questões não devem pontuar (ex: 15)
    
    Returns:
        set: Conjunto com os índices (base 0) das questões não pontuadas
    """
    if quantidade_nao_pontuadas >= total_questoes:
        return set()
    
    indices = list(range(total_questoes))
    nao_pontuadas = random.sample(indices, quantidade_nao_pontuadas)
    return set(nao_pontuadas)


def verificar_resposta(simulado_data, questao_atual, resposta_usuario_raw):
    """
    Verifica se a resposta do usuário (múltipla ou única) está correta.

    Args:
        simulado_data (dict): Dicionário completo com os dados do simulado.
        questao_atual (int): Índice (base 0) da questão.
        resposta_usuario_raw (str/list): A resposta(s) recebida(s) do Flask.

    Returns:
        bool: True se a resposta estiver correta, False caso contrário.
    """
    try:
        questao = simulado_data['questoes'][questao_atual]
        resposta_correta = normalizar_resposta(questao['resposta_correta'])
        resposta_usuario = normalizar_resposta(resposta_usuario_raw)
        
        return collections.Counter(resposta_usuario) == collections.Counter(resposta_correta)
        
    except IndexError:
        print(f"Erro de Lógica: Questão {questao_atual} fora do limite do simulado.")
        return False
    except KeyError:
        print("Erro de Dados: Estrutura da questão faltando chaves essenciais.")
        return False


def calcular_pontuacao(resultados_simulado, questoes_nao_pontuadas=None):
    """
    Calcula a pontuação final considerando apenas as questões pontuadas.
    
    Args:
        resultados_simulado (dict): Dicionário com índices e resultados (True/False)
        questoes_nao_pontuadas (set): Conjunto com índices das questões não pontuadas
    
    Returns:
        tuple: (percentual, acertos_pontuados, total_pontuadas)
    """
    if questoes_nao_pontuadas is None:
        questoes_nao_pontuadas = set()
    
    total_questoes = len(resultados_simulado)
    
    # Filtra apenas as questões que são pontuadas
    acertos_pontuados = 0
    total_pontuadas = 0
    
    for indice_str, acertou in resultados_simulado.items():
        indice = int(indice_str)
        
        # Se a questão NÃO está no conjunto de não pontuadas, ela conta
        if indice not in questoes_nao_pontuadas:
            total_pontuadas += 1
            if acertou:
                acertos_pontuados += 1
    
    if total_pontuadas == 0:
        return 0.0, 0, 0
        
    percentual = (acertos_pontuados / total_pontuadas) * 100
    
    return round(percentual, 1), acertos_pontuados, total_pontuadas