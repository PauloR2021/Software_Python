from tkinter import *
import tkinter
from datetime import datetime




#### Cores #####

cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

fundo = cor1
cor = cor2

###### Iniciando o Aplicativo

#Configurando a Janela do Aplicativo
janela=Tk()
janela.title(" ")
janela.geometry('440x180')
janela.resizable(width=FALSE,height=FALSE)
janela.configure(bg=fundo)

#Criaando Uma Função para Salvar as Configurações do Relogio
def relogio():

    # Verificando o Tempo e a Data
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime('%Y')

    #Mostrando a Hora na Label
    l1.config(text=hora)
    #Criando um Método Dinâmico para chamar o Relogio
    l1.after(200,relogio)
    #Mostrando o Dia da Semana, Dia/Mês/Ano
    l2.config(text=dia_semana +" "+ str(dia)+ "/"+ mes +"/" + str(ano))

#Label aonde vai aparecer a Hora
l1 = Label(janela,text="", font=("Times 80"),bg=fundo,fg=cor3)
l1.grid(row=0, column=0,sticky=NW,padx=5)

#Label para Chamar o Dia/Mês/Ano
l2 = Label(janela,text="", font=('Times 20'),bg=fundo,fg=cor)
l2.grid(row=1, column=0,sticky=NW,padx=5)



#Chamando a Função do Relogio
relogio()
janela.mainloop()