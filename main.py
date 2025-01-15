import pyautogui
import time

#pyautogui.click -> clicar
#pyautogui.write -> escrever
#pyautogui.press -> pressionar tecla
#pyautogui.hotkey -> atalho

# Passo 1: Acessar o sistema

# Colocar uma pausa entre uma ação e outra
pyautogui.PAUSE = 0.5
# Abrir o menu do Windows
pyautogui.press("win")

# Abrir o navegador Opera
pyautogui.write("Opera")

# Abrir o navegador
pyautogui.press("enter")

#Digita na barra de navageção

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Pedir pro computador esperar 3 segundos
time.sleep(3)

# Passo 2: Fazer Login
pyautogui.click(x=670, y=391) # Clica na aba de e-mail com a posição do mouse

pyautogui.write("dragonballzgtx32@gmail.com")
pyautogui.press("tab")  # Passa para a senha
pyautogui.write("123456")
pyautogui.press("tab") # Passa para o botão de "login"
pyautogui.press("enter")
# Passo 3: Importar a base de dados dos produtos
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

  
time.sleep(2)

# Passo 4: Cadastrar 1 produto
pyautogui.click(x=599, y=280) 

# Codigo
pyautogui.write("MOLO000251")
pyautogui.press("tab")
# Marca
pyautogui.write("Logitech")
pyautogui.press("tab")
# Tipo
pyautogui.write("Mouse")
pyautogui.press("tab")
# Categoria
pyautogui.write("1")
pyautogui.press("tab")
# Preço
pyautogui.write("25.95")
pyautogui.press("tab")
#Custo
pyautogui.write("6.50")
pyautogui.press("tab")
# Obs
pyautogui.write("")
pyautogui.press("tab")

pyautogui.press("enter") # Apertar o botão de enviar


