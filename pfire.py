
"""from tkinter import *
import pyrebase

janela = Tk()
janela.title("Exemplo")
janela.geometry("400x400+300+60")


def data():
    
nome =  Label(janela, text="Insira o nome:")
nome.place(x=20,y=20)

e1 = Entry(janela, width=30)
e1.place(x=23,y=45)

bt = Button(janela,text="Enviar")
bt.place(x=23,y=70)

bt2 = Button(janela, text="Limpar",command=data)
bt2.place(x=90,y=70)


janela.mainloop()"""

from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
<Check@MDCheckbox>:
    group: 'group'
    size_hint: None, None
    size: dp(48), dp(48)


FloatLayout:

    Check:
        active: True
        pos_hint: {'center_x': .4, 'center_y': .5}

    Check:
        pos_hint: {'center_x': .6, 'center_y': .5}
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()