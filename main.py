import requests
from bs4 import BeautifulSoup

link = "https://www.google.com/search?q=cotacao+dolar"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0"}

requisicao = requests.get(link,headers=headers)
print(requisicao)
#print(requisicao.text)

site = BeautifulSoup(requisicao.text,"html.parser")

#print(site.prettify())

#titulo = site.find("title")

#print(titulo)

#pesquisa = site.find_all("input")
#print(pesquisa[1])

#pesquisa2 =site.find("input", class_="gLFyf")
#print(pesquisa2)
#print(pesquisa2["value"])

cotacao_dolar = site.find("span",class_ ="SwHCTb")
print(cotacao_dolar["data-value"])
print(cotacao_dolar.get_text())