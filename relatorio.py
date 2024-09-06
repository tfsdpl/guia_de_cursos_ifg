import re

def listar_comandos_e_parametros(arquivo):
    with open(arquivo, 'r') as file:
        conteudo = file.read()

    # Expressão regular para encontrar comandos e seus parâmetros
    comandos = re.findall(r'elif\s+relatorio\s*==\s*[\'"](\w+)[\'"]', conteudo)
    parametros = re.findall(r'parser\.add_argument\(\s*\'--(\w+)\',\s*type=\w+,\s*help=\'([^\']+)\'\s*\)', conteudo)

    return sorted(set(comandos)), parametros

arquivo = 'importador.py'
comandos, parametros = listar_comandos_e_parametros(arquivo)

print("Lista de relatórios comandos:")
for comando in comandos:
    if comando == 'RREO':
        descricao = "Relatório Resumido da Execução Orçamentária"
    elif comando == 'RGF':
        descricao = "Relatório de Gestão Fiscal"
    elif comando == 'EAC':
        descricao = "Extrato de Acompanhamento Contábil"
    elif comando == 'EE':
        descricao = "Extrato de Entregas"
    elif comando == 'DCA':
        descricao = "Declaração de Contas Anuais"
    elif comando == 'MSCP':
        descricao = "Matriz de Saldos Contábeis Patrimonial"
    elif comando == 'MSCORC':
        descricao = "Matriz de Saldos Contábeis Orçamentário"
    elif comando == 'MSCC':
        descricao = "Matriz de Saldos Contábeis Controle"
    elif comando == 'DFES':
        descricao = "Despesas Função Educação SIOPE"
    elif comando == 'RS':
        descricao = "Receita SIOPE"
    elif comando == 'DGSIOPE':
        descricao = "Dados Gerais SIOPE"
    elif comando == 'DS':
        descricao = "Despesas SIOPE"
    elif comando == 'ALL':
        descricao = "Importar todos os relatórios"
    else:
        descricao = "Descrição não disponível"

    print(f"--{comando}: {descricao}")

print("\nLista de parâmetros:")
for param, descricao in parametros:
    print(f"--{param}: {descricao}")

# Exemplo de comando
print("\nExemplo de comando:")
print("python importador.py --r DCA --t 0 --a 2023")
print("Este comando vai baixar o relatório DCA, o intervalo de cada consulta vai ser 0, e ele vai excluir, se existir, os dados de 2023 e baixar novamente. O comando --a é opcional.")