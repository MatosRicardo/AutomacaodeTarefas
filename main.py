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

for linha in tabela.index:
    pyautogui.click(x=599, y=280) 

    # Codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    # Marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    
    # Tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    # Categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    # Preço
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    
    #Custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    # Obs
    obs = tabela.loc[linha, "obs"]
    if obs != "nan":
      pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter") # Apertar o botão de enviar

    # Scrool para cima, número positivo
    # Scroll para baixo,  número negativo
    pyautogui.scroll(5000) 


# Passo 5: Repetir o passo 4 em todos os outros produtos automaticamente
# Feito