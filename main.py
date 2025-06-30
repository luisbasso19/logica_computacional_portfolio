import tkinter as tk
from action.buscar_dados import captura_dados
from action.armazenar_dados import armazena_dados

def gravar_dados():
    resultado = captura_dados() #chama a funcao que realiza a captura dos dados, e armazena os dados retornados em um dicionario
    if resultado["erro"]:#verifica se existe algum valor valido na chave erro
        mensagem = armazena_dados(None, None, None, resultado["erro"]) #chama a variavel que armazena os dados e grava o valor retornado em uma variavel       
        label_resultado["text"] = mensagem #atualiza o label criado, para que mostre a mensagem de retorno da funcao que armazena os dados na planilha
    else:
        mensagem = armazena_dados(resultado["temperatura"], resultado["umidade"],resultado["data_hora"])#chama a variavel que armazena os dados e grava o valor retornado em uma variavel

        label_resultado["text"] = f"{mensagem} | {resultado['data_hora']}" #atualiza o label criado, para que mostre a mensagem de retorno da funcao que armazena os dados na planilha



janela = tk.Tk() #CRIA A JANELA PRINCIPAL
janela.title("Previsão do Tempo em São Paulo") # DEFINE O TITULO DA JANELA
janela.geometry("500x100") # LARGURA X ALTURA

#CRIANDO UM TEXTO
texto = tk.Label(janela, text="Atualizar dados na planilha:")
texto.pack(pady=10) #TEXTO ADICIONADO A JANELA COM ESPACAMENTO VERTICAL

#CRIANDO UM BOTAO
botao = tk.Button(janela, text="Buscar Dados", command=gravar_dados) #cria o botão e coloca a a acao a ser realizada pelo botao, a chamada da funcao gravar_dados
botao.pack() #BOTAO ADICIONADO A JANELA COM ESPACEMENTO VERTICAL

#CRIA UMA AREA DE TEXTO PARA MOSTRAR SE OS DADOS FORAM GRAVADOS CORRETAMENTE.
label_resultado = tk.Label(janela, text="")
label_resultado.pack()

janela.mainloop() #inicia o loop da janela