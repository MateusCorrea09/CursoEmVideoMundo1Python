#Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from util.moeda import transformacao

entrada = 420
reposta = transformacao.resumo(entrada)
print(reposta)