
from tkinter import *
from tkcalendar import DateEntry
from tkinter import *
from tkinter import ttk
from view import *
from tkinter import messagebox




# Cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # azul
co7 = "#ef5350"  # vermelha
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # azul claro

# Criando a janela
janela = Tk()
janela.title("Ficha de Ajuda")  # Titulo da janela
janela.geometry('1043x455')  # Dimensões da janela
janela.configure(background=co9)  # Cor de fundo
janela.resizable(width=FALSE, height=FALSE)  # Impedindo redimensionamento

# Dividindo a janela em frames
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# Texto no topo
app_nome = Label(frame_cima, text='Ficha de Ajuda', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)


#funcao inserir

def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_tel.get()
    data = e_cal_entry.get_date() 
    cidade = e_cidade.get()
    creci = e_creci.get()
    assunto = e_assunto.get()

    lista = [nome,email,telefone,data,cidade,creci,assunto]

    if nome=='':
        messagebox.showerror('Error', 'O nome não pode ser vazio')
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram registrados com sucesso')

        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_tel.delete(0,'end')
        e_cal_entry.delete(0, 'end')
        e_cidade.delete(0,'end')
        e_creci.delete(0,'end')
        e_assunto.delete(0,'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()



#funcao atualizar



    
# Configurando campos no frame de baixo

# Nome
l_nome = Label(frame_baixo, text='Nome', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=10, y=40)

# Email
l_email = Label(frame_baixo, text='Email', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_email.place(x=10, y=70)
e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x=15, y=100)

# Telefone
l_tel = Label(frame_baixo, text='Telefone', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_tel.place(x=10, y=130)
e_tel = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_tel.place(x=15, y=160)

# Data
l_cal_label = Label(frame_baixo, text='Data Nascimento', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cal_label.place(x=10, y=190)
e_cal_entry = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2)
e_cal_entry.place(x=15, y=220)

# Cidade
l_cidade = Label(frame_baixo, text='CEP', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cidade.place(x=160, y=190)
e_cidade = Entry(frame_baixo, width=20, justify='left', relief='solid')
e_cidade.place(x=160, y=220)

# Creci
l_creci = Label(frame_baixo, text='Creci', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_creci.place(x=13, y=260)
e_creci = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_creci.place(x=13, y=290)


# Assunto
l_assunto = Label(frame_baixo, text='Imobiliaria', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_assunto.place(x=15, y=320)
e_assunto = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_assunto.place(x=15, y=350)


#Botao inserir 

b_inserir = Button(frame_baixo, text='Inserir', width=10, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge', command=inserir)
b_inserir.place(x=15, y=375)


#Botao atualizar

b_atualizar= Button(frame_baixo,command=inserir,text='Atualizar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=110, y=375)

#Botao deletar

b_deletar= Button(frame_baixo,text='Deletar', width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=205, y=375)


def mostrar():
    

    lista = mostrar_info()

    # lista para cabecario
    tabela_head = ['ID','Nome',  'email','telefone', 'Data', 'Cidade','Creci','Sobre']


    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=15)


    hd=["nw","nw","nw","nw","nw","nw",'nw', "center"]
    h=[40, 180, 150, 110, 130, 60,40, 80]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
    
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

        frame_direita.grid_rowconfigure(0, weight=1)  # Ajuste o weight conforme necessário


#chamando func mostrar 
mostrar()

janela.mainloop()  # Iniciando o loop principal da janela
