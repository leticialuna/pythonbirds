class Pessoa:
    #atributos de classe = ser criado quando for comum a todos os objetos
    #atributos de instancia = ser criado quando cada objeto tiver um valor especifico
    olhos = 2 #atributo de classe
    def __init__(self, *filhos, nome=None, idade=39): #atributos de instancia
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos) #atributo complexo

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod #decorator
    def metodo_estatico():
        return 42

    @classmethod #metodo de classe
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'

class Mulher(Pessoa): #herança simples -> herda os atributos da classe Pai
    def cumprimentar(self):
        cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3 #sobrescrita de atributo de classe

if __name__ == '__main__':
    leticia = Mutante(nome='Leticia') #herança
    simone = Mulher(leticia, nome='Simone') #herança
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
    print(Pessoa.olhos)
    print(simone.olhos)
    print(leticia.olhos)
    print(id(Pessoa.olhos), id(simone.olhos), id(leticia.olhos))
    print(Pessoa.metodo_estatico(), simone.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), simone.nome_e_atributos_de_classe())
    print(isinstance(Pessoa, Pessoa)) #herança
    print(isinstance(Pessoa, Mulher)) #herança
    print(isinstance(leticia, Pessoa)) #herança
    print(isinstance(leticia, Mulher)) #herança
    print(leticia.olhos)
    print(leticia.cumprimentar())
    print(simone.cumprimentar())