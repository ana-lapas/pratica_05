def calcular_preco_com_desconto(preco_original, porcentagem_desconto):
    desconto = preco_original * (porcentagem_desconto / 100)
    preco_final = preco_original - desconto
    return round(preco_final, 2)

preco_original = float(input("Digite o preço original do produto: "))
porcentagem_desconto = float(input("Digite a porcentagem de desconto: "))
preco_final = calcular_preco_com_desconto(preco_original, porcentagem_desconto)
print(f"O preço final do produto com desconto é: R$ {preco_final}")