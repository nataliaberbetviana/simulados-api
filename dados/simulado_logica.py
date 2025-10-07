# Arquivo: dados/simulado_logica.py
# Contém as funções de LÓGICA de verificação e cálculo de pontuação do simulado.
import collections

def normalizar_resposta(resposta):
    """Garante que a resposta seja sempre uma lista para fácil comparação."""
    if isinstance(resposta, str):
        # Se for string (resposta única), transforma em lista
        return [resposta]
    elif resposta is None:
        return []
    # Se já for uma lista (checkbox), retorna a própria lista
    return resposta


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
        
        # Pega a resposta correta e garante que seja uma lista para padronização
        resposta_correta = normalizar_resposta(questao['resposta_correta'])
        
        # Pega a resposta do usuário e garante que seja uma lista
        resposta_usuario = normalizar_resposta(resposta_usuario_raw)
        
        # A comparação de múltiplas respostas exige que as listas sejam idênticas,
        # independentemente da ordem.
        return collections.Counter(resposta_usuario) == collections.Counter(resposta_correta)
        
    except IndexError:
        print(f"Erro de Lógica: Questão {questao_atual} fora do limite do simulado.")
        return False
    except KeyError:
        print("Erro de Dados: Estrutura da questão faltando chaves essenciais.")
        return False


def calcular_pontuacao(resultados_simulado):
    """
    Calcula a pontuação final com base no dicionário de resultados.
    """
    total_questoes = len(resultados_simulado)
    acertos = sum(1 for resultado in resultados_simulado.values() if resultado is True)
    
    if total_questoes == 0:
        return 0.0, 0
        
    percentual = (acertos / total_questoes) * 100
    
    return round(percentual, 1), acertos