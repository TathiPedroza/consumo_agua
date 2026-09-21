# Programa para calcular o consumo de água e fornecer recomendações com base na categoria do usuário.
# O programa solicita ao usuário que escolha uma categoria (comercial, casa ou apartamento) e insira o consumo mensal de água em metros cúbicos (m³). Com base na categoria e no consumo, o programa fornece recomendações sobre o uso da água.
opcao = input("Digite uma opção (1 - comercial, 2 - casa, 3 - apartamento): ")
consumo_mensal = int(input("Digite o consumo mensal de água em m³: "))

match opcao:
    # Regra 1: Se o tipo for "comercial"
    case "1" | "comercial" | "Comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
        
    # Regra 2: Se o tipo for "apartamento" e o consumo for menor que 10 m³
    case "3" | "apartamento" | "Apartamento" if consumo_mensal < 10:
        print("Consumo econômico – excelente controle de água!")
        
    # Regra 3: Se o tipo for "apartamento" ou "casa" com consumo de até 25 m³
    case ("2" | "casa" | "Casa" | "3" | "apartamento" | "Apartamento") if consumo_mensal <= 25:
        print("Consumo moderado – dentro do padrão residencial.")
        
    # Regra 4: Em qualquer outro caso (acima do limite residencial)
    case _:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")