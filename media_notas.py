#definir notas
nota1 = float(input("Qual a sua primeira nota? ")) #float é igual a real
nota2 = float(input("Qual a sua segunda nota? "))
#calcular a média
media = nota1 + nota2 / 2
#verificar se está aprovado ou reprovado
print (f"Sua média é:{media}")
if media >= 7: 
    print("Aprovado!")
else:
    print("Reprovado")