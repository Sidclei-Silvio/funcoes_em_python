'''
3 - Crie uma função que divida a frase
Escreva uma função com o nome splitSentence, a qual receberá uma 
string e retornará uma array de strings separadas por cada espaço na 
string original.

Exemplo: se a função receber a string "go Trybe", o retorno deverá 
ser ['go', 'Trybe'].

O que será verificado:

Retorne o valor ['go', 'Trybe'] se a função receber a string 'go Trybe'

Retorne o valor ['vamo', 'que', 'vamo']. se a função receber a string 
'vamo que vamo'

Retorne o valor ['foguete'] se a função receber a string 'foguete'

'''




def splitSentence(str):
    words = []
    word = '' 
    
    for i in str:
        if i == " ":
            if word:
                words.append(word)
                word = '' 
        else:
            word += i

    if word:  
        words.append(word)

    return words  


if __name__ == "__main__":
    print(splitSentence("go Trybe"))
    print(splitSentence("vamo que vamo"))
    print(splitSentence("foguete"))
