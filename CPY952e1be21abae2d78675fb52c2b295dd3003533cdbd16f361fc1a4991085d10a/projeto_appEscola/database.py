import sqlite3
from datetime import datetime

# Nome do arquivo do banco de dados
DB_NAME = "escola.db"

def conectar():
    """Cria e retorna uma conexão com o banco de dados."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas pelo nome
    return conn

def criar_tabelas():
    """Cria as tabelas caso não existam."""
    conn = conectar()
    cursor = conn.cursor()
    
    # Tabela de Turmas (Desafio Bônus)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano_letivo INTEGER NOT NULL
        )
    """)
    
    # Tabela de Alunos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_nascimento TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            email TEXT,
            id_turma INTEGER,
            FOREIGN KEY (id_turma) REFERENCES turmas (id)
        )
    """)
    
    conn.commit()
    conn.close()

# ==================== CRUD ALUNOS ====================

def adicionar_aluno(nome, data_nascimento, cpf, email, id_turma=None):
    """Insere um novo aluno no banco de dados."""
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO alunos (nome, data_nascimento, cpf, email, id_turma)
            VALUES (?, ?, ?, ?, ?)
        """, (nome, data_nascimento, cpf, email, id_turma))
        conn.commit()
        return True, "Aluno cadastrado com sucesso!"
    except sqlite3.IntegrityError:
        return False, "Erro: CPF já cadastrado no sistema!"
    except Exception as e:
        return False, f"Erro ao cadastrar: {str(e)}"
    finally:
        conn.close()

def buscar_alunos(filtro_nome=None, filtro_turma=None):
    """Busca alunos com filtros opcionais (nome e turma)."""
    conn = conectar()
    cursor = conn.cursor()
    
    query = """
        SELECT a.id, a.nome, a.data_nascimento, a.cpf, a.email, 
               t.nome as nome_turma, t.ano_letivo
        FROM alunos a
        LEFT JOIN turmas t ON a.id_turma = t.id
        WHERE 1=1
    """
    params = []
    
    if filtro_nome:
        query += " AND a.nome LIKE ?"
        params.append(f"%{filtro_nome}%")
    
    if filtro_turma:
        query += " AND a.id_turma = ?"
        params.append(filtro_turma)
    
    cursor.execute(query, params)
    resultados = cursor.fetchall()
    conn.close()
    
    return resultados

def buscar_aluno_por_id(aluno_id):
    """Busca um aluno específico pelo ID."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos WHERE id = ?", (aluno_id,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

def atualizar_aluno(aluno_id, nome, data_nascimento, cpf, email, id_turma=None):
    """Atualiza os dados de um aluno."""
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE alunos 
            SET nome = ?, data_nascimento = ?, cpf = ?, email = ?, id_turma = ?
            WHERE id = ?
        """, (nome, data_nascimento, cpf, email, id_turma, aluno_id))
        conn.commit()
        return True, "Dados atualizados com sucesso!"
    except sqlite3.IntegrityError:
        return False, "Erro: CPF pertence a outro aluno!"
    except Exception as e:
        return False, f"Erro ao atualizar: {str(e)}"
    finally:
        conn.close()

def excluir_aluno(aluno_id):
    """Exclui um aluno do banco de dados."""
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM alunos WHERE id = ?", (aluno_id,))
        conn.commit()
        return True, "Aluno excluído com sucesso!"
    except Exception as e:
        return False, f"Erro ao excluir: {str(e)}"
    finally:
        conn.close()

# ==================== CRUD TURMAS ====================

def adicionar_turma(nome, ano_letivo):
    """Adiciona uma nova turma."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO turmas (nome, ano_letivo) VALUES (?, ?)", 
                   (nome, ano_letivo))
    conn.commit()
    conn.close()

def listar_turmas():
    """Lista todas as turmas."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM turmas ORDER BY ano_letivo, nome")
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def buscar_turma_por_id(turma_id):
    """Busca uma turma pelo ID."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM turmas WHERE id = ?", (turma_id,))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

def estatisticas_turmas():
    """Retorna estatísticas de alunos por turma."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT t.nome, t.ano_letivo, COUNT(a.id) as total_alunos
        FROM turmas t
        LEFT JOIN alunos a ON t.id = a.id_turma
        GROUP BY t.id
        ORDER BY total_alunos DESC
    """)
    resultados = cursor.fetchall()
    conn.close()
    return resultados

# Inicializa o banco ao importar o módulo
criar_tabelas()