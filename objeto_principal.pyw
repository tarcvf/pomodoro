import tkinter as tk
import time
from config import abrir_config,objconfig
from formatar_tempo import formatar
from playsound import playsound
app = tk.Tk()
app.title("pomodoro simples")
app.geometry("100x200")
app.resizable(False,False)
cima = tk.Frame(app).pack(fill="both")
meio = tk.Frame(app).pack(fill="x")
baixo = tk.Frame(app).pack(fill="x")
config = tk.Button(cima,text="☰",command=(lambda : abrir_config(app))).pack(anchor="nw")
lbcronometro = tk.Label(text="00:00",master=meio,font=("Helvetica", 24))
lbrounds = tk.Label(baixo,text="aguardando...")
lbrounds.pack(side="bottom")
status = tk.Label(baixo, text="pomdoro")
status.pack(side="bottom")
objconfig.tempo = objconfig.pomodoro
rodando = False

def contaseg():
    global rodando
    lbcronometro.config(text=formatar(objconfig.tempo))
    objconfig.tempo-=1
    if rodando:
        if objconfig.tempo>(-1):
            app.after(1000,contaseg)
        else:
            contar(True)
lbcronometro.pack(fill="both")
estado = "pomo"
def contar(rodando):
    global estado
    if rodando == True:
        if objconfig.tempo<=1:
            if (estado == "pomo") and (objconfig.rounds-objconfig.rounds_count+1 !=objconfig.rounds):
                estado = "pcur"
                status.config(text="descanso (curto)")
            elif estado == "pcur" or estado == "plon" :
                estado = "pomo"
                status.config(text="pomodoro")
                objconfig.rounds_count = objconfig.rounds_count -1
            elif (objconfig.rounds-objconfig.rounds_count+1 ==objconfig.rounds) and (estado =="pomo"):
                estado = "plon"
                status.config(text="descanso (longo)")
                objconfig.rounds_count = objconfig.rounds
        lbrounds.config(text=f"{objconfig.rounds-objconfig.rounds_count+1}/{objconfig.rounds}")

        if estado =="pomo":
            objconfig.tempo = objconfig.pomodoro
            playsound(".\\audio\\pomo.mp3")
        if estado == "pcur":
            objconfig.tempo = objconfig.pausacurta
            playsound(".\\audio\\pausa.mp3")
        if estado == "plon":
            objconfig.tempo = objconfig.pausalonga
            playsound(".\\audio\\plon.mp3")

        contaseg()  
    print(estado)           
def playpausef():
    global rodando
    if not rodando:
        rodando = True
        playpause.config(text="||")
        contar(rodando)
    else:
        rodando = False
        playpause.config(text="▶️")  # Altera o texto para o ícone de playsoundução
    print(rodando)

playpause = tk.Button(baixo, text="▶️", font=("Helvetica", 24), command=playpausef)
playpause.pack()

app.mainloop()