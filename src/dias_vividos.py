from datetime import datetime

def calcular_dias_vividos(data_nascimento):
    data_atual = datetime.now()
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    dias_vividos = (data_atual - data_nascimento).days
    return dias_vividos

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dias_vividos = calcular_dias_vividos(data_nascimento)
print(f"Você está vivo há {dias_vividos} dias.")