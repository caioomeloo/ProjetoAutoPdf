#Algoritmo para automatizar a renomeação de pdfs. O algortimo tem o objetivo de renomear cada pdf baseado em uma numeração que está contida dentro deste. 
#Funciona da seguinte forma: Abre a pasta que contém os pdfs -> seleciona um pdf -> abre este -> copia o número que configura a renomeação - > fecha o pdf -> renomeia o pdf baseado no número selecionado.

#Importa as bibliotecas utilizadas no programa.
import pyautogui
import time

#Determina um delay entre as linhas do código para evitar que certas linhas deixem de ser utilizadas de forma correta.
pyautogui.PAUSE = 0.55

#Pressiona o botão CAPSLOCK do teclado com o objetivo de deixar o nome do arquivo pdf em caixa alta.
pyautogui.press('capslock')
#Pressiona o botão WIN do teclado para que seja pesquisado o endereço na barra de pesquisa do Windows.
pyautogui.press('win')
#Digita TESTE na barra de pesquisa.
pyautogui.write('teste')
#Pressiona o botão ENTER para abrir a pasta TESTE.
pyautogui.press('enter')
#Determina um delay de 1 segundo para dar tempo de carregar a pasta TESTE.
time.sleep(1)
#Clica na tela nas coordenadas determinadas. OBS: Essas coordenadas têm de ser alterada para cada monitor em que o código seja aplicado.
pyautogui.click(x=1444, y=470)
#Pressiona o botão PAGEDOWN por 4 vezes para que o último arquivo da pasta seja selecionado. OBS: O número de clicks varia de acordo com a quantidade de arquivos presentes na pasta.
pyautogui.press('pagedown', 4)
#Determina um delay de 1 segundo para dar tempo para que o arquivo seja selecionado corretamente.
time.sleep(1)
#Pressiona o botão ENTER para que o arquivo selecionado seja aberto.
pyautogui.press('enter')

#Estrutura de repetição que garante que todos os arquivos dentro da pasta sejam selecionados um após o outro. OBS: O segundo parâmetro do laço varia de acordo com a quantidade de arquivos presentes na pasta.
for cont in range(0, 52):
    #Determina um delay de 1.1 segundos para dar tempo para que o pdf seja carregado completamente.
    time.sleep(1.1)
    #Clica na tela nas coordenadas determinadas. OBS: Essas coordenadas foram determinadas para que o click seja em cima do número desejado no pdf. E o número de clicks garante que o número seja selecionado automaticamente.
    pyautogui.click(x=926, y=662, clicks=2)
    #Pressiona os botões CTRL+C para que o número seja copiado.
    pyautogui.hotkey('ctrl', 'c')
    #Pressiona os botões CTRL+W para que o pdf seja fechado. OBS: Esse atalho pode mudar de acordo com o programa utilizado para abrir o pdf.
    pyautogui.hotkey('ctrl', 'w')
    #Pressiona F2 para que o arquivo possa ser renomeado.
    pyautogui.press('f2')
    #Inicia a configuração da renomeação escrevendo PP. OBS: Essa configuração é o padrão desejada pelo requerente do programa.
    pyautogui.write('pp ')
    #Pressiona os botões CTRL+V e adiciona o número que estava copiado no nome do arquivo que está sendo renomeado.
    pyautogui.hotkey('ctrl', 'v')
    #Finaliza a configuração da renomeação escrevendo -PM-FPM-AGOSTO-2023. Obs: Essa configuração é o padrão desejada pelo requerente do programa.
    pyautogui.write('-pm-fpm-agosto-2023')
    #Pressiona a tecla ENTER para que a renomeação seja concluída.
    pyautogui.press('enter')
    #Pressiona a tecla UP para que o próximo arquivo (acima) seja selecionado.
    pyautogui.press('up')
    #Pressiona a tecla ENTER para que o arquivo selecionado seja aberto.
    pyautogui.press('enter')
    #Repete o processo até que todos os arquivos tenham sido renomeados.
