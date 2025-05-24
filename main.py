from modules import mesages, operations

nome = input("Digite seu nome: ")
a = int(input("Digite um primeiro número: "))
b = int(input("Digite um segundo número: "))
n = int(input("Digite um terceiro número: "))

print(mesages.boas_vindas(nome))

print("A soma de", a, "+", b, "é =", operations.soma(a, b))
print("A subtração de", a, "+", b, "é =", operations.sub(a, b))
print("A multiplicação de", a, "+", b, "é =", operations.multiplica(a, b))
print("O módulo de", n, "é =", operations.module(n))