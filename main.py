import ttkbootstrap as ttk
import platform
import wmi
import os

def cpu_info() -> str:
    c = wmi.WMI()
    for processor in c.Win32_Processor():
        return f"{processor.Name}"

def info(frame, buttom):
    #frame = ttk.Frame(root_main)
    operative_system = platform.system()
    release_system = platform.release()
    version_system = platform.version()
    machine_name = platform.node()
    processor = platform.processor()
    arch_processor = platform.machine()
    ver_processor = cpu_info()
    
    label_subtitle = ttk.Label(frame, text="Informacion del Sistema Operativo", font=("Arial", 18, "bold"))
    label_subtitle.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    
    separator_widget_info = ttk.Separator(frame, orient="horizontal")
    separator_widget_info.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
    
    label_sistema_operativo = ttk.Label(frame, text="Sistema Operativo: {}".format(operative_system), font=("Arial", 14, "bold"))
    label_sistema_operativo.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    
    label_release = ttk.Label(frame, text="Release: {}".format(release_system), font=("Arial", 14, "bold"))
    label_release.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    
    label_version_system = ttk.Label(frame, text="Version del Sistema: {}".format(version_system), font=("Arial", 14, "bold"))
    label_version_system.grid(row=5, column=0, padx=5, pady=5, sticky="w")
    
    label_machine_name = ttk.Label(frame, text="Nombre de la Maquina: {}".format(machine_name), font=("Arial", 14, "bold"))
    label_machine_name.grid(row=6, column=0, padx=5, pady=5, sticky="w")
    
    label_processor = ttk.Label(frame, text="Procesador: {}".format(processor), font=("Arial", 14, "bold"))
    label_processor.grid(row=7, column=0, padx=5, pady=5, sticky="w")
    
    label_arch_processor = ttk.Label(frame, text="Arquitectura del Procesador: {}".format(arch_processor), font=("Arial", 14, "bold"))
    label_arch_processor.grid(row=8, column=0, padx=5, pady=5, sticky="w")
    
    label_ver_processor = ttk.Label(frame, text="Version del Procesador: {}".format(ver_processor), font=("Arial", 14, "bold"))
    label_ver_processor.grid(row=9, column=0, padx=5, pady=5, sticky="w")
    
    buttom_info.destroy()
    

root_main = ttk.Window(themename='morph')
root_main.title("System Info")
root_main.geometry("800x600")
root_main.resizable(False, False)
root_main.anchor("n")
root_main.iconbitmap(r"C:\Users\juana\OneDrive\Documentos\Codigos\System Info\icon_info_48x48.ico")


frame_titulo = ttk.Frame(root_main)
separator_widget = ttk.Separator(root_main, orient="horizontal")
frame_info = ttk.Frame(root_main)

frame_titulo.grid(row=0, column=0, padx=5, pady=5)
separator_widget.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

frame_info.grid(row=2, column=0, padx=5, pady=5)

label_titulo = ttk.Label(frame_titulo, text="System Info", font=("Arial", 30, "bold"))
label_titulo.grid(row=0, column=0, padx=5, pady=5, sticky="n", columnspan=2)
label_description = ttk.Label(frame_titulo, text="A program made to know the specifications of your computer", font=("Arial", 14))
label_description.grid(row=1, column=0, padx=5, pady=5, sticky="n", columnspan=2)

menuButton_themes = ttk.Menubutton(frame_titulo, text="Theme")
menuButton_themes.grid(row=0, column=1, padx=5, pady=5, sticky="e")
menuButton_themes.option_add("Litera", "Litera")

buttom_info = ttk.Button(frame_info, text="Check the machine", bootstyle="success", command=lambda : info(frame_info, buttom_info))
buttom_info.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

root_main.mainloop()