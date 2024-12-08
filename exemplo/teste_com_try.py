# # Trabalhando com o try except
# excelente para teste 
# não realiza o stop no programa
# mensagem customizadas quando encontra um erro
try:
    letras  = ['a','b','c']
    print(letras[3])
except IndexError:
    print('Index não existe')