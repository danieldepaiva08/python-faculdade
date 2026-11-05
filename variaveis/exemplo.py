def imprimir_dados(numero, texto):
    print("Dentro da função:")
    print("Número vinculado ao parametro 'numero':", numero)
    print("texto vinculado ao parametro 'texto': ", texto)


numero_exemplo = 42
texto_exemplo = "python é incrível!"

print("Fora da função:")
print("Número antes da chamada da função: ", numero_exemplo)
print("Texto antes da chamada da função:", texto_exemplo)

imprimir_dados(numero_exemplo, texto_exemplo)

print("fora da função após a chamada:")
print("Número após a chamada da função", numero_exemplo)
print("Texto após a chamada da função", texto_exemplo)