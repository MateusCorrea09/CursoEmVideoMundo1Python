#modulos e pacotes !
print('Modularização vem de construir módulos!')
# as coisas precisam ser parte de uma arquivo
print('O foco é fragmentar um grande programa e melhroar a manutenção do sistema e a legibilidade')

#   Imaginamos que em um determinado programa precisamos de uma função e não a temos logo precisaremos cria-la
#então vamos usar o exemplo do fatorial
#para isso criamos um novo arquivo.py e adicionamos a ele a função qeu acabamos de criar (seria a fatorial(num))
#depois usamos o 'import' que considera todo arquivo.py como um possivel arquivo a ser importando, e ele vai identificar
#esse mesmo arquivo já existênte e permitir que ele seja importado
#import uteis
from uteis import numeros
num = int(input('Digite um valor '))
#   Para usarmos essa função anteriormente criada, precisamos primeeiro declarar de onde essa função é e logo em seguida udar o '.'
#para que de dentro desse pacote puxamos oq precisamos usar, exmeplo logo a baixo:
fat = numeros.fatorial(num) 
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')

print('\n Você também pode usar from [uteis] import [fatorial], e vai funcionar da mesma forma')
print('A modularização ajuda a organizar seu código, de forma a torna-lo fragmentado a ponto de seu grande problema ser mais legivel aos olhos do programador')
print('A manutenção é mais simples')
print('A ocultação do código permite seu projeto não ficar poluído com muitas linhas de código')
print('\n além da modularização, existem os pacotes que também contribuem com a sua programação')
print('Cada pacote precisa ter um arquivo __init__.py\n para acessarmos a função que agora está dentro de numeros')
print('Precisamos usar from uteis import numeros\n e usamos numeros.fatorial() para usarmos a função')