import tkinter as tk

def mostrar_texto():
    nome = entrada.get()
    lbl_resultado.config(text=f"Olá, {nome}!")

janela = tk.Tk()
janela.title("Exemplo Tkinter")

lbl = tk.Label(janela, text="Digite seu nome:")
lbl.pack()

entrada = tk.Entry(janela)
entrada.pack()

btn = tk.Button(janela, text="Enviar", command=mostrar_texto)
btn.pack()

lbl_resultado = tk.Label(janela, text="")
lbl_resultado.pack()

janela.mainloop()
