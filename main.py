from models import Serie, Filme

vingadores = Filme("Vingadores", 2018, 160)

def teste_print():
  prisonBreak = Serie("Prison break", 2004, 6)
  print(prisonBreak.__str__())

teste_print()