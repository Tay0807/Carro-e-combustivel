carro = int(input("Qual o seu carro: \n 1 - BMW \n 2 - AUDI \n 3 - FIAT \n 4 - FERRARI \n"))
combustivel = int(input("Qual o combustível:\n 1 - Gasolina \n 2 - Álcool \n "))

vcombustivel = 0

if carro == 1 and combustivel == 1:
    print("BMW: 9.8 L/km")
    vcombustivel = 9.8
elif carro == 1 and combustivel == 2:
    print("BMW: 8.9L/km")
    vcombustivel = 8.9
elif carro == 2 and combustivel == 1:
    print("AUDI: 12.8 L/km")
    vcombustivel = 12.8
elif carro == 2 and combustivel == 2:
    print("AUDI: 10.9 L/km")
    vcombustivel = 10.9
elif carro == 3 and combustivel == 1:
    print("FIAT: 26.8 L/km")
    vcombustivel = 26.8
elif carro == 3 and combustivel == 2:
    print("FIAT: 24.9 L/km")
    vcombustivel = 24.9
elif carro == 4 and combustivel == 1:
    print("FERRARI: 13.8 L/km")
    vcombustivel = 13.8
else:
    print("FERRARI: 12.9 L/km")
    vcombustivel = 12.9
    
porta = int(input("Seu carro tem mais de 4 portas? \n 1 - sim \n 2 - não \n"))

if porta == 1:
    vcombustivel -= 0.5
    
pessoas = int(input("Quantas pessoas estarão dentro do carro? \n "))

if pessoas >= 2:
    vcombustivel -= 1.2 
    
bagageiro = int(input("Irão levar bagagem? \n 1 - sim \n 2 - não \n")) 

if bagageiro == 1:
    vcombustivel -= 0.2
    
print (f"O carro irá consumir: {vcombustivel:.2f} L/Km")
    