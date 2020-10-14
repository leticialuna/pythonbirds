class Pessoa:
    def __init__(self, *filhos, nome=None, idade=39): #atributos
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos) #atributo complexo

    def cumprimentar(self):
        return f'Olá{id(self)}'


if __name__ == '__main__':
    leticia = Pessoa(nome='Leticia')
    simone = Pessoa(leticia, nome='Simone')
    print(Pessoa.cumprimentar(simone))
    print(id(simone))
    print(simone.cumprimentar()) #forma usual
    print(simone.nome)
    print(simone.idade)
    for filho in simone.filhos:
        print(filho.nome)

