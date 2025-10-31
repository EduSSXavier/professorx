// Funções para manipulação de dados

// Função para cadastrar uma nova visita
function cadastrarVisita() {
    // captura os dados do formulário
    const paramNome = document.getElementById("nomeVisita").value;
    const paramCpf = document.getElementById("cpfVisita").value;
    const paramEmpresa = document.getElementById("empresaVisita").value;
    const paramMotivo = document.getElementById("motivoVisita").value;
    // descobre o maior id existente e incrementa 1
    const novoId = cadastroVisitantes.length + 1;
    // monta data de entrada e hora atual
    const dataAtual = new Date().toISOString().split('T')[0];
    const horaAtual = new Date().toISOString().split('T')[1].split('.')[0];
    // cria o objeto da nova visita
    const novaVisita = {
        id: novoId,
        nome: paramNome,
        cpf: paramCpf,
        empresa: paramEmpresa,
        motivo: paramMotivo,
        data: dataAtual,
        horaEntrada: horaAtual,
        horaSaida: null
    };
    // adiciona ao array de cadastro
    cadastroVisitantes.push(novaVisita);
    // mensagem e limpa formulário
    document.getElementById("nomeVisita").value = "";
    document.getElementById("cpfVisita").value = "";
    document.getElementById("empresaVisita").value = "";
    document.getElementById("motivoVisita").value = "";
    document.getElementById("saidaRelatorio").innerHTML =
            '<p>Inclusão de visita realizada com sucesso</p>';
}

// Função para cadastrar a saída de um visitante
function registrarSaida() {
    // captura os dados do formulário
    const paramIdVisita = document.getElementById("idVisita").value;
    // monta a hora de saída atual
    const paramHoraSaida = new Date().toISOString().split('T')[1].split('.')[0];
    // procura a visita pelo id e atualiza a hora de saída
    const visitante = cadastroVisitantes.find(v => v.id === parseInt(paramIdVisita));
    // verifica se encontrou o visitante
    if (visitante) {
        // atualiza a hora de saída do visitante
        visitante.horaSaida = paramHoraSaida;
        // mensagem 
        document.getElementById("saidaRelatorio").innerHTML =
            '<p>Registro de saída realizado com sucesso</p>';
    } else {
        // mensagem 
        document.getElementById("saidaRelatorio").innerHTML =
            '<p>ID de visitante não encontrado</p>';
    }
    // limpa formulário
    document.getElementById("idVisita").value = "";
}

// Função para gerar relatório de visitas por data
function relatorioPorData() {
    const paramData = document.getElementById("dataVisitaRelat").value;
    dadosRelatorio = cadastroVisitantes.filter(v => v.data === paramData);
    geradorRelatorio(dadosRelatorio, "Relatório de Visitas por Data");
}

// Função para gerar relatório de visitas por empresa/sala
function relatorioPorEmpresa() {
    const paramEmpresa = document.getElementById("empresaVisitaRelat").value;
    dadosRelatorio = cadastroVisitantes.filter(v => v.empresaId === parseInt(paramEmpresa));
    geradorRelatorio(dadosRelatorio, "Relatório de Visitas por Empresa");
}

// Função para gerar relatório de visitas (todas as visitas)
function relatorioTodas() {
    geradorRelatorio(cadastroVisitantes, "Relatório de Todas as Visitas");
}

// Função para gerar relatório de todas as visitas
function geradorRelatorio(paramDados, paramCabecalho) {
    // Capturar em variável a div onde o relatório será exibido
    let divRelatorio = document.getElementById("saidaRelatorio");
    // Limpar conteúdo anterior
    divRelatorio.innerHTML = "";
    // Exibir o cabeçaho
    divRelatorio.innerHTML = "<h2>" + paramCabecalho + "</h2><hr>";
    // Exibir visitas do array de dados
    if (paramDados.length === 0) {
        divRelatorio.innerHTML += '<p class="linha_relatorio">Nenhum registro encontrado.</p>';
    } else {
        paramDados.forEach(v => {
            divRelatorio.innerHTML += `<p class="linha_relatorio">`+
                        `<span class="id">[ID: ${v.id}] `+
                        `Nome: ${v.nome}</span> `+
                        `CPF: ${v.cpf} / `+
                        `Empresa ID: ${v.empresaId} / `+
                        `Motivo: ${v.motivo} <br>`+
                        `Data: ${v.data} / `+
                        `Hora Entrada: ${v.horaEntrada} / `+
                        `Hora Saída: ${v.horaSaida || 'no Prédio'}`+
                        `</p>`;
        })
    };
    // Mensagem de fim do relatório
    divRelatorio.innerHTML += "<hr><p>Fim do Relatório</p>";
}