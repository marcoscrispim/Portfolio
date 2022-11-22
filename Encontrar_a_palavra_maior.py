frase = input('Digite a frase: ').split()  # Capturar uma frase qualquer e
tam_palavras = list()  # adicioná-la em uma lista;
for palavra in frase:  # Percorrer esta lista e capturar o tamanho de cada palavra
    tam_palavras.append(len(palavra))

maior = max(tam_palavras)  # Inserir o tamanho de cada palavra em outra lista;
print('Maior(es) palavra(s):')
for a, b in zip(frase, tam_palavras):   # Percorrer as duas listas simultaneamente associando cada palavra de maior
    # tamanho ou seu respectivo nome.
    if b == maior:
        print(a)
