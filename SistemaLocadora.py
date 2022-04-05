from tkinter import *
#import tkinter.messagebox
from tkinter import messagebox
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter as tk #radiobuton
from time import sleep #segundo
from tkinter import ttk #combobox,progressbar,abas
from tkinter.ttk import Progressbar
from time import strftime
import tkinter
from tkcalendar import Calendar,DateEntry
from tkinter import filedialog
from PIL import ImageTk,Image
    

def fun():    

    lo = Toplevel()
    lo.title("Login")
    lo.geometry("453x444+500+100")
    lo.resizable(0,0)
    lo.config(bg="#C0C0C0")
    lo.overrideredirect(True)
    lo.focus_force()
    lo.grab_set()
        
    def Cliente():

        janel = Toplevel()
        janel.title("Cadastrar Clientes")
        janel.geometry("644x356+455+131")
        janel.config(bg="grey")
        janel.resizable(0,0)
        janel.iconbitmap("imagem/car.ico")
        janel.transient(loo)
        janel.focus_force()
        janel.grab_set()
        
        def gravar():

            dbo = sqlite3.connect("Sistema.db")
            cur = dbo.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY,nome TEXT,sexo TEXT,telefone INTEGER,morada TEXT,casa TEXT,cd TEXT,ad TEXT,i INTEGER,email TEXT)")
            if id.get()=="" or nome.get()=="" or telefone.get()=="" or morada.get()=="" or email.get()=="" or casa.get()=="" or cd.get()=="" or ad.get()=="" or i.get()=="":
                messagebox.showerror("Rent Car","Por favor preencha os dados correctamente")
            else:
                cur.execute("INSERT INTO clientes VALUES(?,?,?,?,?,?,?,?,?,?)",(id.get(),nome.get(),sexo.get(),telefone.get(),morada.get(),casa.get(),cd.get(),ad.get(),i.get(),email.get()))
                messagebox.showinfo("Rent Car","Dados guardados com corretamente")
                for x in lista.get_children():
                    lista.delete(x)
                cur.execute("SELECT * FROM clientes")
                row = cur.fetchall()
                for data in row:
                    lista.insert('',"end",values=(data))
                dbo.commit()
                limpaar()

        def limpaar():

            id.delete(0,END)
            nome.delete(0,END)
            telefone.delete(0,END)
            morada.delete(0,END)
            email.delete(0,END)
            casa.delete(0,END)
            cd.delete(0,END)
            ad.delete(0,END)
            i.delete(0,END)


        def alterar():

            dbo = sqlite3.connect("Sistema.db")
            cur = dbo.cursor()

            n = id.get()
            p = morada.get()
            m = sexo.get()
            l = i.get()
            s = nome.get()
            v = telefone.get()
            c = ad.get()
            k = cd.get()
            b = casa.get()
            o = email.get()

            if id.get()=="" or nome.get()=="" or telefone.get()=="" or morada.get()=="" or email.get()=="" or casa.get()=="" or cd.get()=="" or ad.get()=="" or i.get()=="":
                messagebox.showerror("Rent Car","Por favor seleciona os dados que pretendes actualizar!")
            else:
                cur.execute("UPDATE clientes SET morada=?,sexo=?,i=?,nome=?,telefone=?,ad=?,cd=?,casa=?,email=? WHERE id=?",(p,m,l,s,v,c,k,b,o,n))
                messagebox.showinfo("Rent Car","Dados Actualizado com sucesso")
                limpaar()
                dbo.commit()
                for s in lista.get_children():
                    lista.delete(s)
                cur.execute("SELECT * FROM clientes")
                sav = cur.fetchall()
                for row in sav:
                    lista.insert("","end",values=(row))
            
        nb = ttk.Notebook(janel)
        nb.place(x=1,y=1,width=642,height=354)

        janela=Frame(nb)
        aluguel=Frame(nb)

        nb.add(janela,text="Cadastrar Cliente")
        nb.add(aluguel,text="Consultar Clientes")
            
        MainFrame = Frame(janela,padx=317,pady=160,bg="#e9e9e9")
        MainFrame.place(x=2,y=2)

        BI = Label(MainFrame,font=("Agency FB",16,"bold"),bg="#e9e9e9",text="",fg="Black")   
        BI.grid(row=0, column=2)

        nome = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Nome",fg="Black")
        nome.place(x=56,y=13)

        nome = Entry(janela,bd=1,width="19",font=(8),relief="solid")
        nome.place(x=59,y=38)

        codigo = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Codigo",fg="Black")
        codigo.place(x=12,y=13)    

        id = Entry(janela,bd=1,width="4",font=(8),relief="solid")
        id.place(x=15,y=38)
           
        morada = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Endereço",fg="Black")
        morada.place(x=240,y=13)

        morada = Entry(janela,bd=1,width="16",font=(8),relief="solid")
        morada.place(x=243,y=38)

        casa = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Casa Nº",fg="Black")
        casa.place(x=392,y=13)

        casa = Entry(janela,bd=1,width="6",font=(8),relief="solid")
        casa.place(x=395,y=38) 

        telefone = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Telefone",fg="Black")
        telefone.place(x=12,y=72)

        telefone = Entry(janela,bd=1,width="24",font=(8),relief="solid")
        telefone.place(x=15,y=97)

        cd = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Província",fg="Black")
        cd.place(x=12,y=132)

        cd = Entry(janela,bd=1,width="18",font=(8),relief="solid")
        cd.place(x=15,y=155)

        ad = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Area de Trabalho",fg="Black")
        ad.place(x=186,y=132)

        ad = Entry(janela,bd=1,width="23",font=(8),relief="solid")
        ad.place(x=190,y=155)

        i = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Idade",fg="Black")
        i.place(x=406,y=132)

        i = Spinbox(janela,bd=1,width="3",font=(8),relief="solid",from_=18, to=100)
        i.place(x=409,y=155)  

        email = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="E-mail",fg="Black")
        email.place(x=240,y=72)

        email = Entry(janela,bd=1,width="23",font=(8),relief="solid")
        email.place(x=243,y=97)

        group = LabelFrame(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Sexo",padx=42,pady=2)
        group.place(x=15,y=180)

        sexo = StringVar()

        AL = tk.Radiobutton(group,font=("Agency FB",12,"bold"),text="Masculino",value="Masculino",variable=sexo,bg="#e9e9e9")
        AL.pack()
                
        AL2 = tk.Radiobutton(group,font=("Agency FB",12,"bold"),text="Femenino",value="Femenino",variable=sexo,bg="#e9e9e9")
        AL2.pack()

        #lis = Listbox(janela,width=20,height=50)
        #lis.place(x=210,y=30)
            
            
        def im2():
            
            global photo
            janel.filename = filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("png files","*.png"),("all files","*.*")))
            fotoo.insert(END,janel.filename)
            #janel.filename.thumbnail((130,130))
            #reside = photo.resize((300,500), Image.ANTIALTAS)
            #pillow
            photo = ImageTk.PhotoImage(Image.open(janel.filename))
            #photo = photo.resize((300,500), Image.ANTIALTAS)
            IM = Label(janel, image=photo)
            IM.place(x=480,y=38)
            
        fotoo = Entry(janela,bd=1,width="40",font=(6),relief="solid")
        fotoo.place(x=190,y=247)

        p = PhotoImage(file="imagem/mb.png")
        po = Label(janela,image=p,bg="#e9e9e9")
        po.place(x=469,y=28) 

        bt = Button(janela,font=("Agency FB",10,"bold"),text="Imagem",width=66,bg="white",height=17,bd=1,relief="solid",command=im2)
        bt.place(x=560,y=246)

        foto = PhotoImage(file="imagem/foto.png")
        bt.config(image=foto,compound=LEFT)

        b2 = Button(janela,font=("Agency FB",10,"bold"),text="SALVAR",bg="white",width="65",height="40",bd=2,relief=RIDGE,command=gravar)
        b2.place(x=560,y=273)

        foto24 = PhotoImage(file="imagem/guardar.png")
        b2.config(image=foto24,compound=TOP)

        b3 = Button(janela,font=("Agency FB",10,"bold"),text="SAIR",bg="white",width="65",height="40",bd=2,relief=RIDGE,command=janel.destroy)
        b3.place(x=401,y=273)

        foto33 = PhotoImage(file="imagem/sair.png")
        b3.config(image=foto33,compound=TOP)

        b2 = Button(janela,font=("Agency FB",10,"bold"),text="ALTERAR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=alterar)
        b2.place(x=481,y=273)

        foto2 = PhotoImage(file="imagem/Alterar.png")
        b2.config(image=foto2,compound=TOP)
            
        def excluir():
          idselect = lista.item(lista.selection())['values'][0]
          db = sqlite3.connect("Sistema.db")
          cur = db.cursor()
          result=tkMessageBox.askquestion("Rent car","Tens Certeza que queres excluir do Sistema?",icon="warning")
          if result == "yes":
              messagebox.showinfo("Rent Car","Dados excluidos do Sistema")
              limpaar()
              delete = cur.execute("delete from clientes where id={}".format(idselect))
              lista.delete(lista.selection())
          db.commit()                  

        def duploclick(event):

            limpaar()
            lista.selection()
            for x in lista.selection():
                col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = lista.item(x, 'values')

            id.insert(END, col1)
            nome.insert(END, col2)
            morada.insert(END, col5)
            casa.insert(END, col6)
            email.insert(END, col10)
            telefone.insert(END, col4)
            cd.insert(END, col7)
            ad.insert(END, col8)
            i.insert(END, col9)
            
        def pesquisar():

           pp = cod.get()
           cur.execute("SELECT * FROM clientes WHERE id = (?)",(pp,))
           row = cur.fetchall()
           if row!=[]:
               limpaar()
               for x in lista.get_children():
                    lista.delete(x)
               for data in row:
                    lista.insert('',"end",values=(data))
                    cod.delete(0,END)
           else:
               messagebox.showerror("Rent Car","Nenhum dado encontrado na base de Dados")
               cod.delete(0,END)
           #cod.delete(0,END)
                    
        def pesquisar2():
            
           p = pes.get()
           cur.execute("SELECT * FROM clientes WHERE nome = (?)",(p,))
           roww = cur.fetchall()
           if roww!=[]:
               limpaar()
               for x in lista.get_children():
                    lista.delete(x)
               for data in roww:
                    lista.insert('',"end",values=(data))
                    pes.delete(0,END)
           else:
               messagebox.showerror("Rent Car","Nenhum dado encontrado na base de Dados")
               pes.delete(0,END)

        def voltar():

               for x in lista.get_children():
                    lista.delete(x)
               cur.execute("SELECT * FROM clientes")
               row = cur.fetchall()
               for data in row:
                   lista.insert('',"end",values=(data))


        MainFrame = Frame(aluguel,padx=314,pady=260,bg="#e9e9e9")
        MainFrame.place(x=2,y=2)

        Lb = Label(MainFrame,font=("Arial",12,"bold"),text="",bg="#e9e9e9")
        Lb.grid(row = 0,column = 2)

        pes = Label(aluguel,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Pesquisar ID")
        pes.place(x=19,y=15)

        cod = Entry(aluguel,font=("Arial",11),fg="black",width=10,bd=1,relief="solid")
        cod.place(x=23,y=40)

        pes = Label(aluguel,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Pesquisar Nome")
        pes.place(x=155,y=15)

        pes = Entry(aluguel,font=("Arial",11),fg="black",width=45,bd=1,relief="solid")
        pes.place(x=158,y=40)

        btm = Button(aluguel,font=("Agency FB",10,"bold"),text="",width=30,bg="white",height=17,bd=2,command=pesquisar,relief=RIDGE)
        btm.place(x=110,y=39)

        foto35 = PhotoImage(file="imagem/p.png")
        btm.config(image=foto35,compound=LEFT)

        bt = Button(aluguel,font=("Agency FB",10,"bold"),text="PESQUIZAR",width=75,bg="white",height=18,bd=2,command=pesquisar2,relief=RIDGE)
        bt.place(x=524,y=37)

        foto32 = PhotoImage(file="imagem/p.png")
        bt.config(image=foto32,compound=LEFT)

        lista = ttk.Treeview(aluguel,height=8,column=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10"),show='headings')   

        lista.heading("#1",text="ID")
        lista.heading("#2",text="Nome")
        lista.heading("#3",text="Sexo")
        lista.heading("#4",text="Telefone")
        lista.heading("#5",text="Endereço")
        lista.heading("#6",text="Casa")
        lista.heading("#7",text="Província")
        lista.heading("#8",text="Area de trabalho")
        lista.heading("#9",text="Idade")
        lista.heading("#10",text="E-mail")

        lista.column("#1",width=32)
        lista.column("#2",width=130)
        lista.column("#3",width=90)
        lista.column("#4",width=90)
        lista.column("#5",width=120)
        lista.column("#6",width=90)
        lista.column("#7",width=90)
        lista.column("#8",width=150)
        lista.column("#9",width=65)
        lista.column("#10",width=160)    

        lista.bind("<Double-1>", duploclick)
        
        lista.place(x=23,y=70,width=571)

        #barra de rolagem
        estiloo = ttk.Style()
        estiloo.theme_use("clam")
        estiloo.configure("Treeview",rowheight=20)
        estiloo.map('Treeview',background=[('selected','grey')])
                   
        barra= ttk.Scrollbar(aluguel,command=lista.yview)
        lista.configure(yscroll=barra.set)
        barra.place(x=593,y=70,height=203)

        barra= ttk.Scrollbar(aluguel,command=lista.xview,orient="horizontal")
        lista.configure(xscroll=barra.set)
        barra.place(x=23,y=259,width=571)

        dbo = sqlite3.connect("Sistema.db")
        cur = dbo.cursor()
        cur.execute("SELECT * FROM clientes")
        row = cur.fetchall()
        for savio in row:
            lista.insert("",END,values=savio)
        dbo.commit()

        b1 = Button(aluguel,font=("Agency FB",10,"bold"),text="VOLTAR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=voltar)
        b1.place(x=455,y=275)

        foto1 = PhotoImage(file="imagem/back.png")
        b1.config(image=foto1,compound=TOP)

        b3 = Button(aluguel,font=("Agency FB",10,"bold"),text="EXCLUIR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=excluir)
        b3.place(x=533,y=275)

        foto3 = PhotoImage(file="imagem/ex.png")
        b3.config(image=foto3,compound=TOP)

        b5 = Button(aluguel,font=("Agency FB",10,"bold"),text="SAIR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=janel.destroy)
        b5.place(x=376,y=275)

        foto5 = PhotoImage(file="imagem/sair.png")
        b5.config(image=foto5,compound=TOP)

        aluguel.mainloop()

    def Veiculo ():

        janel = Toplevel()
        janel.title("Cadastrar Carros")
        janel.geometry("644x356+455+131")
        janel.config(bg="grey")
        janel.resizable(0,0)
        janel.iconbitmap("imagem/car.ico")
        janel.transient(loo)
        janel.focus_force()
        janel.grab_set()
        
        def gravar():

            db = sqlite3.connect("Sistema.db")
            cur = db.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS veiculos(id INTEGER primary key,modelo TEXT,marca TEXT,placa TEXT,tpveiculo TEXT,km INTEGER,V TEXT,ano INTEGER,data INTEGER,data2 INTEGER,Radio TEXT,combu TEXT)")
            if modelo.get()=="" or marca.get()=="" or placa.get()=="" or tpveiculo.get()=="" or km.get()=="" or V.get()=="" or ano.get()=="" or data.get()=="" or data2.get()=="" or Radio.get()==""or combu.get()=="":
                messagebox.showerror("Hertz Rentcar Luanda","Por favor preencha os dados correctamente")
            else:
                cur.execute("INSERT INTO veiculos VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(id.get(),modelo.get(),marca.get(),placa.get(),tpveiculo.get(),km.get(),V.get(),ano.get(),data.get(),data2.get(),Radio.get(),combu.get()))
                messagebox.showinfo("Rent car Luanda","Dados guardados com corretamente")
                for x in lis.get_children():
                    lis.delete(x)
                cur.execute("SELECT * FROM veiculos")
                row = cur.fetchall()
                for dataa in row:
                    lis.insert('',"end",values=(dataa))
                limpar()
            db.commit()

        def limpar():

            id.delete(0,END)
            modelo.delete(0,END)
            marca.delete(0,END)
            placa.delete(0,END)
            tpveiculo.delete(0,END)
            km.delete(0,END)
            V.delete(0,END)
            ano.delete(0,END)
            data.delete(0,END)
            data2.delete(0,END)
            combu.delete(0,END)

        def alterar():

            dbo = sqlite3.connect("Sistema.db")
            cur = dbo.cursor()

            n = id.get()
            p = modelo.get()
            m = marca.get()
            l = placa.get()
            s = tpveiculo.get()
            v = km.get()
            c = V.get()
            k = ano.get()
            b = data.get()
            o = data2.get()
            od = combu.get()
            r = Radio.get()

            if id.get()=="" or modelo.get()=="" or marca.get()=="" or placa.get()=="" or tpveiculo.get()=="" or km.get()=="" or V.get()=="" or ano.get()=="" or data.get()=="" or data2.get()=="" or Radio.get()==""or combu.get()=="": 
                messagebox.showerror("Rent Car","Por favor seleciona os dados que pretendes actualizar!")
            else:
                cur.execute("UPDATE veiculos SET modelo=?,marca=?,placa=?,tpveiculo=?,km=?,V=?,ano=?,data=?,data2=?,combu=?,Radio=? WHERE id=?",(p,m,l,s,v,c,k,b,o,od,r,n))
                messagebox.showinfo("Rent Car","Dados Actualizado com sucesso")
                limpar()
                dbo.commit()
                for s in lis.get_children():
                    lis.delete(s)
                cur.execute("SELECT * FROM veiculos")
                sav = cur.fetchall()
                for row in sav:
                    lis.insert("","end",values=(row))

        def calendar():

            def hj():

                data.delete(0,END)
                data.insert(END, calan.get_date())
                top.destroy()

            top = Toplevel(janela)
            top.title("")
            top.geometry("193x228+800+190")
            top.resizable(0,0)
            top.transient(janela)
            top.focus_force()
            top.grab_set()
            calan = Calendar(top,font=("Agency FB",10),bg="white",width="50",height="3",locale='pt_ao')
            calan.place(x=1,y=1)
            
            calendario = Button(top,text="Inserir data",width=26,height=1,command=hj)
            calendario.place(x=1,y=202)

        def calendar2():

            def hj():

                data2.delete(0,END)
                data2.insert(END, calan.get_date())
                top.destroy()

            top = Toplevel(janela)
            top.title("")
            top.geometry("193x228+800+190")
            top.resizable(0,0)
            top.transient(janela)
            top.focus_force()
            top.grab_set()
            
            calan = Calendar(top,font=("Agency FB",10),bg="white",width="50",height="3",locale='pt_ao')
            calan.place(x=1,y=1)
            
            calendario = Button(top,text="Inserir data",width=26,height=1,command=hj)
            calendario.place(x=1,y=202)
            #f.delete(0,END)

        nb = ttk.Notebook(janel)
        nb.place(x=1,y=1,width=642,height=354)

        janela=Frame(nb)
        aluguel=Frame(nb)

        nb.add(janela,text="Cadastrar Veiculos")
        nb.add(aluguel,text="Estoque de Veiculos")
        
        MainFrame = Frame(janela,padx=317,pady=161,bg="#e9e9e9")
        MainFrame.place(x=2,y=2)

        BI = Label(MainFrame,font=("Agency FB",16,"bold"),bg="#e9e9e9",fg="Black",text="")   
        BI.grid(row=0, column=2)

        def im():
            
            global photo
            janel.filename = filedialog.askopenfilename(initialdir="/",title="Select File",filetypes=(("png files","*.png"),("all files","*.*")))
            f.insert(END,janel.filename)
            #janel.filename.thumbnail((130,130))
            #reside = photo.resize((300,500), Image.ANTIALTAS)
            #pillow
            photo = ImageTk.PhotoImage(Image.open(janel.filename))
            #photo = photo.resize((300,500), Image.ANTIALTAS)
            IM = Label(janel, image=photo)
            IM.place(x=480,y=38)

        codigo = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Codigo",fg="Black")
        codigo.place(x=12,y=24)    

        id = Entry(janela,bd=1,width="5",font=(8),relief="solid")
        id.place(x=15,y=53)

        MO = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Modelo")
        MO.place(x=69,y=24)

        modelo = Entry(janela,bd="1",font=(8),width="18",relief="solid")
        modelo.place(x=72,y=53)

        DE = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Data de Aluguel")
        DE.place(x=243,y=24)

        data = Entry(janela,bd="1",font=(18),width="8",relief="solid")
        data.place(x=246,y=53)

        calendario = Button(janela,bg="white",width=18,command=calendar2)
        calendario.place(x=445,y=50)

        calData = Button(janela,bg="white",width=18,command=calendar)
        calData.place(x=325,y=50)

        fot = PhotoImage(file="imagem/cal.png")
        calendario.config(image=fot,compound=LEFT)

        fo = PhotoImage(file="imagem/cal.png")
        calData.config(image=fo,compound=LEFT)
        
        data2 = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Data de Prazo")
        data2.place(x=363,y=24)

        data2 = Entry(janela,font=(8),width="8",bd=1,relief="solid")
        data2.place(x=366,y=53)    

        TP = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Tipo de Veiculo")
        TP.place(x=12,y=90)

        tpveiculo = ttk.Combobox(janela,font=("Arial",11),width=15)
        tpveiculo['values'] = ("Automatico","Manual")
        tpveiculo.place(x=16,y=116)

        KM = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Nº do Motor")
        KM.place(x=161,y=90)

        km = Entry(janela,bd="1",font=(8),width="17",relief="solid")
        km.place(x=164,y=116)

        V = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Cor")
        V.place(x=327,y=90)

        V = ttk.Combobox(janela,font=("Arial",11),width=15)
        V['values'] = ("Azul","Amarelo","Cinza","Vermelho","Preto")
        V.place(x=330,y=116)

        ANO = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Ano")
        ANO.place(x=400,y=203)

        ano = Entry(janela,bd="1",font=(8),width="7",relief="solid")
        ano.place(x=403,y=228)

        combu = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Combustivel")
        combu.place(x=327,y=150)

        combu = ttk.Combobox(janela,font=("Arial",11),width=15)
        combu['values'] = ("Gasolina","Gasoleo")
        combu.place(x=330,y=175)

        MA = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Marca")
        MA.place(x=144,y=150)

        marca = Entry(janela,bd="1",font=(8),width="19",relief="solid")
        marca.place(x=147,y=175)

        PL = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Matricula")
        PL.place(x=144,y=203)

        placa = Entry(janela,font=(8),width="27",bd=1,relief="solid")
        placa.place(x=147,y=228)

        #imagem
        f = Entry(janela,font=(5),width="44",bd=1,relief="solid")
        f.place(x=147,y=257)

        p = PhotoImage(file="imagem/sd.png")
        po = Label(janela,image=p,bg="#e9e9e9")
        po.place(x=500,y=61)

        bt = Button(janela,font=("Agency FB",10,"bold"),text="Imagem",width=66,bg="white",height=18,bd=1,relief="solid",command=im)
        bt.place(x=555,y=256)

        foto = PhotoImage(file="imagem/foto.png")
        bt.config(image=foto,compound=LEFT)

        group = LabelFrame(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Alugado",padx=30,pady=24)
        group.place(x=15,y=150)

        Radio = StringVar()

        AL = tk.Radiobutton(group,font=(8),text="Sim",value="Sim",variable=Radio,bg="#e9e9e9")
        AL.pack()
                
        AL2 = tk.Radiobutton(group,font=(8),text="Não",value="Não",variable=Radio,bg="#e9e9e9")
        AL2.pack()

        b2 = Button(janela,font=("Agency FB",10,"bold"),text="SALVAR",bg="white",width="65",height="34",bd=2,relief=RIDGE,command=gravar)
        b2.place(x=553,y=281)

        foto2 = PhotoImage(file="imagem/guardar.png")
        b2.config(image=foto2,compound=TOP)    
      
        b3 = Button(janela,font=("Agency FB",10,"bold"),text="SAIR",bg="white",width="65",height="34",bd=2,relief=RIDGE,command=janel.destroy)
        b3.place(x=396,y=281)

        foto357 = PhotoImage(file="imagem/sair.png")
        b3.config(image=foto357,compound=TOP)

        b2 = Button(janela,font=("Agency FB",10,"bold"),text="ALTERAR",bg="white",width=65,height=34,bd=2,relief=RIDGE,command=alterar)
        b2.place(x=475,y=281)

        foto24 = PhotoImage(file="imagem/Alterar.png")
        b2.config(image=foto24,compound=TOP)

        def pesquisar():

           pp = cod.get()
           cur.execute("SELECT * FROM veiculos WHERE id = (?)",(pp,))
           row = cur.fetchall()
           if row!=[]:
               limpar()
               for x in lis.get_children():
                    lis.delete(x)
               for data in row:
                    lis.insert('',"end",values=(data))
                    cod.delete(0,END)
           else:
               messagebox.showerror("Rent Car","Nenhum dado encontrado na base de Dados")
               cod.delete(0,END)
           #cod.delete(0,END)
                    
        def pesquisar2():
            
           p = pes.get()
           cur.execute("SELECT * FROM veiculos WHERE marca = (?)",(p,))
           roww = cur.fetchall()
           if roww!=[]:
               limpar()
               for x in lis.get_children():
                    lis.delete(x)
               for data in roww:
                    lis.insert('',"end",values=(data))
                    pes.delete(0,END)
           else:
               messagebox.showerror("Rent Car","Nenhum dado encontrado na base de Dados")
               pes.delete(0,END)

               
        def voltar():

            for x in lis.get_children():
                lis.delete(x)
            cur.execute("SELECT * FROM veiculos")
            row = cur.fetchall()
            for s in row:
                lis.insert("","end",values=(s))

        def excluir():
            
          idselect = lis.item(lis.selection())['values'][0]
          db = sqlite3.connect("Sistema.db")
          cur = db.cursor()
          result=tkMessageBox.askquestion("Rent Car","Tens Certeza que queres excluir do Sistema?",icon="warning")
          if result == "yes":
              messagebox.showinfo("Rent Car","Dados excluidos do Sistema")
              delete = cur.execute("delete from veiculos where id={}".format(idselect))
              lis.delete(lis.selection())
          db.commit()
            
        def limpar2():
            
            id.delete(0,END)
            modelo.delete(0,END)
            marca.delete(0,END)
            placa.delete(0,END)
            tpveiculo.delete(0,END)
            km.delete(0,END)
            V.delete(0,END)
            ano.delete(0,END)
            data.delete(0,END)
            data2.delete(0,END)
            combu.delete(0,END)

        def duploclick(event):

            limpar2()

            lis.selection()
            for x in lis.selection():
                col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12= lis.item(x, 'values')
                
                id.insert(END, col1)
                modelo.insert(END, col2)
                marca.insert(END, col3)
                placa.insert(END, col4)
                tpveiculo.insert(END, col5)
                km.insert(END, col6)
                V.insert(END, col7)
                ano.insert(END, col8)
                data.insert(END, col9)
                data2.insert(END, col10)
                combu.insert(END, col12)

        def alterar():
           
            db = sqlite3.connect("Sistema.db")
            cur = db.cursor()
            cur.execute("UPDATE clientes SET nome=(?),casa=(?),telefone=(?),morada=(?),email=(?),cd=(?),ad=(?)",(nome.get(),sexo.get(),telefone.get(),morada.get(),casa.get(),cd.get(),ad.get(),email.get()))
            for x in lista.get_children():
                lista.delete(x)
            cur.execute("SELECT * FROM clientes")
            row = cur.fetchall()
            for data in row:
                lista.insert('',"end",values=(data))
            db.commit()
            db.close()


        def calendar():

            def hj():

                data.delete(0,END)
                data.insert(END, calan.get_date())
                top.destroy()

            top = Toplevel(aluguel)
            top.title("")
            top.geometry("193x228+800+90")
            top.resizable(0,0)
            top.transient(aluguel)
            top.focus_force()
            top.grab_set()
            calan = Calendar(top,font=("Agency FB",10),bg="white",width=500,height=3,locale='pt_ao')
            calan.place(x=1,y=1)
            
            calendario = Button(top,text="Inserir data",width=26,height=1,command=hj)
            calendario.place(x=1,y=202)

        def calendar2():

            def hj():

                data2.delete(0,END)
                data2.insert(END, calan.get_date())
                top.destroy()

            top = Toplevel(aluguel)
            top.title("")
            top.geometry("193x228+800+90")
            top.resizable(0,0)
            top.transient(aluguel)
            top.focus_force()
            top.grab_set()
            
            calan = Calendar(top,font=("Agency FB",10),bg="white",width=75,height=3,locale='pt_ao')
            calan.place(x=1,y=1)
            
            calendario = Button(top,text="Inserir data",width=26,height=1,command=hj)
            calendario.place(x=1,y=202)  

        MainFrame = Frame(aluguel,padx=317,pady=164,bg="#e9e9e9")
        MainFrame.place(x=2,y=2)

        Lb = Label(MainFrame,font=("Arial",12,"bold"),text="",bg="#e9e9e9")
        Lb.grid(row = 0,column = 2)

        pes = Label(aluguel,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Pesquisar ID")
        pes.place(x=19,y=15)

        cod = Entry(aluguel,font=("Arial",11),fg="black",width=10,bd=1,relief="solid")
        cod.place(x=22,y=41)

        pes = Label(aluguel,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Pesquisar Marca")
        pes.place(x=152,y=15)

        pes = Entry(aluguel,font=("Arial",11),fg="black",width=45,bd=1,relief="solid")
        pes.place(x=155,y=41)

        btm = Button(aluguel,font=("Agency FB",10,"bold"),text="",width=30,bg="white",height=17,bd=2,command=pesquisar,relief=RIDGE)
        btm.place(x=110,y=40)

        foto35 = PhotoImage(file="imagem/p.png")
        btm.config(image=foto35,compound=LEFT)

        bt = Button(aluguel,font=("Agency FB",10,"bold"),text="PESQUIZAR",width=73,bg="white",height=18,bd=2,command=pesquisar2,relief=RIDGE)
        bt.place(x=524,y=38)

        foto32 = PhotoImage(file="imagem/p.png")
        bt.config(image=foto32,compound=LEFT)

        b1 = Button(aluguel,font=("Agency FB",10,"bold"),text="SAIR",bg="white",width=65,height=37,bd=2,relief=RIDGE,command=janel.destroy)
        b1.place(x=377,y=276)

        foto156 = PhotoImage(file="imagem/sair.png")
        b1.config(image=foto156,compound=TOP)

        b1 = Button(aluguel,font=("Agency FB",10,"bold"),text="VOLTAR",bg="white",width=65,height=37,bd=2,relief=RIDGE,command=voltar)
        b1.place(x=456,y=276)

        foto1 = PhotoImage(file="imagem/back.png")
        b1.config(image=foto1,compound=TOP)

        b3 = Button(aluguel,font=("Agency FB",10,"bold"),text="EXCLUIR",bg="white",width=65,height=37,bd=2,relief=RIDGE,command=excluir)
        b3.place(x=535,y=276)

        foto3 = PhotoImage(file="imagem/ex.png")
        b3.config(image=foto3,compound=TOP)
        
        lis = ttk.Treeview(aluguel,height=8,column=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10","col11","col12"),show='headings')   

        lis.heading("#0",text="")
        lis.heading("#1",text="ID")
        lis.heading("#2",text="Modelo")
        lis.heading("#3",text="Marca")
        lis.heading("#4",text="Matricula")
        lis.heading("#5",text="Tipo de Carro")
        lis.heading("#6",text="Nºdo Motor")
        lis.heading("#7",text="Cor")
        lis.heading("#8",text="Ano")
        lis.heading("#9",text="Data de Prazo")
        lis.heading("#10",text="Data de Aluguel")
        lis.heading("#11",text="Alugado")
        lis.heading("#12",text="Combustível")

        lis.column("#0",width=0)
        lis.column("#1",width=60)
        lis.column("#2",width=100)
        lis.column("#3",width=95)
        lis.column("#4",width=100)
        lis.column("#5",width=110)
        lis.column("#6",width=120)
        lis.column("#7",width=80)
        lis.column("#8",width=60)
        lis.column("#9",width=100)
        lis.column("#10",width=100)
        lis.column("#11",width=70)
        lis.column("#12",width=100)

        lis.bind("<Double-1>", duploclick)    
        lis.place(x=23,y=73,width=571)
        
        #barra de rolagem
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Treeview",rowheight=20)
        estilo.map('Treeview',background=[('selected','grey')])
                   
        barra= ttk.Scrollbar(aluguel,command=lis.yview)
        lis.configure(yscroll=barra.set)
        barra.place(x=593,y=73,height=199)

        barra= ttk.Scrollbar(aluguel,command=lis.xview,orient="horizontal")
        lis.configure(xscroll=barra.set)
        barra.place(x=23,y=258,width=571)

        dbo = sqlite3.connect("Sistema.db")
        cur = dbo.cursor()
        cur.execute("SELECT * FROM veiculos")
        row = cur.fetchall()
        for savio in row:
            lis.insert("",END,values=savio)
        dbo.commit()

        janel.mainloop()
        
    def motorista():

        aluguel = Toplevel()
        aluguel.title("Cadatrar Motorista")
        aluguel.geometry("644x356+455+130")
        aluguel.config(bg="grey")
        aluguel.resizable(0,0)
        aluguel.iconbitmap("imagem/car.ico")
        aluguel.transient(loo)
        aluguel.focus_force()
        aluguel.grab_set()

        def salvar():

            sv = sqlite3.connect("Sistema.db")
            cur =sv.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS motorista(id INTEGER PRIMARY KEY,nome TEXT,morada TEXT,casa INTEGER,telefone INTEGER,senha TEXT,cd TEXT,ad TEXT,sl INTEGER,sexo TEXT,i INTEGER,email TEXT)")
            if nome.get()=="" or telefone.get()=="" or morada.get()=="" or email.get()=="" or casa.get()=="" or cd.get()=="" or ad.get()=="" or i.get()=="" or senha.get()=="" or sexo.get()=="":
                messagebox.showerror("Hertz Rentcar Luanda","Por favor preencha os dados correctamente")
            else:
                cur.execute("INSERT INTO motorista VALUES(NULL,?,?,?,?,?,?,?,?,?,?,?)",(nome.get(),morada.get(),casa.get(),telefone.get(),senha.get(),cd.get(),ad.get(),sl.get(),sexo.get(),i.get(),email.get()))
                messagebox.showinfo("Hertz Rentcar Luanda","Dados guardados com corretamente")
                limpaar()
            sv.commit()

        def limpaar():
            
            nome.delete(0,END)
            telefone.delete(0,END)
            morada.delete(0,END)
            email.delete(0,END)
            casa.delete(0,END)
            cd.delete(0,END)
            ad.delete(0,END)
            i.delete(0,END)
            sl.delete(0,END)
            senha.delete(0,END)
            
        nb = ttk.Notebook(aluguel)
        nb.place(x=1,y=1,width=642,height=354)

        janela=Frame(nb)
        aluguell=Frame(nb)

        nb.add(janela,text="Cadastrar Motorista")
        nb.add(aluguell,text="Consultar Motorista")

        MainFrame = Frame(janela,padx=317,pady=160,bg="#e9e9e9")
        MainFrame.place(x=2,y=2)

        BI = Label(MainFrame,font=("Agency FB",16,"bold"),bg="#e9e9e9",text="",fg="Black")   
        BI.grid(row=0, column=2)

        nome = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Nome",fg="Black")
        nome.place(x=56,y=13)

        nome = Entry(janela,bd=1,width="19",font=(8),relief="solid")
        nome.place(x=59,y=38)

        codigo = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Codigo",fg="Black")
        codigo.place(x=12,y=13)    

        id = Entry(janela,bd=1,width="4",font=(8),relief="solid")
        id.place(x=15,y=38)
       
        morada = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Endereço",fg="Black")
        morada.place(x=240,y=13)

        morada = Entry(janela,bd=1,width="15",font=(8),relief="solid")
        morada.place(x=243,y=38)

        casa = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Casa Nº",fg="Black")
        casa.place(x=387,y=13)

        casa = Entry(janela,bd=1,width="8",font=(8),relief="solid")
        casa.place(x=390,y=38)

        telefone = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Telefone",fg="Black")
        telefone.place(x=12,y=72)

        telefone = Entry(janela,bd=1,width="24",font=(8),relief="solid")
        telefone.place(x=15,y=97)

        senha = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Anos Condução",fg="Black")
        senha.place(x=240,y=72)

        senha = Spinbox(janela,bd=1,width=8,font=(8),relief="solid",from_=2, to=60)
        senha.place(x=243,y=97)

        cd = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Província",fg="Black")
        cd.place(x=12,y=132)

        cd = Entry(janela,bd=1,width="16",font=(8),relief="solid")
        cd.place(x=15,y=155)

        ad = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Carta Condução",fg="Black")
        ad.place(x=327,y=132)

        ad = ttk.Combobox(janela,font=("Arial",10),width=17)
        ad['values'] = ("Ligeiro Amador","Ligeiro Profissional")
        ad.place(x=330,y=155)

        sl = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Salario Actual",fg="Black")
        sl.place(x=169,y=132)

        sl = Entry(janela,bd=1,width="16",font=(8),relief="solid")
        sl.place(x=172,y=155)

        group = LabelFrame(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Sexo",padx=33,pady=2)
        group.place(x=15,y=180)

        sexo = StringVar()

        AL = tk.Radiobutton(group,font=("Agency FB",12,"bold"),text="Masculino",value="Masculino",variable=sexo,bg="#e9e9e9")
        AL.pack()
            
        AL2 = tk.Radiobutton(group,font=("Agency FB",12,"bold"),text="Femenino",value="Femenino",variable=sexo,bg="#e9e9e9")
        AL2.pack()

        i = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Idade",fg="Black")
        i.place(x=387,y=72)

        i = Spinbox(janela,bd=1,width="7",font=(8),relief="solid",from_=21, to=100)
        i.place(x=390,y=97)

        email = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="E-mail",fg="Black")
        email.place(x=169,y=180)

        email = Entry(janela,bd=1,width="33",font=(8),relief="solid")
        email.place(x=172,y=205)

        p = PhotoImage(file="imagem/mb.png")
        po = Label(janela,image=p,bg="#e9e9e9")
        po.place(x=475,y=45)        

        fotoo = Entry(janela,bd=1,width="42",font=(6),relief="solid")
        fotoo.place(x=172,y=247)

        bt = Button(janela,font=("Agency FB",10,"bold"),text="Imagem",width=66,bg="white",height=18,bd=1,relief="solid")
        bt.place(x=560,y=245)

        foton = PhotoImage(file="imagem/foto.png")
        bt.config(image=foton,compound=LEFT)
    
        b2 = Button(janela,font=("Agency FB",10,"bold"),text="SALVAR",bg="white",width="65",height="40",bd=2,relief=RIDGE)
        b2.place(x=560,y=273)

        foto24 = PhotoImage(file="imagem/guardar.png")
        b2.config(image=foto24,compound=TOP)

        b3 = Button(janela,font=("Agency FB",10,"bold"),text="SAIR",bg="white",width="65",height="40",bd=2,relief=RIDGE,command=aluguel.destroy)
        b3.place(x=401,y=273)

        foto33 = PhotoImage(file="imagem/sair.png")
        b3.config(image=foto33,compound=TOP)

        b2 = Button(janela,font=("Agency FB",10,"bold"),text="ALTERAR",bg="white",width=65,height=40,bd=2,relief=RIDGE)
        b2.place(x=481,y=273)

        foto29 = PhotoImage(file="imagem/Alterar.png")
        b2.config(image=foto29,compound=TOP)

        MainFrame = Frame(aluguell,padx=314,pady=260,bg="#e9e9e9")
        MainFrame.place(x=2,y=2)

        Lb = Label(MainFrame,font=("Arial",12,"bold"),text="",bg="#e9e9e9")
        Lb.grid(row = 0,column = 2)

        pes = Label(aluguell,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Pesquisar ID")
        pes.place(x=19,y=15)

        cod = Entry(aluguell,font=("Arial",11),fg="black",width=10,bd=1,relief="solid")
        cod.place(x=22,y=41)

        pes = Label(aluguell,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Pesquisar Marca")
        pes.place(x=152,y=15)

        pes = Entry(aluguell,font=("Arial",11),fg="black",width=45,bd=1,relief="solid")
        pes.place(x=155,y=41)

        btm = Button(aluguell,font=("Agency FB",10,"bold"),text="",width=30,bg="white",height=17,bd=2,relief=RIDGE)
        btm.place(x=110,y=40)

        foto35 = PhotoImage(file="imagem/p.png")
        btm.config(image=foto35,compound=LEFT)

        bt = Button(aluguell,font=("Agency FB",10,"bold"),text="PESQUIZAR",width=73,bg="white",height=18,bd=2,relief=RIDGE)
        bt.place(x=524,y=38)

        foto32 = PhotoImage(file="imagem/p.png")
        bt.config(image=foto32,compound=LEFT)

        lista = ttk.Treeview(aluguell,height=8,column=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10","col11","col12"),show='headings')   

        lista.heading("#1",text="ID")
        lista.heading("#2",text="Nome")
        lista.heading("#3",text="Morada")
        lista.heading("#4",text="Casa")
        lista.heading("#5",text="Telefone")
        lista.heading("#6",text="Anos Condução")
        lista.heading("#7",text="Província")
        lista.heading("#8",text="Carta Condução")
        lista.heading("#9",text="Salario Actual")
        lista.heading("#10",text="Sexo")
        lista.heading("#11",text="Idade")
        lista.heading("#12",text="E-mail")        

        lista.column("#1",width=32)
        lista.column("#2",width=128)
        lista.column("#3",width=90)
        lista.column("#4",width=90)
        lista.column("#5",width=120)
        lista.column("#6",width=100)
        lista.column("#7",width=90)
        lista.column("#8",width=140)
        lista.column("#9",width=140)
        lista.column("#10",width=90)
        lista.column("#11",width=50)
        lista.column("#12",width=95)
        
        #lista.bind("<Double-1>", duploclick)
    
        lista.place(x=23,y=70,width=571)
    
        estiloo = ttk.Style()
        estiloo.theme_use("clam")
        estiloo.configure("Treeview",rowheight=20)
        estiloo.map('Treeview',background=[('selected','grey')])
               
        barra= ttk.Scrollbar(aluguell,command=lista.yview)
        lista.configure(yscroll=barra.set)
        barra.place(x=593,y=70,height=203)

        barra= ttk.Scrollbar(aluguell,command=lista.xview,orient="horizontal")
        lista.configure(xscroll=barra.set)
        barra.place(x=23,y=259,width=571)

        dbo = sqlite3.connect("Sistema.db")
        cur = dbo.cursor()
        cur.execute("SELECT * FROM funcionarios")
        row = cur.fetchall()
        for savio in row:
            lista.insert("",END,values=savio)
        dbo.commit()

        def voltar():

            for i in lista.get_children():
                lista.delete(i)

            dbo = sqlite3.connect("Sistema.db")
            cur = dbo.cursor()
            cur.execute("SELECT * FROM funcionarios")
            row = cur.fetchall()
            for savio in row:
                lista.insert("",END,values=savio)
            dbo.commit()

        b1 = Button(aluguell,font=("Agency FB",10,"bold"),text="VOLTAR",bg="white",width=65,height=40,bd=2,relief=RIDGE)
        b1.place(x=455,y=275)

        foto1 = PhotoImage(file="imagem/back.png")
        b1.config(image=foto1,compound=TOP)

        b3 = Button(aluguell,font=("Agency FB",10,"bold"),text="EXCLUIR",bg="white",width=65,height=40,bd=2,relief=RIDGE)
        b3.place(x=533,y=275)

        foto3 = PhotoImage(file="imagem/ex.png")
        b3.config(image=foto3,compound=TOP)

        b5 = Button(aluguell,font=("Agency FB",10,"bold"),text="SAIR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=aluguel.destroy)
        b5.place(x=376,y=275)

        foto5 = PhotoImage(file="imagem/sair.png")
        b5.config(image=foto5,compound=TOP)
        
        aluguel.mainloop()
        
    def aluguel():
        
        janela = Toplevel()
        janela.title("Listar Aluguel")
        janela.geometry("644x355+455+131")
        janela.config(bg="grey")
        janela.resizable(0,0)
        janela.iconbitmap("imagem/car.ico")
        janela.transient(loo)
        janela.focus_force()
        janela.grab_set()
        
        MainFrame = Frame(janela,pady=163,padx=317,bg="#e9e9e9")
        MainFrame.place(x=2,y=2)

        Lb = Label(MainFrame,font=("Arial",12,"bold"),text="",bg="#e9e9e9")
        Lb.grid(row = 0,column = 2)

        pes = Label(janela,font=("Agency FB",13,"bold"),bg="#e9e9e9",text="Pesquisar Nome")
        pes.place(x=10,y=18)

        bt = Button(janela,font=("Agency FB",10,"bold"),text="PESQUIZAR",width=75,bg="white",height=19,bd=2,relief=RIDGE)
        bt.place(x=550,y=45)

        foto = PhotoImage(file="imagem/p.png")
        bt.config(image=foto,compound=LEFT)

        lis = ttk.Treeview(janela,height=6,column=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10","col11","col12","col13","col14","col15","col16","col17"),show='headings')

        lis.heading("#0",text="")
        lis.heading("#1",text="Nome")
        lis.heading("#2",text="Modelo")
        lis.heading("#3",text="Marca")
        lis.heading("#4",text="Matricula")
        lis.heading("#5",text="Tipo de veiculo")
        lis.heading("#6",text="Nºdo Motor")
        lis.heading("#7",text="Cor")
        lis.heading("#8",text="Ano")
        lis.heading("#9",text="Data de Prazo")
        lis.heading("#10",text="Data de Aluguel")
        lis.heading("#11",text="Alugado")
        lis.heading("#12",text="Combustível")
        lis.heading("#13",text="Forma de Pagamento")
        lis.heading("#14",text="Pago")
        lis.heading("#15",text="Multa")
        lis.heading("#16",text="Quantidade de Dias")
        lis.heading("#17",text="Valor Total")

        lis.column("#0",width=0)
        lis.column("#1",width=100)
        lis.column("#2",width=100)
        lis.column("#3",width=110)
        lis.column("#4",width=120)
        lis.column("#5",width=100)
        lis.column("#6",width=100)
        lis.column("#7",width=100)
        lis.column("#8",width=100)
        lis.column("#9",width=100)
        lis.column("#10",width=100)
        lis.column("#11",width=100)
        lis.column("#12",width=100)
        lis.column("#13",width=135)
        lis.column("#14",width=70)
        lis.column("#15",width=100)
        lis.column("#16",width=135)
        lis.column("#17",width=100) 
        
        lis.place(x=13,y=80,width=606)

        #barra de rolagem
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Treeview",rowheight=20)
        estilo.map('Treeview',background=[('selected','grey')])
                   
        barra= ttk.Scrollbar(janela,command=lis.yview)
        lis.configure(yscroll=barra.set)
        barra.place(x=618,y=80,height=163)

        barra= ttk.Scrollbar(janela,command=lis.xview,orient="horizontal")
        lis.configure(xscroll=barra.set)
        barra.place(x=13,y=229,width=605)

        bdo = sqlite3.connect("Sistema.db")
        cur = bdo.cursor()
        cur.execute("SELECT * FROM veiculos")
        row = cur.fetchall()
        for igk in row:
            lis.insert("","end",values=(igk))
        bdo.commit()

        Lb1 = Label(janela,font=("Agency FB",13,"bold"),text="Forma de Pagamento",fg="black",bg="#e9e9e9")  
        Lb1.place(x=12,y=245)

        Lb3 = Label(janela,font=("Agency FB",13,"bold"),text="Pago",fg="black",bg="#e9e9e9")  
        Lb3.place(x=167,y=245)

        Lb = Label(janela,font=("Agency FB",13,"bold"),text="Quantidades de Dias",fg="black",bg="#e9e9e9")  
        Lb.place(x=12,y=300)

        Lb2 = Label(janela,font=("Agency FB",13,"bold"),text="Multa",fg="black",bg="#e9e9e9")  
        Lb2.place(x=167,y=300)

        Lb3 = Label(janela,font=("Agency FB",13,"bold"),text="Valor Total",fg="green",bg="#e9e9e9")  
        Lb3.place(x=322,y=300)
        
        codd = ttk.Combobox(janela,font=("Arial",10),width=17)
        codd['values'] = ("Dinheiro","Credito")
        codd.place(x=15,y=270)

        lb2 = ttk.Combobox(janela,font=("Arial",10),width=10)
        lb2['values'] = ("Sim","Nao")
        lb2.place(x=170,y=270)

        pes = Entry(janela,font=("Arial",12),fg="black",width=58,bd=1,relief="solid")
        pes.place(x=13,y=48)
        
        lb1 = Entry(janela,font=("Arial",10),fg="black",width=20,bd=1,relief="solid")
        lb1.place(x=15,y=325)  

        DT2 = Entry(janela,font=("Arial",10),fg="black",width=20,bd=1,relief="solid")
        DT2.place(x=170,y=325)  

        DT3 = Entry(janela,font=("Arial",10),fg="black",width=16,bd=1,relief="solid")
        DT3.place(x=325,y=325)

        b2 = Button(janela,font=("Agency FB",10,"bold"),text="Excluir",bg="white",width=65,height=45,bd=2,relief=RIDGE)
        b2.place(x=480,y=292)

        fo = PhotoImage(file="imagem/ex.png")
        b2.config(image=fo,compound=TOP)

        b3 = Button(janela,font=("Agency FB",10,"bold"),text="Relatorio",bg="white",width=65,height=45,bd=2,relief=RIDGE)
        b3.place(x=560,y=292)

        foto3 = PhotoImage(file="imagem/rel.png")
        b3.config(image=foto3,compound=TOP)

        janela.mainloop()

    def Contas():

        global janela
        janela = Toplevel()
        janela.title("Contas & Taxas")
        janela.geometry("644x355+455+131")
        janela.config(bg="grey")
        janela.resizable(0,0)
        janela.iconbitmap("imagem/car.ico")
        janela.transient(loo)
        janela.focus_force()
        janela.grab_set()

        nb = ttk.Notebook(janela)
        nb.place(x=1,y=1,width=642,height=353)

        tb1=Frame(nb)
        tb2=Frame(nb)

        nb.add(tb1,text="Contas a Receber  ")
        nb.add(tb2,text=" Taxas de Locaçoes ")

        tb1.configure(bg="#e9e9e9")

        def gravar():

            sv = sqlite3.connect("Sistema.db")
            cur = sv.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS contas(id INTEGER PRIMARY KEY,dev TEXT,ref TEXT,dt INTEGER,v INTEGER,sit TEXT)")
            if dev.get()=="" or ref.get()=="" or dt.get()=="" or v.get()=="" or sit.get()=="":
                messagebox.showerror("Rent car","Por favor preencha os dados correctamente")
            else:
                cur.execute("INSERT INTO contas VALUES(NULL,?,?,?,?,?)",(dev.get(),ref.get(),dt.get(),v.get(),sit.get()))
                messagebox.showinfo("Rent car","Dados guardados correctamente")
                limpar()
                for x in lista.get_children():
                    lista.delete(x)
                cur.execute("SELECT * FROM contas")
                row = cur.fetchall()
                for data in row:
                    lista.insert('',"end",values=(data))
                sv.commit()

        def salvar():

            svv = sqlite3.connect("Sistema.db")
            cur = svv.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS taxas(id INTEGER PRIMARY KEY,cat TEXT,dia TEXT,se INTEGER,cd INTEGER,ad TEXT)")
            if cat.get()=="" or dia.get()=="" or se.get()=="" or cd.get()=="" or ad.get()=="":
                messagebox.showerror("Rent car","Por favor preencha os dados correctamente")
            else:
                cur.execute("INSERT INTO taxas VALUES(NULL,?,?,?,?,?)",(cat.get(),dia.get(),se.get(),cd.get(),ad.get()))
                for x in lista.get_children():
                    lista.delete(x)
                cur.execute("SELECT * FROM taxas")
                row = cur.fetchall()
                for data in row:
                    lista.insert('',"end",values=(data))
                limpaar()
                svv.commit()

        def limpaar():
            
            cat.delete(0,END)
            dia.delete(0,END)
            se.delete(0,END)
            cd.delete(0,END)
            ad.delete(0,END)

        def limpar():
            
            dev.delete(0,END)
            ref.delete(0,END)
            dt.delete(0,END)
            v.delete(0,END)
            sit.delete(0,END)

        def calendar():

            def hj():

                dd.delete(0,END)
                dd.insert(END, calan.get_date())
                top.destroy()

            top = Toplevel(janela)
            top.title("")
            top.geometry("193x228+800+190")
            top.resizable(0,0)
            top.transient(janela)
            top.focus_force()
            top.grab_set()
            calan = Calendar(top,font=("Agency FB",10),bg="white",width="50",height="3",locale='pt_ao')
            calan.place(x=1,y=1)
            
            calendario = Button(top,text="Inserir data",width=26,height=1,command=hj)
            calendario.place(x=1,y=202)

        def calendar2():

            def hj():

                dt.delete(0,END)
                dt.insert(END, calan.get_date())
                top.destroy()

            top = Toplevel(janela)
            top.title("")
            top.geometry("193x228+800+190")
            top.resizable(0,0)
            top.transient(janela)
            top.focus_force()
            top.grab_set()
            
            calan = Calendar(top,font=("Agency FB",10),bg="white",width="50",height="3",locale='pt_ao')
            calan.place(x=1,y=1)
            
            calendario = Button(top,text="Inserir data",width=26,height=1,command=hj)
            calendario.place(x=1,y=202)
            
        def pesquisar():

               pp = cod.get()
               cur.execute("SELECT * FROM taxas WHERE id = (?)",(pp,))
               row = cur.fetchall()
               if row!=[]:
                   limpar()
                   for x in lista.get_children():
                        lista.delete(x)
                   for data in row:
                        lista.insert('',"end",values=(data))
                        cod.delete(0,END)
               else:
                   messagebox.showerror("Rent Car","Nenhum dado encontrado na base de Dados")
                   cod.delete(0,END)
                   
        def pesquisarr():

               p = pes.get()
               cur.execute("SELECT * FROM taxas WHERE cat = (?)",(p,))
               row = cur.fetchall()
               if row!=[]:
                   limpar()
                   for x in lista.get_children():
                        lista.delete(x)
                   for data in row:
                        lista.insert('',"end",values=(data))
                        cod.delete(0,END)
               else:
                   messagebox.showerror("Rent Car","Nenhum dado encontrado na base de Dados")
                   cod.delete(0,END)                   

        def voltar():
            for x in lista.get_children():
                lista.delete(x)
            cur.execute("SELECT * FROM taxas")
            row = cur.fetchall()
            for s in row:
                lista.insert("","end",values=(s))

        def back():
            for x in lista.get_children():
                lista.delete(x)
            cur.execute("SELECT * FROM contas")
            row = cur.fetchall()
            for s in row:
                lista.insert("","end",values=(s))

        def excluir():
            
          idselect = lista.item(lista.selection())['values'][0]
          db = sqlite3.connect("Sistema.db")
          cur = db.cursor()
          result=tkMessageBox.askquestion("Rent Car","Tens Certeza que queres excluir do Sistema?",icon="warning")
          if result == "yes":
              messagebox.showinfo("Rent Car","Dados excluidos do Sistema")
              delete = cur.execute("delete from taxas where id={}".format(idselect))
              lista.delete(lista.selection())
          db.commit()

        def apagar():
            
          idselect = lista.item(lista.selection())['values'][0]
          db = sqlite3.connect("Sistema.db")
          cur = db.cursor()
          result=tkMessageBox.askquestion("Rent Car","Tens Certeza que queres excluir do Sistema?",icon="warning")
          if result == "yes":
              messagebox.showinfo("Rent Car","Dados excluidos do Sistema")
              delete = cur.execute("delete from contas where id={}".format(idselect))
              lista.delete(lista.selection())
          db.commit()

        def alterar():

            dbo = sqlite3.connect("Sistema.db")
            cur = dbo.cursor()

            m = dia.get()
            l = se.get()
            s = cd.get()
            v = ad.get()

            if dia.get()=="" or se.get()=="" or cd.get()=="" or ad.get()=="": 
                messagebox.showerror("Rent Car","Por favor seleciona os dados que pretendes actualizar!")
            else:
                cur.execute("UPDATE taxas SET dia=?,se=?,cd=?,ad=? WHERE id=?",(m,l,s,v))
                messagebox.showinfo("Rent Car","Dados Actualizado com sucesso")
                limpaar()
                dbo.commit()
                for s in lista.get_children():
                    lista.delete(s)
                cur.execute("SELECT * FROM taxas")
                sav = cur.fetchall()
                for row in sav:
                    lista.insert("","end",values=(row))

        def duploclick(event):

            limpaar()

            lista.selection()
            for x in lista.selection():
                col1,col2,col3,col4,col5,col6 = lista.item(x, 'values')
                
                cat.insert(END, col2)
                dia.insert(END, col3)
                se.insert(END, col4)
                cd.insert(END, col5)
                ad.insert(END, col6)
            
        dev = Label(tb1,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Devedor",fg="Black")
        dev.place(x=32,y=10)

        dev = Entry(tb1,bd=1,width="20",font=(8),relief="solid")
        dev.place(x=35,y=35)

        ref = Label(tb1,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Referência",fg="Black")
        ref.place(x=427,y=10)            

        ref = ttk.Combobox(tb1,font=("Arial",10),width=20)
        ref['values'] = ("Dinheiro","Credito")
        ref.place(x=430,y=35)

        dt = Label(tb1,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Data de Vencimento",fg="Black")
        dt.place(x=32,y=60)

        dt = Entry(tb1,bd=1,width="10",font=(8),relief="solid")
        dt.place(x=35,y=85)

        ad = Label(tb1,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Data de Prazo",fg="Black")
        ad.place(x=240,y=60)

        dd = Entry(tb1,bd=1,width="10",font=(8),relief="solid")
        dd.place(x=243,y=85)

        calendario = Button(tb1,bg="white",width=18,command=calendar2)
        calendario.place(x=133,y=83)

        calData = Button(tb1,bg="white",width=18,command=calendar)
        calData.place(x=341,y=83)

        fot = PhotoImage(file="imagem/cal.png")
        calendario.config(image=fot,compound=LEFT)

        fo = PhotoImage(file="imagem/cal.png")
        calData.config(image=fo,compound=LEFT)

        v = Label(tb1,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Valor Total",fg="Black")
        v.place(x=427,y=60)
        
        v = Entry(tb1,bd=1,width="18",font=(8),relief="solid")
        v.place(x=430,y=85) 

        sit = Label(tb1,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Situação",fg="Black")
        sit.place(x=240,y=10)

        sit = ttk.Combobox(tb1,font=("Arial",10),width=20)
        sit['values'] = ("Aberto","Fechado")
        sit.place(x=243,y=35)

        pes = Label(tb1,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Pesquisar ID")
        pes.place(x=32,y=115)

        cod = Entry(tb1,font=("Arial",11),fg="black",width=10,bd=1,relief="solid")
        cod.place(x=35,y=140)

        pes = Label(tb1,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Pesquisar por Devedor")
        pes.place(x=167,y=115)

        pes = Entry(tb1,bd=1,width=47,font=("Arial",11),relief="solid")
        pes.place(x=170,y=140)

        bt = Button(tb1,font=("Agency FB",10,"bold"),text="",width=30,bg="white",height=18,bd=2,relief=RIDGE,command=pesquisar)
        bt.place(x=559,y=138)

        foto04 = PhotoImage(file="imagem/p.png")
        bt.config(image=foto04,compound=LEFT)

        btm = Button(tb1,font=("Agency FB",10,"bold"),text="",width=30,bg="white",height=17,bd=2,relief=RIDGE,command=pesquisar)
        btm.place(x=125,y=139)

        foto375 = PhotoImage(file="imagem/p.png")
        btm.config(image=foto375,compound=LEFT)

        lista = ttk.Treeview(tb1,height=3,column=("col1","col2","col3","col4","col5","col6","col7"),show='headings')   

        lista.heading("#1",text="ID")
        lista.heading("#2",text="Devedor")
        lista.heading("#3",text="Referencia")
        lista.heading("#4",text="Data de Vencimento")
        lista.heading("#5",text="Data de Prazo")
        lista.heading("#6",text="Situaçao")
        lista.heading("#7",text="Valor Total")

        lista.column("#1",width=32)
        lista.column("#2",width=128)
        lista.column("#3",width=90)
        lista.column("#4",width=120)
        lista.column("#5",width=120)
        lista.column("#6",width=100)
        lista.column("#7",width=130)
        
        lista.place(x=35,y=165,width=546)

        #barra de rolagem
        estiloo = ttk.Style()
        estiloo.theme_use("clam")
        estiloo.configure("Treeview",rowheight=20)
        estiloo.map('Treeview',background=[('selected','grey')])
                   
        barra= ttk.Scrollbar(tb1,command=lista.yview)
        lista.configure(yscroll=barra.set)
        barra.place(x=580,y=165,height=103)

        barra= ttk.Scrollbar(tb1,command=lista.xview,orient="horizontal")
        lista.configure(xscroll=barra.set)
        barra.place(x=35,y=254,width=546)

        b19 = Button(tb1,font=("Agency FB",10,"bold"),text="VOLTAR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=back)
        b19.place(x=264,y=273)

        foto06 = PhotoImage(file="imagem/back.png")
        b19.config(image=foto06,compound=TOP)

        b1 = Button(tb1,font=("Agency FB",10,"bold"),text="SAIR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=janela.destroy)
        b1.place(x=180,y=273)

        foto0 = PhotoImage(file="imagem/sair.png")
        b1.config(image=foto0,compound=TOP)

        b1 = Button(tb1,font=("Agency FB",10,"bold"),text="GUARDAR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=gravar)
        b1.place(x=349,y=273)

        foto1 = PhotoImage(file="imagem/guardar.png")
        b1.config(image=foto1,compound=TOP)

        b2 = Button(tb1,font=("Agency FB",10,"bold"),text="ALTERAR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=alterar)
        b2.place(x=435,y=273)

        foto2 = PhotoImage(file="imagem/Alterar.png")
        b2.config(image=foto2,compound=TOP)

        b3 = Button(tb1,font=("Agency FB",10,"bold"),text="EXCLUIR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=apagar)
        b3.place(x=520,y=273)
        
        foto11 = PhotoImage(file="imagem/ex.png")
        b3.config(image=foto11,compound=TOP)
        tb2.configure(bg="#e9e9e9")

        dbo = sqlite3.connect("Sistema.db")
        cur = dbo.cursor()
        cur.execute("SELECT * FROM contas")
        row = cur.fetchall()
        for savio in row:
            lista.insert("",END,values=savio)
        dbo.commit()
        
        catu = Label(tb2,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Grupo",fg="Black")
        catu.place(x=20,y=10)

        cat = ttk.Combobox(tb2,font=("Arial",10),width=15)
        cat['values'] = ("Caminhões","Carro grande","Van","Autocarro","Carro Pequeno")
        cat.place(x=23,y=35)
           
        dia = Label(tb2,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Diaria",fg="Black")
        dia.place(x=167,y=10)

        dia = Entry(tb2,bd=1,width="10",font=(8),relief="solid")
        dia.place(x=170,y=35)

        se = Label(tb2,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Semanal",fg="Black")
        se.place(x=277,y=10)

        se = Entry(tb2,bd=1,width="10",font=(8),relief="solid")
        se.place(x=280,y=35)

        cd = Label(tb2,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Mensal",fg="Black")
        cd.place(x=387,y=10)

        cd = Entry(tb2,bd=1,width="10",font=(8),relief="solid")
        cd.place(x=390,y=35)

        ad = Label(tb2,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Fim de Semana",fg="Black")
        ad.place(x=497,y=10)

        ad = Entry(tb2,bd=1,width="10",font=(8),relief="solid")
        ad.place(x=500,y=35)
        
        pes = Label(tb2,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Pesquisar ID")
        pes.place(x=20,y=65)

        cod = Entry(tb2,font=("Arial",11),fg="black",width=10,bd=1,relief="solid")
        cod.place(x=23,y=91)

        pes = Label(tb2,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Pesquisar por Grupo")
        pes.place(x=167,y=65)

        pes = Entry(tb2,bd=1,width=42,font=(8),relief="solid")
        pes.place(x=170,y=91)

        bt = Button(tb2,font=("Agency FB",10,"bold"),text="",width=30,bg="white",height=18,bd=2,relief=RIDGE,command=pesquisarr)
        bt.place(x=559,y=89)

        foto = PhotoImage(file="imagem/p.png")
        bt.config(image=foto,compound=LEFT)

        btm = Button(tb2,font=("Agency FB",10,"bold"),text="",width=30,bg="white",height=17,bd=2,relief=RIDGE,command=pesquisar)
        btm.place(x=110,y=89)

        foto35 = PhotoImage(file="imagem/p.png")
        btm.config(image=foto35,compound=LEFT)

        lista = ttk.Treeview(tb2,height=5,column=("col1","col2","col3","col4","col5","col6"),show='headings')   

        lista.heading("#1",text="ID")
        lista.heading("#2",text="Grupo")
        lista.heading("#3",text="Diaria")
        lista.heading("#4",text="Semanal")
        lista.heading("#5",text="Mensal")
        lista.heading("#6",text="Fim de Semana")

        lista.column("#1",width=32)
        lista.column("#2",width=100)
        lista.column("#3",width=100)
        lista.column("#4",width=90)
        lista.column("#5",width=100)
        lista.column("#6",width=100)

        lista.bind("<Double-1>", duploclick)
        
        lista.place(x=23,y=135,width=560)

        #barra de rolagem
        estiloo = ttk.Style()
        estiloo.theme_use("clam")
        estiloo.configure("Treeview",rowheight=20)
        estiloo.map('Treeview',background=[('selected','grey')])
                   
        barra= ttk.Scrollbar(tb2,command=lista.yview)
        lista.configure(yscroll=barra.set)
        barra.place(x=580,y=135,height=129)

        b1 = Button(tb2,font=("Agency FB",10,"bold"),text="VOLTAR",bg="white",width=70,height=40,bd=2,relief=RIDGE,command=voltar)
        b1.place(x=240,y=270)

        foto7 = PhotoImage(file="imagem/back.png")
        b1.config(image=foto7,compound=TOP)

        b1 = Button(tb2,font=("Agency FB",10,"bold"),text="SAIR",bg="white",width=70,height=40,bd=2,relief=RIDGE,command=janela.destroy)
        b1.place(x=150,y=270)

        foto03 = PhotoImage(file="imagem/sair.png")
        b1.config(image=foto03,compound=TOP)

        b1 = Button(tb2,font=("Agency FB",10,"bold"),text="GUARDAR",bg="white",width=70,height=40,bd=2,relief=RIDGE,command=salvar)
        b1.place(x=333,y=270)

        foto9 = PhotoImage(file="imagem/guardar.png")
        b1.config(image=foto9,compound=TOP)

        b2 = Button(tb2,font=("Agency FB",10,"bold"),text="ALTERAR",bg="white",width=70,height=40,bd=2,relief=RIDGE,command=alterar)
        b2.place(x=425,y=270)

        foto8 = PhotoImage(file="imagem/Alterar.png")
        b2.config(image=foto8,compound=TOP)

        b3 = Button(tb2,font=("Agency FB",10,"bold"),text="EXCLUIR",bg="white",width=70,height=40,bd=2,relief=RIDGE,command=excluir)
        b3.place(x=516,y=270)

        foto6 = PhotoImage(file="imagem/ex.png")
        b3.config(image=foto6,compound=TOP)

        dbo = sqlite3.connect("Sistema.db")
        cur = dbo.cursor()
        cur.execute("SELECT * FROM taxas")
        row = cur.fetchall()
        for savio in row:
            lista.insert("",END,values=savio)
        dbo.commit()        
            
        janela.mainloop()

    def entrar():
            
            limpar()
            lo.destroy()
            loo.destroy()
                        
            janelaa = Tk()
            janelaa.title("Rent Car Funcionario")
            janelaa.resizable(0,0)
            janelaa.geometry("787x395+320+100")
            janelaa.iconbitmap("imagem/car.ico")   

            MainFrame = Frame(janelaa,bg="white",bd=2,padx=6,pady=7,relief=RIDGE)
            MainFrame.grid()

            TitFrame = Frame(MainFrame,bg="#C0C0C0",padx=50,pady=172,relief=RIDGE)
            TitFrame.pack(side=LEFT)

            lb = Label(TitFrame,font=("Agency FB",16),bg="grey",text=" ")
            lb.grid(row=0,column=1)

            bt = Button(janelaa,text="Clientes",bd=1,height="56",width="101",command=Cliente,relief=RIDGE)
            #bt.grid(row=0, column=1)
            bt.place(x=10,y=11)

            ico = PhotoImage(file="imagem/lo.png")
            bt.config(image=ico,compound=TOP)

            bt2 = Button(janelaa,text="Veiculos",bd="1",height="56",width="101",command=Veiculo,relief=RIDGE)
            #bt2.grid(row=0, column=2)
            bt2.place(x=10,y=73)

            ico2 = PhotoImage(file="imagem/carro.png")
            bt2.config(image=ico2,compound=TOP)

            bt3 = Button(janelaa,text="Motorista",bd="1",height="56",width="101",relief=RIDGE,command=motorista)
            #bt3.grid(row=0, column=4)
            bt3.place(x=10,y=135)

            ico3 = PhotoImage(file="imagem/oii.png")
            bt3.config(image=ico3,compound=TOP)

            bt4 = Button(janelaa,text="Contas & Taxas",bd="1",height="56",width="101",relief=RIDGE,command=Contas)
            #bt4.grid(row=0, column=3)
            bt4.place(x=10,y=259)

            ico4 = PhotoImage(file="imagem/na.png")
            bt4.config(image=ico4,compound=TOP)

            bt5 = Button(janelaa,text="Rastrear Veiculo",bd="1",height="56",width="101",relief=RIDGE)
            #bt5.grid(row=0, column=5)
            bt5.place(x=10,y=197)

            ico5 = PhotoImage(file="imagem/ras.png")
            bt5.config(image=ico5,compound=TOP)

            bt6 = Button(janelaa,text="Alugueis",bd="1",height="56",width="101",relief=RIDGE,command=aluguel)
            #bt6.grid(row=0, column=6)
            bt6.place(x=10,y=321)

            ico6 = PhotoImage(file="imagem/ya.png")
            bt6.config(image=ico6,compound=TOP)

            p = PhotoImage(file="imagem/bg.png")
            Label(image=p, bg="white").place(x=128,y=2)

            janelaa.mainloop()


    def mostrar():
    
        Lb["text"]=e2.get()
    
    def limpar():

        e1.delete(0,END)
        e2.delete(0,END)
       
    fot = PhotoImage(file="imagem/cas.png")
    r = Label(lo,image=fot,bg="white")
    r.place(x=15,y=15)

    fotoi = PhotoImage(file="imagem/FUN.png")
    rp = Label(lo,image=fotoi,bg="white")
    rp.place(x=140,y=100)

    nome = Label(lo,font=("Agency FB",12,"bold"),fg="grey",text="NOME")
    nome.place(x=52,y=152)

    e1=Entry(lo,width="48",fg="grey",justify="center",relief="solid",borderwidth=1,font=("Agency FB",12,"bold"))
    e1.place (x=54,y=180)
    e1.focus()

    senha = Label(lo,font=("Agency FB",12,"bold"),fg="grey",text="SENHA")
    senha.place(x=52,y=232)

    e2=Entry(lo,width="48",fg="grey",justify="center",relief="solid",borderwidth=1,font=("Agency FB",12,"bold"))
    e2.place (x=54,y=260)
    e2['show'] = '*'
    e2.focus()

    photo0 = PhotoImage(file ="imagem/usu.png")
    p = Label(lo, image=photo0, bg="white")
    p.place(x=58,y=181)

    photo1 = PhotoImage(file ="imagem/chave.png")
    j = Label(lo, image=photo1, bg="white")
    j.place(x=58,y=262)

    photo2 = Button(lo,width=30,height=15,bg="white",borderwidth=0,command=mostrar)
    photo2.place(x=360,y=263)
    
    foto = PhotoImage(file ="imagem/vista.png")
    photo2.config(image=foto,compound=TOP)

    Lb = Label(lo,justify="center",font=("Agency FB",12,"bold"),fg="grey")
    Lb.place(x=208,y=290)

    foto2 = PhotoImage(file="imagem/pj.png")
    b = Label(lo, image=foto2,bg="white")
    b.place(x=15,y=15)

    b3 = Button(lo,font=("Agency FB",10,"bold"),text=" ENTRAR",bg="white",fg="grey",width=65,height=38,bd=2,relief=RIDGE,command=entrar)
    b3.place(x=54,y=360)

    foto6 = PhotoImage(file="imagem/en.png")
    b3.config(image=foto6,compound=TOP)

    b5 = Button(lo,font=("Agency FB",10,"bold"),text="LIMPAR",bg="white",fg="grey",width=65,height=38,bd=2,relief=RIDGE,command=limpar)
    b5.place(x=190,y=360)

    foto8 = PhotoImage(file="imagem/lim.png")
    b5.config(image=foto8,compound=TOP)

    b4 = Button(lo,font=("Agency FB",10,"bold"),text="SAIR",bg="white",fg="grey",width=65,height=38,bd=2,relief=RIDGE,command=lo.destroy)
    b4.place(x=320,y=360)

    foto7 = PhotoImage(file="imagem/sair.png")
    b4.config(image=foto7,compound=TOP)

    lo.mainloop()

def adimi():

    #loo.destroy()

    lo = Toplevel()
    lo.title("Login")
    lo.resizable(0,0)
    lo.geometry("453x444+500+100")
    lo.resizable(0,0)
    lo.config(bg="#C0C0C0")
    lo.overrideredirect(True)
    lo.focus_force()
    lo.grab_set()

    def administrador():

        aluguel = Toplevel()
        aluguel.title("Cadatrar Administrador")
        aluguel.geometry("644x356+455+131")
        aluguel.config(bg="grey")
        aluguel.resizable(0,0)
        aluguel.iconbitmap("imagem/car.ico")
        aluguel.transient(loo)
        aluguel.focus_force()
        aluguel.grab_set()
        
        def salvar():

            sv = sqlite3.connect("Sistema.db")
            cur =sv.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS adm(id INTEGER PRIMARY KEY,nome TEXT,morada TEXT,casa INTEGER,telefone INTEGER,senha TEXT,cd TEXT,sexo TEXT,i INTEGER,email TEXT)")
            if id.get()=="" or nome.get()=="" or telefone.get()=="" or morada.get()=="" or email.get()=="" or casa.get()=="" or cd.get()=="" or i.get()=="" or senha.get()=="" or sexo.get()=="":
                messagebox.showerror("Rent Car","Por favor preencha os dados correctamente")
            else:
                cur.execute("INSERT INTO adm VALUES(?,?,?,?,?,?,?,?,?,?)",(id.get(),nome.get(),morada.get(),casa.get(),telefone.get(),senha.get(),cd.get(),sexo.get(),i.get(),email.get()))
                messagebox.showinfo("Rent Car","Dados guardados com corretamente")
                limpaar()
                for x in lista.get_children():
                    lista.delete(x)
                cur.execute("SELECT * FROM adm")
                row = cur.fetchall()
                for data in row:
                    lista.insert('',"end",values=(data))
                dbo.commit()
                
            sv.commit()

        def limpaar():

            id.delete(0,END)
            nome.delete(0,END)
            telefone.delete(0,END)
            morada.delete(0,END)
            email.delete(0,END)
            casa.delete(0,END)
            cd.delete(0,END)
            i.delete(0,END)
            senha.delete(0,END)

        def alterar():

            dbo = sqlite3.connect("Sistema.db")
            cur = dbo.cursor()

            n = id.get()
            p = morada.get()
            m = sexo.get()
            l = i.get()
            s = nome.get()
            v = telefone.get()
            k = cd.get()
            b = casa.get()
            o = email.get()
            bi = senha.get()

            if id.get()=="" or nome.get()=="" or telefone.get()=="" or morada.get()=="" or sexo.get()=="" or email.get()=="" or casa.get()==""or senha.get()=="" or cd.get()=="" or i.get()=="":
                messagebox.showerror("Rent Car","Por favor seleciona os dados que pretendes actualizar!")
            else:
                cur.execute("UPDATE adm SET morada=?,sexo=?,i=?,nome=?,telefone=?,cd=?,casa=?,email=?,senha=? WHERE id=?",(p,m,l,s,v,k,b,o,bi,n))
                messagebox.showinfo("Rent Car","Dados Actualizado com sucesso")
                limpaar()
                dbo.commit()
                for s in lista.get_children():
                    lista.delete(s)
                cur.execute("SELECT * FROM adm")
                sav = cur.fetchall()
                for row in sav:
                    lista.insert("","end",values=(row))

        def duploclick(event):

            limpaar()
            lista.selection()
            for x in lista.selection():
                col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = lista.item(x, 'values')

            id.insert(END, col1)
            nome.insert(END, col2)
            morada.insert(END, col3)
            casa.insert(END, col4)
            telefone.insert(END, col5)
            senha.insert(END, col6)
            cd.insert(END, col7)
            i.insert(END, col8)
            email.insert(END, col10)

        def excluir():
          idselect = lista.item(lista.selection())['values'][0]
          db = sqlite3.connect("Sistema.db")
          cur = db.cursor()
          result=tkMessageBox.askquestion("Rent car","Tens Certeza que queres excluir do Sistema?",icon="warning")
          if result == "yes":
              messagebox.showinfo("Rent Car","Dados excluidos do Sistema")
              limpaar()
              delete = cur.execute("delete from adm where id={}".format(idselect))
              lista.delete(lista.selection())
          db.commit()              

        def pesquisar():

           pp = cod.get()
           cur.execute("SELECT * FROM adm WHERE id = (?)",(pp,))
           row = cur.fetchall()
           if row!=[]:
               limpaar()
               for x in lista.get_children():
                    lista.delete(x)
               for data in row:
                    lista.insert('',"end",values=(data))
                    cod.delete(0,END)
           else:
               messagebox.showerror("Rent Car","Nenhum dado encontrado na base de Dados")
               cod.delete(0,END)
           #cod.delete(0,END)
                    
        def pesquisar2():
            
           p = pes.get()
           cur.execute("SELECT * FROM adm WHERE nome = (?)",(p,))
           roww = cur.fetchall()
           if roww!=[]:
               limpaar()
               for x in lista.get_children():
                    lista.delete(x)
               for data in roww:
                    lista.insert('',"end",values=(data))
                    pes.delete(0,END)
           else:
               messagebox.showerror("Rent Car","Nenhum dado encontrado na base de Dados")
               pes.delete(0,END)

        
        nb = ttk.Notebook(aluguel)
        nb.place(x=1,y=1,width=642,height=354)

        janela=Frame(nb)
        aluguell=Frame(nb)

        nb.add(janela,text="Cadastrar Administrador")
        nb.add(aluguell,text="Consultar Administrador")

        MainFrame = Frame(janela,padx=317,pady=160,bg="#e9e9e9")
        MainFrame.place(x=2,y=2)

        BI = Label(MainFrame,font=("Agency FB",16,"bold"),bg="#e9e9e9",text="",fg="Black")   
        BI.grid(row=0, column=2)

        nome = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Nome",fg="Black")
        nome.place(x=56,y=13)

        nome = Entry(janela,bd=1,width="19",font=(8),relief="solid")
        nome.place(x=59,y=38)

        codigo = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Codigo",fg="Black")
        codigo.place(x=12,y=13)    

        id = Entry(janela,bd=1,width="4",font=(8),relief="solid")
        id.place(x=15,y=38)
       
        morada = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Endereço",fg="Black")
        morada.place(x=240,y=13)

        morada = Entry(janela,bd=1,width="15",font=(8),relief="solid")
        morada.place(x=243,y=38)

        casa = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Casa Nº",fg="Black")
        casa.place(x=387,y=13)

        casa = Entry(janela,bd=1,width="8",font=(8),relief="solid")
        casa.place(x=390,y=38)

        telefone = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Telefone",fg="Black")
        telefone.place(x=12,y=72)

        telefone = Entry(janela,bd=1,width="24",font=(8),relief="solid")
        telefone.place(x=15,y=97)

        senha = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Senha",fg="Black")
        senha.place(x=240,y=72)

        senha = Entry(janela,bd=1,width="15",font=(8),relief="solid")
        senha['show'] = '*'
        senha.place(x=243,y=97)

        cd = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Província",fg="Black")
        cd.place(x=12,y=132)

        cd = Entry(janela,bd=1,width="16",font=(8),relief="solid")
        cd.place(x=15,y=155)

        group = LabelFrame(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Sexo",padx=33,pady=2)
        group.place(x=15,y=180)

        sexo = StringVar()

        AL = tk.Radiobutton(group,font=("Agency FB",12,"bold"),text="Masculino",value="Masculino",variable=sexo,bg="#e9e9e9")
        AL.pack()
            
        AL2 = tk.Radiobutton(group,font=("Agency FB",12,"bold"),text="Femenino",value="Femenino",variable=sexo,bg="#e9e9e9")
        AL2.pack()

        i = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Idade",fg="Black")
        i.place(x=387,y=72)

        i = Spinbox(janela,bd=1,width="7",font=(8),relief="solid",from_=1, to=100)
        i.place(x=390,y=97)

        email = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="E-mail",fg="Black")
        email.place(x=169,y=132)

        email = Entry(janela,bd=1,width="33",font=(8),relief="solid")
        email.place(x=172,y=155)

        p = PhotoImage(file="imagem/kp.png")
        po = Label(janela,image=p,bg="#e9e9e9")
        po.place(x=481,y=25)

        fotoo = Entry(janela,bd=1,width="42",font=(6),relief="solid")
        fotoo.place(x=172,y=245)

        bt = Button(janela,font=("Agency FB",10,"bold"),text="Imagem",width=66,bg="white",height=18,bd=1,relief="solid")
        bt.place(x=560,y=244)

        foton = PhotoImage(file="imagem/foto.png")
        bt.config(image=foton,compound=LEFT)
    
        b2 = Button(janela,font=("Agency FB",10,"bold"),text="SALVAR",bg="white",width="65",height="40",bd=2,relief=RIDGE,command=salvar)
        b2.place(x=560,y=273)

        foto24 = PhotoImage(file="imagem/guardar.png")
        b2.config(image=foto24,compound=TOP)

        b3 = Button(janela,font=("Agency FB",10,"bold"),text="SAIR",bg="white",width="65",height="40",bd=2,relief=RIDGE,command=aluguel.destroy)
        b3.place(x=401,y=273)

        foto33 = PhotoImage(file="imagem/sair.png")
        b3.config(image=foto33,compound=TOP)

        b2 = Button(janela,font=("Agency FB",10,"bold"),text="ALTERAR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=alterar)
        b2.place(x=481,y=273)

        foto29 = PhotoImage(file="imagem/Alterar.png")
        b2.config(image=foto29,compound=TOP)

        MainFrame = Frame(aluguell,padx=314,pady=260,bg="#e9e9e9")
        MainFrame.place(x=2,y=2)

        Lb = Label(MainFrame,font=("Arial",12,"bold"),text="",bg="#e9e9e9")
        Lb.grid(row = 0,column = 2)

        pes = Label(aluguell,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Pesquisar ID")
        pes.place(x=19,y=15)

        cod = Entry(aluguell,font=("Arial",11),fg="black",width=10,bd=1,relief="solid")
        cod.place(x=22,y=41)

        pes = Label(aluguell,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Pesquisar Marca")
        pes.place(x=152,y=15)

        pes = Entry(aluguell,font=("Arial",11),fg="black",width=45,bd=1,relief="solid")
        pes.place(x=155,y=41)

        btm = Button(aluguell,font=("Agency FB",10,"bold"),text="",width=30,bg="white",height=17,bd=2,command=pesquisar,relief=RIDGE)
        btm.place(x=110,y=40)

        foto35 = PhotoImage(file="imagem/p.png")
        btm.config(image=foto35,compound=LEFT)

        bt = Button(aluguell,font=("Agency FB",10,"bold"),text="PESQUIZAR",width=73,bg="white",height=18,bd=2,command=pesquisar2,relief=RIDGE)
        bt.place(x=524,y=38)

        foto32 = PhotoImage(file="imagem/p.png")
        bt.config(image=foto32,compound=LEFT)

        lista = ttk.Treeview(aluguell,height=8,column=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10"),show='headings')   

        lista.heading("#1",text="ID")
        lista.heading("#2",text="Nome")
        lista.heading("#3",text="Morada")
        lista.heading("#4",text="Casa")
        lista.heading("#5",text="Telefone")
        lista.heading("#6",text="Senha")
        lista.heading("#7",text="Província")
        lista.heading("#8",text="Idade")
        lista.heading("#9",text="Sexo")
        lista.heading("#10",text="E-mail")        

        lista.column("#1",width=32)
        lista.column("#2",width=128)
        lista.column("#3",width=90)
        lista.column("#4",width=90)
        lista.column("#5",width=120)
        lista.column("#6",width=60)
        lista.column("#7",width=90)
        lista.column("#8",width=60)
        lista.column("#9",width=90)
        lista.column("#10",width=140)
        
        lista.bind("<Double-1>", duploclick)
    
        lista.place(x=23,y=70,width=571)
    
        estiloo = ttk.Style()
        estiloo.theme_use("clam")
        estiloo.configure("Treeview",rowheight=20)
        estiloo.map('Treeview',background=[('selected','grey')])
               
        barra= ttk.Scrollbar(aluguell,command=lista.yview)
        lista.configure(yscroll=barra.set)
        barra.place(x=593,y=70,height=203)

        barra= ttk.Scrollbar(aluguell,command=lista.xview,orient="horizontal")
        lista.configure(xscroll=barra.set)
        barra.place(x=23,y=259,width=571)

        dbo = sqlite3.connect("Sistema.db")
        cur = dbo.cursor()
        cur.execute("SELECT * FROM adm")
        row = cur.fetchall()
        for savio in row:
            lista.insert("",END,values=savio)
        dbo.commit()

        def voltar():

            for i in lista.get_children():
                lista.delete(i)

            dbo = sqlite3.connect("Sistema.db")
            cur = dbo.cursor()
            cur.execute("SELECT * FROM adm")
            row = cur.fetchall()
            for savio in row:
                lista.insert("",END,values=savio)
            dbo.commit()

        b1 = Button(aluguell,font=("Agency FB",10,"bold"),text="VOLTAR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=voltar)
        b1.place(x=455,y=275)

        foto1 = PhotoImage(file="imagem/back.png")
        b1.config(image=foto1,compound=TOP)

        b3 = Button(aluguell,font=("Agency FB",10,"bold"),text="EXCLUIR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=excluir)
        b3.place(x=533,y=275)

        foto3 = PhotoImage(file="imagem/ex.png")
        b3.config(image=foto3,compound=TOP)

        b5 = Button(aluguell,font=("Agency FB",10,"bold"),text="SAIR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=aluguel.destroy)
        b5.place(x=376,y=275)

        foto5 = PhotoImage(file="imagem/sair.png")
        b5.config(image=foto5,compound=TOP)

        aluguel.mainloop()

    def funcionario():

        aluguel = Toplevel()
        aluguel.title("Cadatrar Funcionario")
        aluguel.geometry("644x356+455+131")
        aluguel.config(bg="grey")
        aluguel.resizable(0,0)
        aluguel.iconbitmap("imagem/car.ico")
        aluguel.transient(loo)
        aluguel.focus_force()
        aluguel.grab_set()
        
        def salvar():

            sv = sqlite3.connect("Sistema.db")
            cur =sv.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS funcionarios(id INTEGER PRIMARY KEY,nome TEXT,morada TEXT,casa INTEGER,telefone INTEGER,senha TEXT,cd TEXT,ad TEXT,sl INTEGER,sexo TEXT,i INTEGER,email TEXT)")
            if id.get()=="" or nome.get()=="" or telefone.get()=="" or morada.get()=="" or email.get()=="" or casa.get()=="" or cd.get()=="" or ad.get()=="" or i.get()=="" or senha.get()=="" or sexo.get()=="":
                messagebox.showerror("Rent Car","Por favor preencha os dados correctamente")
            else:
                cur.execute("INSERT INTO funcionarios VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(id.get(),nome.get(),morada.get(),casa.get(),telefone.get(),senha.get(),cd.get(),ad.get(),sl.get(),sexo.get(),i.get(),email.get()))
                messagebox.showinfo("Rent Car","Dados guardados com corretamente")
                limpaar()
                for x in lista.get_children():
                    lista.delete(x)
                cur.execute("SELECT * FROM funcionarios")
                row = cur.fetchall()
                for data in row:
                    lista.insert('',"end",values=(data))
                dbo.commit()
                
            sv.commit()

        def limpaar():

            id.delete(0,END)
            nome.delete(0,END)
            telefone.delete(0,END)
            morada.delete(0,END)
            email.delete(0,END)
            casa.delete(0,END)
            cd.delete(0,END)
            ad.delete(0,END)
            i.delete(0,END)
            sl.delete(0,END)
            senha.delete(0,END)

        def alterar():

            dbo = sqlite3.connect("Sistema.db")
            cur = dbo.cursor()

            n = id.get()
            p = morada.get()
            m = sexo.get()
            l = i.get()
            s = nome.get()
            v = telefone.get()
            c = ad.get()
            k = cd.get()
            b = casa.get()
            o = email.get()
            bi = senha.get()
            on = sl.get()

            if id.get()=="" or nome.get()=="" or telefone.get()=="" or morada.get()=="" or sexo.get()=="" or email.get()=="" or casa.get()=="" or sl.get()=="" or senha.get()=="" or cd.get()=="" or ad.get()=="" or i.get()=="":
                messagebox.showerror("Rent Car","Por favor seleciona os dados que pretendes actualizar!")
            else:
                cur.execute("UPDATE funcionarios SET morada=?,sexo=?,i=?,nome=?,telefone=?,ad=?,cd=?,casa=?,email=?,senha=?,sl=? WHERE id=?",(p,m,l,s,v,c,k,b,o,bi,on,n))
                messagebox.showinfo("Rent Car","Dados Actualizado com sucesso")
                limpaar()
                dbo.commit()
                for s in lista.get_children():
                    lista.delete(s)
                cur.execute("SELECT * FROM funcionarios")
                sav = cur.fetchall()
                for row in sav:
                    lista.insert("","end",values=(row))

        def duploclick(event):

            limpaar()
            lista.selection()
            for x in lista.selection():
                col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12 = lista.item(x, 'values')

            id.insert(END, col1)
            nome.insert(END, col2)
            morada.insert(END, col3)
            casa.insert(END, col4)
            telefone.insert(END, col5)
            senha.insert(END, col6)
            cd.insert(END, col7)
            ad.insert(END, col8)
            sl.insert(END, col9)
            i.insert(END, col11)
            email.insert(END, col12)

        def excluir():
          idselect = lista.item(lista.selection())['values'][0]
          db = sqlite3.connect("Sistema.db")
          cur = db.cursor()
          result=tkMessageBox.askquestion("Rent car","Tens Certeza que queres excluir do Sistema?",icon="warning")
          if result == "yes":
              messagebox.showinfo("Rent Car","Dados excluidos do Sistema")
              limpaar()
              delete = cur.execute("delete from funcionarios where id={}".format(idselect))
              lista.delete(lista.selection())
          db.commit()              

        def pesquisar():

           pp = cod.get()
           cur.execute("SELECT * FROM funcionarios WHERE id = (?)",(pp,))
           row = cur.fetchall()
           if row!=[]:
               limpaar()
               for x in lista.get_children():
                    lista.delete(x)
               for data in row:
                    lista.insert('',"end",values=(data))
                    cod.delete(0,END)
           else:
               messagebox.showerror("Rent Car","Nenhum dado encontrado na base de Dados")
               cod.delete(0,END)
           #cod.delete(0,END)
                    
        def pesquisar2():
            
           p = pes.get()
           cur.execute("SELECT * FROM funcionarios WHERE nome = (?)",(p,))
           roww = cur.fetchall()
           if roww!=[]:
               limpaar()
               for x in lista.get_children():
                    lista.delete(x)
               for data in roww:
                    lista.insert('',"end",values=(data))
                    pes.delete(0,END)
           else:
               messagebox.showerror("Rent Car","Nenhum dado encontrado na base de Dados")
               pes.delete(0,END)

        
        nb = ttk.Notebook(aluguel)
        nb.place(x=1,y=1,width=642,height=354)

        janela=Frame(nb)
        aluguell=Frame(nb)

        nb.add(janela,text="Cadastrar Funcionario")
        nb.add(aluguell,text="Consultar Funcionario")

        MainFrame = Frame(janela,padx=317,pady=160,bg="#e9e9e9")
        MainFrame.place(x=2,y=2)

        BI = Label(MainFrame,font=("Agency FB",16,"bold"),bg="#e9e9e9",text="",fg="Black")   
        BI.grid(row=0, column=2)

        nome = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Nome",fg="Black")
        nome.place(x=56,y=13)

        nome = Entry(janela,bd=1,width="19",font=(8),relief="solid")
        nome.place(x=59,y=38)

        codigo = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Codigo",fg="Black")
        codigo.place(x=12,y=13)    

        id = Entry(janela,bd=1,width="4",font=(8),relief="solid")
        id.place(x=15,y=38)
       
        morada = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Endereço",fg="Black")
        morada.place(x=240,y=13)

        morada = Entry(janela,bd=1,width="15",font=(8),relief="solid")
        morada.place(x=243,y=38)

        casa = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Casa Nº",fg="Black")
        casa.place(x=387,y=13)

        casa = Entry(janela,bd=1,width="8",font=(8),relief="solid")
        casa.place(x=390,y=38)

        telefone = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Telefone",fg="Black")
        telefone.place(x=12,y=72)

        telefone = Entry(janela,bd=1,width="24",font=(8),relief="solid")
        telefone.place(x=15,y=97)

        senha = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Senha",fg="Black")
        senha.place(x=240,y=72)

        senha = Entry(janela,bd=1,width="15",font=(8),relief="solid")
        senha['show'] = '*'
        senha.place(x=243,y=97)

        cd = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Província",fg="Black")
        cd.place(x=12,y=132)

        cd = Entry(janela,bd=1,width="16",font=(8),relief="solid")
        cd.place(x=15,y=155)

        ad = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Cargo",fg="Black")
        ad.place(x=335,y=132)

        ad = ttk.Combobox(janela,font=("Arial",11),width=14)
        ad['values'] = ("Tecnico","Atendor","Secretario","Gestor/a","Contabilista")
        ad.place(x=338,y=155)

        sl = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Salario Actual",fg="Black")
        sl.place(x=169,y=132)

        sl = Entry(janela,bd=1,width="17",font=(8),relief="solid")
        sl.place(x=172,y=155)

        group = LabelFrame(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Sexo",padx=33,pady=2)
        group.place(x=15,y=180)

        sexo = StringVar()

        AL = tk.Radiobutton(group,font=("Agency FB",12,"bold"),text="Masculino",value="Masculino",variable=sexo,bg="#e9e9e9")
        AL.pack()
            
        AL2 = tk.Radiobutton(group,font=("Agency FB",12,"bold"),text="Femenino",value="Femenino",variable=sexo,bg="#e9e9e9")
        AL2.pack()

        i = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Idade",fg="Black")
        i.place(x=387,y=72)

        i = Spinbox(janela,bd=1,width="7",font=(8),relief="solid",from_=1, to=100)
        i.place(x=390,y=97)

        email = Label(janela,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="E-mail",fg="Black")
        email.place(x=169,y=180)

        email = Entry(janela,bd=1,width="33",font=(8),relief="solid")
        email.place(x=172,y=205)

        p = PhotoImage(file="imagem/mb.png")
        po = Label(janela,image=p,bg="#e9e9e9")
        po.place(x=475,y=45)        

        fotoo = Entry(janela,bd=1,width="42",font=(6),relief="solid")
        fotoo.place(x=172,y=247)

        bt = Button(janela,font=("Agency FB",10,"bold"),text="Imagem",width=66,bg="white",height=18,bd=1,relief="solid")
        bt.place(x=560,y=245)

        foton = PhotoImage(file="imagem/foto.png")
        bt.config(image=foton,compound=LEFT)
    
        b2 = Button(janela,font=("Agency FB",10,"bold"),text="SALVAR",bg="white",width="65",height="40",bd=2,relief=RIDGE,command=salvar)
        b2.place(x=560,y=273)

        foto24 = PhotoImage(file="imagem/guardar.png")
        b2.config(image=foto24,compound=TOP)

        b3 = Button(janela,font=("Agency FB",10,"bold"),text="SAIR",bg="white",width="65",height="40",bd=2,relief=RIDGE,command=aluguel.destroy)
        b3.place(x=401,y=273)

        foto33 = PhotoImage(file="imagem/sair.png")
        b3.config(image=foto33,compound=TOP)

        b2 = Button(janela,font=("Agency FB",10,"bold"),text="ALTERAR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=alterar)
        b2.place(x=481,y=273)

        foto29 = PhotoImage(file="imagem/Alterar.png")
        b2.config(image=foto29,compound=TOP)

        MainFrame = Frame(aluguell,padx=314,pady=260,bg="#e9e9e9")
        MainFrame.place(x=2,y=2)

        Lb = Label(MainFrame,font=("Arial",12,"bold"),text="",bg="#e9e9e9")
        Lb.grid(row = 0,column = 2)

        pes = Label(aluguell,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Pesquisar ID")
        pes.place(x=19,y=15)

        cod = Entry(aluguell,font=("Arial",11),fg="black",width=10,bd=1,relief="solid")
        cod.place(x=22,y=41)

        pes = Label(aluguell,font=("Agency FB",12,"bold"),bg="#e9e9e9",text="Pesquisar Marca")
        pes.place(x=152,y=15)

        pes = Entry(aluguell,font=("Arial",11),fg="black",width=45,bd=1,relief="solid")
        pes.place(x=155,y=41)

        btm = Button(aluguell,font=("Agency FB",10,"bold"),text="",width=30,bg="white",height=17,bd=2,command=pesquisar,relief=RIDGE)
        btm.place(x=110,y=40)

        foto35 = PhotoImage(file="imagem/p.png")
        btm.config(image=foto35,compound=LEFT)

        bt = Button(aluguell,font=("Agency FB",10,"bold"),text="PESQUIZAR",width=73,bg="white",height=18,bd=2,command=pesquisar2,relief=RIDGE)
        bt.place(x=524,y=38)

        foto32 = PhotoImage(file="imagem/p.png")
        bt.config(image=foto32,compound=LEFT)

        lista = ttk.Treeview(aluguell,height=8,column=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10","col11","col12"),show='headings')   

        lista.heading("#1",text="ID")
        lista.heading("#2",text="Nome")
        lista.heading("#3",text="Morada")
        lista.heading("#4",text="Casa")
        lista.heading("#5",text="Telefone")
        lista.heading("#6",text="Senha")
        lista.heading("#7",text="Província")
        lista.heading("#8",text="Cargo")
        lista.heading("#9",text="Salario Actual")
        lista.heading("#10",text="Sexo")
        lista.heading("#11",text="Idade")
        lista.heading("#12",text="E-mail")        

        lista.column("#1",width=32)
        lista.column("#2",width=128)
        lista.column("#3",width=90)
        lista.column("#4",width=90)
        lista.column("#5",width=120)
        lista.column("#6",width=60)
        lista.column("#7",width=90)
        lista.column("#8",width=120)
        lista.column("#9",width=140)
        lista.column("#10",width=90)
        lista.column("#11",width=50)
        lista.column("#12",width=95)
        
        lista.bind("<Double-1>", duploclick)
    
        lista.place(x=23,y=70,width=571)
    
        estiloo = ttk.Style()
        estiloo.theme_use("clam")
        estiloo.configure("Treeview",rowheight=20)
        estiloo.map('Treeview',background=[('selected','grey')])
               
        barra= ttk.Scrollbar(aluguell,command=lista.yview)
        lista.configure(yscroll=barra.set)
        barra.place(x=593,y=70,height=203)

        barra= ttk.Scrollbar(aluguell,command=lista.xview,orient="horizontal")
        lista.configure(xscroll=barra.set)
        barra.place(x=23,y=259,width=571)

        dbo = sqlite3.connect("Sistema.db")
        cur = dbo.cursor()
        cur.execute("SELECT * FROM funcionarios")
        row = cur.fetchall()
        for savio in row:
            lista.insert("",END,values=savio)
        dbo.commit()

        def voltar():

            for i in lista.get_children():
                lista.delete(i)

            dbo = sqlite3.connect("Sistema.db")
            cur = dbo.cursor()
            cur.execute("SELECT * FROM funcionarios")
            row = cur.fetchall()
            for savio in row:
                lista.insert("",END,values=savio)
            dbo.commit()

        b1 = Button(aluguell,font=("Agency FB",10,"bold"),text="VOLTAR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=voltar)
        b1.place(x=455,y=275)

        foto1 = PhotoImage(file="imagem/back.png")
        b1.config(image=foto1,compound=TOP)

        b3 = Button(aluguell,font=("Agency FB",10,"bold"),text="EXCLUIR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=excluir)
        b3.place(x=533,y=275)

        foto3 = PhotoImage(file="imagem/ex.png")
        b3.config(image=foto3,compound=TOP)

        b5 = Button(aluguell,font=("Agency FB",10,"bold"),text="SAIR",bg="white",width=65,height=40,bd=2,relief=RIDGE,command=aluguel.destroy)
        b5.place(x=376,y=275)

        foto5 = PhotoImage(file="imagem/sair.png")
        b5.config(image=foto5,compound=TOP)

        aluguel.mainloop()
        
    def entrar():

        dg = sqlite3.connect("Sistema.db")
        cur = dg.cursor()
        cur.execute("SELECT * FROM adm WHERE nome = ? AND senha = ?",(e1.get(),e2.get()))
        row = cur.fetchall()
        dg.close()
        print(row)

        if row!=[]:

            #messagebox.showinfo("Autorizado","Acesso Autorizado!!")
            lo.destroy()
            loo.destroy()
            janelaa = Tk()
            janelaa.title("Rent Car Administrador")
            janelaa.resizable(0,0)
            janelaa.geometry("787x395+320+100")
            janelaa.iconbitmap("imagem/car.ico")
            janelaa.focus_force()
            janelaa.grab_set()

            def sair():
                result=tkMessageBox.askquestion("Confirmar Saida","Tens Certeza que queres sair?",icon="warning")
                if result == "yes":
                    janelaa.destroy()
                    exit()
                    
            def tic():
                sa['text'] = strftime('%H:%M')

            def tac():
                tic()
                sa.after(1000, tac)

            MainFrame = Frame(janelaa, bg="white",bd=2,padx=6,pady=100,relief=RIDGE)
            MainFrame.grid()

            TitFrame = Frame(MainFrame,bg="#C0C0C0",padx=50,pady=82,relief=RIDGE)
            TitFrame.pack(side=LEFT)

            lb = Label(TitFrame,font=("Agency FB",16),bg="#C0C0C0",text=" ")
            lb.grid(row=0,column=1)

            bt = Button(janelaa,text="Administrador",bd=1,height="56",width="105",relief=RIDGE,command=administrador)
            bt.place(x=11,y=105)

            ico = PhotoImage(file="imagem/oii.png")
            bt.config(image=ico,compound=TOP)

            bt2 = Button(janelaa,text=" Sair",bd="1",height="56",width="99",relief=RIDGE,command=sair)
            bt2.place(x=11,y=233)

            ico2 = PhotoImage(file="imagem/pl.png")
            bt2.config(image=ico2,compound=TOP)

            bt3 = Button(janelaa,text="Funcionarios",bd="1",height="56",width="90",relief=RIDGE,command=funcionario)
            bt3.place(x=11,y=169)

            ico3 = PhotoImage(file="imagem/lo.png")
            bt3.config(image=ico3,compound=TOP)

            p = PhotoImage(file="imagem/bg.png")
            Label(image=p, bg="white").place(x=128,y=2)

            pJ = PhotoImage(file="imagem/adm.png")
            Label(image=pJ, bg="#e9e9e9").place(x=2,y=10)

            sa = tkinter.Label(janelaa)
            sa['font'] = 'Agency 12 bold'
            sa['fg'] = 'grey'
            sa['bg'] = 'white'
            sa.place(x=40,y=31)
            tac()

            janelaa.mainloop()
        else:
            messagebox.showerror("Erro ao inicializar","Acesso Negado!!")

    def sair():
        result=tkMessageBox.askquestion("Confirmar Saida","Tens Certeza que queres sair?",icon="warning")
        if result == "yes":
            lo.destroy()
            exit()

    def mostrar():
    
        Lb["text"]=e2.get()
    
    def limpar():

        e1.delete(0,END)
        e2.delete(0,END)


    fot = PhotoImage(file="imagem/cas.png")
    r = Label(lo,image=fot,bg="white")
    r.place(x=15,y=15)

    fotoi = PhotoImage(file="imagem/ADMi.png")
    rp = Label(lo,image=fotoi,bg="white")
    rp.place(x=135,y=100)

    nome = Label(lo,font=("Agency FB",12,"bold"),fg="grey",text="NOME")
    nome.place(x=52,y=152)

    e1=Entry(lo,width="40",fg="grey",justify="center",relief="solid",borderwidth=1,font=("Agency FB",12,"bold"))
    e1.place (x=54,y=180)
    e1.focus()

    senha = Label(lo,font=("Agency FB",12,"bold"),fg="grey",text="SENHA")
    senha.place(x=52,y=232)

    e2=Entry(lo,width="40",fg="grey",justify="center",relief="solid",borderwidth=1,font=("Agency FB",12,"bold"))
    e2.place (x=54,y=260)
    e2['show'] = '*'
    e2.focus()

    photo0 = PhotoImage(file ="imagem/usu.png")
    p = Label(lo, image=photo0, bg="white")
    p.place(x=58,y=181)

    photo1 = PhotoImage(file ="imagem/chave.png")
    j = Label(lo, image=photo1, bg="white")
    j.place(x=58,y=262)

    photo2 = Button(lo,width=30,height=15,bg="white",borderwidth=0,command=mostrar)
    photo2.place(x=360,y=263)
    
    foto = PhotoImage(file ="imagem/vista.png")
    photo2.config(image=foto,compound=TOP)

    Lb = Label(lo,justify="center",font=("Agency FB",12,"bold"),fg="grey")
    Lb.place(x=208,y=290)

    foto2 = PhotoImage(file="imagem/pj.png")
    b = Label(lo, image=foto2,bg="white")
    b.place(x=15,y=15)

    b3 = Button(lo,font=("Agency FB",10,"bold"),text=" ENTRAR",bg="white",fg="grey",width=65,height=38,bd=2,relief=RIDGE,command=entrar)
    b3.place(x=54,y=360)

    foto6 = PhotoImage(file="imagem/en.png")
    b3.config(image=foto6,compound=TOP)

    b5 = Button(lo,font=("Agency FB",10,"bold"),text="LIMPAR",bg="white",fg="grey",width=65,height=38,bd=2,relief=RIDGE,command=limpar)
    b5.place(x=190,y=360)

    foto8 = PhotoImage(file="imagem/lim.png")
    b5.config(image=foto8,compound=TOP)

    b4 = Button(lo,font=("Agency FB",10,"bold"),text="SAIR",bg="white",fg="grey",width=65,height=38,bd=2,relief=RIDGE,command=lo.destroy)
    b4.place(x=320,y=360)

    foto7 = PhotoImage(file="imagem/sair.png")
    b4.config(image=foto7,compound=TOP)

    lo.mainloop()

def sair():
    result=tkMessageBox.askquestion("Confirmar Saida","Tens Certeza que queres sair?",icon="warning")
    if result == "yes":
        loo.destroy()
        exit()

loo = Tk()
loo.title("")
loo.geometry("430x370+512+130")
loo.config(bg="white")
loo.resizable(0,0)
loo.overrideredirect(True)

fra = Frame(loo,width=412,height=352,bg="#e9e9e9")
fra.place(x=9,y=9)

p = PhotoImage(file="imagem/klo.png")
j = Label(loo,image=p, bg="#e9e9e9")
j.place(x=167,y=27)

pJ = PhotoImage(file="imagem/NIV.png")
l = Label(loo,image=pJ, bg="white")
l.place(x=59,y=98)

b3 = Button(loo,font=("Agency FB",10,"bold"),text="ADMINSTRADOR",bg="white",fg="grey",width=110,height=30,bd=2,relief=RIDGE,command=adimi)
b3.place(x=59,y=200)

foto67 = PhotoImage(file="imagem/sem.png")
b3.config(image=foto67,compound=LEFT)

b2 = Button(loo,font=("Agency FB",10,"bold"),text="FUNCIONARIO",bg="white",fg="grey",width=110,height=30,bd=2,relief=RIDGE,command=fun)
b2.place(x=248,y=200)

foto69 = PhotoImage(file="imagem/plk.png")
b2.config(image=foto69,compound=LEFT)

b3 = Button(loo,font=("Agency FB",10,"bold"),text="SAIR",bg="white",fg="grey",width=300,height=30,bd=2,relief=RIDGE,command=sair)
b3.place(x=59,y=280)

foto698 = PhotoImage(file="imagem/sair.png")
b3.config(image=foto698,compound=LEFT)

loo.mainloop()

