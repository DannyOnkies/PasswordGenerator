##
# GENERA UNA PASSWORD
# SECONDO LO SCHEMA SEGUENTE
#   L L L L N S N L L S L
# DOVE L=LETTERA S=SIMBOLO N=NUMERO
# es. (xcgw7/3hx*G) (ayxq0)6hz"Q)
#
import tkinter
from random import randint
import tkinter as tk
from tkinter import messagebox

# VISUALIZZA UNA FINESTRA DI INFORMAZIONE
def msghelp():
    #messagebox.showinfo('Python help','Qui ci va il messaggio')
    messagebox.showinfo('Python help', "Qui ci va il messaggio", icon="question") # silenzioso


# restituisce una stringa
# contenente la password generata
def pwd():
    pwd = []
    # 4 LETTERE
    for i in range(4):
        lettere = randint(97, 122)
        pwd.append(chr(lettere))
    # 1 NUMERO
    numeri = randint(48, 57)
    pwd.append(chr(numeri))
    # 1 SIMBOLO
    simboli1 = randint(33, 47)
    pwd.append(chr(simboli1))
    # 1 NUMERO
    numeri = randint(48, 57)
    pwd.append(chr(numeri))
    # 2 LETTERE
    for i in range(2):
        lettere = randint(97, 122)
        pwd.append(chr(lettere))
    # 1 SIMBOLO
    simboli1 = randint(33, 47)
    pwd.append(chr(simboli1))
    # 1 LETTERA
    lettere = randint(65, 90)
    pwd.append(chr(lettere))
    # converto la lista in una stringa
    pwd_str = ''.join(pwd)
    # Una variabile StringVar() viene usata per cambiare il testo dei widget
    var.set(pwd_str)
    # Setto il focus sul widget ENTRY
    output.focus_set()
    # Seleziono il testo contenuto
    output.select_range(0, tkinter.END)
    # pulisco la clipboard
    window.clipboard_clear()
    # copio il contenuto del widget ENTRY nella clipboard
    window.clipboard_append(pwd_str)


window = tk.Tk()
window.geometry("380x70")
window.title("Generatore di password")
window.resizable(False, False)

var = tk.StringVar()
var.set("Click per generare una password")

# CASELLA INPUT
output = tk.Entry(window, textvariable=var)
output.focus_set()
output.select_range(0, tkinter.END)
output.grid(row=0, column=0, padx=10, pady=10, ipadx=30)

# PULSANTE
button = tk.Button(text="Genera", width=15, command=pwd)
button.grid(row=0, column=1, padx=10, pady=10)

# ETICHETTE
etichetta1 = tk.Label(text="La password viene", fg="red")
etichetta1.grid(row=1, column=0, sticky="E")
etichetta2 = tk.Label(text="copiata negli appunti", fg="red")
etichetta2.grid(row=1, column=1, sticky="W")
butt_help = tk.Button(text="?", width=1,command=msghelp)
butt_help.grid(row=0,column=2)

window.mainloop()
