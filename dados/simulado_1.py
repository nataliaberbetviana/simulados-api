DADOS_SIMULADO = {
    "id": 1,
    "titulo": "AWS Cloud Practitioner - Simulado Completo",
    "questoes": [
        # Domínio 1: Conceitos da Nuvem (16 questões)
        {
            "pergunta": "Qual dos seguintes é um benefício de usar a nuvem AWS que permite que você pague apenas pelos recursos que consome?",
            "opcoes": ["Elasticidade", "Economia de escala", "Pagamento conforme o uso", "Alta disponibilidade"],
            "resposta_correta": "Pagamento conforme o uso",
            "multipla_escolha": False,
            "explicacao": "O modelo 'pagamento conforme o uso' (Pay-as-you-go) é um dos principais benefícios da nuvem, eliminando a necessidade de grandes investimentos de capital e permitindo que você pague apenas pelos recursos que utiliza."
        },
        {
            "pergunta": "Uma empresa precisa de uma plataforma para desenvolver e implantar aplicativos sem se preocupar com a infraestrutura subjacente, como servidores e sistemas operacionais. Qual modelo de serviço em nuvem é o mais adequado?",
            "opcoes": ["Infraestrutura como Serviço (IaaS)", "Plataforma como Serviço (PaaS)", "Software como Serviço (SaaS)", "Funções como Serviço (FaaS)"],
            "resposta_correta": "Plataforma como Serviço (PaaS)",
            "multipla_escolha": False,
            "explicacao": "PaaS fornece uma plataforma para os desenvolvedores construírem e implantarem aplicativos, abstraindo a complexidade do gerenciamento da infraestrutura subjacente."
        },
        {
            "pergunta": "Qual modelo de implantação envolve o uso de uma combinação de recursos da nuvem pública e recursos de um data center on-premises?",
            "opcoes": ["Nuvem pública", "Nuvem privada", "Nuvem híbrida", "Nuvem de comunidade"],
            "resposta_correta": "Nuvem híbrida",
            "multipla_escolha": False,
            "explicacao": "Uma nuvem híbrida é um modelo de implantação que combina uma nuvem pública (como a AWS) com um ambiente de infraestrutura on-premises (nuvem privada), permitindo que os dados e as aplicações sejam compartilhados entre eles."
        },
        {
            "pergunta": "Uma empresa deseja otimizar seus custos na AWS. Qual dos seguintes princípios do pilar de Otimização de Custos do AWS Well-Architected Framework seria mais útil?",
            "opcoes": ["Aumentar a utilização de recursos", "Adotar um modelo de pagamento por hora", "Implementar o monitoramento de segurança contínuo", "Usar tipos de instância de uso geral"],
            "resposta_correta": "Aumentar a utilização de recursos",
            "multipla_escolha": False,
            "explicacao": "O pilar de Otimização de Custos do Well-Architected Framework visa maximizar o valor dos recursos. Aumentar a utilização de recursos é uma forma eficaz de otimizar os custos."
        },
        {
            "pergunta": "Quais dos seguintes são benefícios da computação em nuvem?",
            "opcoes": ["Elasticidade", "Altos custos de capital (Capex)", "Agilidade e inovação", "Pagamento por assinatura de software"],
            "resposta_correta": ["Elasticidade", "Agilidade e inovação"],
            "multipla_escolha": True,
            "explicacao": "A elasticidade (capacidade de escalar) e a agilidade e inovação são benefícios da computação em nuvem, enquanto altos custos de capital são característicos de ambientes on-premises."
        },
        {
            "pergunta": "Uma empresa tem uma carga de trabalho que exige que um aplicativo permaneça operacional mesmo que um dos componentes falhe. Qual pilar do AWS Well-Architected Framework trata desse requisito?",
            "opcoes": ["Otimização de Custos", "Excelência Operacional", "Confiabilidade", "Segurança"],
            "resposta_correta": "Confiabilidade",
            "multipla_escolha": False,
            "explicacao": "O pilar de Confiabilidade do AWS Well-Architected Framework garante que um sistema possa se recuperar de falhas e continuar funcionando, o que é um dos principais objetivos da alta disponibilidade."
        },
        {
            "pergunta": "O que é a computação sem servidor (serverless)?",
            "opcoes": ["Um modelo onde os servidores são substituídos por contêineres.", "Um modelo de nuvem onde você não precisa se preocupar com o provisionamento ou gerenciamento de servidores.", "Um serviço que permite criar e gerenciar uma rede privada virtual.", "Um tipo de computação de alto desempenho usado para análise de big data."],
            "resposta_correta": "Um modelo de nuvem onde você não precisa se preocupar com o provisionamento ou gerenciamento de servidores.",
            "multipla_escolha": False,
            "explicacao": "A computação sem servidor (serverless) é um modelo de execução de nuvem em que a AWS gerencia a infraestrutura, permitindo que os desenvolvedores foquem no código do aplicativo sem se preocuparem com servidores, escalabilidade ou gerenciamento."
        },
        {
            "pergunta": "Qual é a principal diferença entre um grupo de disponibilidade (Availability Zone) e uma região (Region) da AWS?",
            "opcoes": ["Uma região é uma coleção de grupos de disponibilidade isolados.", "Um grupo de disponibilidade é uma área geográfica com várias regiões.", "Uma região é um único data center, enquanto um grupo de disponibilidade é uma rede de data centers.", "Um grupo de disponibilidade é um data center, enquanto uma região é uma área geográfica."],
            "resposta_correta": "Uma região é uma coleção de grupos de disponibilidade isolados.",
            "multipla_escolha": False,
            "explicacao": "Uma Região da AWS é uma área geográfica que contém dois ou mais Grupos de Disponibilidade (Availability Zones). Um Grupo de Disponibilidade é um ou mais data centers com energia, rede e conectividade redundantes em uma Região."
        },
        {
            "pergunta": "Quais são os principais benefícios de migrar para a nuvem?",
            "opcoes": ["Eliminar completamente a necessidade de planejamento de capacidade.", "Requer um investimento inicial significativo em hardware.", "Permitir o pagamento apenas pelo que é usado.", "Aumentar a velocidade e agilidade da implantação de aplicativos."],
            "resposta_correta": ["Permitir o pagamento apenas pelo que é usado.", "Aumentar a velocidade e agilidade da implantação de aplicativos."],
            "multipla_escolha": True,
            "explicacao": "A computação em nuvem permite o modelo de pagamento conforme o uso e aumenta a agilidade e a velocidade de implantação, em contraste com a necessidade de planejamento de capacidade e o alto investimento em hardware de ambientes on-premises."
        },
        {
            "pergunta": "Qual termo se refere à capacidade de um sistema de se recuperar de falhas e continuar funcionando?",
            "opcoes": ["Elasticidade", "Escalabilidade", "Confiabilidade", "Segurança"],
            "resposta_correta": "Confiabilidade",
            "multipla_escolha": False,
            "explicacao": "A confiabilidade é a capacidade de um sistema de funcionar corretamente mesmo quando ocorrem falhas, o que é um dos pilares do AWS Well-Architected Framework."
        },
        {
            "pergunta": "O que é o propósito do AWS Global Infrastructure?",
            "opcoes": ["Fornecer uma rede de data centers e regiões para hospedar serviços.", "Apenas fornecer serviços de armazenamento de dados em todo o mundo.", "Gerenciar a infraestrutura de rede de data centers de clientes.", "Oferecer servidores virtuais para aplicativos de alto desempenho."],
            "resposta_correta": "Fornecer uma rede de data centers e regiões para hospedar serviços.",
            "multipla_escolha": False,
            "explicacao": "A AWS Global Infrastructure é composta por Regiões e Zonas de Disponibilidade interconectadas para fornecer uma infraestrutura escalável, confiável e de alto desempenho para hospedar os serviços e aplicativos de nuvem."
        },
        {
            "pergunta": "Quais são os principais benefícios da computação em nuvem para startups?",
            "opcoes": ["Oferece economias de escala.", "Requer um alto investimento inicial.", "Permite a flexibilidade para crescer.", "Exige o gerenciamento completo de servidores e hardware."],
            "resposta_correta": ["Oferece economias de escala.", "Permite a flexibilidade para crescer."],
            "multipla_escolha": True,
            "explicacao": "A nuvem permite que startups evitem altos custos de capital e se beneficiem de economias de escala e flexibilidade, escalando rapidamente para cima ou para baixo, conforme a demanda."
        },
        {
            "pergunta": "Qual dos seguintes serviços é um exemplo de Infraestrutura como Serviço (IaaS)?",
            "opcoes": ["Amazon EC2", "Amazon S3", "Amazon RDS", "Amazon Lambda"],
            "resposta_correta": "Amazon EC2",
            "multipla_escolha": False,
            "explicacao": "O Amazon EC2 é um exemplo de IaaS, pois oferece instâncias de computação (servidores virtuais), dando aos usuários o controle sobre o sistema operacional e os aplicativos."
        },
        {
            "pergunta": "O que o pilar de Otimização de Custos do AWS Well-Architected Framework visa?",
            "opcoes": ["Aumentar o uso de recursos para maximizar a receita.", "Manter os custos no mínimo, independentemente do desempenho.", "Evitar gastos desnecessários e maximizar o valor dos recursos.", "Pagar por licenças de software anuais."],
            "resposta_correta": "Evitar gastos desnecessários e maximizar o valor dos recursos.",
            "multipla_escolha": False,
            "explicacao": "O objetivo do pilar de Otimização de Custos é evitar gastos excessivos e garantir que a arquitetura da solução esteja alinhada com os objetivos de custo da empresa, através do uso eficiente dos recursos."
        },
        {
            "pergunta": "Qual das seguintes opções não é um benefício de se migrar para a nuvem da AWS?",
            "opcoes": ["Oportunidade de economizar custos de capital.", "Aumento da velocidade e agilidade.", "Possibilidade de implantar globalmente em minutos.", "Redução da equipe de TI."],
            "resposta_correta": "Redução da equipe de TI.",
            "multipla_escolha": False,
            "explicacao": "A migração para a nuvem não necessariamente reduz a equipe de TI, mas sim muda o foco das atividades, de tarefas de manutenção de hardware para o gerenciamento e otimização de serviços em nuvem."
        },
        {
            "pergunta": "O que é um 'compute instance'?",
            "opcoes": ["Um servidor físico dedicado a um único cliente.", "Um servidor virtual na nuvem que você pode usar para executar aplicativos.", "Um tipo de banco de dados usado para análise de dados.", "Um serviço de armazenamento de objetos."],
            "resposta_correta": "Um servidor virtual na nuvem que você pode usar para executar aplicativos.",
            "multipla_escolha": False,
            "explicacao": "Uma instância de computação (compute instance), como no Amazon EC2, é um servidor virtual na nuvem que fornece capacidade de processamento para executar uma variedade de cargas de trabalho."
        },
        
        # Domínio 2: Segurança e Conformidade (20 questões)
        {
            "pergunta": "De acordo com o Modelo de Responsabilidade Compartilhada da AWS, quem é responsável pela segurança do sistema operacional convidado, dos aplicativos e das configurações de segurança do firewall?",
            "opcoes": ["AWS", "O cliente", "Um provedor de serviços terceirizado", "Ninguém, pois é um recurso automatizado"],
            "resposta_correta": "O cliente",
            "multipla_escolha": False,
            "explicacao": "No Modelo de Responsabilidade Compartilhada, a AWS é responsável pela segurança 'da nuvem' (hardware, software, rede, etc.), enquanto o cliente é responsável pela segurança 'na nuvem' (dados, sistema operacional, aplicativos, etc.)."
        },
        {
            "pergunta": "Qual serviço da AWS permite que você gerencie o acesso de usuários e permissões de forma centralizada em sua conta AWS?",
            "opcoes": ["Amazon EC2", "AWS Identity and Access Management (IAM)", "Amazon S3", "Amazon GuardDuty"],
            "resposta_correta": "AWS Identity and Access Management (IAM)",
            "multipla_escolha": False,
            "explicacao": "O AWS IAM é o serviço que controla o acesso a recursos da AWS, permitindo que você crie e gerencie usuários e defina permissões para que possam acessar os serviços da AWS de forma segura."
        },
        {
            "pergunta": "Uma empresa precisa garantir que dados sensíveis não sejam acessados por pessoas não autorizadas. Qual princípio de segurança é mais relevante neste caso?",
            "opcoes": ["Disponibilidade", "Integridade", "Confidencialidade", "Escalabilidade"],
            "resposta_correta": "Confidencialidade",
            "multipla_escolha": False,
            "explicacao": "A confidencialidade é o princípio de que a informação só pode ser acessada por indivíduos autorizados, o que é fundamental para proteger dados sensíveis."
        },
        {
            "pergunta": "Quais serviços da AWS podem ser usados para proteger aplicativos web de exploits comuns, como injeção de SQL e ataques de negação de serviço (DDoS)?",
            "opcoes": ["AWS WAF", "AWS Shield", "Amazon RDS", "Amazon VPC"],
            "resposta_correta": ["AWS WAF", "AWS Shield"],
            "multipla_escolha": True,
            "explicacao": "O AWS WAF (Web Application Firewall) protege contra injeção de SQL e outros exploits, enquanto o AWS Shield protege contra ataques DDoS."
        },
        {
            "pergunta": "Uma empresa deseja monitorar e registrar todas as ações tomadas por um usuário em sua conta AWS para fins de auditoria. Qual serviço AWS deve ser usado?",
            "opcoes": ["AWS Trusted Advisor", "AWS CloudTrail", "Amazon CloudWatch", "AWS Shield"],
            "resposta_correta": "AWS CloudTrail",
            "multipla_escolha": False,
            "explicacao": "O AWS CloudTrail registra as chamadas da API e as ações de usuários em sua conta, fornecendo um histórico de atividades para auditoria e governança."
        },
        {
            "pergunta": "De acordo com o Modelo de Responsabilidade Compartilhada da AWS, quem é responsável pela segurança 'da nuvem'?",
            "opcoes": ["O cliente", "A AWS", "Ambos, o cliente e a AWS, em uma parceria 50/50", "Um consultor de segurança independente"],
            "resposta_correta": "A AWS",
            "multipla_escolha": False,
            "explicacao": "A segurança 'da nuvem' é responsabilidade da AWS e inclui a segurança da infraestrutura física, hardware, software, rede e instalações que executam os serviços da AWS."
        },
        {
            "pergunta": "Qual serviço permite que você analise vulnerabilidades e desvios de conformidade em suas instâncias do Amazon EC2?",
            "opcoes": ["AWS Trusted Advisor", "Amazon Inspector", "Amazon GuardDuty", "AWS Shield"],
            "resposta_correta": "Amazon Inspector",
            "multipla_escolha": False,
            "explicacao": "O Amazon Inspector é um serviço automatizado de avaliação de segurança que ajuda a melhorar a segurança e a conformidade de aplicativos implantados na AWS."
        },
        {
            "pergunta": "Uma empresa precisa criar usuários e grupos de usuários, atribuir políticas de permissões e gerenciar credenciais para acesso à conta AWS. Qual serviço é a solução?",
            "opcoes": ["AWS KMS", "AWS Systems Manager", "AWS CloudTrail", "AWS IAM"],
            "resposta_correta": "AWS IAM",
            "multipla_escolha": False,
            "explicacao": "O AWS IAM (Identity and Access Management) é o serviço central para gerenciar usuários, grupos, funções e permissões de acesso aos recursos da AWS."
        },
        {
            "pergunta": "O que significa 'identidade' no contexto do AWS IAM?",
            "opcoes": ["A forma como a AWS se identifica com os clientes.", "A forma como um recurso AWS se identifica com outro.", "Uma entidade (como um usuário, grupo ou função) que pode ser autenticada e autorizada para acessar recursos.", "Um endereço IP único para cada conta AWS."],
            "resposta_correta": "Uma entidade (como um usuário, grupo ou função) que pode ser autenticada e autorizada para acessar recursos.",
            "multipla_escolha": False,
            "explicacao": "Uma identidade IAM é uma entidade que pode ser usada para autenticar e conceder permissões para acessar os serviços da AWS."
        },
        {
            "pergunta": "Quais dos seguintes são responsabilidades do cliente sob o Modelo de Responsabilidade Compartilhada da AWS?",
            "opcoes": ["Segurança do data center físico", "Segurança do sistema operacional do convidado", "Criptografia de dados do cliente", "Manutenção da infraestrutura de rede da AWS"],
            "resposta_correta": ["Segurança do sistema operacional do convidado", "Criptografia de dados do cliente"],
            "multipla_escolha": True,
            "explicacao": "O cliente é responsável pela segurança 'na nuvem', o que inclui o sistema operacional convidado e a criptografia dos dados. A AWS é responsável pela segurança 'da nuvem', incluindo a segurança física e a manutenção da infraestrutura."
        },
        {
            "pergunta": "Qual serviço da AWS ajuda a auditar a governança, o risco e a conformidade de sua conta AWS, registrando as ações da API?",
            "opcoes": ["AWS CloudTrail", "AWS Config", "AWS KMS", "AWS IAM"],
            "resposta_correta": "AWS CloudTrail",
            "multipla_escolha": False,
            "explicacao": "O AWS CloudTrail fornece um registro de todas as ações de API e eventos de serviço, o que é crucial para auditoria, governança e conformidade."
        },
        {
            "pergunta": "Qual é a principal finalidade da criptografia de dados em repouso?",
            "opcoes": ["Proteger dados enquanto estão em trânsito pela rede.", "Proteger dados armazenados em serviços como Amazon S3 e Amazon EBS.", "Apenas para proteger informações de cartão de crédito.", "Autenticar a identidade de um usuário."],
            "resposta_correta": "Proteger dados armazenados em serviços como Amazon S3 e Amazon EBS.",
            "multipla_escolha": False,
            "explicacao": "A criptografia de dados em repouso protege os dados enquanto eles estão armazenados em um meio físico, como discos rígidos e armazenamento em nuvem."
        },
        {
            "pergunta": "Qual serviço AWS é usado para criar e gerenciar chaves criptográficas para proteger seus dados na nuvem?",
            "opcoes": ["AWS Secrets Manager", "AWS Key Management Service (KMS)", "AWS IAM", "Amazon GuardDuty"],
            "resposta_correta": "AWS Key Management Service (KMS)",
            "multipla_escolha": False,
            "explicacao": "O AWS KMS (Key Management Service) é um serviço gerenciado que permite criar e controlar as chaves criptográficas usadas para criptografar dados."
        },
        {
            "pergunta": "Uma empresa precisa de um serviço que monitore continuamente a atividade maliciosa e o comportamento não autorizado para proteger contas e cargas de trabalho na AWS. Qual serviço é ideal para essa tarefa?",
            "opcoes": ["Amazon Inspector", "Amazon CloudWatch", "Amazon GuardDuty", "AWS Security Hub"],
            "resposta_correta": "Amazon GuardDuty",
            "multipla_escolha": False,
            "explicacao": "O Amazon GuardDuty é um serviço de detecção de ameaças que monitora continuamente atividades maliciosas e comportamento não autorizado para proteger suas contas e dados da AWS."
        },
        {
            "pergunta": "Qual dos seguintes é um exemplo de controle de segurança físico de acordo com o Modelo de Responsabilidade Compartilhada da AWS?",
            "opcoes": ["Gerenciar patches de segurança no sistema operacional do servidor.", "Controlar o acesso físico aos data centers da AWS.", "Configurar as permissões de acesso aos dados do cliente.", "Proteger o acesso à rede de um aplicativo."],
            "resposta_correta": "Controlar o acesso físico aos data centers da AWS.",
            "multipla_escolha": False,
            "explicacao": "A segurança física dos data centers é responsabilidade exclusiva da AWS, conforme o Modelo de Responsabilidade Compartilhada."
        },
        {
            "pergunta": "Quais ferramentas da AWS podem fornecer recomendações para otimização de custos e segurança da sua conta?",
            "opcoes": ["AWS Trusted Advisor", "AWS CloudTrail", "AWS Cost Explorer", "Amazon VPC"],
            "resposta_correta": ["AWS Trusted Advisor", "AWS Cost Explorer"],
            "multipla_escolha": True,
            "explicacao": "O AWS Trusted Advisor e o AWS Cost Explorer fornecem insights e recomendações para otimizar custos e o uso de recursos."
        },
        {
            "pergunta": "Qual é a principal função do AWS Security Hub?",
            "opcoes": ["Gerenciar permissões de usuário de forma centralizada.", "Oferecer um ponto de vista abrangente do seu estado de segurança na AWS.", "Ajudar a criptografar dados em trânsito.", "Proteger contra ataques DDoS."],
            "resposta_correta": "Oferecer um ponto de vista abrangente do seu estado de segurança na AWS.",
            "multipla_escolha": False,
            "explicacao": "O AWS Security Hub oferece uma visão abrangente de seu estado de segurança, agregando alertas e descobertas de segurança de vários serviços da AWS."
        },
        {
            "pergunta": "Qual serviço permite que você armazene e gerencie segredos, como credenciais de banco de dados e chaves de API?",
            "opcoes": ["AWS Secrets Manager", "AWS KMS", "AWS IAM", "AWS Organizations"],
            "resposta_correta": "AWS Secrets Manager",
            "multipla_escolha": False,
            "explicacao": "O AWS Secrets Manager ajuda a proteger os segredos necessários para acessar aplicativos, serviços e recursos. Ele permite rotacionar, gerenciar e auditar credenciais de forma centralizada."
        },
        {
            "pergunta": "O que o AWS Marketplace ajuda a garantir em termos de segurança?",
            "opcoes": ["Todos os produtos oferecidos são gratuitos e de código aberto.", "Todos os produtos foram verificados e estão prontos para serem usados na AWS.", "A AWS não é responsável por nenhum produto de terceiros.", "Os produtos são exclusivamente para fins de desenvolvimento."],
            "resposta_correta": "Todos os produtos foram verificados e estão prontos para serem usados na AWS.",
            "multipla_escolha": False,
            "explicacao": "O AWS Marketplace oferece um catálogo de software de terceiros que foi verificado e é compatível para ser executado no ambiente da AWS."
        },
        {
            "pergunta": "Qual das seguintes opções é uma prática recomendada para gerenciar credenciais de acesso do usuário raiz da conta AWS?",
            "opcoes": ["Usar a conta raiz diariamente para todas as tarefas.", "Compartilhar as credenciais com a equipe de desenvolvimento.", "Desativar a conta raiz e usar usuários IAM para todas as tarefas.", "Armazenar as credenciais em um local seguro e usá-las apenas para tarefas que exigem acesso raiz."],
            "resposta_correta": "Armazenar as credenciais em um local seguro e usá-las apenas para tarefas que exigem acesso raiz.",
            "multipla_escolha": False,
            "explicacao": "A conta raiz tem acesso irrestrito a todos os recursos. A melhor prática é não usá-la para tarefas diárias, em vez disso, criar e usar usuários IAM com as permissões necessárias."
        },
        
        # Domínio 3: Tecnologia e Serviços da Nuvem (22 questões)
        {
            "pergunta": "Qual é um dos principais casos de uso para o Amazon S3 (Simple Storage Service)?",
            "opcoes": ["Executar aplicativos complexos.", "Hospedar um banco de dados relacional.", "Armazenar arquivos de objetos, como imagens e vídeos.", "Criar uma rede privada virtual."],
            "resposta_correta": "Armazenar arquivos de objetos, como imagens e vídeos.",
            "multipla_escolha": False,
            "explicacao": "O Amazon S3 é um serviço de armazenamento de objetos, ideal para armazenar dados não estruturados, como documentos, imagens, vídeos, logs e backups."
        },
        {
            "pergunta": "Você precisa de um serviço de computação escalável que permita executar código em resposta a eventos, sem gerenciar servidores. Qual serviço é a melhor opção?",
            "opcoes": ["Amazon EC2", "Amazon S3", "AWS Lambda", "Amazon RDS"],
            "resposta_correta": "AWS Lambda",
            "multipla_escolha": False,
            "explicacao": "O AWS Lambda é um serviço de computação sem servidor que executa código em resposta a eventos, sem a necessidade de provisionar ou gerenciar servidores."
        },
        {
            "pergunta": "Qual serviço é uma coleção de servidores virtuais (instâncias) na nuvem da AWS?",
            "opcoes": ["Amazon S3", "Amazon EC2", "Amazon RDS", "Amazon VPC"],
            "resposta_correta": "Amazon EC2",
            "multipla_escolha": False,
            "explicacao": "O Amazon EC2 (Elastic Compute Cloud) fornece capacidade de computação escalável na nuvem na forma de instâncias de máquinas virtuais."
        },
        {
            "pergunta": "Uma empresa precisa de um banco de dados relacional totalmente gerenciado na AWS. Qual serviço deve ser usado?",
            "opcoes": ["Amazon Aurora", "Amazon DynamoDB", "Amazon Redshift", "Amazon S3"],
            "resposta_correta": "Amazon Aurora",
            "multipla_escolha": False,
            "explicacao": "O Amazon Aurora é um banco de dados relacional compatível com MySQL e PostgreSQL, que é totalmente gerenciado pela AWS. O DynamoDB é NoSQL, o Redshift é um data warehouse e o S3 é um serviço de armazenamento de objetos."
        },
        {
            "pergunta": "Qual serviço de computação sem servidor permite que você execute contêineres Docker sem gerenciar a infraestrutura subjacente?",
            "opcoes": ["Amazon EC2", "Amazon ECS", "AWS Fargate", "Amazon EC2 Container Service"],
            "resposta_correta": "AWS Fargate",
            "multipla_escolha": False,
            "explicacao": "O AWS Fargate é um motor de computação sem servidor para o Amazon ECS e EKS, permitindo que você execute contêineres sem provisionar, gerenciar ou escalar clusters de instâncias EC2."
        },
        {
            "pergunta": "Qual dos seguintes serviços é um banco de dados NoSQL totalmente gerenciado e não relacional da AWS?",
            "opcoes": ["Amazon RDS", "Amazon DynamoDB", "Amazon Redshift", "Amazon Aurora"],
            "resposta_correta": "Amazon DynamoDB",
            "multipla_escolha": False,
            "explicacao": "O Amazon DynamoDB é um serviço de banco de dados NoSQL rápido, flexível e totalmente gerenciado, projetado para aplicativos de alto desempenho."
        },
        {
            "pergunta": "Você precisa criar uma rede isolada na AWS onde possa implantar seus recursos, como instâncias EC2 e bancos de dados. Qual serviço você usaria?",
            "opcoes": ["Amazon Virtual Private Cloud (VPC)", "Amazon S3", "AWS Lambda", "Amazon Route 53"],
            "resposta_correta": "Amazon Virtual Private Cloud (VPC)",
            "multipla_escolha": False,
            "explicacao": "O Amazon VPC permite que você crie uma rede virtual isolada e defina sua topologia, permitindo que você controle a conectividade e a segurança de seus recursos."
        },
        {
            "pergunta": "Qual serviço da AWS é usado para armazenar dados em cache para melhorar o desempenho de aplicativos?",
            "opcoes": ["Amazon DynamoDB", "Amazon Redshift", "Amazon ElastiCache", "Amazon SQS"],
            "resposta_correta": "Amazon ElastiCache",
            "multipla_escolha": False,
            "explicacao": "O Amazon ElastiCache é um serviço de caching na memória totalmente gerenciado, que melhora o desempenho de aplicativos, permitindo que você recupere informações de caches na memória, em vez de depender de bancos de dados baseados em disco mais lentos."
        },
        {
            "pergunta": "Qual serviço de mensagens na AWS é um serviço de enfileiramento de mensagens totalmente gerenciado, que desacopla componentes de aplicativos?",
            "opcoes": ["Amazon SNS", "Amazon SQS", "Amazon Connect", "Amazon Kinesis"],
            "resposta_correta": "Amazon SQS",
            "multipla_escolha": False,
            "explicacao": "O Amazon SQS (Simple Queue Service) é um serviço de fila de mensagens, que permite desacoplar e escalar microsserviços, sistemas distribuídos e aplicativos sem servidor."
        },
        {
            "pergunta": "O que o Amazon CloudFront faz?",
            "opcoes": ["Oferece um banco de dados relacional.", "Atua como um serviço de entrega de conteúdo (CDN) para distribuir conteúdo em todo o mundo.", "Permite o gerenciamento de permissões de usuários.", "É um serviço de computação sem servidor."],
            "resposta_correta": "Atua como um serviço de entrega de conteúdo (CDN) para distribuir conteúdo em todo o mundo.",
            "multipla_escolha": False,
            "explicacao": "O Amazon CloudFront é um serviço de CDN que acelera a entrega de conteúdo web dinâmico e estático para os usuários, com baixa latência e alta velocidade."
        },
        {
            "pergunta": "Quais serviços da AWS podem ser usados para gerenciamento de contêineres e orquestração?",
            "opcoes": ["AWS Lambda", "Amazon EKS (Elastic Kubernetes Service)", "Amazon EC2", "Amazon ECS (Elastic Container Service)"],
            "resposta_correta": ["Amazon EKS (Elastic Kubernetes Service)", "Amazon ECS (Elastic Container Service)"],
            "multipla_escolha": True,
            "explicacao": "Tanto o Amazon EKS (Kubernetes) quanto o Amazon ECS (Docker) são serviços de orquestração de contêineres que ajudam a implantar, gerenciar e escalar contêineres na AWS."
        },
        {
            "pergunta": "Você precisa de um serviço de banco de dados para armazenar grandes quantidades de dados para análise de business intelligence. Qual serviço de data warehouse é a melhor opção?",
            "opcoes": ["Amazon RDS", "Amazon DynamoDB", "Amazon Redshift", "Amazon EC2"],
            "resposta_correta": "Amazon Redshift",
            "multipla_escolha": False,
            "explicacao": "O Amazon Redshift é um data warehouse totalmente gerenciado e otimizado para análise de grandes conjuntos de dados, ideal para business intelligence."
        },
        {
            "pergunta": "Qual é a principal função do Amazon Route 53?",
            "opcoes": ["Gerenciar um banco de dados NoSQL.", "Atuar como um serviço de roteamento de rede.", "É um serviço de DNS (Sistema de Nomes de Domínio) escalável e altamente disponível.", "Oferecer um serviço de entrega de conteúdo."],
            "resposta_correta": "É um serviço de DNS (Sistema de Nomes de Domínio) escalável e altamente disponível.",
            "multipla_escolha": False,
            "explicacao": "O Amazon Route 53 é um serviço web de DNS que ajuda a rotear o tráfego de usuários para aplicativos hospedados na AWS ou fora dela."
        },
        {
            "pergunta": "Qual serviço da AWS permite que você transmita dados em tempo real a partir de fontes de dados para processamento e análise?",
            "opcoes": ["Amazon Redshift", "Amazon Kinesis", "Amazon SQS", "Amazon SNS"],
            "resposta_correta": "Amazon Kinesis",
            "multipla_escolha": False,
            "explicacao": "O Amazon Kinesis é uma plataforma para coletar, processar e analisar dados de streaming em tempo real."
        },
        {
            "pergunta": "Qual dos seguintes serviços de armazenamento de blocos é projetado para ser usado com instâncias do Amazon EC2?",
            "opcoes": ["Amazon S3", "Amazon Elastic File System (EFS)", "Amazon Elastic Block Store (EBS)", "Amazon Glacier"],
            "resposta_correta": "Amazon Elastic Block Store (EBS)",
            "multipla_escolha": False,
            "explicacao": "O Amazon EBS fornece volumes de armazenamento em nível de bloco que podem ser anexados a instâncias EC2, funcionando como um disco rígido virtual."
        },
        {
            "pergunta": "Quais são as principais diferenças entre o Amazon SQS e o Amazon SNS?",
            "opcoes": ["O SQS é um serviço de fila de mensagens.", "O SNS é um serviço de publicação/assinatura.", "O SQS envia mensagens para múltiplos assinantes.", "O SNS armazena mensagens em uma fila."],
            "resposta_correta": ["O SQS é um serviço de fila de mensagens.", "O SNS é um serviço de publicação/assinatura."],
            "multipla_escolha": True,
            "explicacao": "O Amazon SQS é um serviço de fila, enquanto o Amazon SNS é um serviço de publicação/assinatura."
        },
        {
            "pergunta": "Qual serviço da AWS permite que você armazene dados de forma durável e altamente disponível, com replicação automática em múltiplos dispositivos em um único grupo de disponibilidade?",
            "opcoes": ["Amazon S3", "Amazon EBS", "Amazon EFS", "Amazon Glacier"],
            "resposta_correta": "Amazon EBS",
            "multipla_escolha": False,
            "explicacao": "O Amazon EBS oferece volumes de armazenamento de bloco persistentes para uso com instâncias EC2. Ele replica os dados automaticamente em um único Grupo de Disponibilidade (AZ) para protegê-lo de falhas de componentes."
        },
        {
            "pergunta": "Uma empresa precisa de um serviço para coordenar e orquestrar fluxos de trabalho distribuídos entre vários serviços da AWS. Qual serviço deve ser usado?",
            "opcoes": ["AWS Lambda", "Amazon SQS", "AWS Step Functions", "Amazon SNS"],
            "resposta_correta": "AWS Step Functions",
            "multipla_escolha": False,
            "explicacao": "O AWS Step Functions permite que você construa e orquestre fluxos de trabalho visualmente, combinando funções do AWS Lambda e outros serviços para formar aplicações."
        },
        {
            "pergunta": "Qual serviço da AWS é um serviço de gerenciamento de banco de dados que simplifica a configuração, operação e escalabilidade de um banco de dados MySQL, PostgreSQL, Oracle, SQL Server ou MariaDB?",
            "opcoes": ["Amazon DynamoDB", "Amazon Aurora", "Amazon RDS", "Amazon Redshift"],
            "resposta_correta": "Amazon RDS",
            "multipla_escolha": False,
            "explicacao": "O Amazon RDS (Relational Database Service) é um serviço de banco de dados relacional gerenciado que lida com tarefas administrativas, como patches, backups e escalabilidade."
        },
        {
            "pergunta": "O que é um grupo de segurança (Security Group) no contexto do Amazon EC2?",
            "opcoes": ["Um grupo de usuários com permissões de segurança.", "Um firewall virtual que controla o tráfego de entrada e saída de uma instância EC2.", "Um serviço que protege contra ataques DDoS.", "Uma coleção de instâncias EC2 com as mesmas permissões."],
            "resposta_correta": "Um firewall virtual que controla o tráfego de entrada e saída de uma instância EC2.",
            "multipla_escolha": False,
            "explicacao": "Um Security Group atua como um firewall virtual para controlar o tráfego de entrada e saída em instâncias EC2."
        },
        {
            "pergunta": "Qual serviço AWS permite que você use a inteligência artificial para extrair texto e dados de documentos?",
            "opcoes": ["Amazon Comprehend", "Amazon Lex", "Amazon Textract", "Amazon SageMaker"],
            "resposta_correta": "Amazon Textract",
            "multipla_escolha": False,
            "explicacao": "O Amazon Textract é um serviço de machine learning que extrai automaticamente texto e dados de documentos digitalizados."
        },
        {
            "pergunta": "Qual serviço da AWS é usado para monitorar seus recursos e aplicações em tempo real?",
            "opcoes": ["AWS CloudTrail", "Amazon CloudWatch", "Amazon SNS", "AWS Trusted Advisor"],
            "resposta_correta": "Amazon CloudWatch",
            "multipla_escolha": False,
            "explicacao": "O Amazon CloudWatch é o serviço de monitoramento da AWS para recursos e aplicações que você executa na nuvem."
        },
        
        # Domínio 4: Cobrança, Preços e Suporte (7 questões)
        {
            "pergunta": "Qual dos seguintes fatores não afeta o custo de uma instância do Amazon EC2?",
            "opcoes": ["O tipo da instância.", "A região em que a instância está localizada.", "A quantidade de dados processados pelo banco de dados da instância.", "O sistema operacional da instância."],
            "resposta_correta": "A quantidade de dados processados pelo banco de dados da instância.",
            "multipla_escolha": False,
            "explicacao": "O custo de uma instância EC2 é afetado pelo tipo de instância, a região, o sistema operacional e a forma de pagamento, mas não pela quantidade de dados processados pelo banco de dados, que é um custo separado."
        },
        {
            "pergunta": "Qual plano de suporte da AWS é gratuito e inclui acesso a documentação técnica, fóruns de suporte e o AWS Service Health Dashboard?",
            "opcoes": ["Desenvolvedor", "Básico", "Empresarial", "Business"],
            "resposta_correta": "Básico",
            "multipla_escolha": False,
            "explicacao": "O plano de suporte Básico é gratuito para todos os clientes da AWS e oferece acesso a recursos de autoatendimento, como documentação, whitepapers e fóruns de suporte."
        },
        {
            "pergunta": "Qual serviço da AWS permite que você visualize, entenda e gerencie seus custos e uso da AWS ao longo do tempo?",
            "opcoes": ["AWS Billing and Cost Management", "AWS Simple Monthly Calculator", "AWS Cost Explorer", "AWS Trusted Advisor"],
            "resposta_correta": "AWS Cost Explorer",
            "multipla_escolha": False,
            "explicacao": "O AWS Cost Explorer é uma ferramenta de análise de custos que permite visualizar, entender e gerenciar seus custos e uso da AWS ao longo do tempo."
        },
        {
            "pergunta": "Uma empresa precisa de um plano de suporte que inclua um Gerente Técnico de Contas (TAM) e tempo de resposta de 15 minutos para problemas críticos. Qual plano atende a esses requisitos?",
            "opcoes": ["Desenvolvedor", "Business", "Empresarial", "Básico"],
            "resposta_correta": "Empresarial",
            "multipla_escolha": False,
            "explicacao": "O plano de suporte Empresarial oferece o mais alto nível de suporte, incluindo um Gerente Técnico de Contas dedicado e tempos de resposta rápidos para problemas críticos."
        },
        {
            "pergunta": "Quais das seguintes são características do AWS Free Tier?",
            "opcoes": ["Fornece acesso ilimitado a todos os serviços da AWS.", "Permite o uso de certos serviços da AWS sem custo por um tempo limitado ou até um determinado limite.", "É válido por um período de 12 meses, mas apenas para a conta raiz.", "É apenas para estudantes e não para empresas."],
            "resposta_correta": ["Permite o uso de certos serviços da AWS sem custo por um tempo limitado ou até um determinado limite.", "É válido por um período de 12 meses, mas apenas para a conta raiz."],
            "multipla_escolha": True,
            "explicacao": "O AWS Free Tier permite que os usuários experimentem os serviços da AWS gratuitamente, com limites específicos de uso por um período de 12 meses após a criação da conta."
        },
        {
            "pergunta": "Qual ferramenta pode ser usada para estimar o custo mensal de uso de um novo serviço da AWS?",
            "opcoes": ["AWS Cost Explorer", "AWS Simple Monthly Calculator", "AWS Trusted Advisor", "AWS Budgets"],
            "resposta_correta": "AWS Simple Monthly Calculator",
            "multipla_escolha": False,
            "explicacao": "O AWS Simple Monthly Calculator é uma ferramenta que ajuda a estimar os custos de uma nova arquitetura ou aplicação na AWS, antes de começar a usar os serviços."
        },
        {
            "pergunta": "O que a cobrança 'pagamento por uso' significa na AWS?",
            "opcoes": ["Você paga um valor fixo mensal, independentemente do uso.", "Você paga apenas pelos recursos que consome, sem taxas antecipadas ou contratos de longo prazo.", "Você deve pagar por um ano de uso de um serviço antecipadamente.", "A cobrança é baseada no número de usuários que acessam seu serviço."],
            "resposta_correta": "Você paga apenas pelos recursos que consome, sem taxas antecipadas ou contratos de longo prazo.",
            "multipla_escolha": False,
            "explicacao": "O modelo de pagamento por uso é um dos princípios da nuvem, onde você paga apenas pelos recursos que efetivamente consome, o que evita o desperdício de recursos e o alto custo inicial."
        }
    ]
}