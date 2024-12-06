# Cross Validation / Validação cruzada
## Descrição

Este repositório contém uma implementação do algoritmo de validação cruzada, uma técnica fundamental em aprendizado de máquina para avaliar a eficácia de modelos preditivos. A validação cruzada ajuda a garantir que o modelo não esteja sobreajustado aos dados de treinamento e fornece uma estimativa mais confiável de sua performance em dados não vistos.

## O que é Validação Cruzada?

A validação cruzada é um método que divide o conjunto de dados em várias partes (ou "folds") e utiliza essas partes para treinar e testar o modelo. O processo típico envolve:

1. **Divisão dos Dados**: O conjunto de dados é dividido em `k` partes.
2. **Treinamento e Teste**: O modelo é treinado em `k-1` partes e testado na parte restante.
3. **Repetição**: Esse processo é repetido `k` vezes, cada vez utilizando uma parte diferente como conjunto de teste.
4. **Média dos Resultados**: Os resultados dos testes são então combinados para fornecer uma estimativa final da performance do modelo.
