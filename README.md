# Cross Validation / Validação cruzada
## Descrição

Este repositório contém uma implementação do algoritmo de validação cruzada, uma técnica fundamental em aprendizado de máquina para avaliar a eficácia de modelos preditivos. A validação cruzada ajuda a garantir que o modelo não esteja sobreajustado aos dados de treinamento e fornece uma estimativa mais confiável de sua performance em dados não vistos.

## O que é Validação Cruzada?

A validação cruzada é um método que divide o conjunto de dados em várias partes (ou "folds") e utiliza essas partes para treinar e testar o modelo. O processo típico envolve:

1. **Divisão dos Dados**: O conjunto de dados é dividido em `k` partes.
2. **Treinamento e Teste**: O modelo é treinado em `k-1` partes e testado na parte restante.
3. **Repetição**: Esse processo é repetido `k` vezes, cada vez utilizando uma parte diferente como conjunto de teste.
4. **Média dos Resultados**: Os resultados dos testes são então combinados para fornecer uma estimativa final da performance do modelo.

# Seleção de Atributos Utilizando Variância

## Descrição

Este projeto tem como objetivo demonstrar técnicas de seleção de atributos em conjuntos de dados, focando na variância como critério principal. A seleção de atributos é uma etapa crucial no pré-processamento de dados, pois ajuda a melhorar a performance dos modelos de machine learning, reduzindo a dimensionalidade e eliminando ruídos.

## Motivação

Com o aumento da quantidade de dados disponíveis, a seleção de atributos se torna essencial para garantir que os modelos sejam treinados de forma eficiente. A variância é uma medida que quantifica a dispersão dos dados e pode ser utilizada para identificar atributos que não trazem informação relevante.

## Metodologia

Utilizamos a seguinte abordagem para a seleção de atributos:

1. **Cálculo da Variância**: Para cada atributo no conjunto de dados, calculamos a variância.
2. **Definição de um Limite**: Estabelecemos um limite de variância abaixo do qual os atributos serão descartados.
3. **Filtragem de Atributos**: Atributos com variância abaixo do limite são removidos do conjunto de dados.
