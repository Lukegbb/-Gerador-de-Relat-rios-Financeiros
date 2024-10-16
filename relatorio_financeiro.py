import pandas as pd
import matplotlib.pyplot as plt

# Função para carregar os dados do CSV
def carregar_transacoes(arquivo_csv):
    try:
        transacoes = pd.read_csv(arquivo_csv)
        return transacoes
    except FileNotFoundError:
        print("Arquivo não encontrado!")
        return None

# Função para calcular o total de receitas e despesas
def calcular_balanco(transacoes):
    receitas = transacoes[transacoes['Tipo'] == 'Receita']['Valor'].sum()
    despesas = transacoes[transacoes['Tipo'] == 'Despesa']['Valor'].sum()
    saldo = receitas + despesas
    return receitas, despesas, saldo

# Função para gerar o relatório em texto
def gerar_relatorio(receitas, despesas, saldo):
    print(f"Total de Receitas: R${receitas:.2f}")
    print(f"Total de Despesas: R${-despesas:.2f}")
    print(f"Saldo Final: R${saldo:.2f}")
    
    with open("relatorio_financeiro.txt", "w") as relatorio:
        relatorio.write(f"Total de Receitas: R${receitas:.2f}\n")
        relatorio.write(f"Total de Despesas: R${-despesas:.2f}\n")
        relatorio.write(f"Saldo Final: R${saldo:.2f}\n")

# Função para gerar gráfico de receitas e despesas
def gerar_grafico(transacoes):
    transacoes.groupby('Tipo')['Valor'].sum().plot(kind='bar', color=['green', 'red'])
    plt.title('Receitas vs Despesas')
    plt.ylabel('Valor (R$)')
    plt.show()

# Main - Execução do programa
if __name__ == "__main__":
    arquivo_csv = 'transacoes.csv'
    transacoes = carregar_transacoes(arquivo_csv)
    
    if transacoes is not None:
        receitas, despesas, saldo = calcular_balanco(transacoes)
        gerar_relatorio(receitas, despesas, saldo)
        gerar_grafico(transacoes)
