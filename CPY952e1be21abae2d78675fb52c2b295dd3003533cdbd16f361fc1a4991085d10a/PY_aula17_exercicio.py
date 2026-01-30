# Código Completo do Exercício
import sqlite3


# Passo 1: Conectar/Criar o banco de dados
conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()
print("Banco de dados conectado com sucesso!\n")


# Passo 2: Criar a tabela Turmas
cursor.execute('''
CREATE TABLE IF NOT EXISTS turmas (
    id_turma INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_turma VARCHAR(50) NOT NULL,
    ano INTEGER NOT NULL,
    periodo VARCHAR(20)
)
''')
print("Tabela 'turmas' criada.\n")


# Passo 3: Criar a tabela Alunos com chave estrangeira
cursor.execute('''
CREATE TABLE IF NOT EXISTS alunos (
    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    id_turma INTEGER,
    FOREIGN KEY (id_turma) REFERENCES turmas(id_turma)
)
''')
print("Tabela 'alunos' criada.\n")


# Passo 4: Inserir turmas
turmas = [
    ('Turma A - Matemática', 2024, 'Manhã'),
    ('Turma B - História', 2024, 'Tarde'),
    ('Turma C - Ciências', 2024, 'Noite')
]
cursor.executemany('''
    INSERT INTO turmas (nome_turma, ano, periodo)
    VALUES (?, ?, ?)
''', turmas)
# OBS: para executar um INSERT de cada vez o cursor pode acionar o método "execute":
#    cursor.execute('''
#       INSERT INTO turmas (nome_turma, ano, periodo)
#       VALUES (?, ?, ?)
#    ''', ('Turma D - Geografia', 2024, 'Manhã'))

print(f"{cursor.rowcount} turmas inseridas.\n")


# Passo 5: Inserir alunos
alunos = [
    ('Ana Paula Silva', '2006-03-15', 1),
    ('Bruno Costa Santos', '2005-07-22', 1),
    ('Carla Souza Lima', '2006-11-10', 2),
    ('Daniel Oliveira', '2005-01-30', 2),
    ('Elena Ferreira', '2006-09-05', 3),
    ('Felipe Martins', '2005-12-18', 3)
]
cursor.executemany('''
    INSERT INTO alunos (nome, data_nascimento, id_turma)
    VALUES (?, ?, ?)
    ''', alunos)
print(f"{cursor.rowcount} alunos inseridos.\n")


# Salvar alterações
conexao.commit()


# Passo 6: Consultar todos os alunos
print("="*60)
print("TODOS OS ALUNOS:")
print("="*60)

cursor.execute('SELECT * FROM alunos')

for aluno in cursor.fetchall():
    print(f"ID: {aluno[0]}, Nome: {aluno[1]}, "
f"Nascimento: {aluno[2]}, Turma ID: {aluno[3]}")
    print("\n" + "="*60)
    print("TODAS AS TURMAS:")
    print("="*60)

cursor.execute('SELECT * FROM turmas')

for turma in cursor.fetchall():
    print(f"ID: {turma[0]}, Nome: {turma[1]}, "
          f"Ano: {turma[2]}, Período: {turma[3]}")