from tkinter import *
from tkinter import messagebox
from datetime import date
from tkinter import ttk

import pymysql

def Cadastro():
    dataatual = date.today()

    datadia = dataatual.day
    datames = dataatual.month
    dataano = dataatual.year


    try:
        conexao = pymysql.connect(

            host='localhost',
            user='root',
            passwd='',
            db='Gastos',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor

        )

    except:
        messagebox.showinfo('ERRO', ' NAO TA CONECTANDO AO BANCO DE DADOS')

    produtin = produto.get()
    gastin = gasto.get()

    try:
        with conexao.cursor() as cursor:
            cursor.execute('insert into despesas (compra, gasto, dia, mes, ano) values (%s, %s, %s, %s, %s)',(produtin, gastin, datadia, datames, dataano))
            conexao.commit()
            messagebox.showinfo('CADASTRADO', f'{produtin}, ADICIONADO COM SUCESSO')
    except:
        messagebox.showinfo('ERRO', 'ERRO AO TENTAR O INSERT')

def Vergastos():

    try:
        conexao = pymysql.connect(

            host='localhost',
            user='root',
            passwd='',
            db='Gastos',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor

        )

    except:
        messagebox.showinfo('ERRO', ' NAO TA CONECTANDO AO BANCO DE DADOS')

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from despesas')
            resultado = cursor.fetchall()
    except:
        messagebox.showinfo('ERRO', 'ERRO AO TENTAR O INSERT')


    carrinho = ttk.Treeview(Principal, selectmode="browse", column=("column1", "column2", "column3", "column4", "column5"), show='headings')
    carrinho.column("column1", width=200, minwidth=500, stretch=NO)
    carrinho.heading('#1', text='COMPRA')

    carrinho.column("column2", width=80, minwidth=200, stretch=NO)
    carrinho.heading('#2', text='GASTO')

    carrinho.column("column3", width=50, minwidth=500, stretch=NO)
    carrinho.heading('#3', text='DIA')

    carrinho.column("column4", width=50, minwidth=500, stretch=NO)
    carrinho.heading('#4', text='MES')

    carrinho.column("column5", width=50, minwidth=500, stretch=NO)
    carrinho.heading('#5', text='ANO')

    carrinho.grid(row=100, column=0, padx=20, pady=20, columnspan=5)


    carrinho.delete(*carrinho.get_children())

    linhaV = []

    for linha in resultado:
        linhaV.append(linha['compra'])
        linhaV.append(linha['gasto'])
        linhaV.append(linha['dia'])
        linhaV.append(linha['mes'])
        linhaV.append(linha['ano'])



        carrinho.insert("", END, values=linhaV, tag='1')

        linhaV.clear()

    soma = 0

    for valor in resultado:

        sominha = float(valor['gasto'])
        soma += sominha

    Label(Principal, text='TEUS GASTOS', width=30).grid(row=101, column=0, columnspan = 5, pady=5, padx=5)
    Button(Principal, text=soma, bg='#E1DF41', fg='black', width=30, relief='flat', font='impact').grid(row=102, column=0, columnspan=5, pady=5, padx=5)








Principal = Tk()
Principal.title('CORTA GASTOS')
Principal['bg'] = '#2ACD8D'

Label(Principal, text='QUANTO TU JA GASTOU', bg='black', fg='white', width=100).grid(row=0, column=0, columnspan=5, pady=10)
gasto = Entry(Principal, text='', bg='white', fg='black', width=30)
gasto.grid(row=1, column=0, columnspan=5, pady=10)


Label(Principal, text='OQUE COMPROU', bg='black', fg='white', width=100).grid(row=2, column=0, columnspan=5, pady=10)

produto = Entry(Principal, text='', bg='white', fg='black', width=30)
produto.grid(row=3, column=0, columnspan=5, pady=10)

Button(Principal, text='CADASTRAR DESPESA', bg='#2A88CD', fg='black', width=30, relief='flat', font='impact', command=Cadastro).grid(row=4, column=0, columnspan=5, pady=60)

Button(Principal, text='VER MEUS GASTOS', bg='#E89B33', fg='black', width=30, relief='flat', font='impact', command=Vergastos).grid(row=5, column=0, columnspan=5)




Principal.mainloop()
