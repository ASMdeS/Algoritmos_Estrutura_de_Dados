# Função para calcular Fibonacci com Programação Dinâmica e Memorização
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


# Lê o valor de N a partir do input, Calcula o valor de Fibonacci para N e Imprime o resultado
print(fibonacci(int(input())))
