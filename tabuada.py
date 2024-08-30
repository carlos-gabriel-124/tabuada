numb = int(input("DIGITE O NÚMERO QUE VOCÊ QUER A TABUADA: "))
print(f"----TABUADA DO NÚMERO {numb}----")
for i in range(1, 11):
    resultado = numb * i
    print(f"{numb} x {i} = {resultado}")
