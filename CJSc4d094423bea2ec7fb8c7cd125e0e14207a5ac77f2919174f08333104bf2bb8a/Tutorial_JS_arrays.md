# Arrays: Criando e Acessando Listas

## 1. Introdução: Coleções de Dados

Na programação, frequentemente precisamos trabalhar com múltiplos valores relacionados. Imagine que você precisa armazenar as notas de 30 alunos em uma prova. Criar 30 variáveis separadas (nota1, nota2, nota3...) seria impraticável e difícil de gerenciar.

É aqui que entram as **coleções de dados**: estruturas que permitem armazenar e manipular grupos de valores de forma organizada e eficiente. Em vez de gerenciar dezenas de variáveis individuais, você pode trabalhar com uma única estrutura que contém todos os dados relacionados.

**Exemplo conceitual:**
```javascript
// Sem coleções (difícil de gerenciar)
let aluno1 = "João";
let aluno2 = "Maria";
let aluno3 = "Pedro";

// Com coleções (organizado e escalável)
let alunos = ["João", "Maria", "Pedro"];
```

As coleções permitem que você agrupe valores logicamente relacionados, facilitando operações como busca, ordenação, filtragem e manipulação de dados em conjunto.

---

## 2. O que são Arrays e Para que Servem

Um **array** é uma estrutura de dados que armazena uma coleção ordenada de elementos. Cada elemento ocupa uma posição específica, chamada de **índice**, que começa em 0 (zero).

**Características principais:**
- Armazenam múltiplos valores em uma única variável
- Os elementos são ordenados e acessados por índices numéricos
- Podem conter dados de qualquer tipo (números, strings, booleanos, objetos, até outros arrays)
- São dinâmicos: podem crescer ou diminuir de tamanho

**Para que servem:**
- Armazenar listas de itens (produtos, usuários, tarefas)
- Processar conjuntos de dados (cálculos, estatísticas)
- Gerenciar sequências de informações (histórico, registros)
- Criar estruturas de dados mais complexas

**Exemplo:**
```javascript
// Array de números
let numeros = [10, 20, 30, 40, 50];

// Array de strings
let frutas = ["maçã", "banana", "laranja"];

// Array misto (não recomendado, mas possível)
let misto = [42, "texto", true, null];

console.log(frutas); // ["maçã", "banana", "laranja"]
```

---

## 3. Criação, Acesso e Modificação de Elementos

### Criação de Arrays

Existem duas formas principais de criar arrays em JavaScript:

**Sintaxe literal (mais comum):**
```javascript
let vazio = [];
let numeros = [1, 2, 3, 4, 5];
let nomes = ["Ana", "Bruno", "Carlos"];
```

**Usando o construtor Array:**
```javascript
let array1 = new Array();        // array vazio
let array2 = new Array(5);       // array com 5 posições vazias
let array3 = new Array(1, 2, 3); // array com elementos [1, 2, 3]
```

### Acesso a Elementos

Os elementos são acessados através de seus índices, usando colchetes `[]`. Lembre-se: **o primeiro índice é 0**.

**Exemplo:**
```javascript
let cores = ["vermelho", "verde", "azul", "amarelo"];

console.log(cores[0]); // "vermelho" (primeiro elemento)
console.log(cores[2]); // "azul" (terceiro elemento)
console.log(cores[5]); // undefined (índice não existe)

// Acessar o último elemento
let ultimoIndice = cores.length - 1;
console.log(cores[ultimoIndice]); // "amarelo"
```

### Modificação de Elementos

Para modificar um elemento, basta atribuir um novo valor ao índice desejado:

**Exemplo:**
```javascript
let animais = ["gato", "cachorro", "coelho"];

console.log(animais); // ["gato", "cachorro", "coelho"]

// Modificar o segundo elemento
animais[1] = "papagaio";

console.log(animais); // ["gato", "papagaio", "coelho"]

// Adicionar elemento em posição específica
animais[3] = "peixe";

console.log(animais); // ["gato", "papagaio", "coelho", "peixe"]
```

---

## 4. Tamanho do Array (length)

A propriedade `length` retorna o número de elementos presentes no array. É uma das propriedades mais utilizadas ao trabalhar com arrays.

**Características:**
- É uma propriedade, não um método (não usa parênteses)
- Retorna sempre um número inteiro
- Pode ser modificada para alterar o tamanho do array

**Exemplo:**
```javascript
let numeros = [10, 20, 30, 40, 50];

console.log(numeros.length); // 5

// Array vazio tem length 0
let vazio = [];
console.log(vazio.length); // 0

// Usando length em condições
if (numeros.length > 0) {
    console.log("O array contém elementos");
}

// Modificando o length (trunca o array)
numeros.length = 3;
console.log(numeros); // [10, 20, 30]

// Aumentar o length cria posições vazias
numeros.length = 5;
console.log(numeros); // [10, 20, 30, empty × 2]
```

**Uso prático:**
```javascript
let notas = [7.5, 8.0, 9.5, 6.0];
let soma = 0;

// Usar length para calcular média
for (let i = 0; i < notas.length; i++) {
    soma += notas[i];
}

let media = soma / notas.length;
console.log("Média:", media); // Média: 7.75
```

---

## 5. Iteração com for e while

Iterar (ou percorrer) um array significa acessar cada elemento sequencialmente para realizar operações. Os loops `for` e `while` são as estruturas mais básicas para essa tarefa.

### Iteração com for

O loop `for` é ideal para percorrer arrays, pois permite controle preciso sobre o índice:

**Exemplo:**
```javascript
let frutas = ["maçã", "banana", "laranja", "uva"];

// For tradicional
for (let i = 0; i < frutas.length; i++) {
    console.log("Índice " + i + ": " + frutas[i]);
}
// Saída:
// Índice 0: maçã
// Índice 1: banana
// Índice 2: laranja
// Índice 3: uva

// Percorrer de trás para frente
for (let i = frutas.length - 1; i >= 0; i--) {
    console.log(frutas[i]);
}
// Saída: uva, laranja, banana, maçã
```

### Iteração com while

O loop `while` também pode ser usado, embora seja menos comum para arrays:

**Exemplo:**
```javascript
let numeros = [5, 10, 15, 20, 25];
let i = 0;

while (i < numeros.length) {
    console.log("Número:", numeros[i]);
    i++;
}
// Saída:
// Número: 5
// Número: 10
// Número: 15
// Número: 20
// Número: 25

// Buscar elemento específico
let produtos = ["notebook", "mouse", "teclado", "monitor"];
let buscado = "teclado";
let encontrado = false;
let indice = 0;

while (indice < produtos.length && !encontrado) {
    if (produtos[indice] === buscado) {
        encontrado = true;
        console.log("Produto encontrado no índice:", indice);
    }
    indice++;
}
```

---

## 6. Inserção, Remoção e Substituição Básica

Além de acessar e modificar elementos existentes, frequentemente precisamos adicionar ou remover elementos dos arrays.

### Inserção

**No final (push):**
```javascript
let numeros = [1, 2, 3];

numeros.push(4);
console.log(numeros); // [1, 2, 3, 4]

numeros.push(5, 6);
console.log(numeros); // [1, 2, 3, 4, 5, 6]
```

**No início (unshift):**
```javascript
let cores = ["verde", "azul"];

cores.unshift("vermelho");
console.log(cores); // ["vermelho", "verde", "azul"]
```

### Remoção

**Do final (pop):**
```javascript
let frutas = ["maçã", "banana", "laranja"];

let removida = frutas.pop();
console.log(removida);  // "laranja"
console.log(frutas);    // ["maçã", "banana"]
```

**Do início (shift):**
```javascript
let animais = ["gato", "cachorro", "coelho"];

let primeiro = animais.shift();
console.log(primeiro); // "gato"
console.log(animais);  // ["cachorro", "coelho"]
```

### Substituição

Substituir elementos é simples: acesse o índice e atribua um novo valor:

**Exemplo completo:**
```javascript
let tarefas = ["estudar", "exercitar", "ler"];

// Adicionar tarefas
tarefas.push("cozinhar");
console.log(tarefas); // ["estudar", "exercitar", "ler", "cozinhar"]

// Substituir tarefa
tarefas[1] = "correr";
console.log(tarefas); // ["estudar", "correr", "ler", "cozinhar"]

// Remover última tarefa
tarefas.pop();
console.log(tarefas); // ["estudar", "correr", "ler"]

// Adicionar no início
tarefas.unshift("acordar");
console.log(tarefas); // ["acordar", "estudar", "correr", "ler"]

// Remover primeira tarefa
tarefas.shift();
console.log(tarefas); // ["estudar", "correr", "ler"]
```

### Métodos Avançados: slice e splice

Além dos métodos básicos, JavaScript oferece `slice()` e `splice()` para operações mais sofisticadas com arrays.

#### slice() - Copiar Parte do Array

O método `slice()` **extrai** uma parte do array e retorna um **novo array**, sem modificar o array original.

**Sintaxe:** `array.slice(início, fim)`
- `início`: índice inicial (inclusivo)
- `fim`: índice final (exclusivo) - opcional

**Exemplo:**
```javascript
let numeros = [10, 20, 30, 40, 50, 60];

// Copiar do índice 1 ao 4 (não inclui o 4)
let parte = numeros.slice(1, 4);
console.log(parte);    // [20, 30, 40]
console.log(numeros);  // [10, 20, 30, 40, 50, 60] - original intacto

// Copiar do índice 2 até o final
let resto = numeros.slice(2);
console.log(resto);    // [30, 40, 50, 60]

// Copiar os últimos 3 elementos (índices negativos)
let ultimos = numeros.slice(-3);
console.log(ultimos);  // [40, 50, 60]

// Copiar todo o array (clonar)
let copia = numeros.slice();
console.log(copia);    // [10, 20, 30, 40, 50, 60]
```

**Uso prático:**
```javascript
let frutas = ["maçã", "banana", "laranja", "uva", "manga", "abacaxi"];

// Pegar as 3 primeiras frutas
let primeiras = frutas.slice(0, 3);
console.log("Primeiras:", primeiras); // ["maçã", "banana", "laranja"]

// Pegar frutas do meio
let meio = frutas.slice(2, 5);
console.log("Do meio:", meio); // ["laranja", "uva", "manga"]
```

#### splice() - Modificar o Array Original

O método `splice()` **modifica** o array original, podendo **remover**, **adicionar** ou **substituir** elementos.

**Sintaxe:** `array.splice(início, quantidade, item1, item2, ...)`
- `início`: índice onde começar a modificação
- `quantidade`: número de elementos a remover
- `item1, item2, ...`: elementos a adicionar (opcional)

**Retorno:** Array com os elementos removidos

**Exemplo 1 - Remover elementos:**
```javascript
let cores = ["vermelho", "verde", "azul", "amarelo", "roxo"];

// Remover 2 elementos a partir do índice 1
let removidas = cores.splice(1, 2);
console.log(removidas); // ["verde", "azul"]
console.log(cores);     // ["vermelho", "amarelo", "roxo"]
```

**Exemplo 2 - Adicionar elementos:**
```javascript
let numeros = [1, 2, 5, 6];

// Adicionar elementos no índice 2 (sem remover nada)
numeros.splice(2, 0, 3, 4);
console.log(numeros); // [1, 2, 3, 4, 5, 6]
```

**Exemplo 3 - Substituir elementos:**
```javascript
let animais = ["gato", "cachorro", "coelho", "hamster"];

// Remover 2 elementos e adicionar 3 novos no índice 1
animais.splice(1, 2, "papagaio", "peixe", "tartaruga");
console.log(animais); // ["gato", "papagaio", "peixe", "tartaruga", "hamster"]
```

**Exemplo 4 - Remover até o final:**
```javascript
let letras = ["a", "b", "c", "d", "e", "f"];

// Remover todos os elementos a partir do índice 3
letras.splice(3);
console.log(letras); // ["a", "b", "c"]
```

**Comparação slice vs splice:**
```javascript
let original = [1, 2, 3, 4, 5];

// slice - NÃO modifica o original
let copiaSlice = original.slice(1, 3);
console.log("slice:", copiaSlice);  // [2, 3]
console.log("original:", original); // [1, 2, 3, 4, 5]

// splice - MODIFICA o original
let removidosSplice = original.splice(1, 3);
console.log("splice removidos:", removidosSplice); // [2, 3, 4]
console.log("original após splice:", original);    // [1, 5]
```

---

## Exercícios de Fixação

### Exercício 1 - Básico: Soma de Elementos
Crie um array com 5 números e calcule a soma de todos os elementos usando um loop `for`.

**Solução:**
```javascript
let numeros = [5, 10, 15, 20, 25];
let soma = 0;

for (let i = 0; i < numeros.length; i++) {
    soma += numeros[i];
}

console.log("Soma total:", soma); // Soma total: 75
```

---

### Exercício 2 - Básico/Intermediário: Contar Ocorrências
Crie um array de strings e conte quantas vezes uma palavra específica aparece nele.

**Solução:**
```javascript
let palavras = ["sol", "lua", "sol", "estrela", "sol", "lua"];
let palavraBusca = "sol";
let contador = 0;

for (let i = 0; i < palavras.length; i++) {
    if (palavras[i] === palavraBusca) {
        contador++;
    }
}

console.log("A palavra '" + palavraBusca + "' aparece " + contador + " vezes");
// A palavra 'sol' aparece 3 vezes
```

---

### Exercício 3 - Intermediário: Inverter Array
Crie um programa que inverta a ordem dos elementos de um array sem usar métodos prontos como `reverse()`.

**Solução:**
```javascript
let original = [1, 2, 3, 4, 5];
let invertido = [];

for (let i = original.length - 1; i >= 0; i--) {
    invertido.push(original[i]);
}

console.log("Array original:", original);
console.log("Array invertido:", invertido);
// Array original: [1, 2, 3, 4, 5]
// Array invertido: [5, 4, 3, 2, 1]
```

---

### Exercício 4 - Intermediário: Maior e Menor Valor
Encontre o maior e o menor valor em um array de números usando apenas loops.

**Solução:**
```javascript
let numeros = [45, 12, 89, 23, 67, 34, 91, 8];
let maior = numeros[0];
let menor = numeros[0];

for (let i = 1; i < numeros.length; i++) {
    if (numeros[i] > maior) {
        maior = numeros[i];
    }
    if (numeros[i] < menor) {
        menor = numeros[i];
    }
}

console.log("Maior valor:", maior); // Maior valor: 91
console.log("Menor valor:", menor); // Menor valor: 8
```

---

### Exercício 5 - Intermediário/Avançado: Remover Duplicatas
Crie um programa que remova elementos duplicados de um array, mantendo apenas a primeira ocorrência de cada elemento.

**Solução:**
```javascript
let numeros = [1, 2, 3, 2, 4, 1, 5, 3, 6];
let semDuplicatas = [];

for (let i = 0; i < numeros.length; i++) {
    let jaExiste = false;
    
    // Verificar se o elemento já está no array semDuplicatas
    for (let j = 0; j < semDuplicatas.length; j++) {
        if (numeros[i] === semDuplicatas[j]) {
            jaExiste = true;
            break;
        }
    }
    
    // Se não existe, adicionar
    if (!jaExiste) {
        semDuplicatas.push(numeros[i]);
    }
}

console.log("Array original:", numeros);
console.log("Sem duplicatas:", semDuplicatas);
// Array original: [1, 2, 3, 2, 4, 1, 5, 3, 6]
// Sem duplicatas: [1, 2, 3, 4, 5, 6]
```

---

## Desafio Final

Agora que você domina os conceitos fundamentais de arrays, está pronto para o desafio final!

**[Clique aqui para acessar o Desafio Final: Sistema de Gerenciamento de Biblioteca](#)**

O desafio consiste em criar um sistema completo de gerenciamento de biblioteca que consolida todos os conceitos aprendidos: criação de arrays, acesso a elementos, iteração com loops, inserção, remoção, modificação e lógica de programação para criar um sistema funcional e útil.

---

## Conclusão

Parabéns por concluir este tutorial! Você aprendeu:

✅ O conceito de coleções de dados e arrays  
✅ Como criar, acessar e modificar elementos  
✅ Trabalhar com a propriedade `length`  
✅ Iterar usando `for` e `while`  
✅ Manipular arrays com métodos básicos e avançados  
✅ Usar `slice()` e `splice()` para operações complexas  

Continue praticando com os exercícios e o desafio final para solidificar seu conhecimento!