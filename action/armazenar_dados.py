import os
from openpyxl import Workbook, load_workbook


def armazena_dados(temperatura, umidade, data, erro=None):
    arquivo_planilha = "capturas.xlsx"
    pasta_armazenamento = "dados_capturados/"
    caminho = pasta_armazenamento + arquivo_planilha
    if not os.path.exists(caminho):
        #cria um novo workbook e coloca os cabecalhos
        wb = Workbook()
        ws = wb.active
        ws.title = 'Capturas'
        ws.append(("Data - Hora","Temperatura", "Umidade"))

        wb.save(caminho)

    if erro:
        pass
    else:
        wb = load_workbook(caminho)
        ws = wb.active

        ws.append((data, temperatura, umidade))

        wb.save(caminho)

        return "Dados salvos com sucesso!"