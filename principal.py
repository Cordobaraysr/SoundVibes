import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("USER LOGIN")
        self.root.geometry("600x400")
        self.root.configure(bg="#2B124C")

        # Imagen
        imagen = Image.open("chica.png").resize((330, 238))
        self.foto = ImageTk.PhotoImage(imagen)
        label_imagen = tk.Label(root, image=self.foto, bg="#2B124C")
        label_imagen.place(x=10, y=80)

        # Ícono de perfil
        profile_icon = tk.Label(root, text="👤", font=("Arial", 48), bg="#2B124C", fg="white")
        profile_icon.place(x=425, y=30)

        # Título
        titulo = tk.Label(root, text="USER LOGIN", font=("Arial", 18, "bold"), fg="#FBE4D8", bg="#2B124C")
        titulo.place(x=230, y=20)

        # Campo de correo
        label_correo = tk.Label(root, text="Correo Electrónico:", font=("Arial", 12), fg="#DFB6B2", bg="#2B124C")
        label_correo.place(x=350, y=125)
        email_icon = tk.Label(root, text="✉️", font=("Arial", 18), bg="#2B124C", fg="white")
        email_icon.place(x=350, y=146)
        self.entry_correo = tk.Entry(root, width=20, font=("Arial", 12), bg="#522B5B", fg="#FBE4D8", borderwidth=0,
                                     highlightthickness=1, highlightbackground="#522B5B")
        self.entry_correo.place(x=380, y=150)

        # Campo de contraseña
        label_contraseña = tk.Label(root, text="Contraseña:", font=("Arial", 12), fg="#DFB6B2", bg="#2B124C")
        label_contraseña.place(x=353, y=200)
        password_icon = tk.Label(root, text="🔒", font=("Arial", 15), bg="#2B124C", fg="white")
        password_icon.place(x=353, y=223)
        self.entry_contraseña = tk.Entry(root, width=20, font=("Arial", 12), bg="#522B5B", fg="#FBE4D8", show="*", 
                                         borderwidth=0, highlightthickness=1, highlightbackground="#522B5B")
        self.entry_contraseña.place(x=380, y=230)

        # Botón de login
        boton_login = tk.Button(root, text="LOGIN", font=("Arial", 15), command=self.login, bg="#522B5B", fg="#FBE4D8")
        boton_login.place(x=420, y=275)

        # Botón de registro
        boton_registro = tk.Button(root, text="¿No tienes cuenta? Regístrate", font=("Arial", 10, "underline"), 
                                   fg="blue", bg="#2B124C", relief="flat", cursor="hand2", command=self.crear_cuenta)
        boton_registro.place(x=365, y=330)

    def login(self):
        correo = self.entry_correo.get()
        contraseña = self.entry_contraseña.get()

        # Validaciones
        if "@" not in correo:
            messagebox.showerror("Error", "El correo electrónico debe contener '@'")
        elif not correo or not contraseña:
            messagebox.showwarning("Login", "Por favor, ingresa tus datos")
        else:
            messagebox.showinfo("Login", f"Bienvenido, {correo}")
            self.abrir_reproductor()

    def crear_cuenta(self):
        # Cierra la ventana actual y abre la ventana de registro
        self.root.destroy()
        from crear import Usuario  # Importa la clase Usuario desde crear.py
        nueva_ventana = tk.Tk()
        Usuario(nueva_ventana)
        nueva_ventana.mainloop()

    def abrir_reproductor(self):
        # Cierra la ventana actual y abre el reproductor de música
        self.root.destroy()
        from interfaz import MusicPlayer  # Importa la clase MusicPlayer desde interfaz.py
        nueva_ventana = tk.Tk()
        MusicPlayer(nueva_ventana)
        nueva_ventana.mainloop()


# Bloque principal
if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
