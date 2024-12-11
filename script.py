from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
 
sevirce = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions() 
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(service=sevirce, options=options)


driver.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

driver.implicitly_wait(2)  

email = driver.find_element(value="email").send_keys("pythonimpressionador@gmail.com")
senha = driver.find_element(value="password").send_keys('sua_senha') 
submit = driver.find_element(value='pgtpy-botao').click()

df = pd.read_csv('produtos.csv')

for index, row in df.iterrows():
    
    codigo = driver.find_element(value="codigo").send_keys(row['codigo'])
    marca = driver.find_element(value="marca").send_keys(row['marca'])
    tipo = driver.find_element(value="tipo").send_keys(row['tipo'])
    categoria = driver.find_element(value="categoria").send_keys(row['categoria'])
    preco_unitario = driver.find_element(value="preco_unitario").send_keys(row['preco_unitario'])
    custo = driver.find_element(value="custo").send_keys(row['custo'])
    if not pd.isna(row['obs']):
        obs = driver.find_element(value="obs").send_keys(row['obs'])
    submit = driver.find_element(value='pgtpy-botao').click()
    