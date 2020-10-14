class Pessoa:
    #atributos de classe = ser criado quando for comum a todos os objetos
    #atributos de instancia = ser criado quando cada objeto tiver um valor especifico
    olhos = 2 #atributo de classe
    def __init__(self, *filhos, nome=None, idade=39): #atributos de instancia
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
    simone.sobrenome = 'Santos' #atributo dinamico
    del simone.filhos #deletar atributo dinamico
    print(simone.__dict__) #permite acessar os atributos
    print(leticia.__dict__)
    leticia.olhos = 3
    print(Pessoa.olhos)
    print(simone.olhos)
    print(leticia.olhos)
    print(id(Pessoa.olhos), id(simone.olhos), id(leticia.olhos))
