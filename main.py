import tkinter as tk

janela = tk.Tk() #CRIA A JANELA PRINCIPAL
janela.title("Previsão do Tempo em São Paulo") # DEFINE O TITULO DA JANELA
janela.geometry("500x100") # LARGURA X ALTURA

#CRIANDO UM TEXTO
texto = tk.Label(janela, text="Atualizar dados na planilha:")
texto.pack(pady=10) #TEXTO ADICIONADO A JANELA COM ESPACAMENTO VERTICAL

#CRIANDO UM BOTAO
botao = tk.Button(janela, text="Buscar Dados")
botao.pack(pady=10) #BOTAO ADICIONADO A JANELA COM ESPACEMENTO VERTICAL

janela.mainloop() #inicia o loop da janela