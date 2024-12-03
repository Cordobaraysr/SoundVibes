import os
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import pygame
from mutagen.mp3 import MP3


class News:
    def __init__(self, root):
        self.root = root
        self.root.title("News")
        self.root.geometry("1360x568")
        self.root.configure(bg="#190019")
        
        self.bg_color = "#190019"
        self.frame_color = "#2B124C"
        self.button_color = "#522B5B"
        self.button_border_color = "#4B0082"
        self.text_light = "#FBE4D8"
        self.label_color = "#FFC0CB"
        # Inicializar pygame mixer
        pygame.mixer.init()

        # Variables globales
        self.songs = []
        self.current_song_index = -1
        self.is_playing = False
        self.current_duration = 0

        # Cargar canciones desde la misma carpeta
        self.load_songs()

        # Crear interfaz
        self.create_widgets()

    def create_widgets(self):
        # Marco de navegación
        nav_frame = tk.Frame(self.root, bg="#2B124C")
        nav_frame.place(x=0, y=0, width=150, height=768)

        # Logo en la esquina superior izquierda
        logo_path = "logo1.png"
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
            ("News", lambda: print("Discover clicked")),
            ("System", self.open_System),
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

        # Título de novedades
        novedades_label = tk.Label(
            self.root,
            text="NOVEDADES: ÚLTIMOS LANZAMIENTOS PARA TI",
            font=("Arial", 16, "bold"),
            bg="#190019",
            fg="#FFC0CB",
        )
        novedades_label.place(x=300, y=10)
        
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
                
        # Frame para mostrar archivos de música
        novedades_frame = tk.Frame(self.root, bg="#2B124C")
        novedades_frame.place(x=300, y=50, width=1050, height=300)

        # Imagen dentro del frame
        artist_photo_path = "perfil.png"
        if os.path.exists(artist_photo_path):
            artist_img = Image.open(artist_photo_path).resize((150, 150))
            artist_img = ImageTk.PhotoImage(artist_img)
            artist_label = tk.Label(novedades_frame, image=artist_img, bg="#2B124C")
            artist_label.image = artist_img
            artist_label.place(x=10, y=10)

        # Label y Entry para comentario
        tk.Label(
            novedades_frame,
            text="Escribe un comentario:",
            font=("Arial", 12),
            bg="#2B124C",
            fg="#FBE4D8",
        ).place(x=200, y=10)
        tk.Entry(
            novedades_frame,
            font=("Arial", 12),
            bg="#FBE4D8",
            fg="#190019",
            width=80,
        ).place(x=200, y=50)

        # Lista de canciones en el frame
        self.song_listbox = tk.Listbox(novedades_frame, bg="#522B5B", fg="#FBE4D8", font=("Arial", 12))
        self.song_listbox.place(x=200, y=100, width=800, height=150)

        # Cargar canciones a la lista
        self.update_song_listbox()

        # Evento para reproducir una canción al seleccionarla
        self.song_listbox.bind("<<ListboxSelect>>", self.play_selected_song)

        # Barra de progreso
        self.progress_bar = ttk.Scale(self.root, from_=0, to=100, orient="horizontal", length=1000)
        self.progress_bar.place(x=300, y=370, width=1000, height=20)

        self.elapsed_time_label = tk.Label(self.root, text="0:00", bg="#190019", fg="#FFC0CB", font=("Arial", 10))
        self.elapsed_time_label.place(x=300, y=370, width=50, height=20)

        self.total_time_label = tk.Label(self.root, text="0:00", bg="#190019", fg="#FFC0CB", font=("Arial", 10))
        self.total_time_label.place(x=1250, y=370, width=50, height=20)

        # Barra de volumen
        volume_label = tk.Label(self.root, text="Volume:", bg="#190019", fg="#FFC0CB", font=("Arial", 10))
        volume_label.place(x=300, y=410, width=80, height=30)

        volume_slider = ttk.Scale(self.root, from_=0, to=100, orient="horizontal", length=200, command=self.adjust_volume)
        volume_slider.set(50)
        volume_slider.place(x=380, y=410, width=200, height=30)

        # Controles de reproducción
        self.create_playback_buttons()

    def create_playback_buttons(self):
        tk.Button(self.root, text="<< 10s", bg="#DFB6B2", fg="#190019", command=lambda: self.seek_song_manual(-10)).place(x=300, y=450, width=100, height=40)
        tk.Button(self.root, text="10s >>", bg="#DFB6B2", fg="#190019", command=lambda: self.seek_song_manual(+10)).place(x=410, y=450, width=100, height=40)
        tk.Button(self.root, text="Play", bg="#DFB6B2", fg="#190019", command=self.play_selected_song).place(x=520, y=450, width=100, height=40)
        tk.Button(self.root, text="Pause", bg="#DFB6B2", fg="#190019", command=self.pause_song).place(x=630, y=450, width=100, height=40)
        tk.Button(self.root, text="Stop", bg="#DFB6B2", fg="#190019", command=self.stop_song).place(x=740, y=450, width=100, height=40)
        tk.Button(self.root, text="Next", bg="#DFB6B2", fg="#190019", command=self.play_next_song).place(x=850, y=450, width=100, height=40)
        tk.Button(self.root, text="Previous", bg="#DFB6B2", fg="#190019", command=self.play_previous_song).place(x=960, y=450, width=100, height=40)

    def load_songs(self):
        """Carga todos los archivos MP3 de la misma carpeta."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        for file in os.listdir(current_dir):
            if file.endswith(".mp3"):
                self.songs.append(os.path.join(current_dir, file))

    def update_song_listbox(self):
        """Actualiza la lista de canciones en la interfaz."""
        self.song_listbox.delete(0, tk.END)
        for song in self.songs:
            self.song_listbox.insert(tk.END, os.path.basename(song))

    def play_selected_song(self, event=None):
        """Reproduce una canción seleccionada en la lista."""
        if self.song_listbox.curselection():
            self.current_song_index = self.song_listbox.curselection()[0]
            song_path = self.songs[self.current_song_index]
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            print(f"Reproduciendo: {song_path}")

    def pause_song(self):
        """Pausa la canción."""
        pygame.mixer.music.pause()
        print("Reproducción pausada")

    def stop_song(self):
        """Detiene la reproducción."""
        pygame.mixer.music.stop()
 
    def play_next_song(self):
        if self.current_song_index < len(self.songs) - 1:
            self.current_song_index += 1
            self.play_song_by_index(self.current_song_index)

    def play_previous_song(self):
        if self.current_song_index > 0:
            self.current_song_index -= 1
            self.play_song_by_index(self.current_song_index)        

    def seek_song_manual(self, seconds):
        """Simula un cambio en la posición de la canción."""
        print(f"Seek {seconds} seconds")

    def adjust_volume(self, val):
        """Ajusta el volumen del reproductor."""
        volume = float(val) / 100
        pygame.mixer.music.set_volume(volume)

    def go_back_to_music_player(self):
        """Regresa al reproductor de música."""
        self.root.destroy()
        from interfaz import MusicPlayer
        main_window = tk.Tk()
        MusicPlayer(main_window)
        main_window.mainloop()

    def go_back_to_artist(self):
        """Abre la ventana de Artistas."""
        self.root.destroy()
        from artista import Artistas
        artist_window = tk.Tk()
        Artistas(artist_window)
        artist_window.mainloop()
        
    def open_profile(self):
         """Abre la ventana de Perfil."""
         self.root.destroy()  # Oculta la ventana actual
         from conectar import PerfilApp  # Importa la clase PerfilApp
         profile_window = tk.Tk()
         PerfilApp(profile_window)  # Inicializa la clase con la ventana
         profile_window.mainloop()
         
    def open_library(self):
        """Abre la biblioteca."""
        self.root.destroy()
        from libreria import Biblioteca
        library_window = tk.Tk()
        Biblioteca(library_window)
        library_window.mainloop()
        
    def open_Perfil(self):
         """Abre la ventana de Perfil."""
         self.root.destroy()  # Oculta la ventana actual
         from principal import LoginApp  # Importa la clase PerfilApp
         Perfil_window = tk.Tk()
         LoginApp(Perfil_window)  # Inicializa la clase con la ventana
         Perfil_window.mainloop()
                 
    def open_System(self):
        """Cierra esta ventana y abre la interfaz de Artistas."""
        self.root.destroy()
        from sistema import System 
        new_window = tk.Tk()
        System(new_window)
        new_window.mainloop()

    def open_Albums(self):
        """Cierra esta ventana y abre la interfaz de Artistas."""
        self.root.destroy()
        from albums import MainApp 
        new_window = tk.Tk()
        MainApp(new_window)
        new_window.mainloop()                           

    def browse_file(self):
        """Permite seleccionar un archivo de música."""
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.songs.append(file_path)
            self.update_song_listbox()
            print(f"Archivo seleccionado: {file_path}")


# Bloque principal para pruebas
if __name__ == "__main__":
    root = tk.Tk()
    News(root)
    root.mainloop()
