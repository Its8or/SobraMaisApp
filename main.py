import tkinter as tk

def openWindow():
    janela_nova = tk.Toplevel()
    janela_nova.title("New Window")
    janela_nova.geometry("200x100")
    botao_fechar = tk.Button(janela_nova, text="Close", command=janela_nova.destroy)
    botao_fechar.pack()

janela_principal = tk.Tk()
janela_principal.title("Main Window")
janela_principal.geometry("300x200")

botao_abrir = tk.Button(janela_principal, text="Abrir Nova Janela", command=openWindow)
botao_abrir.pack()

janela_principal.mainloop()