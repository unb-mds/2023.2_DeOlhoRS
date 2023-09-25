from PyPDF2 import PdfReader

#Ler e printar a página

'''reader = PdfReader("RioGrandeDoSul.pdf")
page = reader.pages[0] #escolher a página
print(page.extract_text())

'''
#Ignorar o cabeçalho e colocar em um arquivo
reader = PdfReader("RioGrandeDoSul.pdf")
page = reader.pages[2]

parts = []


def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 50 and y < 720:
        parts.append(text)


page.extract_text(visitor_text=visitor_body)
text_body = "".join(parts)

print(text_body)

#colocando no aquivo
arquivo = open('arq02.txt','w')
arquivo.write(text_body)
arquivo.close()