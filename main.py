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
pyautogui.click(x=670, y=391)

pyautogui.write("dragonballzgtx32@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("enter")