# 1. Logar no site:
#     site: https://intranet.sicoobcredialto.com.br/
    
# 2. Pegar o código de acesso.

# 3. Ir para a parte de chamados.

# 4. Ir em abrir novo chamado.

# 5. Importar base de dados

# 6. Escolher o nome do solicitante

# 7. Selecionar o setor (T.I)

# 8. Selecionar o departamento (Suporte ao usuário)

# 9. Preencher os campos:
    
#     Descrição: Solicitação de suporte 
#     Tipo de suporte: Registro de ligação
#     Motivo Suporte: Falha
#     Sistemas de informação: Office 365
    
# 10. Abrir chamado.

# 11. Clicar em "OK"

# 12. Voltar ao passo 4

import pyautogui

pyautogui.PAUSE = 0.7

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# pyautogui.countdown(1)

pyautogui.write("https://intranet.sicoobcredialto.com.br/")

pyautogui.press("enter")

pyautogui.countdown(3)
#pyautogui.PAUSE = 5
pyautogui.PAUSE = 1

pyautogui.click(x=1198, y=458) #1
pyautogui.click(x=1257, y=489) #2
pyautogui.click(x=1269, y=586) #3
pyautogui.click(x=1736, y=61) #4
pyautogui.click(x=1669, y=296) #5
pyautogui.click(x=1628, y=396) #6
pyautogui.countdown(3)
pyautogui.click(x=971, y=576) #7
#pyautogui.click(x=811, y=682)

pyautogui.countdown(3)
pyautogui.hotkey("ctrl", "v")