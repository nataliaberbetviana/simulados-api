# Arquivo: dados/simulado_1.py
# Contém as questões e dados do Simulado 1
DADOS_SIMULADO = {
    "id": 1,
    "titulo": "Serviços Essenciais AWS",
    "questoes": [
        {
            "pergunta": "Qual serviço da AWS oferece capacidade computacional escalável na nuvem, permitindo que você alugue máquinas virtuais?",
            "opcoes": ["Amazon S3", "Amazon EC2", "Amazon RDS", "Amazon Lambda"],
            "resposta_correta": "Amazon EC2",
            "explicacao": "O Amazon EC2 (Elastic Compute Cloud) é o serviço que fornece capacidade computacional escalável através de instâncias (máquinas virtuais). O S3 é para armazenamento de objetos, o RDS é para bancos de dados relacionais, e o Lambda é para computação serverless."
        },
        {
            "pergunta": "Qual conceito da AWS se refere a uma rede virtual isolada para seus recursos na nuvem?",
            "opcoes": ["Amazon S3", "Amazon Route 53", "Amazon VPC", "Amazon DynamoDB"],
            "resposta_correta": "Amazon VPC",
            "explicacao": "Amazon VPC (Virtual Private Cloud) permite criar uma rede virtual isolada na AWS onde você pode definir sub-redes, tabelas de roteamento, gateways e configurações de segurança. É fundamental para controlar o ambiente de rede dos seus recursos."
        },
        {
            "pergunta": "Para armazenar objetos (arquivos) com alta durabilidade e disponibilidade, qual serviço deve ser usado?",
            "opcoes": ["Amazon EBS", "Amazon EFS", "Amazon S3", "Amazon Aurora"],
            "resposta_correta": "Amazon S3",
            "explicacao": "Amazon S3 (Simple Storage Service) é o serviço ideal para armazenar objetos com 99.999999999% (11 noves) de durabilidade. EBS é para volumes de blocos anexados a EC2, EFS é para sistemas de arquivos compartilhados, e Aurora é um banco de dados relacional."
        }
    ]
}