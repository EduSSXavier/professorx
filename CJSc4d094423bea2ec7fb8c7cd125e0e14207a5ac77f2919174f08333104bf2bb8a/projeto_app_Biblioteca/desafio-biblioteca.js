// ====================================================
// DESAFIO FINAL: SISTEMA DE GERENCIAMENTO DE BIBLIOTECA
// ====================================================

/*
OBJETIVO:
Criar um sistema completo de gerenciamento de biblioteca que permita:

1. CADASTRAR LIVROS com as seguintes informações:
   - Título
   - Autor
   - Ano de publicação
   - Status (disponível ou emprestado)

2. FUNCIONALIDADES DO SISTEMA:
   - Adicionar novos livros
   - Listar todos os livros
   - Buscar livros por título ou autor
   - Emprestar livro (mudar status para emprestado)
   - Devolver livro (mudar status para disponível)
   - Remover livro do acervo
   - Listar apenas livros disponíveis
   - Listar apenas livros emprestados
   - Calcular estatísticas (total de livros, disponíveis, emprestados)
*/

// ============================================
// EXPLICAÇÃO DO DESAFIO
// ============================================

/*
CONCEITOS APLICADOS:

1. ESTRUTURA DE DADOS COMPLEXA
   - Cada livro é um objeto com múltiplas propriedades
   - Os objetos são armazenados em um array (biblioteca)
   - Demonstra como arrays podem conter dados estruturados

2. OPERAÇÕES CRUD (Create, Read, Update, Delete)
   - CREATE: adicionarLivro() - adiciona novos livros ao array
   - READ: listarTodos(), buscarPorTitulo(), buscarPorAutor()
   - UPDATE: emprestarLivro(), devolverLivro() - modifica status
   - DELETE: removerLivro() - remove elementos do array

3. BUSCA E FILTRAGEM
   - Implementa buscas usando indexOf() para comparação parcial
   - Usa toLowerCase() para tornar a busca case-insensitive
   - Armazena resultados encontrados em arrays temporários

4. MANIPULAÇÃO DE STATUS
   - Gerencia estados dos livros (disponível/emprestado)
   - Valida operações (não emprestar livro já emprestado)
   - Controla o fluxo de empréstimo/devolução

5. ESTATÍSTICAS E ANÁLISE
   - Percorre o array para calcular totais
   - Calcula percentuais e gera relatórios
   - Demonstra uso prático de contadores e loops

6. REMOÇÃO MANUAL DE ELEMENTOS
   - Implementa remoção sem usar splice()
   - Desloca elementos manualmente para preencher o espaço
   - Usa pop() para remover o último elemento duplicado

7. VALIDAÇÃO E TRATAMENTO DE ERROS
   - Verifica se livros existem antes de operar
   - Retorna mensagens apropriadas ao usuário
   - Usa flags (booleanos) para controle de fluxo

DESAFIOS EXTRAS PARA PRATICAR:

1. Adicione uma função para ordenar livros por título ou ano
2. Implemente um sistema de categorias (ficção, não-ficção, etc.)
3. Crie um histórico de empréstimos com datas
4. Adicione limite de livros que podem ser emprestados
5. Implemente busca por ano ou intervalo de anos
6. Crie função para exportar/importar dados da biblioteca
7. Adicione avaliações (1-5 estrelas) aos livros
8. Implemente reserva de livros emprestados

DICAS DE MELHORIAS:

- Use slice() para criar cópias de arrays ao buscar
- Use splice() para remover elementos de forma mais eficiente
- Considere adicionar IDs únicos aos livros
- Implemente validação de dados de entrada
- Adicione função para editar informações de livros existentes
*/ SOLUÇÃO
// ============================================

// Array para armazenar os livros
let biblioteca = [];

// Função para adicionar um livro
function adicionarLivro(titulo, autor, ano) {
    let livro = {
        titulo: titulo,
        autor: autor,
        ano: ano,
        status: "disponível"
    };
    biblioteca.push(livro);
    console.log("Livro '" + titulo + "' adicionado com sucesso!");
}

// Função para listar todos os livros
function listarTodos() {
    console.log("\n=== TODOS OS LIVROS ===");
    if (biblioteca.length === 0) {
        console.log("Nenhum livro cadastrado.");
        return;
    }
    
    for (let i = 0; i < biblioteca.length; i++) {
        console.log("\nLivro " + (i + 1) + ":");
        console.log("  Título: " + biblioteca[i].titulo);
        console.log("  Autor: " + biblioteca[i].autor);
        console.log("  Ano: " + biblioteca[i].ano);
        console.log("  Status: " + biblioteca[i].status);
    }
}

// Função para buscar livros por título
function buscarPorTitulo(titulo) {
    console.log("\n=== BUSCA POR TÍTULO: " + titulo + " ===");
    let encontrados = [];
    
    for (let i = 0; i < biblioteca.length; i++) {
        if (biblioteca[i].titulo.toLowerCase().indexOf(titulo.toLowerCase()) !== -1) {
            encontrados.push(biblioteca[i]);
        }
    }
    
    if (encontrados.length === 0) {
        console.log("Nenhum livro encontrado.");
    } else {
        for (let i = 0; i < encontrados.length; i++) {
            console.log("\nEncontrado:");
            console.log("  Título: " + encontrados[i].titulo);
            console.log("  Autor: " + encontrados[i].autor);
            console.log("  Status: " + encontrados[i].status);
        }
    }
}

// Função para buscar livros por autor
function buscarPorAutor(autor) {
    console.log("\n=== BUSCA POR AUTOR: " + autor + " ===");
    let encontrados = [];
    
    for (let i = 0; i < biblioteca.length; i++) {
        if (biblioteca[i].autor.toLowerCase().indexOf(autor.toLowerCase()) !== -1) {
            encontrados.push(biblioteca[i]);
        }
    }
    
    if (encontrados.length === 0) {
        console.log("Nenhum livro encontrado.");
    } else {
        for (let i = 0; i < encontrados.length; i++) {
            console.log("\nEncontrado:");
            console.log("  Título: " + encontrados[i].titulo);
            console.log("  Autor: " + encontrados[i].autor);
            console.log("  Status: " + encontrados[i].status);
        }
    }
}

// Função para emprestar livro
function emprestarLivro(titulo) {
    let encontrado = false;
    
    for (let i = 0; i < biblioteca.length; i++) {
        if (biblioteca[i].titulo.toLowerCase() === titulo.toLowerCase()) {
            if (biblioteca[i].status === "disponível") {
                biblioteca[i].status = "emprestado";
                console.log("Livro '" + titulo + "' emprestado com sucesso!");
                encontrado = true;
                break;
            } else {
                console.log("Livro '" + titulo + "' já está emprestado.");
                encontrado = true;
                break;
            }
        }
    }
    
    if (!encontrado) {
        console.log("Livro '" + titulo + "' não encontrado.");
    }
}

// Função para devolver livro
function devolverLivro(titulo) {
    let encontrado = false;
    
    for (let i = 0; i < biblioteca.length; i++) {
        if (biblioteca[i].titulo.toLowerCase() === titulo.toLowerCase()) {
            if (biblioteca[i].status === "emprestado") {
                biblioteca[i].status = "disponível";
                console.log("Livro '" + titulo + "' devolvido com sucesso!");
                encontrado = true;
                break;
            } else {
                console.log("Livro '" + titulo + "' já está disponível.");
                encontrado = true;
                break;
            }
        }
    }
    
    if (!encontrado) {
        console.log("Livro '" + titulo + "' não encontrado.");
    }
}

// Função para remover livro
function removerLivro(titulo) {
    let indiceRemover = -1;
    
    for (let i = 0; i < biblioteca.length; i++) {
        if (biblioteca[i].titulo.toLowerCase() === titulo.toLowerCase()) {
            indiceRemover = i;
            break;
        }
    }
    
    if (indiceRemover !== -1) {
        // Remover o livro deslocando os elementos
        for (let i = indiceRemover; i < biblioteca.length - 1; i++) {
            biblioteca[i] = biblioteca[i + 1];
        }
        biblioteca.pop();
        console.log("Livro '" + titulo + "' removido com sucesso!");
    } else {
        console.log("Livro '" + titulo + "' não encontrado.");
    }
}

// Função para listar apenas livros disponíveis
function listarDisponiveis() {
    console.log("\n=== LIVROS DISPONÍVEIS ===");
    let contador = 0;
    
    for (let i = 0; i < biblioteca.length; i++) {
        if (biblioteca[i].status === "disponível") {
            contador++;
            console.log("\n" + contador + ". " + biblioteca[i].titulo);
            console.log("   Autor: " + biblioteca[i].autor);
        }
    }
    
    if (contador === 0) {
        console.log("Nenhum livro disponível no momento.");
    }
}

// Função para listar apenas livros emprestados
function listarEmprestados() {
    console.log("\n=== LIVROS EMPRESTADOS ===");
    let contador = 0;
    
    for (let i = 0; i < biblioteca.length; i++) {
        if (biblioteca[i].status === "emprestado") {
            contador++;
            console.log("\n" + contador + ". " + biblioteca[i].titulo);
            console.log("   Autor: " + biblioteca[i].autor);
        }
    }
    
    if (contador === 0) {
        console.log("Nenhum livro emprestado no momento.");
    }
}

// Função para exibir estatísticas
function exibirEstatisticas() {
    let totalLivros = biblioteca.length;
    let disponiveis = 0;
    let emprestados = 0;
    
    for (let i = 0; i < biblioteca.length; i++) {
        if (biblioteca[i].status === "disponível") {
            disponiveis++;
        } else {
            emprestados++;
        }
    }
    
    console.log("\n=== ESTATÍSTICAS DA BIBLIOTECA ===");
    console.log("Total de livros: " + totalLivros);
    console.log("Livros disponíveis: " + disponiveis);
    console.log("Livros emprestados: " + emprestados);
    
    if (totalLivros > 0) {
        let percentualDisponivel = (disponiveis / totalLivros * 100).toFixed(1);
        console.log("Percentual disponível: " + percentualDisponivel + "%");
    }
}

// ============================================
// TESTANDO O SISTEMA
// ============================================

console.log("=== SISTEMA DE GERENCIAMENTO DE BIBLIOTECA ===\n");

// Adicionar livros
adicionarLivro("1984", "George Orwell", 1949);
adicionarLivro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954);
adicionarLivro("Dom Casmurro", "Machado de Assis", 1899);
adicionarLivro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997);
adicionarLivro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943);

// Listar todos os livros
listarTodos();

// Emprestar alguns livros
console.log("\n--- EMPRÉSTIMOS ---");
emprestarLivro("1984");
emprestarLivro("Harry Potter e a Pedra Filosofal");

// Listar livros disponíveis e emprestados
listarDisponiveis();
listarEmprestados();

// Buscar livros
buscarPorTitulo("Senhor");
buscarPorAutor("Machado");

// Devolver um livro
console.log("\n--- DEVOLUÇÕES ---");
devolverLivro("1984");

// Tentar emprestar livro já emprestado
console.log("\n--- TENTATIVA DE EMPRÉSTIMO DUPLICADO ---");
emprestarLivro("Harry Potter e a Pedra Filosofal");

// Remover um livro
console.log("\n--- REMOÇÃO ---");
removerLivro("O Pequeno Príncipe");

// Exibir estatísticas finais
exibirEstatisticas();

// Listar todos novamente para ver as mudanças
listarTodos();

// ============================================
//