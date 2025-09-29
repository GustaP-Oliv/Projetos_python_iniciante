#calculadora

print("Calculadora")
print("Digite 'sair' para encerrar.")

while True:
    expressao = input("Digite a conta")

    if expressao.lower() == "sair":
        print("Até mais!")
        break

    try:
        resultado = eval(expressao)  # cuidado: eval executa código direto
        print("Resultado:", resultado)
    except:
        print("Expressão inválida, tente de novo!")
# fim do código