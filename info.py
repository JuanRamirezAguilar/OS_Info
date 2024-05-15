import platform
import wmi
import os

def cpu_info() -> str:
    c = wmi.WMI()
    for processor in c.Win32_Processor():
        return f"{processor.Name}"

def main() -> None:
    os.system("cls")
    print("Sistema Operativo:", platform.system())
    print("Release:", platform.release())
    print("Version:", platform.version())
    print("Nombre de la Maquina:",platform.node())
    print("Procesador:", platform.processor())
    print("Arquitectura del Procesador:", platform.machine())
    print("Version del Procesador", cpu_info())
    
    

if __name__ == "__main__":
    main()