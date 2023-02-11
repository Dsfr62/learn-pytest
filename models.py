class Programa:
  def __init__(self, nome, ano):
    self.__nome = nome.title()
    self.ano = ano
    self.__likes = 0

  def __str__(self):
    return f"\nNome: {self.nome}\nAno: {self.ano}\nLikes: {self.likes}"
  
  @property
  def nome(self):
    return self.__nome
  
  @nome.setter
  def nome(self, novo_nome):
    if novo_nome == self.__nome:
      raise Exception("Novo nome é igual ao nome antigo.")
    self.__nome = novo_nome

  @property
  def likes(self):
    return self.__likes

  def dar_like(self, quantidade:int=1):
    self.__likes += quantidade

class Filme(Programa):
  def __init__(self, nome, ano, duracao):
    super().__init__(nome, ano)
    self.duracao = duracao

class Serie(Programa):
  def __init__(self, nome, ano, temporadas):
    super().__init__(nome, ano)
    self.temporadas = temporadas

