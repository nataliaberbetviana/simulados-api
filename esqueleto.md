# Qual o problema?
Um aplicativo para facilitar o estudo da certificação AWS Practitioner, com simulados, links uteis, resumos, etc.

# Requisitos
* Calendário com datas importantes
* Acesso a links úteis
* Acesso à resumos
* Simulados interativos
* Histórico de pontuação

# Público-alvo
Estudantes da certificação da AWS Practitioner ou que só queiram entender da computação em nuvem que a AWS oferece

# Tecnologias
* Linguagem: Python
* Banco de Dados: ??
* Framework web: Django ou Flask

# Desenho da lógica
* Tela inicial com opções
    * Calendário
        * Acessa página com calendário 
            * Personalizar agendamento
            * Visualizar agendamento 
    * Links Úteis
        * Acessa página com links úteis ao estudo
            * Visualizar links
            * Adicionar link
            * Alterar/Excluir links
            * Criar/excluir categorias
            * Categorizar os links
    * Resumos
        * Acessa página dos resumos
            * Editor de texto pra adicionar resumo
            * Adicionar/Excluir resumo
            * Acesso aos existentes
            * Criar/Excluir categorias
            * Categorizar os resumos
    * Simulados 
        * Acesso aos simulados
            * Escolhe qual simulado fazer
        * Acesso ao histórico
            * Pontuação já feita em cada simulado
            * Desempenho em gráfico por simulado e de forma geral
