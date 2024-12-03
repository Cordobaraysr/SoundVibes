import tkinter as tk
import os
from PIL import Image, ImageTk


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Albums")
        self.root.geometry("1360x768")
        self.root.configure(bg="#190019")

        # Colores
        self.bg_color = "#190019"
        self.frame_color = "#2B124C"
        self.button_color = "#522B5B"
        self.button_border_color = "#4B0082"
        self.text_light = "#FBE4D8"
        self.label_color = "#FFC0CB"

        # Marco de navegación
        nav_frame = tk.Frame(self.root, bg=self.bg_color)
        nav_frame.place(x=0, y=0, width=150, height=768)
        
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
        
        logo_path = "logo1.png"
        if os.path.exists(logo_path):
            logo_img = Image.open(logo_path).resize((100, 100))
            logo_img = ImageTk.PhotoImage(logo_img)
            logo_label = tk.Label(nav_frame, image=logo_img, bg=self.bg_color)
            logo_label.image = logo_img
            logo_label.place(x=25, y=10)
        # Botones de navegación
        tk.Button(
            nav_frame,
            text="Library",
            bg=self.frame_color,
            fg=self.text_light,
            font=("Arial", 10),
            highlightbackground=self.button_border_color,
            highlightthickness=2,
            command=self.open_library,
        ).place(x=10, y=120, width=130, height=40)

        tk.Button(
            nav_frame,
            text="Artists",
            bg=self.frame_color,
            fg=self.text_light,
            font=("Arial", 10),
            command=self.open_artists,
        ).place(x=10, y=170, width=130, height=40)

        tk.Button(
            nav_frame,
            text="News",
            bg=self.frame_color,
            fg=self.text_light,
            font=("Arial", 10),
            command=self.open_news,
        ).place(x=10, y=220, width=130, height=40)

        tk.Button(
            nav_frame,
            text="System",
            bg=self.frame_color,
            fg=self.text_light,
            font=("Arial", 10),
            command=self.open_System,
        ).place(x=10, y=270, width=130, height=40)

        buttons = ["Podcast", "Like", "Browse"]
        y_offset = 370
        for btn in buttons:
            tk.Button(
                nav_frame,
                text=btn,
                bg=self.frame_color,
                fg=self.text_light,
                font=("Arial", 10),
                command=lambda name=btn: print(f"{name} clicked")
            ).place(x=10, y=y_offset, width=130, height=40)
            y_offset += 50

        # Campo de búsqueda
        tk.Button(
            self.root,
            text="Search                                                                               🔍",
            bg=self.frame_color,
            fg=self.text_light,
            font=("Arial", 10),
            command=self.open_Search,
        ).place(x=500, y=20, width=410, height=40)

        # Título principal
        title = tk.Label(
            self.root, text="Music Albums", font=("Arial", 25, "bold"),
            bg=self.bg_color, fg=self.text_light
        )
        title.place(x=600, y=60)

        # Frame para los botones de álbumes
        album_frame = tk.Frame(self.root, bg=self.bg_color)
        album_frame.place(x=360, y=100)

        # Álbumes y sus imágenes
        albums = [
            {"name": "Ed Maverick - Eduardo", "image": "album3.jpg", "command": self.open_ed_maverick},
            {"name": "Ariana Grande - Thank U, Next", "image": "album2.jpg", "command": self.open_ariana_grande},
            {"name": "AC/DC - Power Up", "image": "album5.jpg", "command": self.open_acdc},
            {"name": "Nirvana - Nevermind", "image": "album4.jpg", "command": self.open_nirvana},
            {"name": "Pink Floyd - The Dark Side of the Moon", "image": "album1.jpg", "command": self.open_pink_floyd}
        ]

        for i, album in enumerate(albums):
            row = i // 3  # Calcula la fila
            col = i % 3   # Calcula la columna
            frame = tk.Frame(album_frame, bg=self.bg_color)
            frame.grid(row=row, column=col, padx=20, pady=20)

            # Imagen del álbum
            if album["image"]:
                img = Image.open(album["image"]).resize((200, 200))
                album_img = ImageTk.PhotoImage(img)
                img_label = tk.Label(frame, image=album_img, bg=self.bg_color)
                img_label.image = album_img
                img_label.pack()

            # Botón para abrir el álbum
            btn = tk.Button(
                frame, text=album["name"], bg=self.button_color, fg=self.text_light,
                font=("Arial", 12), width=25, command=album["command"]
            )
            btn.pack(pady=10)

    # Funciones de los botones de navegación
    def open_library(self):
        """Cierra esta ventana y abre la interfaz de la biblioteca."""
        self.root.destroy()
        from libreria import Biblioteca
        new_window = tk.Tk()
        Biblioteca(new_window)
        new_window.mainloop()

    def open_profile(self):
         """Abre la ventana de Perfil."""
         self.root.destroy()  # Oculta la ventana actual
         from conectar import PerfilApp  # Importa la clase PerfilApp
         profile_window = tk.Tk()
         PerfilApp(profile_window)  # Inicializa la clase con la ventana
         profile_window.mainloop()
         
    def open_artists(self):
        """Cierra esta ventana y abre la interfaz de Artistas."""
        self.root.destroy()
        from artista import Artistas
        new_window = tk.Tk()
        Artistas(new_window)
        new_window.mainloop()

    def open_news(self):
        """Cierra esta ventana y abre la interfaz de Artistas."""
        self.root.destroy()
        from Novedades import News
        new_window = tk.Tk()
        News(new_window)
        new_window.mainloop()

    def open_System(self):
        """Cierra esta ventana y abre la interfaz de Artistas."""
        self.root.destroy()
        from sistema import System
        new_window = tk.Tk()
        System(new_window)
        new_window.mainloop()

    def open_Search(self):
        """Abre la ventana de búsqueda."""
        self.root.destroy()
        from buscar import FolderExplorer
        new_window = tk.Tk()
        FolderExplorer(new_window)
        new_window.mainloop()

    # Funciones para abrir las ventanas de los álbumes
    def open_ed_maverick(self):
        self.root.destroy()
        from Ed_maverick import EdMaverickApp
        new_window = tk.Tk()
        EdMaverickApp(new_window)
        new_window.mainloop()

    def open_ariana_grande(self):
        self.root.destroy()
        from Ariana import ArianaGrandeApp
        new_window = tk.Tk()
        ArianaGrandeApp(new_window)
        new_window.mainloop()

    def open_acdc(self):
        self.root.destroy()
        from acdc import ACDCApp
        new_window = tk.Tk()
        ACDCApp(new_window)
        new_window.mainloop()

    def open_nirvana(self):
        self.root.destroy()
        from nirvana import NirvanaApp
        new_window = tk.Tk()
        NirvanaApp(new_window)
        new_window.mainloop()

    def open_pink_floyd(self):
        self.root.destroy()
        from Pink_Floyd import PinkFloydApp
        new_window = tk.Tk()
        PinkFloydApp(new_window)
        new_window.mainloop()


# Bloque principal
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
