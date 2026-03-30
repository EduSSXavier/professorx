export const dados = {
  "themes": [
    {
      "id": "python-basico",
      "name": "Python Básico",
      "questions": [
        {
          "id": 1,
          "question": "Qual palavra-chave é usada para definir uma função em Python?",
          "options": ["function", "def", "func", "define"],
          "correct": 1
        },
        {
          "id": 2,
          "question": "Qual é o resultado de: 10 // 3 em Python?",
          "options": ["3.33", "3", "4", "3.0"],
          "correct": 1
        },
        {
          "id": 3,
          "question": "Como se escreve um comentário de uma linha em Python?",
          "options": ["// comentário", "/* comentário */", "# comentário", "-- comentário"],
          "correct": 2
        },
        {
          "id": 4,
          "question": "Qual método é usado para adicionar um elemento ao final de uma lista?",
          "options": ["add()", "append()", "insert()", "push()"],
          "correct": 1
        },
        {
          "id": 5,
          "question": "Qual tipo de dado representa True ou False em Python?",
          "options": ["int", "string", "boolean", "bool"],
          "correct": 3
        },
        {
          "id": 6,
          "question": "Como se cria uma lista vazia em Python?",
          "options": ["list = {}", "list = ()", "list = []", "list = <>"],
          "correct": 2
        },
        {
          "id": 7,
          "question": "Qual função é usada para exibir saída no console?",
          "options": ["echo()", "console.log()", "print()", "display()"],
          "correct": 2
        },
        {
          "id": 8,
          "question": "O que o operador ** faz em Python?",
          "options": ["Multiplicação", "Divisão", "Exponenciação", "Módulo"],
          "correct": 2
        },
        {
          "id": 9,
          "question": "Qual estrutura de dados em Python não permite elementos duplicados?",
          "options": ["Lista", "Tupla", "Dicionário", "Set"],
          "correct": 3
        },
        {
          "id": 10,
          "question": "Como se verifica o tipo de uma variável em Python?",
          "options": ["typeof()", "type()", "getType()", "varType()"],
          "correct": 1
        }
      ]
    },
    {
      "id": "python-oop",
      "name": "Prog. Orientada a Objetos em Python",
      "questions": [
        {
          "id": 1,
          "question": "Qual palavra-chave é usada para criar uma classe em Python?",
          "options": ["class", "Class", "define", "object"],
          "correct": 0
        },
        {
          "id": 2,
          "question": "Qual método é automaticamente chamado quando um objeto é criado?",
          "options": ["__init__", "__start__", "__create__", "__new__"],
          "correct": 0
        },
        {
          "id": 3,
          "question": "O que representa o parâmetro 'self' em métodos de classe?",
          "options": ["A classe pai", "A instância atual do objeto", "Um método estático", "O construtor"],
          "correct": 1
        },
        {
          "id": 4,
          "question": "Como se define um método privado em Python?",
          "options": ["private def metodo()", "def _metodo()", "def __metodo()", "def metodo_private()"],
          "correct": 2
        },
        {
          "id": 5,
          "question": "Qual conceito permite que uma classe herde características de outra?",
          "options": ["Polimorfismo", "Encapsulamento", "Herança", "Abstração"],
          "correct": 2
        },
        {
          "id": 6,
          "question": "Como se cria uma classe que herda de outra chamada 'Animal'?",
          "options": ["class Cachorro extends Animal:", "class Cachorro(Animal):", "class Cachorro inherits Animal:", "class Cachorro -> Animal:"],
          "correct": 1
        },
        {
          "id": 7,
          "question": "Qual decorador é usado para criar um método de classe?",
          "options": ["@staticmethod", "@classmethod", "@property", "@method"],
          "correct": 1
        },
        {
          "id": 8,
          "question": "O que é polimorfismo em POO?",
          "options": ["Ocultar dados internos", "Criar múltiplas classes", "Mesma interface com comportamentos diferentes", "Herdar de várias classes"],
          "correct": 2
        },
        {
          "id": 9,
          "question": "Qual decorador transforma um método em uma propriedade?",
          "options": ["@property", "@attribute", "@getter", "@field"],
          "correct": 0
        },
        {
          "id": 10,
          "question": "Como se chama o método pai dentro de uma classe filha?",
          "options": ["parent()", "base()", "super()", "inherit()"],
          "correct": 2
        }
      ]
    },
    {
      "id": "python-modulos",
      "name": "Módulos em Python",
      "questions": [
        {
          "id": 1,
          "question": "Qual palavra-chave é usada para importar um módulo em Python?",
          "options": ["include", "require", "import", "using"],
          "correct": 2
        },
        {
          "id": 2,
          "question": "Como importar apenas a função 'sqrt' do módulo math?",
          "options": ["import sqrt from math", "from math import sqrt", "import math.sqrt", "using math import sqrt"],
          "correct": 1
        },
        {
          "id": 3,
          "question": "Qual comando importa todas as funções de um módulo?",
          "options": ["import math.*", "from math import all", "from math import *", "import * from math"],
          "correct": 2
        },
        {
          "id": 4,
          "question": "Como dar um apelido ao importar um módulo?",
          "options": ["import numpy as np", "import numpy alias np", "import numpy -> np", "from numpy use np"],
          "correct": 0
        },
        {
          "id": 5,
          "question": "Qual módulo é usado para trabalhar com datas e horas?",
          "options": ["time", "datetime", "date", "calendar"],
          "correct": 1
        },
        {
          "id": 6,
          "question": "Qual módulo fornece funções matemáticas como sqrt e sin?",
          "options": ["mathematics", "calc", "math", "numpy"],
          "correct": 2
        },
        {
          "id": 7,
          "question": "Como criar um módulo personalizado em Python?",
          "options": ["Criar um arquivo .mod", "Criar um arquivo .py", "Criar um arquivo .module", "Usar o comando module"],
          "correct": 1
        },
        {
          "id": 8,
          "question": "Qual módulo é usado para gerar números aleatórios?",
          "options": ["rand", "random", "numbers", "generator"],
          "correct": 1
        },
        {
          "id": 9,
          "question": "O que a variável __name__ contém quando um módulo é executado diretamente?",
          "options": ["O nome do arquivo", "None", "'__main__'", "'__module__'"],
          "correct": 2
        },
        {
          "id": 10,
          "question": "Qual comando instala módulos externos via pip?",
          "options": ["pip download", "pip get", "pip install", "pip add"],
          "correct": 2
        }
      ]
    },
    {
      "id": "eng-social",
      "name": "Segurança - Engenharia Social",
      "questions": [
        {
          "id": 1,
          "question": "Você recebe um e-mail aparentemente do departamento de TI da sua empresa solicitando que você clique em um link para atualizar sua senha corporativa com urgência, pois sua conta será bloqueada em 24 horas. O remetente é 'ti-suporte@empresa-corp.net'. Qual é o melhor curso de ação?",
          "options": [
            "Clicar no link e alterar a senha imediatamente para evitar o bloqueio.",
            "Encaminhar o e-mail para colegas para ver se eles também receberam.",
            "Não clicar no link; acessar o portal de TI diretamente pelo navegador e reportar o e-mail como phishing ao time de segurança.",
            "Responder ao e-mail pedindo mais informações antes de agir."
          ],
          "correct": 2
        },
        {
          "id": 2,
          "question": "Ao navegar na internet, um pop-up avisa que seu computador está infectado com vírus e oferece um botão 'Remover Agora' que baixará um software de segurança gratuito. O que você deve fazer?",
          "options": [
            "Clicar em 'Remover Agora', pois o software gratuito irá limpar o vírus.",
            "Fechar o pop-up imediatamente pelo gerenciador de tarefas se necessário, e verificar seu computador com o antivírus corporativo oficial.",
            "Reiniciar o computador e clicar no link na próxima vez que aparecer.",
            "Compartilhar o link com colegas para que todos possam instalar a proteção."
          ],
          "correct": 1,
        },
        {
          "id": 3,
          "question": "Um colega lhe envia por mensagem um arquivo chamado 'relatorio_q3_final.pdf.exe' dizendo ser um relatório urgente. Ao passar o mouse, você percebe a extensão dupla. O que você faz?",
          "options": [
            "Abrir o arquivo pois veio de um colega conhecido e é urgente.",
            "Salvar na área de trabalho e abrir amanhã.",
            "Não abrir o arquivo; contactar o colega por outro canal para confirmar se ele realmente enviou e reportar ao time de TI.",
            "Renomear o arquivo removendo o '.exe' antes de abrir."
          ],
          "correct": 2
        },
        {
          "id": 4,
          "question": "Ao ligar seu computador pela manhã, você vê uma mensagem em tela cheia dizendo que seus arquivos foram criptografados e que você deve pagar R$5.000 em criptomoeda em 48 horas para recuperá-los. Qual a ação correta?",
          "options": [
            "Pagar o resgate imediatamente para recuperar os arquivos antes do prazo.",
            "Desligar o computador imediatamente, isolar o dispositivo da rede, não pagar o resgate e acionar a equipe de segurança e TI para iniciar o protocolo de resposta a incidentes.",
            "Continuar usando o computador para trabalhar enquanto decide o que fazer.",
            "Formatar o computador sozinho antes de chamar o suporte."
          ],
          "correct": 1
        },
        {
          "id": 5,
          "question": "Você percebe que um colega que pediu demissão está copiando grandes volumes de dados da empresa para um pendrive pessoal fora do horário habitual. O que você deve fazer?",
          "options": [
            "Ignorar, pois ele ainda está empregado e pode usar os dados.",
            "Confrontar o colega diretamente e pedir que ele pare.",
            "Reportar o comportamento suspeito ao gestor e ao time de segurança da informação imediatamente, sem confrontar o colega.",
            "Esperar para ver se ele realmente vai embora antes de fazer algo."
          ],
          "correct": 2
        },
        {
          "id": 6,
          "question": "Você recebe uma mensagem no WhatsApp de um número desconhecido dizendo ser do RH e pedindo que você confirme CPF e dados bancários para receber o 14º salário oferecido pela empresa. O que fazer?",
          "options": [
            "Enviar os dados, pois um 14º salário seria muito bem-vindo.",
            "Ligar para o número que enviou a mensagem para confirmar.",
            "Não fornecer nenhum dado; contactar o RH pelos canais oficiais da empresa para verificar a informação e reportar a tentativa de golpe.",
            "Pedir ao remetente mais provas de que é do RH antes de enviar."
          ],
          "correct": 2
        },
        {
          "id": 7,
          "question": "Você encontra um pendrive sem identificação no estacionamento da empresa com a etiqueta 'SALÁRIOS 2025'. O que você deve fazer?",
          "options": [
            "Conectar ao computador para identificar o dono do pendrive.",
            "Levar para casa e verificar no computador pessoal.",
            "Não conectar o pendrive em nenhum dispositivo e entregá-lo ao time de segurança da informação para análise forense.",
            "Jogar fora, pois não tem identificação."
          ],
          "correct": 2
        },
        {
          "id": 8,
          "question": "Você precisa enviar um contrato com dados pessoais de clientes para um parceiro externo. Qual é a forma mais segura de fazer isso?",
          "options": [
            "Enviar por e-mail normal, pois o parceiro é confiável.",
            "Postar o arquivo no grupo de WhatsApp da empresa.",
            "Utilizar uma plataforma aprovada pela empresa com criptografia, enviar o arquivo protegido por senha e comunicar a senha por um canal separado.",
            "Imprimir e enviar por correio sem rastreamento."
          ],
          "correct": 2
        },
        {
          "id": 9,
          "question": "Para prevenir ataques de ransomware na sua empresa, qual das práticas abaixo representa a camada de defesa mais eficaz?",
          "options": [
            "Pagar antecipadamente por chaves de descriptografia.",
            "Manter backups regulares e testados em local isolado (offline ou imutável), combinados com atualizações de sistema e treinamento de usuários.",
            "Desabilitar completamente o acesso à internet.",
            "Confiar apenas no antivírus para bloquear todos os ataques."
          ],
          "correct": 1
        },
        {
          "id": 10,
          "question": "A empresa está implementando um novo sistema e percebe que um funcionário com acesso privilegiado está acessando bancos de dados de outros departamentos sem justificativa de negócio. Qual é a melhor abordagem?",
          "options": [
            "Não fazer nada para não criar conflito com o funcionário.",
            "Dar mais permissões ao funcionário para que ele entenda melhor os sistemas.",
            "Aplicar o princípio do menor privilégio, revisar e revogar acessos desnecessários, ativar logs de auditoria detalhados e investigar o comportamento com o time de segurança.",
            "Enviar um e-mail para o funcionário perguntando por que ele está acessando esses dados."
          ],
          "correct": 2
        }
      ]
    },
    {
      "id": "compil-lexer",
      "name": "Compiladores - Analise Léxica",
      "questions": [
        {
          "id": 1,
          "question": "Qual é a principal tarefa do analisador léxico na primeira fase de um compilador?",
          "options": [
            "Ler os caracteres de entrada e produzir uma sequência de tokens.",
            "Agrupar os tokens em coleções aninhadas com significado coletivo.",
            "Verificar se os componentes de um programa se combinam de forma significativa.",
            "Traduzir o código intermediário para a linguagem de máquina alvo."
          ],
          "correct": 0
        },
        {
          "id": 2,
          "question": "Como é definida a sequência de caracteres do programa fonte que forma um token?",
          "options": [
            "Atributo léxico",
            "Lexema",
            "Expressão regular",
            "Símbolo terminal"
          ],
          "correct": 1
        },
        {
          "id": 3,
          "question": "O que um 'token' representa no contexto da análise léxica?",
          "options": [
            "Uma unidade lógica com um significado coletivo.",
            "O endereço de memória de uma variável.",
            "Uma regra de produção da gramática livre de contexto.",
            "Um erro de sintaxe detectado no código-fonte."
          ],
          "correct": 0
        },
        {
          "id": 4,
          "question": "Qual das seguintes tarefas NÃO é comumente realizada por um analisador léxico?",
          "options": [
            "Remoção de espaços em branco e comentários.",
            "Identificação de palavras-chave e operadores.",
            "Verificação da compatibilidade de tipos em expressões aritméticas.",
            "Inserção de identificadores na tabela de símbolos."
          ],
          "correct": 2
        },
        {
          "id": 5,
          "question": "Qual notação é mais apropriada e comumente usada para especificar os padrões de tokens?",
          "options": [
            "BNF (Backus-Naur Form)",
            "Expressões Regulares",
            "Diagramas Sintáticos",
            "Árvores de Derivação"
          ],
          "correct": 1
        },
        {
          "id": 6,
          "question": "Qual modelo matemático é utilizado como base para implementar o reconhecimento de tokens em um analisador léxico?",
          "options": [
            "Máquina de Turing",
            "Autômato de Pilha",
            "Autômato Finito",
            "Grafo de Fluxo de Controle"
          ],
          "correct": 2
        },
        {
          "id": 7,
          "question": "Por que o analisador léxico tem uma capacidade limitada de detectar erros no programa?",
          "options": [
            "Porque ele não tem acesso à tabela de símbolos.",
            "Porque ele possui uma visão extremamente local do programa fonte.",
            "Porque ele só analisa linguagens regulares (Tipo 3).",
            "Porque ele é a última fase do processo de compilação."
          ],
          "correct": 1
        },
        {
          "id": 8,
          "question": "Qual é o objetivo técnico de utilizar 'pares de buffers' e 'sentinelas' na análise léxica?",
          "options": [
            "Facilitar a recuperação de erros sintáticos.",
            "Reduzir o tempo de compilação na fase de síntese.",
            "Acelerar a leitura de caracteres e o reconhecimento de padrões que exigem lookahead.",
            "Garantir que a gramática da linguagem seja livre de contexto."
          ],
          "correct": 2
        },
        {
          "id": 9,
          "question": "Qual ferramenta é amplamente utilizada para gerar automaticamente analisadores léxicos a partir de expressões regulares?",
          "options": [
            "Yacc",
            "Bison",
            "Lex (ou Flex)",
            "Gcc"
          ],
          "correct": 2
        },
        {
          "id": 10,
          "question": "Na interação com outras fases, para onde o analisador léxico envia o fluxo de tokens?",
          "options": [
            "Para o Gerador de Código Intermediário.",
            "Para o Analisador Sintático (Parser).",
            "Diretamente para a Tabela de Símbolos.",
            "Para o Otimizador de Código."
          ],
          "correct": 1
        }
      ]
    }
  ]
}
