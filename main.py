import customtkinter as ctk
from mtk_functions import check_preloader, frp_remove

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FRPApp:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Tecno Camon 40 Pro - FRP Tool")
        self.root.geometry("700x500")

        ctk.CTkLabel(self.root, text="Tecno Camon 40 Pro FRP Tool", font=("Arial", 20, "bold")).pack(pady=20)

        ctk.CTkButton(self.root, text="🔍 Detectar en Modo Preloader", command=self.detect_preloader, width=300, height=40).pack(pady=10)
        ctk.CTkButton(self.root, text="🔓 Quitar FRP (MTKClient)", command=self.remove_frp, width=300, height=40).pack(pady=10)
        ctk.CTkButton(self.root, text="🔄 Reiniciar en Fastboot", command=lambda: self.reboot("fastboot"), width=300, height=40).pack(pady=10)
        ctk.CTkButton(self.root, text="⏻ Apagar Teléfono", command=lambda: self.reboot("shutdown"), width=300, height=40).pack(pady=10)

        self.log = ctk.CTkTextbox(self.root, width=650, height=200)
        self.log.pack(pady=20)

    def detect_preloader(self):
        self.log.insert("end", "Detectando Preloader...\n")
        result = check_preloader()
        self.log.insert("end", result + "\n")

    def remove_frp(self):
        self.log.insert("end", "Iniciando bypass FRP...\n")
        result = frp_remove()
        self.log.insert("end", result + "\n")

    def reboot(self, mode):
        self.log.insert("end", f"Reiniciando en modo {mode}...\n")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FRPApp()
    app.run()