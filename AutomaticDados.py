import openpyxl             # leitura de arquivos Excel
import pyperclip            # copiar textos com caracteres especiais
import pyautogui            # para movimentar o mouse entre campos
from time import sleep

# Entrar na planilha
workbook = openpyxl.load_workbook('produtos_ficticios.xlsx')
sheet_produtos = workbook['Produtos']

# Loop através das linhas na planilha
for linha in sheet_produtos.iter_rows(min_row=2): 
    nome_produto = linha[0].value 
    pyperclip.copy(nome_produto)
    pyautogui.click(1371, 347, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    descricao = linha[1].value
    pyperclip.copy(descricao)
    pyautogui.click(1418, 436, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    categoria = linha[2].value
    pyperclip.copy(categoria)
    pyautogui.click(1384, 568, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    codigo_produto = linha[3].value
    pyperclip.copy(codigo_produto)
    pyautogui.click(1359, 651, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    peso = linha[4].value
    pyperclip.copy(peso)
    pyautogui.click(1364, 738, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    dimensao = linha[5].value
    pyperclip.copy(dimensao)
    pyautogui.click(1364, 823, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.click(1368, 889, duration=1)
    sleep(3)

    preco = linha[6].value
    pyperclip.copy(preco)
    pyautogui.click(1361, 372, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    quantdade_em_estoque = linha[7].value
    pyperclip.copy(quantdade_em_estoque)
    pyautogui.click(1358,455, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    data_de_validade = linha[8].value
    pyperclip.copy(data_de_validade)
    pyautogui.click(1402, 538, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    cor = linha[9].value
    pyperclip.copy(cor)
    pyautogui.click(1374, 629, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    tamanho = linha[10].value
    pyautogui.click(1391,713, duration=1)
    if tamanho == 'pequeno':
        pyautogui.click(1381,745, duration=1)
    elif tamanho == 'Médio':
        pyautogui.click(1383,766, duration=1)
    else:
        pyautogui.click(1380,789, duration=1)

    material = linha[11].value
    pyperclip.copy(material)
    pyautogui.click(1379, 800, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    pyautogui.click(1369, 861, duration=1)

    fabricante = linha[12].value
    pyperclip.copy(fabricante)
    pyautogui.click(1406, 394, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    pais_origem = linha[13].value
    pyperclip.copy(pais_origem)
    pyautogui.click(1355, 479, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    obsevacoes = linha[14].value
    pyperclip.copy(obsevacoes)
    pyautogui.click(1358, 560, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    codigo_de_barras = linha[15].value
    pyperclip.copy(codigo_de_barras)
    pyautogui.click(1378, 697, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    localizacao_armazem = linha[16].value
    pyperclip.copy(localizacao_armazem)
    pyautogui.click(1362, 780, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    # Botão concluir
    pyautogui.click(1406, 849, duration=1)

    # Botão Salva no banco de dados!
    pyautogui.click(1773, 190, duration=1)

    # Botão cadastra novamente
    pyautogui.click(1580, 615, duration=1)

    # Repetir esses passos para outros campos até aparecer campos daquela página
    # Clicar em próximo
    # Repetir os mesmos passos e ir para a próxima página (página 2)
    # Repetir os mesmos passos e finalizar o cadastro daquele produto e clicar em concluir
    # Clicar em OK para finalizar o processo
    # Clicar em "Adicionar mais um" e repetir o processo até finalizar a planilha
