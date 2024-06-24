from tkinter import *
from tkinter import ttk
root = Tk()
pagina = ttk.Frame(root, padding=5)
pagina.grid()
ttk.Label(pagina, text="ops").grid()
ttk.Button(pagina, text="faça", command=root.quit).grid()



root.mainloop()
root.destroy()