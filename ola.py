
'''
Crie um programa que lei dois números inteiros,substitua o mair pela diferença e 
escreva ambos no console'''

primeiro_numero =input ("Digite um numero inteiro")
primeiro_numero =int (primeiro_numero)
segundo_numero =input ("Digite um numero inteiro")
segundo_numero =int (primeiro_numero)

if primeiro_numero > segundo_numero:
    primeiro_numero = segundo_numero - segundo_numero
 
elif segundo_numero> primeiro_numero:
    segundo_numero=segundo_numero-primeiro_numero

else:
    print( "numeros são iguais")

