# Como exercício prático do curso de Python pela DSA foi sugerido criar uma calculadora para demonstrar habilidade prática com variáveis e operações lógicas matemáticas

print("\n********************CALCULADORA JUROS COMPOSTOS********************\n")
# Montante = capital * (1 + taxa/100)^(tempo)


def calcular_juros_compostos(c, i, t):
    M = c * (1+i/100)**(t)
    return M


capital_inicial = float(input("Digite o capital inicial (P): "))
taxa_juros = float(input("Digite a taxa de juros anual (em %): "))
tempo = float(input("Digite o tempo da aplicação em anos (t): "))

# Cálculo dos juros compostos
montante = calcular_juros_compostos(capital_inicial, taxa_juros, tempo)

# Exibindo o resultado
print("O montante final após", ' ', tempo, ' ', 'anos será: R$', ' ', montante)

print('\nO resultado do seu lucro será:', ' ', (montante - capital_inicial))
