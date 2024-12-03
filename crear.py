import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk, ImageDraw


class Usuario:
    def __init__(self, ventana):
        # Configuración de la ventana principal
        self.ventana = ventana
        self.ventana.title("Crear una cuenta nueva")
        self.ventana.geometry("900x570")
        self.ventana.configure(bg="#2B124C")

        # Variables
        self.foto = None

        # Configuración de la interfaz
        self.cargar_imagen_perfil()
        self.crear_widgets()

    def cargar_imagen_perfil(self):
        """Carga la imagen inicial del perfil."""
        imagen = Image.open("perfil.png")  # Cambia la ruta si es necesario
        imagen = imagen.resize((225, 225))
        self.foto = ImageTk.PhotoImage(imagen)
        self.label_imagen = tk.Label(self.ventana, image=self.foto, bg="#2B124C")
        self.label_imagen.place(x=525, y=130)

    def cargar_imagen(self):
        """Carga una nueva imagen de perfil."""
        archivo = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg")])
        if archivo:
            img = Image.open(archivo).resize((225, 225))
            mascara = Image.new("L", (225, 225), 0)
            draw = ImageDraw.Draw(mascara)
            draw.ellipse((0, 0, 225, 225), fill=255)
            img_circular = Image.new("RGBA", (225, 225))
            img_circular.paste(img, (0, 0), mask=mascara)

            # Convertir a formato compatible con tkinter y mostrar
            nueva_foto = ImageTk.PhotoImage(img_circular)
            self.label_imagen.config(image=nueva_foto)
            self.label_imagen.image = nueva_foto

    def registrar_usuario(self):
        """Valida los datos ingresados y registra al usuario."""
        nombre = self.entry_nombre.get()
        email = self.entry_email.get()
        contraseña = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()
        fecha_nacimiento = self.date_entry.get()

        # Validaciones de datos
        if not nombre or not email or not contraseña or not confirm_password:
            messagebox.showwarning("Campos vacíos", "Por favor, completa todos los campos obligatorios.")
            return
        if "@" not in email:
            messagebox.showerror("Error de email", "El correo electrónico debe contener '@'.")
            return
        if contraseña != confirm_password:
            messagebox.showerror("Contraseñas no coinciden", "Las contraseñas ingresadas no coinciden.")
            return
        if not fecha_nacimiento:
            messagebox.showwarning("Fecha de nacimiento", "Por favor, selecciona una fecha de nacimiento.")
            return

        # Mensaje de éxito
        messagebox.showinfo("Registro exitoso", f"¡Bienvenido {nombre}! Tu cuenta ha sido creada con éxito.")

        # Redirigir a la ventana de login
        self.volver_a_login()

    def crear_widgets(self):
        """Crea y configura todos los widgets de la interfaz."""
        # Título principal
        titulo = tk.Label(self.ventana, text="Crear una cuenta nueva", font=("Arial", 24, "bold"), fg="#FBE4D8", bg="#2B124C")
        titulo.place(x=250, y=20)

        # Botón para iniciar sesión
        btn_iniciar_sesion = tk.Button(
            self.ventana,
            text="¿Ya estás registrado? Inicia sesión aquí.",
            font=("Arial", 10, "underline"),
            fg="blue",
            bg="#2B124C",
            relief="flat",
            cursor="hand2",
            command=self.volver_a_login
        )
        btn_iniciar_sesion.place(x=300, y=70)

        # Campo para el nombre
        label_nombre = tk.Label(self.ventana, text="NOMBRE", font=("Arial", 12, "bold"), fg="#FBE4D8", bg="#2B124C")
        label_nombre.place(x=50, y=115)
        self.entry_nombre = tk.Entry(self.ventana, width=40, font=("Arial", 12), bg="#854F6C", fg="#FBE4D8", insertbackground="#FBE4D8", relief="flat")
        self.entry_nombre.place(x=50, y=150)

        # Campo para el correo electrónico
        label_email = tk.Label(self.ventana, text="EMAIL", font=("Arial", 12, "bold"), fg="#FBE4D8", bg="#2B124C")
        label_email.place(x=50, y=190)
        self.entry_email = tk.Entry(self.ventana, width=40, font=("Arial", 12), bg="#854F6C", fg="#FBE4D8", insertbackground="#FBE4D8", relief="flat")
        self.entry_email.place(x=50, y=220)

        # Campo para la contraseña
        label_password = tk.Label(self.ventana, text="CONTRASEÑA", font=("Arial", 12, "bold"), fg="#FBE4D8", bg="#2B124C")
        label_password.place(x=50, y=265)
        self.entry_password = tk.Entry(self.ventana, width=40, font=("Arial", 12), show="*", bg="#854F6C", fg="#FBE4D8", insertbackground="#FBE4D8", relief="flat")
        self.entry_password.place(x=50, y=295)

        # Campo para confirmar la contraseña
        label_confirm_password = tk.Label(self.ventana, text="CONFIRMAR CONTRASEÑA", font=("Arial", 12, "bold"), fg="#FBE4D8", bg="#2B124C")
        label_confirm_password.place(x=50, y=345)
        self.entry_confirm_password = tk.Entry(self.ventana, width=40, font=("Arial", 12), show="*", bg="#854F6C", fg="#FBE4D8", insertbackground="#FBE4D8", relief="flat")
        self.entry_confirm_password.place(x=50, y=375)

        # Selector de fecha de nacimiento
        label_fecha_nacimiento = tk.Label(self.ventana, text="FECHA DE NACIMIENTO", font=("Arial", 12, "bold"), fg="#FBE4D8", bg="#2B124C")
        label_fecha_nacimiento.place(x=50, y=425)
        self.date_entry = DateEntry(self.ventana, width=20, background="#854F6C", foreground="#FBE4D8", font=("Arial", 12), date_pattern="dd/mm/yyyy")
        self.date_entry.place(x=50, y=455)

        # Etiqueta para cargar imagen de perfil
        profile_icon = tk.Button(self.ventana, text="➕", font=("Arial", 15), command=self.cargar_imagen, bg="#2B124C", fg="#FBE4D8", relief="flat")
        profile_icon.place(x=720, y=130)

        boton_cargar_imagen = tk.Label(self.ventana, text="Agregar una foto de perfil (No es obligatorio)", font=("Arial", 10), bg="#2B124C", fg="#DFB6B2", borderwidth=0, cursor="hand2")
        boton_cargar_imagen.place(x=500, y=380)

        # Botón de registro
        boton_registrar = tk.Button(self.ventana, text="Ingresar", font=("Arial", 12, "bold"), width=15, bg="#522B5B", fg="#FBE4D8", command=self.registrar_usuario)
        boton_registrar.place(x=550, y=420)

    def volver_a_login(self):
        """Cierra la ventana actual y regresa a la ventana de login."""
        self.ventana.destroy()
        from principal import LoginApp  # Importa la clase LoginApp
        root = tk.Tk()
        LoginApp(root)
        root.mainloop()


# Bloque principal
if __name__ == "__main__":
    root = tk.Tk()
    Usuario(root)
    root.mainloop()
