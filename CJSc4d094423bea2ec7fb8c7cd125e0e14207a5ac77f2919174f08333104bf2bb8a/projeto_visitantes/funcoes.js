// Funções para manipulação de dados

// Função para cadastrar uma nova visita
function cadastrarVisita(paramNome, paramCpf, paramEmpresa, paramMotivo) {
    // descobre o maior id existente e incrementa 1
    const novoId = cadastroVisitantes.length + 1;
    const dataEntrada = new Date().toISOString().split('T')[0];
    const novaVisita = {
        id: novoId,
        nome: paramNome,
        cpf: paramCpf,
        empresa: paramEmpresa,
        motivo: paramMotivo,
        dataEntrada: dataEntrada,
        dataSaida: null
    };
    cadastroVisitantes.push(novaVisita);
    return novaVisita;
}

// Função para cadastrar a saída de um visitante
function cadastrarSaida(paramIdVisita, paramHoraSaida) {
    const visitante = cadastroVisitantes.find(v => v.id === parseInt(paramIdVisita));
    if (visitante) {
        visitante.horaSaida = paramHoraSaida;
        return true;
    }
    return false;
}

// Função para gerar relatório de visitas por data
function gerarRelatorioPorData(paramData) {
    dadosRelatorio = cadastroVisitantes.filter(v => v.dataEntrada === paramData);
    gerarRelatorio(dadosRelatorio, "Relatório de Visitas por Data");
}

// Função para gerar relatório de visitas por empresa/sala
function gerarRelatorioPorEmpresa(paramEmpresa) {
    dadosRelatorio = cadastroVisitantes.filter(v => v.empresaId === paramEmpresa);
    gerarRelatorio(dadosRelatorio, "Relatório de Visitas por Empresa");
}

// Função para gerar relatório de visitas (todas as visitas)
function gerarRelatorioTodas() {
    gerarRelatorio(cadastroVisitantes, "Relatório de Todas as Visitas");
}
// Função para gerar relatório de todas as visitas
function gerarRelatorio(paramDados, paramCabecalho) {
    console.log("====================================");
    console.log(paramCabecalho);
    console.log("====================================");
    paramDados.forEach(v => {
        console.log(`ID: ${v.id}, Nome: ${v.nome}, CPF: ${v.cpf}, Empresa ID: ${v.empresaId}, Motivo: ${v.motivo}, Data: ${v.data}, Entrada: ${v.horaEntrada}, Saída: ${v.horaSaida || 'N/A'}\n`);
    });
    if (paramDados.length === 0) {
        console.log("Nenhum registro encontrado.");
    }
    console.log("====================================");
    }