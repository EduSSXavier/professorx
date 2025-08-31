        let currentSlideIndex = 0;
        const slides = document.querySelectorAll('.slide');
        const totalSlides = slides.length;

        // Atualizar contador total
        document.getElementById('totalSlides').textContent = totalSlides;

        function showSlide(index) {
            // Esconder todos os slides
            slides.forEach(slide => slide.classList.remove('active'));
            
            // Mostrar slide atual
            slides[index].classList.add('active');
            
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

        // Inicializar apresentação
        showSlide(0);

        // Adicionar efeitos hover nos cards
        document.querySelectorAll('.topic-card').forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-8px) scale(1.02)';
                this.style.boxShadow = '0 10px 25px rgba(0,0,0,0.2)';
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0) scale(1)';
                this.style.boxShadow = 'none';
            });
        });

        // Efeito de digitação para códigos
        function typeWriter(element, text, speed = 50) {
            let i = 0;
            element.innerHTML = '';
            
            function type() {
                if (i < text.length) {
                    element.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(type, speed);
                }
            }
            
            type();
        }

        // Contador de progresso
        function updateProgress() {
            const progress = ((currentSlideIndex + 1) / totalSlides) * 100;
            // Você pode adicionar uma barra de progresso aqui se desejar
        }
