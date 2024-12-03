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

        # Colores
        self.bg_color = "#2B124C"
        self.button_color = "#522B5B"
        self.label_color = "#DFB6B2"
        self.text_color = "#FBE4D8"
        self.highlight_color = "#854F6C"

        # Variables
        self.username = tk.StringVar(value="Username")
        self.imagen_perfil = "perfil.png"
        self.imagen_perfil_circular = None  # Imagen circularizada

        # Cargar la interfaz inicial
        self.cargar_primera_interfaz()

    def cargar_primera_interfaz(self):
        """Carga la interfaz inicial del perfil."""
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        # Usar imagen circularizada
        if not self.imagen_perfil_circular:
            self.imagen_perfil_circular = self.cargar_imagen_circular(self.imagen_perfil)

        label_imagen = tk.Label(self.root, image=self.imagen_perfil_circular, bg=self.bg_color)
        label_imagen.place(x=50, y=50)

        # Username
        username_label = tk.Label(self.root, textvariable=self.username, bg=self.bg_color, fg=self.label_color,
                                  font=("Arial", 15, "bold"))
        username_label.place(x=150, y=370)

        # Seguidores y seguidos
        seguidores_label = tk.Label(self.root, text="Seguidores: 120", bg=self.bg_color, fg=self.label_color,
                                     font=("Georgia", 14))
        seguidores_label.place(x=150, y=425)

        seguidos_label = tk.Label(self.root, text="Seguidos: 80", bg=self.bg_color, fg=self.label_color,
                                   font=("Georgia", 14))
        seguidos_label.place(x=150, y=460)

        # Botones
        editar_perfil_button = tk.Button(self.root, text="Editar Perfil ✎", bg=self.button_color, fg=self.text_color,
                                         font=("Arial", 15), command=self.cargar_segunda_interfaz)
        editar_perfil_button.place(x=360, y=50)

        amigos_button = tk.Button(self.root, text="👥 Información de la cuenta", bg=self.bg_color, fg=self.text_color,
                                   font=("Arial", 13), command=self.cargar_tercera_interfaz)
        amigos_button.place(x=455, y=150)

        compartir_button = tk.Button(self.root, text="⮹ Compartir Perfil", bg=self.bg_color, fg=self.text_color,
                                      font=("Arial", 13), command=self.cargar_cuarta_interfaz)
        compartir_button.place(x=435, y=220)

        codigo_button = tk.Button(self.root, text="⥱ Mostrar Código QR", bg=self.bg_color, fg=self.text_color,
                                   font=("Arial", 13), command=self.mostrar_qr)
        codigo_button.place(x=440, y=290)

        # Actividad reciente
        actividad_label = tk.Label(self.root, text="No hay actividad reciente", bg=self.bg_color, fg=self.label_color,
                                   font=("Arial", 16), wraplength=300)
        actividad_label.place(x=400, y=360)

        # Descubrir música
        musica_label = tk.Label(self.root, text="🎵 Descubre música nueva ahora", bg=self.bg_color, fg=self.text_color,
                                font=("Arial", 12, "underline"), wraplength=300, cursor="hand2")
        musica_label.place(x=430, y=400)
        musica_label.bind("<Button-1>", lambda e: messagebox.showinfo("Redirección", "Redirigiendo a música nueva..."))

    def cargar_segunda_interfaz(self):
        """Carga la interfaz de edición del perfil."""
        for widget in self.root.winfo_children():
            widget.destroy()

        label_imagen = tk.Label(self.root, image=self.imagen_perfil_circular, bg=self.bg_color)
        label_imagen.place(x=80, y=40)

        cambiar_button = tk.Button(self.root, text="➕ Cambiar imagen", font=("Arial", 12),
                                   command=self.cambiar_imagen, bg=self.button_color, fg=self.text_color)
        cambiar_button.place(x=150, y=300)

        entry_nombre = tk.Entry(self.root, textvariable=self.username, font=("Arial", 14),
                                bg=self.button_color, fg=self.text_color)
        entry_nombre.place(x=150, y=360)

        guardar_button = tk.Button(self.root, text="💾 Guardar cambios", font=("Arial", 14), bg=self.button_color,
                                   fg=self.text_color, command=self.guardar_cambios)
        guardar_button.place(x=150, y=420)

        volver_button = tk.Button(self.root, text="↩ Volver", font=("Arial", 15), command=self.cargar_primera_interfaz,
                                  bg=self.button_color, fg=self.text_color)
        volver_button.place(x=20, y=20)

    def cambiar_imagen(self):
        """Permite seleccionar una nueva imagen de perfil."""
        archivo = filedialog.askopenfilename(title="Selecciona una imagen",
                                             filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")])
        if archivo:
            self.imagen_perfil = archivo
            self.imagen_perfil_circular = self.cargar_imagen_circular(archivo)
            self.cargar_segunda_interfaz()

    def cargar_imagen_circular(self, archivo):
        """Circulariza una imagen."""
        img = Image.open(archivo).resize((300, 300))
        mascara = Image.new("L", (300, 300), 0)
        draw = ImageDraw.Draw(mascara)
        draw.ellipse((0, 0, 300, 300), fill=255)
        img_circular = Image.new("RGBA", (300, 300))
        img_circular.paste(img, (0, 0), mask=mascara)
        return ImageTk.PhotoImage(img_circular)

    def cargar_tercera_interfaz(self):
        """Carga la interfaz de información de la cuenta."""
        for widget in self.root.winfo_children():
            widget.destroy()

        titulo = tk.Label(self.root, text="👤 Información de la cuenta", font=("Arial", 20, "bold"),
                          bg=self.bg_color, fg=self.text_color)
        titulo.place(x=100, y=20)

        labels = ["📛 Nombre:", "✉ Correo electrónico:", "🔒 Contraseña:", "🎂 Fecha de nacimiento:"]
        for i, text in enumerate(labels):
            tk.Label(self.root, text=text, font=("Arial", 14), bg=self.bg_color, fg=self.label_color).place(x=50, y=100 + i * 80)

        volver_button = tk.Button(self.root, text="↩ Volver", font=("Arial", 15), command=self.cargar_primera_interfaz,
                                  bg=self.button_color, fg=self.text_color)
        volver_button.place(x=20, y=20)

    def cargar_cuarta_interfaz(self):
        """Carga la interfaz de compartir perfil."""
        for widget in self.root.winfo_children():
            widget.destroy()

        label_imagen = tk.Label(self.root, image=self.imagen_perfil_circular, bg=self.bg_color)
        label_imagen.place(x=50, y=50)

        info_label = tk.Label(self.root, text="🌟 Perfil SoundVibes", bg=self.bg_color, fg=self.label_color,
                              font=("Arial", 12))
        info_label.place(x=100, y=420)

        boton_copiar = tk.Button(self.root, text="📋 Copiar enlace", font=("Arial", 13), bg=self.button_color,
                                 fg=self.text_color, command=self.copiar_enlace)
        boton_copiar.place(x=400, y=190)

        boton_correo = tk.Button(self.root, text="📧 Compartir por correo", font=("Arial", 13), bg=self.button_color,
                                 fg=self.text_color, command=self.compartir_correo)
        boton_correo.place(x=400, y=240)

        volver_button = tk.Button(self.root, text="↩ Volver", font=("Arial", 15), bg=self.button_color,
                                  fg=self.text_color, command=self.cargar_primera_interfaz)
        volver_button.place(x=20, y=20)

    def mostrar_qr(self):
        """Muestra un código QR con información del perfil."""
        enlace = "https://mi-perfil.com/usuario123"
        qr = qrcode.make(enlace)

        # Crear ventana secundaria
        qr_ventana = tk.Toplevel(self.root)
        qr_ventana.title("Código QR")
        qr_ventana.geometry("300x300")
        qr_img = ImageTk.PhotoImage(qr)
        qr_label = tk.Label(qr_ventana, image=qr_img)
        qr_label.image = qr_img
        qr_label.pack()

    def copiar_enlace(self):
        """Copia un enlace al portapapeles."""
        enlace = "https://mi-perfil.com/usuario123"
        pyperclip.copy(enlace)
        messagebox.showinfo("Copiado", "El enlace se copió al portapapeles.")

    def compartir_correo(self):
        """Abre un cliente de correo para compartir el perfil."""
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
