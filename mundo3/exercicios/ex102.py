# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
#  o primeiro que indique o número a calcular e outro chamado show,
#  que será um valor lógico (opcional) indicando se será mostrado ou não na tela
#  o processo de cálculo do fatorial.
def fatorial(a,b = 0): #0 significa não mostrar na tela
    '''
    Docstring for fatorial
    
    :param a: Entrada a ser realizada para descobrir o resltado do fatorial
    :param b: numero lógico que indica se será necessário printar cada etapa do calculo, 0 = não 1 = sim
    :return: resultado final do calculo
    '''

    resultado_final = a
  
    for i in range(a,1,-1): #a=5
        resultado_final = a * i        
    return resultado_final

def fatorial_certo(a, show = False):
    resultado_final = 0
    for i in range(a - 1, 0, -1):
        if show == True:
            if i == a - 1:
                resultado =+ a * i
                resultado_final += resultado
                print(resultado_final)
            else:
                resultado_final = resultado_final * i
                print(resultado_final)
        else:
            if i == a - 1:
                resultado =+ a * i
                resultado_final += resultado
            else:
                resultado_final = resultado_final * i
                
    if a == 1:
        return 1
    return resultado_final
print(fatorial_certo(5))

#Obs: eu hoje não estou bem, fazer esse exrecício foi muito difícil pois não estou conseguindo pensar direito
#comecei a fazeras 8hrs da manhã e agora são +=12hrs então vou para por agora. Eu consegui entregar sem usar nenhum
#recurso alternativo como chatGTP então mesmo forçando eu cosnegui entregar :D mas sei que se fosse outro dia eu conseguiria
#fzer tranquilamente... esse fatorial que que tem ess condição predefinida 