import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw
import pyperclip
import qrcode
import webbrowser

class PerfilApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Perfil")
        self.root.geometry("770x570")
        self.root.configure(bg="#2B124C")

        # Colores y variables iniciales
        self.bg_color = "#2B124C"
        self.button_color = "#522B5B"
        self.label_color = "#DFB6B2"
        self.text_color = "#FBE4D8"
        self.highlight_color = "#854F6C"
        self.username = tk.StringVar(value="Username")
        self.imagen_perfil = "perfil.png"
        self.imagen_perfil_circular = None

        # Cargar la interfaz principal
        self.cargar_primera_interfaz()

    def cargar_primera_interfaz(self):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        # Imagen de perfil
        if not self.imagen_perfil_circular:
            self.imagen_perfil_circular = self.cargar_imagen_circular(self.imagen_perfil)
        label_imagen = tk.Label(self.root, image=self.imagen_perfil_circular, bg=self.bg_color)
        label_imagen.place(x=50, y=50)

        # Etiquetas
        username_label = tk.Label(self.root, textvariable=self.username, bg=self.bg_color, fg=self.label_color,
                                  font=("Arial", 15, "bold"))
        username_label.place(x=150, y=370)

        seguidores_label = tk.Label(self.root, text="Seguidores: 0", bg=self.bg_color, fg=self.label_color,
                                     font=("Georgia", 14))
        seguidores_label.place(x=100, y=425)

        seguidos_label = tk.Label(self.root, text="Seguidos: 0", bg=self.bg_color, fg=self.label_color,
                                   font=("Georgia", 14))
        seguidos_label.place(x=100, y=460)

        # Botones con emojis
        editar_perfil_button = tk.Button(self.root, text="Editar Perfil ✏️", bg=self.button_color, fg=self.text_color,
                                         font=("Arial", 15), activebackground=self.highlight_color,
                                         command=self.cargar_segunda_interfaz)
        editar_perfil_button.place(x=390, y=50)


        compartir_button = tk.Button(self.root, text="Cerrar Sesion ⮹", bg=self.button_color, fg=self.text_color,
                                      font=("Arial", 13), command=self.cargar_cuarta_interfaz)
        compartir_button.place(x=390, y=220)

        codigo_button = tk.Button(self.root, text="Mostrar Código de Cuenta ⥱", bg=self.button_color, fg=self.text_color,
                                   font=("Arial", 13), command=self.mostrar_qr)
        codigo_button.place(x=390, y=290)

        # Actividad reciente
        actividad_label = tk.Label(self.root, text="No hay actividad reciente", bg=self.bg_color, fg=self.label_color,
                                   font=("Arial", 16), wraplength=300)
        actividad_label.place(x=390, y=360)

        # Descubrir música
        musica_label = tk.Label(self.root, text="Descubre música nueva ahora 🎵", bg=self.bg_color, fg=self.text_color,
                                font=("Arial", 10, "underline"), wraplength=300)
        musica_label.place(x=390, y=390)
        musica_label.bind("<Button-1>", lambda e: print("Redirigiendo a página de inicio..."))

        # Botón para volver a interfaz.py
        volver_button = tk.Button(self.root, text="🔙", bg=self.button_color, fg=self.text_color,
                                   font=("Arial", 15), command=self.volver_a_interfaz)
        volver_button.place(x=20, y=20)

    def cargar_segunda_interfaz(self):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        # Imagen de perfil
        if not self.imagen_perfil_circular:
            self.imagen_perfil_circular = self.cargar_imagen_circular(self.imagen_perfil)

        label_imagen = tk.Label(self.root, image=self.imagen_perfil_circular, bg=self.bg_color)
        label_imagen.place(x=80, y=40)

        # Cambiar foto de perfil
        cambiar_label = tk.Label(self.root, text="Cambiar foto de perfil", font=("Arial", 12), fg=self.label_color,
                                 bg=self.bg_color)
        cambiar_label.place(x=150, y=360)

        cambiar_button = tk.Button(self.root, text="➕", font=("Arial", 15), command=self.cambiar_imagen,
                                   bg=self.bg_color, fg=self.text_color, relief="flat")
        cambiar_button.place(x=350, y=290)

        # Cambiar nombre de usuario
        cambiar_nombre_label = tk.Label(self.root, text="Cambiar nombre de usuario:", font=("Arial", 15),
                                        fg=self.label_color, bg=self.bg_color)
        cambiar_nombre_label.place(x=100, y=425)

        entry_nombre = tk.Entry(self.root, textvariable=self.username, width=30, font=("Arial", 13),
                                bg=self.button_color, fg=self.text_color)
        entry_nombre.place(x=100, y=460)

        # Botones de acción
        aceptar_button = tk.Button(self.root, text="Guardar Cambios ✅", font=("Arial", 15), command=self.guardar_cambios,
                                   bg=self.button_color, fg=self.text_color)
        aceptar_button.place(x=370, y=20)

        volver_button = tk.Button(self.root, text="Volver 🔙", font=("Arial", 15), command=self.cargar_primera_interfaz,
                                  bg=self.button_color, fg=self.text_color)
        volver_button.place(x=20, y=20)

    def cargar_cuarta_interfaz(self):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        # Imagen de perfil
        if not self.imagen_perfil_circular:
            self.imagen_perfil_circular = self.cargar_imagen_circular(self.imagen_perfil)
        label_imagen = tk.Label(self.root, image=self.imagen_perfil_circular, bg=self.bg_color)
        label_imagen.place(x=50, y=50)

        username_label = tk.Label(self.root, textvariable=self.username, bg=self.bg_color, fg=self.label_color,
                                  font=("Arial", 15, "bold"))
        username_label.place(x=150, y=370)

        info_label = tk.Label(self.root, text="Perfil SoundVibes", bg=self.bg_color, fg=self.label_color,
                              font=("Arial", 12))
        info_label.place(x=100, y=420)

        boton_copiar = tk.Button(self.root, text="Si?", font=("Arial", 13), bg=self.button_color,
                                 fg=self.text_color, command=self.open_Perfil)
        boton_copiar.place(x=400, y=190)


        volver_button = tk.Button(self.root, text="Volver 🔙", font=("Arial", 15), bg=self.button_color,
                                   fg=self.text_color, command=self.cargar_primera_interfaz)
        volver_button.place(x=20, y=20)

        # Botón para volver a interfaz.py
        volver_inicio_button = tk.Button(self.root, text="Volver a Inicio 🔙", font=("Arial", 13),
                                          bg=self.button_color, fg=self.text_color, command=self.volver_a_interfaz)
        volver_inicio_button.place(x=20, y=500)

    def volver_a_interfaz(self):
        """Regresa a la pantalla principal (interfaz.py)."""
        self.root.destroy()
        from interfaz import MusicPlayer
        main_window = tk.Tk()
        MusicPlayer(main_window)
        main_window.mainloop()

    def mostrar_qr(self):
        enlace = "https://mi-perfil.com/usuario123"
        qr = qrcode.make(enlace)

        # Mostrar el código QR
        qr_ventana = tk.Toplevel(self.root)
        qr_ventana.title("Código QR")
        qr_img = ImageTk.PhotoImage(qr)
        qr_label = tk.Label(qr_ventana, image=qr_img)
        qr_label.image = qr_img
        qr_label.pack()

    def cambiar_imagen(self):
        archivo = filedialog.askopenfilename(title="Selecciona una imagen",
                                             filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")])
        if archivo:
            self.imagen_perfil = archivo
            self.imagen_perfil_circular = self.cargar_imagen_circular(archivo)
            self.cargar_primera_interfaz()

    def cargar_imagen_circular(self, archivo):
        img = Image.open(archivo).resize((300, 300))
        mascara = Image.new("L", (300, 300), 0)
        draw = ImageDraw.Draw(mascara)
        draw.ellipse((0, 0, 300, 300), fill=255)
        img_circular = Image.new("RGBA", (300, 300))
        img_circular.paste(img, (0, 0), mask=mascara)
        return ImageTk.PhotoImage(img_circular)

    def guardar_cambios(self):
        messagebox.showinfo("Aceptar", "Cambios realizados exitosamente")
        self.cargar_primera_interfaz()

    def open_Perfil(self):
         """Abre la ventana de Perfil."""
         self.root.destroy()  # Oculta la ventana actual
         from principal import LoginApp  # Importa la clase PerfilApp
         Perfil_window = tk.Tk()
         LoginApp(Perfil_window)  # Inicializa la clase con la ventana
         Perfil_window.mainloop()

    def compartir_correo(self):
        enlace = "https://mi-perfil.com/usuario123"
        asunto = "¡Mira mi perfil!"
        cuerpo = f"Hola,\n\nTe comparto mi perfil: {enlace}\n\n¡Saludos!"
        mailto = f"mailto:?subject={asunto}&body={cuerpo}"
        webbrowser.open(mailto)


# Bloque principal
if __name__ == "__main__":
    root = tk.Tk()
    app = PerfilApp(root)
    root.mainloop()
