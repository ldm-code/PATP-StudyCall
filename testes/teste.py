import pyautogui
import time
import os
import subprocess
import pygetwindow as gw


pyautogui.FAILSAFE = True

BASE_DIR = os.path.dirname(__file__)  
IMG_DIR = os.path.join(BASE_DIR, "imagens")

def clicar(img, confidence=0.9):
    caminho = os.path.join(IMG_DIR, img)
    print("Procurando:", caminho)

    try:
        posicao = pyautogui.locateCenterOnScreen(
            caminho,
            confidence=confidence,
            grayscale=True
        )
    except pyautogui.ImageNotFoundException:
        posicao = None

    if posicao:
        pyautogui.click(posicao)
        print("Clique realizado")
        return True
    else:
        print("Imagem não encontrada na tela")
        return False
def digitar(img, texto,confidence=0.9):
    caminho = os.path.join(IMG_DIR, img)
    print("Procurando:", caminho)

    try:
        posicao = pyautogui.locateCenterOnScreen(
            caminho,
            confidence=confidence,
            grayscale=True
        )
    except pyautogui.ImageNotFoundException:
        posicao = None

    if posicao:
        pyautogui.click(posicao)
        print("Clique realizado")
        time.sleep(2)
        pyautogui.write(texto,interval=0.1)
        return True
    else:
        print("Imagem não encontrada na tela")
        return False
script_pyqt = r"C:\Users\User\Desktop\PATP-StudyCall\main.py"


subprocess.Popen(["python", script_pyqt])
time.sleep(5)  
       

janela = gw.getWindowsWithTitle("StudyCall")[0]
janela.activate()
time.sleep(1)

clicar("adm_botao.png")
time.sleep(2)
clicar("log_btn.png")
time.sleep(2)
digitar('email.png',"rafael@gmail.com")
time.sleep(2)
clicar("tela_login.png")
time.sleep(3)
digitar('senha.png',"123")
time.sleep(2)
clicar('login.png')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
clicar('seleciona_chamado.png')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
clicar('media.png')
time.sleep(2)
clicar('resolvido.png')
time.sleep(2)
digitar('data.png','11/11/2026')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('enter')

