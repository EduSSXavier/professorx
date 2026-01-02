// Importando perguntas do teste
import { dados } from './dados_quiz.js';

// script.js - Quiz com seleção de temas via JSON Server
let themes = [];
let selectedTheme = null;
let quizData = [];
let currentQuestion = 0;
let score = 0;
let selectedOption = null;

const themeSelection = document.getElementById('theme-selection');
const themesList = document.getElementById('themes-list');
const quizSection = document.getElementById('quiz');
const questionEl = document.getElementById('question');
const optionsEl = document.getElementById('options');
const nextBtn = document.getElementById('next-btn');
const resultSection = document.getElementById('result');
const scoreEl = document.getElementById('score');
const restartBtn = document.getElementById('restart-btn');

nextBtn.addEventListener('click', nextQuestion);
restartBtn.addEventListener('click', restartQuiz);

// Iniciar carregamento dos temas
window.addEventListener('load', loadThemes);

// Carregar temas da API ao iniciar
//async function loadThemes() {
function loadThemes() {
    try {
        //const response = await fetch(API_URL);
        //if (!response.ok) throw new Error('Erro na API');
        //themes = await response.json();
        themes = dados["themes"];
        displayThemes();
    } catch (error) {
        console.error('Erro ao carregar temas:', error);
        themesList.innerHTML = '<p style="color:red;">Erro ao conectar ao servidor. Verifique se o JSON Server está rodando.</p>';
    }
}

function displayThemes() {
    themesList.innerHTML = '';
    themes.forEach(theme => {
        const btn = document.createElement('button');
        btn.classList.add('theme-button');
        btn.textContent = `${theme.name} (${theme.questions.length} perguntas)`;
        btn.addEventListener('click', () => startQuizWithTheme(theme));
        themesList.appendChild(btn);
    });
}

function startQuizWithTheme(theme) {
    selectedTheme = theme;
    quizData = theme.questions;
    currentQuestion = 0;
    score = 0;

    themeSelection.style.display = 'none';
    quizSection.style.display = 'block';
    showQuestion();
}

function showQuestion() {
    const q = quizData[currentQuestion];
    questionEl.textContent = q.question;
    optionsEl.innerHTML = '';
    selectedOption = null;
    nextBtn.disabled = true;

    q.options.forEach((option, index) => {
        const optionEl = document.createElement('div');
        optionEl.classList.add('option');
        optionEl.textContent = option;
        optionEl.addEventListener('click', () => selectOption(index, optionEl));
        optionsEl.appendChild(optionEl);
    });
}

function selectOption(index, element) {
    const options = optionsEl.querySelectorAll('.option');
    options.forEach(opt => opt.classList.remove('selected'));
    element.classList.add('selected');
    selectedOption = index;
    nextBtn.disabled = false;
}

function nextQuestion() {
    const q = quizData[currentQuestion];
    const options = optionsEl.querySelectorAll('.option');

    // Mostrar feedback de acerto/erro
    if (selectedOption === q.correct) {
        score++;
        options[selectedOption].classList.add('correct');
    } else {
        options[selectedOption].classList.add('incorrect');
        options[q.correct].classList.add('correct');
    }

    // Desabilitar cliques nas opções e no botão Próxima
    options.forEach(opt => opt.style.pointerEvents = 'none');
    nextBtn.disabled = true;  // <-- Desabilita o botão imediatamente

    currentQuestion++;

    if (currentQuestion < quizData.length) {
        // Após o delay, mostra a próxima pergunta e REABILITA o botão
        setTimeout(() => {
            showQuestion();
            // Em showQuestion(), o botão já começa desabilitado até escolher uma opção
        }, 1500);
    } else {
        // Após o delay, mostra o resultado
        setTimeout(showResult, 1500);
    }
}

function showResult() {
    quizSection.style.display = 'none';
    resultSection.style.display = 'block';
    scoreEl.textContent = `Você acertou ${score} de ${quizData.length} perguntas no tema "${selectedTheme.name}"!`;
}

function restartQuiz() {
    resultSection.style.display = 'none';
    themeSelection.style.display = 'block';
    displayThemes(); // Atualiza caso tenha mudado no db.json
}
