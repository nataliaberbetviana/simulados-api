<a id='inicio'></a>
![Status do Projeto](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow?logo=github)
<h1 align="center">
  AWS Practitioner - Preparação Simplificada
  <h3 align="center">Seu guia completo para a certificação AWS Certified Cloud Practitioner!</h3>
  <br>
  <img src=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ9emTxu1j5V7TbxJ7EngDoRayDa8wC0SyPgg&s width="100%">
</h1>



## 📖 Sobre

Este projeto é uma plataforma interativa e completa, criada para simplificar a sua jornada rumo à certificação **AWS Certified Cloud Practitioner**. Com ele, estudantes, profissionais de TI e qualquer pessoa interessada em computação em nuvem têm acesso a uma ferramenta poderosa para dominar os fundamentos da AWS.

## 🚀 Funcionalidades

* **Links Úteis**: Acesse uma curadoria de links, organizados por categorias, para aprofundar seu conhecimento.
* **Resumos Interativos**: Adicione, edite e categorize seus próprios resumos, criando um material de estudo personalizado.
* **Simulados Interativos**: Teste seus conhecimentos com simulados que replicam a experiência da prova.
* **Histórico de Desempenho**: Acompanhe seu progresso com gráficos de pontuação e estatísticas detalhadas.

## 🛠️ Tecnologias

* **Linguagem**: Python
* **Framework Web**: Flask
* **Banco de Dados**:  Flask-SQLAlchemy
## ⚙️ Como Rodar o Projeto

Siga os passos abaixo para ter o projeto rodando em sua máquina local.

### Preparação Inicial
**1. Clone o repositório**
```bash
git clone git@github.com:nataliaberbetviana/simulados-api.git
cd simulados-api
```
**2. Configure o ambiente virtual**

* Para Linux/macOS
```bash
python3 -m venv venv
source venv/bin/activate
```
* Para Windows
```bash
python -m venv venv
venv\Scripts\activate
```
**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

### Criação do Banco de Dados
O banco de dados será criado na primeira vez que você rodar o aplicativo

**1. Execute a aplicação**
<br>
Para executar a aplicação Flask, use o comando abaixo. Ele garante que o servidor de desenvolvimento será iniciado corretamente
```
python app.py
```
Se seu arquivo principal for diferente de app.py, use:
```bash
export FLASK_APP=seu_arquivo.py
flask run
```

**2. No seu terminal, você verá a mensagem de confirmação:**
```bash
Banco de dados 'site.db' criado com sucesso!
```

**3. Acesso à plataforma**
<br>
A aplicação estará disponível em http://localhost:5000.

## 🔄 Gerenciamento e Atualização (Sem Perder o Histórico)

Para atualizar o projeto após puxar novas modificações do repositório (como novos simulados) sem deletar suas pontuações, siga esta rotina:
1. Puxe as alterações do Git:
```bash
git pull origin main
```
2. Reinstale as dependências (se houver)
```bash
pip install -r requirements.txt
```
3. Inicie a aplicação
```bash
python app.py
```
IMPORTANTE: Como o banco de dados já existe, o bloco de criação automática do app.py será ignorado, e seus dados de histórico serão preservados.

### Como Deletar e Resetar o Histórico

Se você quiser apagar todos os resultados salvos (para começar do zero), acesse a rota de administração:
* Certifique-se de que o servidor Flask está rodando.
* Acesse esta URL no seu navegador: http://localhost:5000/resetar-historico
* A página de histórico será recarregada, mostrando a tabela vazia.


## 📄 Licença

Este projeto está sob a licença [MIT](https://choosealicense.com/licenses/mit/).

## ✉️ Contato

Se você tiver alguma dúvida, sugestão, ou quiser discutir possíveis alterações no projeto, sinta-se à vontade para entrar em contato comigo.
* [**LinkedIn**](https://www.linkedin.com/in/nataliaberbetviana/)
* [**E-mail**](mailto:nabevia@gmail.com)


  <div align="right">
  <a href="#inicio" style="
    display: inline-block;
    padding: 8px 15px;
    background-color: #007bff; /* Cor de fundo azul */
    color: white;             /* Cor do texto branco */
    text-decoration: none;    /* Remove o sublinhado */
    border-radius: 5px;       /* Bordas arredondadas */
    font-weight: bold;        /* Texto em negrito */
    font-family: sans-serif;  /* Fonte mais legível */
  ">Voltar ao Início</a>
</div>
