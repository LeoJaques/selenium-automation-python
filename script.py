from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
from time import sleep
 
sevirce = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions() 
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=sevirce, options=options)


driver.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

driver.implicitly_wait(2)  # Ajustei para 2 segundos para garantir tempo de carregamento

email = driver.find_element(by=By.ID, value="email").send_keys("pythonimpressionador@gmail.com")
senha = driver.find_element(by=By.ID, value="password").send_keys('sua senha')  # Verifique o ID correto do campo de senha
submit = driver.find_element(by=By.ID, value='pgtpy-botao').click()

df = pd.read_csv('produtos.csv')

for line in df.iterrows():
    
    codigo = driver.find_element(by=By.ID, value="codigo").send_keys(line[1]['codigo'])
    marca = driver.find_element(by=By.ID, value="marca").send_keys(line[1]['marca'])
    tipo = driver.find_element(by=By.ID, value="tipo").send_keys(line[1]['tipo'])
    categoria = driver.find_element(by=By.ID, value="categoria").send_keys(line[1]['categoria'])
    preco_unitario = driver.find_element(by=By.ID, value="preco_unitario").send_keys(line[1]['preco_unitario'])
    custo = driver.find_element(by=By.ID, value="custo").send_keys(line[1]['custo'])
    if not pd.isna(line[1]['obs']):
        obs = driver.find_element(by=By.ID, value="obs").send_keys(line[1]['obs'])
    submit = driver.find_element(by=By.ID, value='pgtpy-botao').click()
    