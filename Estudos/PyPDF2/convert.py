from PyPDF2 import PdfReader

#Ler e printar a página

'''reader = PdfReader("RioGrandeDoSul.pdf")
page = reader.pages[0] #escolher a página
print(page.extract_text())

'''
#Ignorar o cabeçalho e colocar em um arquivo
reader = PdfReader("RioGrandeDoSul.pdf")

def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 50 and y < 720:
        parts.append(text)

#page = reader.pages[9]

parts = []
i = 0
nome = '51pages.txt'
arquivo = open(nome,'w')
while(i<50):
    page = reader.pages[i]
    page.extract_text(visitor_text=visitor_body)
    text_body = "".join(parts)
    #print(text_body)
    
    print("Opa ",i)
    i += 1

arquivo.write(text_body)

#colocando no aquivo


arquivo.close()