import spacy
from spacy.lang.pt.examples import sentences 
import re



# Carregar o modelo de linguagem para português
nlp = spacy.load("pt_core_news_sm")


import spacy


def encontrar_posicoes_palavras_chave(doc, palavras_chave):
  """
  Encontra as posições das palavras-chave em um documento spaCy.

  Args:
    doc: Um documento spaCy.
    palavras_chave: Uma lista de palavras-chave.

  Returns:
    Uma lista de posições das palavras-chave.
  """

  posições = []
  for palavra_chave in palavras_chave:
    palavra_chave_casefold = palavra_chave.casefold()
    for token in doc:
      if token.text.casefold() == palavra_chave_casefold:
        posições.append(token.i)
  return posições

with open("WebScraping/txt/2009/2009-07-03.txt", "r", encoding="utf-8") as file:
  text = file.read()



def filtrar_nomes(text, palavras_chave):
  """
  Filtra nomes de pessoas em um texto, com base em uma lista de palavras-chave.

  Args:
    text: O texto a ser filtrado.
    palavras_chave: Uma lista de palavras-chave.

  Returns:
    Uma lista de nomes de pessoas encontrados.
  """

  # Processar o texto com spaCy
  doc = spacy.load("pt_core_news_sm")(text)

  # Encontrar nomes de pessoas próximos às palavras-chave
  nomes_nom = []
  for ent in doc.ents:
    if ent.label_ == "PER":
      for pos in encontrar_posicoes_palavras_chave(doc, palavras_chave):
        if 0 <= abs(ent.start - pos) <= 10:
          nomes_nom.append(ent.text)

  # Remover duplicatas
  nomes_nom = list(set(nomes_nom))

  return nomes_nom





nomes_nom = filtrar_nomes(text, [ "nomear",  "NOMEIA", "nomeado", "nomeada", "Nomear"])
nomes_exo = filtrar_nomes(text, ["exonera", "EXONERA",  "exonerada", "exonerado", "exonerar"])

print(nomes_nom)
print(nomes_exo)
