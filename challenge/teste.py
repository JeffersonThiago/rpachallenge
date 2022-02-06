from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd


navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
navegador.get("https://www.rpachallenge.com/?lang=EN")

#carregando a tabela do excel em uma variável tabela
tabela = pd.read_excel("challenge.xlsx")


navegador.find_element(By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button").click()

#recuperando as informações de cada linha da tabela
for i, email in enumerate(tabela["Email"]):
	firstName = tabela.loc[i,"First Name"]
	lastName = tabela.loc[i,"Last Name "]
	companyName = tabela.loc[i,"Company Name"]
	roleInCompany = tabela.loc[i,"Role in Company"]
	adress = tabela.loc[i,"Address"]
	phoneNumber = tabela.loc[i,"Phone Number"]

	#recuperando o label de cada campo do formulário, pegando o input mais próximo desse label e setando com cada linha da tabela
	navegador.find_element(By.XPATH,".//label[text() = 'Phone Number']/following-sibling::input").send_keys(str(phoneNumber))
	navegador.find_element(By.XPATH,".//label[text() = 'Email']/following-sibling::input").send_keys(email)
	navegador.find_element(By.XPATH,".//label[text() = 'Address']/following-sibling::input").send_keys(adress)
	navegador.find_element(By.XPATH,".//label[text() = 'Role in Company']/following-sibling::input").send_keys(roleInCompany)
	navegador.find_element(By.XPATH,".//label[text() = 'Company Name']/following-sibling::input").send_keys(companyName)
	navegador.find_element(By.XPATH,".//label[text() = 'Last Name']/following-sibling::input").send_keys(lastName)
	navegador.find_element(By.XPATH,".//label[text() = 'First Name']/following-sibling::input").send_keys(firstName)
	navegador.find_element(By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input").click()

#recupera o resultado do teste, salva e atualiza o arquivo texto.txt
texto1 = navegador.find_element(By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[1]").text
texto2 = navegador.find_element(By.XPATH,"/html/body/app-root/div[2]/app-rpa1/div/div[2]/div[2]").text
f = open('texto.txt' , 'w')
f.write(texto1)
f.write(texto2)
f.close()
#imprime no prompt a informação salva
f = open('texto.txt' , 'r')
print(f.read())
f.close()
