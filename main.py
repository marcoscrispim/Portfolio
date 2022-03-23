idades = [18, 22, 15, 50]
def verifica_se_pode_dirigir(idades):
    for idade in idades:
        if idade >= 18:
            print(f'{idade} anos de idade, TEM permissão para dirigir')
        else:
            print(f'{idade} anos de idade, NÃO tem permissão para dirigir')


                print (verifica_se_pode_dirigir(idade))