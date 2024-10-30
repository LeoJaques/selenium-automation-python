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

for line in df.iterrows():
    
    codigo = driver.find_element(value="codigo").send_keys(line[1]['codigo'])
    marca = driver.find_element(value="marca").send_keys(line[1]['marca'])
    tipo = driver.find_element(value="tipo").send_keys(line[1]['tipo'])
    categoria = driver.find_element(value="categoria").send_keys(line[1]['categoria'])
    preco_unitario = driver.find_element(value="preco_unitario").send_keys(line[1]['preco_unitario'])
    custo = driver.find_element(value="custo").send_keys(line[1]['custo'])
    if not pd.isna(line[1]['obs']):
        obs = driver.find_element(value="obs").send_keys(line[1]['obs'])
    submit = driver.find_element(value='pgtpy-botao').click()
    