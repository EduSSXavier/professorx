// Empresas / salas ocupadas no prédio
const proprietarios = [ 
    { id: 1, nome: "Dr. Carlos Mendes", sala: "101", especialidade: "Advocacia" }, 
    { id: 2, nome: "Dra. Ana Costa", sala: "205", especialidade: "Contabilidade" }, 
    { id: 3, nome: "Eng. Pedro Santos", sala: "310", especialidade: "Engenharia" } 
];

// Cadastro de visitas realizadas
const cadastroVisitantes = [
    { id: 1, nome: "Maria dos Santos", cpf: "123.456.789-00", 
        empresaId: 2, motivo: "Reunião", 
        data: "2025-10-01", horaEntrada: "09:00", horaSaida: "10:00" },
    { id: 2, nome: "João da Silva", cpf: "987.654.321-00", 
        empresaId: 1, motivo: "Entrega de Documentos", 
        data: "2025-10-02", horaEntrada: "11:00", horaSaida: null }
];