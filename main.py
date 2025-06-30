import tkinter as tk
from action.buscar_dados import captura_dados
from action.armazenar_dados import armazena_dados

def gravar_dados():
    resultado = captura_dados()
    if resultado["erro"]:
        mensagem = armazena_dados(None, None, None, resultado["erro"])        
    else:
        mensagem = armazena_dados(resultado["temperatura"], resultado["umidade"],resultado["data_hora"])

    label_resultado["text"] = mensagem



janela = tk.Tk() #CRIA A JANELA PRINCIPAL
janela.title("Previsão do Tempo em São Paulo") # DEFINE O TITULO DA JANELA
janela.geometry("500x100") # LARGURA X ALTURA

#CRIANDO UM TEXTO
texto = tk.Label(janela, text="Atualizar dados na planilha:")
texto.pack(pady=10) #TEXTO ADICIONADO A JANELA COM ESPACAMENTO VERTICAL

#CRIANDO UM BOTAO
botao = tk.Button(janela, text="Buscar Dados", command=gravar_dados)
botao.pack() #BOTAO ADICIONADO A JANELA COM ESPACEMENTO VERTICAL

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop() #inicia o loop da janela