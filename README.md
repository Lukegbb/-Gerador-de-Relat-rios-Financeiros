# Gerador de Relatórios Financeiros

Este é um projeto simples em Python para gerar relatórios financeiros a partir de um arquivo CSV contendo transações de receitas e despesas. Ele calcula o total de receitas, despesas e saldo, além de gerar um gráfico de barras comparando receitas e despesas.

## Funcionalidades

- Leitura de transações financeiras a partir de um arquivo CSV.
- Cálculo do total de receitas e despesas.
- Geração de um relatório de texto com o saldo final.
- Exibição de um gráfico de barras com comparações de receitas e despesas.

##  Estrutura do Projeto
transacoes.csv: Arquivo CSV contendo as transações financeiras.
relatorio_financeiro.py: Script Python que gera o relatório e o gráfico.
relatorio_financeiro.txt: Relatório de texto gerado após a execução do script.

## O arquivo CSV deve conter as seguintes colunas:

Data: Data da transação no formato YYYY-MM-DD.
Descrição: Descrição breve da transação.
Tipo: "Receita" ou "Despesa".
Valor: Valor da transação. Receitas são valores positivos e despesas são valores negativos.

## Pré-requisitos

Antes de executar o projeto, você precisará instalar as seguintes dependências:


pip install pandas matplotlib

## Financial Report Generator

This is a simple Python project to generate financial reports from a CSV file containing income and expense transactions. It calculates the total income, expenses, and balance, and generates a bar chart comparing income and expenses.

## Features

- Read financial transactions from a CSV file.
- Calculate total income and expenses.
- Generate a text report with the final balance.
- Display a bar chart comparing income and expenses.
  
## Project Structure
transactions.csv: CSV file containing financial transactions.
financial_report.py: Python script that generates the report and chart.
financial_report.txt: Text report generated after running the script.

## The CSV file should contain the following columns:

Date: Date of the transaction in YYYY-MM-DD format.
Description: Brief description of the transaction.
Type: "Income" or "Expense".
Amount: Transaction amount. Incomes are positive values and expenses are negative values.

## Prerequisites

Before running the project, you will need to install the following dependencies:

```bash
pip install pandas matplotlib
