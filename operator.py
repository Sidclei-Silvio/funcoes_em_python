# 1 - Crie uma função usando o operador &&

# Considerando isso, implemente na função compareTrue, um código que ao receber dois parâmetros booleanos deve:

# Retornar true se ambos os valores forem verdadeiros;
# Retornar false se um ou ambos os parâmetros forem falsos.
# Faça a função somente utilizando o operador &&.

# O que será verificado:

# Retorne false quando se chamar a função compareTrue com um parâmetro de valor false e outro de valor true

# Retorne false quando se chamar a função compareTrue com dois parâmetros de valor false

# Retorne true quando se chamar a função compareTrue com dois parâmetros de valor true



def compareTrue(a, b):
    return a or b


if __name__ == "__main__":
    print(compareTrue(True, True))
    print(compareTrue(True, False))
    print(compareTrue(False, True))
    print(compareTrue(False, False))
