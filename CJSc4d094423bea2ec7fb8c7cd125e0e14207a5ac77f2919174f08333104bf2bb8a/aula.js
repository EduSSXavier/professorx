let currentSlideIndex = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;

// Atualizar contador total
document.getElementById('totalSlides').textContent = totalSlides;

function showSlide(index) {
    // Esconder todos os slides
    slides.forEach(slide => slide.classList.remove('ativo'));
    
    // Mostrar slide atual
    slides[index].classList.add('ativo');
    
    // Atualizar contador
    document.getElementById('currentSlide').textContent = index + 1;
    
    // Atualizar botões
    document.getElementById('prevBtn').disabled = index === 0;
    document.getElementById('nextBtn').disabled = index === totalSlides - 1;
}

function nextSlide() {
    if (currentSlideIndex < totalSlides - 1) {
        currentSlideIndex++;
        showSlide(currentSlideIndex);
    }
}

function previousSlide() {
    if (currentSlideIndex > 0) {
        currentSlideIndex--;
        showSlide(currentSlideIndex);
    }
}

// Navegação por teclado
document.addEventListener('keydown', function(event) {
    if (event.key === 'ArrowRight' || event.key === ' ') {
        event.preventDefault();
        nextSlide();
    } else if (event.key === 'ArrowLeft') {
        event.preventDefault();
        previousSlide();
    }
});

// Contador de progresso
function updateProgress() {
    const progress = ((currentSlideIndex + 1) / totalSlides) * 100;
    // Você pode adicionar uma barra de progresso aqui se desejar
}

// Exibir exercício oculto
function exibirRespostaExercicio(idExercicio) {
    // Exibe resposta oculta de um exercício
    let exercicio = document.getElementById(idExercicio);
    if (exercicio.style.display === 'none') {
        exercicio.style.display = 'block';
    } else {
        exercicio.style.display = 'none';    
    }    
}
// Inicializar apresentação
showSlide(0);

