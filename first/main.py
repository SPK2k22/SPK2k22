print("-------------------------------------")
print("Bem vindo a calculadora de calorias! ")
print("para podermos começar, nos informe: ")
print("-------------------------------------")


nome = input("Como devemos te chamar? ")
peso = float(input("Qual o seu peso (kg)? "))
altura = float(input("Qual a sua altura (cm)? "))
idade = int(input("Qual a sua idade? "))
objetivo = input("O seu objetivo é perder ou ganhar peso? ").lower()


print("")
print("-------------------------------------")
print("")
print("Qual destas opções corresponde ao seu nível de atividade física?")
print("a) Sedentário")
print("b) Levemente ativo")
print("c) Moderadamente ativo")
print("d) Muito ativo")
print("e) Extremamente ativo")

nivel_atv = input("Escolha uma opção (a, b, c, d, ou e): ").lower()

fatores = {
    "a": 1.2,
    "b": 1.375,
    "c": 1.55,
    "d": 1.725,
    "e": 1.9
}


if nivel_atv in fatores:
    fator_escolhido = fatores[nivel_atv]
    
   
    tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    
    
    calorias_totais = tmb * fator_escolhido

    print("-------------------------------------")
    print(f"Ok, {nome}, vamos começar.")
    print("-------------------------------------")

    
    if objetivo == "ganhar":
        calorias_totais += calorias_totais * 0.15  
        print(f"Para ganhar peso, você deve consumir cerca de {calorias_totais:.2f} calorias por dia.")
    elif objetivo == "perder":
        calorias_totais -= calorias_totais * 0.15 
        print(f"Para perder peso, você deve consumir cerca de {calorias_totais:.2f} calorias por dia.")
    else:
        print(f"Para manter o peso, você deve consumir cerca de {calorias_totais:.2f} calorias por dia.")
else:
    print("Opção de nível de atividade inválida. Por favor, reinicie o programa e escolha uma opção válida.")


print("-------------------------------------")
