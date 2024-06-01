# CLASSE BASE

class Produto:

    def __init__(self, nome: str, cod: int, valor: float, qtd: int):
        self.nome = nome
        self.cod = cod
        self.valor = valor
        self.qtd = qtd


    def exibirInfo(self):
        return (f'Nome: {self.nome} | Código: {self.cod} | Valor: R$ {self.valor} | Quantidade: {self.qtd}')
    def adicionar(self, qtd: int = 1):
        self.qtd += qtd

    def adicionar(self, qtd: int = 1):
        self.qtd -= qtd

class Aliemtno(Produto):
    def __init__(self, nome, cod, valor, qtd, validade, peso):
        super().__init__(nome, cod, valor, qtd)
        self.__validade = validade
        self.__peso = peso

    def exibirInfo(self):
        return (f'Nome: {self.nome} | Código: {self.cod} | Valor: R$ {self.valor} | Quantidade: {self.qtd} | Validade: {self.__validade} | Peso: {self.__peso}')


class Bebida(Produto):
    def __init__(self, nome:str, cod:int, valor:float, qtd:int, alcoolica: bool, mL:int):
        super().__init__(nome, cod, valor, qtd)
        self.__alcoolica = alcoolica
        self.__mL = mL


class Estoque:
    def __init__(self, listaProdutos = []):
        self.__listaProdutos = listaProdutos


    def adcionar(self, produto):
        self.__listaProdutos.append(produto)

    def remover(self, codProduto):
        for produto in self.__listaProdutos:
            if codProduto == produto.cod:
                self.__listaProdutos.remove(produto)


    def exibirDisponivel(self):
        for produto in self.__listaProdutos:
            if produto.qtd >= 1:
                print(produto.exibirInfo())

    def exibirIndisponivel(self):
        for produto in self.__listaProdutos:
            if produto.qtd == 0:
                print(produto.exibirInfo())
                
    
bebida1 = Bebida(nome='achocolatado', cod=1, valor=2.90, qtd=10, alcoolica=False, mL=250)
alimentos = Aliemtno(nome='arroz', cod=2, valor= 5.9, qtd=50, validade='10/12/2025', peso= '1kg')

estoque = Estoque()
estoque.adcionar(bebida1)
estoque.adcionar(alimentos)

estoque.exibirDisponivel()

