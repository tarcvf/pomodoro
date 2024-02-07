from tkinter import *
from formatar_tempo import formatar
from tkinter import messagebox
class classeobj:
    def __init__(self):
        self.pausalonga = 1200
        self.pausacurta = 300
        self.pomodoro = 900
        self.rounds = 4
        self.tempo = self.pomodoro
        self.rounds_count = self.rounds

objconfig = classeobj()
def abrir_config(master):
    global objconfig
    config = Toplevel()
    config.title("Configurações") 
    config.geometry('300x300')     
    config.resizable(False, False)
    lbpom = Label(config,text="00:00")
    lbpausacurta= Label(config,text="00:00")
    lbpausalonga = Label(config,text="00:00")
    lbnumpausa  = Label(config,text="0")
    def mudapomodoro(value):
        lbpom.config(text=str(formatar(int(value))))
        global pom_value
        pom_value = value

    def mudapausacurta(value):
        lbpausacurta.config(text=str(formatar(int(value))))
        global pausacurta_value
        pausacurta_value = value

    def mudapausalonga(value):
        lbpausalonga.config(text=str(formatar(int(value))))
        global pausalonga_value
        pausalonga_value = value
    def mudanumpausa(value):
        lbnumpausa.config(text=str(int(value)))
        global numpausa_value
        numpausa_value = value

    pom = Scale(config,from_=5,to=2000,orient=HORIZONTAL,label="pomodoro",showvalue=0,length=250,command=mudapomodoro).pack()
    lbpom.pack()

    pausacurta = Scale(config,from_=5,to=2000,orient=HORIZONTAL,label="pausa curta",showvalue=0,length=250,command=mudapausacurta).pack()
    lbpausacurta.pack()

    pausalonga = Scale(config,from_=5,to=2000,orient=HORIZONTAL,label="pausa longa",showvalue=0,length=250,command=mudapausalonga).pack()
    lbpausalonga.pack()

    numoausa=Scale(config,from_=2,to=20,orient=HORIZONTAL,label="pausas",showvalue=0,length=250,command=mudanumpausa).pack()
    lbnumpausa.pack()
    def tudocerto():
        try:
            objconfig.pausacurta = int(pausacurta_value)
            objconfig.pausalonga = int(pausalonga_value)
            objconfig.pomodoro = int(pom_value)
            objconfig.rounds = int(numpausa_value)
            objconfig.rounds_count = objconfig.rounds
            config.destroy()
        except:
            messagebox.showinfo("tudo zerado","por favor configure seu pomodoro")
    btnfim=Button(config,text="tudo certo!!",command=tudocerto).pack()












    
