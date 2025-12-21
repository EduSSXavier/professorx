async function sha256(texto) {
    const encoder = new TextEncoder();
    const data = encoder.encode(texto);
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('')
}

async function urlExiste(url) {
  try {
    const response = await fetch(url, { method: 'HEAD' });
    return response.ok;  // true se status for 2xx (ex: 200), false otherwise
  } catch (error) {
    return false;  // Erro de rede ou CORS
  }
}

const curso = new URLSearchParams(window.location.search).get('curso'); // Retorna 'valor1'
botao = document.getElementById('botao');
botao.addEventListener('click', () => {
    const senha = document.getElementById('senha').value;
    const hash = sha256(senha).then(hs => {
        const url = './C'+curso+hs+'/menu_aulas.html'
        //console.log('URL:',url);
        urlExiste(url).then(existe => {
            if (existe) {
                // curso existe
                window.location.assign(url); 
            } else {
                // curso não existe
                document.getElementById('mensagem').innerText = 
                        'Senha incorreta. Solicite a senha ao professor';
            }
        });
    })
})