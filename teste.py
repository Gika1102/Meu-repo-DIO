# 1 - Concatenando Dados 🐾
print("Desafio 1 - Concatenando Dados 🐾")
dado1 = input("Digite o seu nome: ")
dado2 = input("Digite o seu sobrenome: ")
concatenado = dado1 + " " + dado2
print("Concatenado:", concatenado)

# 2 - Repetindo Textos ✏️
print("\nDesafio 2 - Repetindo Textos ✏️")
texto = input("Digite uma frase: ")
vezes = int(input("Digite um número inteiro: "))
print("Repetido:", texto * vezes)

# 3 - Operações Matemáticas Simples 📐
print("\nDesafio 3 - Operações Matemáticas Simples 📐")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
print(f"Soma: {soma}")

# 4 - Verificando Números Pares e Ímpares 🧮
print("\nDesafio 4 - Verificando Números Pares e Ímpares 🧮")
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
	print("O número é par.")
else:
	print("O número é ímpar.")

# 5 - Calculando Média de Notas 📚
print("\nDesafio 5 - Calculando Média de Notas 📚")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"Média: {media:.2f}")

# 6 - Verificando Palíndromos 🔄
print("\nDesafio 6 - Verificando Palíndromos 🔄")
palavra = input("Digite uma palavra: ")
if palavra == palavra[::-1]:
	print("É um palíndromo!")
else:
	print("Não é um palíndromo.")


print("Hellouuu Prof!")
