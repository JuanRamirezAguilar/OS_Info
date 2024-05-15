import ttkbootstrap as ttk

root_main = ttk.Window(themename='morph')
root_main.title("Windows Info")
root_main.geometry("800x600")
root_main.resizable(False, False)
root_main.anchor("n")


frame_titulo = ttk.Frame(root_main)
separator_widget = ttk.Separator(root_main, orient="horizontal")
frame_info = ttk.Frame(root_main)

frame_titulo.grid(row=0, column=0, padx=5, pady=5)
separator_widget.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

frame_info.grid(row=2, column=0, padx=5, pady=5)

label_titulo = ttk.Label(frame_titulo, text="Windows Info", font=("Arial", 30, "bold"))
label_titulo.grid(row=0, column=0, padx=5, pady=5, sticky="n", columnspan=2)
label_description = ttk.Label(frame_titulo, text="A program made to know the specifications of your computer", font=("Arial", 14))
label_description.grid(row=1, column=0, padx=5, pady=5, sticky="n", columnspan=2)

menuButton_themes = ttk.Menubutton(frame_titulo, text="Theme")
menuButton_themes.grid(row=0, column=1, padx=5, pady=5, sticky="e")
menuButton_themes.option_add("Litera", "Litera")

label_info = ttk.Label(frame_info, text="Texto de Prueba")
label_info.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

root_main.mainloop()