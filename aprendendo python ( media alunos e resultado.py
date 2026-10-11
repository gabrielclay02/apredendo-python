print("ola, aluno")

nome5 = input("digite aqui seu nome: ")
nota1 = int(input("digite sua nota primeiro bimestre: "))
nota2 = int(input("digite sua nota segundo bimestre: "))
nota3 = int(input("digite sua nota terceiro bimestre: "))

nota_final = (nota1 + nota2 + nota3) / 3

print(f"a nota do aluno {nome5} e {nota_final}")

if nota_final >= 7:
    print("aprovado")
else:
    print("reprovado")