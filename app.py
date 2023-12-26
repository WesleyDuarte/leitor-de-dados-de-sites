from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

driver = webdriver.Edge()
driver.get('https://www.kabum.com.br/computadores/pc/pc-gamer?gad_source=1&gclid=Cj0KCQiAkKqsBhC3ARIsAEEjuJjR1_1_pBZjQxHwR9oyjVli2dJwe4nyo1NU4YLW_vv3nHe1r3nPvisaArAfEALw_wcB')
titulos = driver.find_elements(By.XPATH,"//span[@class='sc-d79c9c3f-0 nlmfp sc-cdc9b13f-16 eHyEuD nameCard']")
precos = driver.find_elements(By.XPATH,"//span[@class='sc-620f2d27-2 bMHwXA priceCard']")

#criando planilha
workbook = openpyxl.Workbook()
#criando a pagina produtos dentro da planilha
workbook.create_sheet('produtos')
#selecionando a pagina produtos e armazenando em uma variavel
sheetProdutos = workbook['produtos']
sheetProdutos['A1'].value = 'Produto'
sheetProdutos['B1'].value = 'Preço'


for titulo,preco in zip(titulos, precos):
    sheetProdutos.append([titulo.text, preco.text])
    
workbook.save('produtos.xlsx')