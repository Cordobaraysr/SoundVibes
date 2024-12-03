import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


class System:
    def __init__(self, root):
        self.root = root
        self.root.title("System")
        self.root.geometry("1360x768")
        self.root.configure(bg="#190019")
        # Colores
        self.bg_color = "#190019"
        self.frame_color = "#2B124C"
        self.button_color = "#522B5B"
        self.button_border_color = "#4B0082"
        self.text_light = "#FBE4D8"
        self.label_color = "#FFC0CB"
        
        # Crear la interfaz
        self.create_widgets()

    def create_widgets(self):
        # Marco de navegación
        nav_frame = tk.Frame(self.root, bg="#2B124C")
        nav_frame.place(x=0, y=0, width=150, height=768)

        # Logo en la esquina superior izquierda
        logo_path = "logo.Jpg"
        if os.path.exists(logo_path):
            logo_img = Image.open(logo_path).resize((100, 100))
            logo_img = ImageTk.PhotoImage(logo_img)
            logo_label = tk.Label(nav_frame, image=logo_img, bg="#2B124C")
            logo_label.image = logo_img
            logo_label.place(x=25, y=10)

        # Botones de navegación
        buttons = [
            ("Back", self.go_back_to_music_player),
            ("Library", self.open_library),
            ("Artist", self.go_back_to_artist),
            ("News", self.open_news),  # Nuevo botón para abrir News
            ("System", lambda: print("Songs clicked")),            
            ("Albums", self.open_Albums),
            ("Browse", self.browse_file),
        ]

        y_offset = 120
        for text, command in buttons:
            tk.Button(
                nav_frame,
                text=text,
                bg="#522B5B",
                fg="#FBE4D8",
                font=("Arial", 10),
                highlightbackground="#4B0082",
                highlightthickness=2,
                command=command,
            ).place(x=10, y=y_offset, width=130, height=40)
            y_offset += 50

        # Frame central para botones
        center_frame = tk.Frame(self.root, bg="#2B124C")
        center_frame.place(x=450, y=150, width=560, height=400)

        # Botones centrales en disposición vertical
        center_buttons = [
            ("Screen", lambda: messagebox.showinfo("Información", "1360x768")),
            ("Audio", lambda: messagebox.showinfo("Información", "Audio 50%")),
            ("News", lambda: messagebox.showinfo("Información", "Nothing New ")),
            ("Location", lambda: messagebox.showinfo("Información", "CBTIS 260")),
            ("Drogas", lambda: messagebox.showinfo("Información", "\n LAS DROGAS DESTRUYEN, PERO LA MUSICA SANA ELIGE CANCIONES QUE INSPIREN Y TE LLENEN DE VIDA, EN LUGAR DE CAMINOS QUE ALEGEN TUS SUEÑOS")),
        ]

        button_y = 30
        for text, command in center_buttons:
            tk.Button(
                center_frame,
                text=text,
                bg="#522B5B",
                fg="#FBE4D8",
                font=("Arial", 14),
                width=20,
                height=2,
                command=command,
            ).place(x=170, y=button_y)
            button_y += 70
        title = tk.Label(
            self.root, text="System ", font=("Arial", 25, "bold"),
            bg=self.bg_color, fg=self.text_light
        )
        title.place(x=660, y=60)
        config_button = tk.Button(
            self.root,
            text="Config",
            bg=self.frame_color,
            fg=self.text_light,
            font=("Arial", 12, "bold"),
            highlightbackground=self.button_border_color,
            highlightthickness=2,
            command=self.open_profile  # Método que abre la ventana de Perfil
        )
        config_button.place(x=1250, y=10, width=100, height=40)             
        
        title.place(x=660, y=60)
        config_button = tk.Button(
            self.root,
            text="Cerrar Sesion",
            bg=self.frame_color,
            fg=self.text_light,
            font=("Arial", 12, "bold"),
            highlightbackground=self.button_border_color,
            highlightthickness=2,
            command=self.open_Perfil  # Método que abre la ventana de Perfil
        )
        config_button.place(x=1100, y=10, width=100, height=40)  

        
        # Imagen de perfil a la derecha
        profile_photo_path = "logo.jpg"
        if os.path.exists(profile_photo_path):
            profile_img = Image.open(profile_photo_path).resize((150, 150))
            profile_img = ImageTk.PhotoImage(profile_img)
            profile_label = tk.Label(self.root, image=profile_img, bg="#190019")
            profile_label.image = profile_img
            profile_label.place(x=1150, y=70)

        profile1_photo_path = "dgeti.png"
        if os.path.exists(profile1_photo_path):
            profile1_img = Image.open(profile1_photo_path).resize((150, 150))
            profile1_img = ImageTk.PhotoImage(profile1_img)
            profile1_label = tk.Label(self.root, image=profile1_img, bg="#190019")
            profile1_label.image = profile1_img
            profile1_label.place(x=175, y=50)
            
        profile2_photo_path = "cbtis.png"
        if os.path.exists(profile2_photo_path):
            profile2_img = Image.open(profile2_photo_path).resize((150, 150))
            profile2_img = ImageTk.PhotoImage(profile2_img)
            profile2_label = tk.Label(self.root, image=profile2_img, bg="#190019")
            profile2_label.image = profile2_img
            profile2_label.place(x=175, y=300)
                        
    def go_back_to_music_player(self):
        """Regresa al reproductor de música."""
        self.root.destroy()
        from interfaz import MusicPlayer
        main_window = tk.Tk()
        MusicPlayer(main_window)
        main_window.mainloop()

    def open_library(self):
        """Abre la biblioteca."""
        self.root.destroy()
        from libreria import Biblioteca
        library_window = tk.Tk()
        Biblioteca(library_window)
        library_window.mainloop()
    def open_profile(self):
         """Abre la ventana de Perfil."""
         self.root.destroy()  # Oculta la ventana actual
         from conectar import PerfilApp  # Importa la clase PerfilApp
         profile_window = tk.Tk()
         PerfilApp(profile_window)  # Inicializa la clase con la ventana
         profile_window.mainloop()
         
    def go_back_to_artist(self):
        """Abre la ventana de Artistas."""
        self.root.destroy()
        from artista import Artistas
        artist_window = tk.Tk()
        Artistas(artist_window)
        artist_window.mainloop()

    def open_news(self):
        """Abre la ventana de Novedades (News)."""
        self.root.destroy()
        from Novedades import News
        news_window = tk.Tk()
        News(news_window)
        news_window.mainloop()

    def open_Albums(self):
        """Cierra esta ventana y abre la interfaz de Artistas."""
        self.root.destroy()
        from albums import MainApp 
        new_window = tk.Tk()
        MainApp(new_window)
        new_window.mainloop()
        
    def open_Perfil(self):
         """Abre la ventana de Perfil."""
         self.root.destroy()  # Oculta la ventana actual
         from principal import LoginApp  # Importa la clase PerfilApp
         Perfil_window = tk.Tk()
         LoginApp(Perfil_window)  # Inicializa la clase con la ventana
         Perfil_window.mainloop()
                 
    def browse_file(self):
        """Permite seleccionar un archivo de música."""
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            print(f"Archivo seleccionado: {file_path}")


# Bloque principal para pruebas
if __name__ == "__main__":
    root = tk.Tk()
    System(root)
    root.mainloop()
