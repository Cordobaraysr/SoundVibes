import os
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import pygame
from mutagen.mp3 import MP3


class PinkFloydApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pink Floyd - The Dark Side of the Moon")
        self.root.geometry("1360x768")
        self.root.configure(bg="#190019")

        # Inicializar pygame mixer
        pygame.mixer.init()

        # Colores
        self.bg_color = "#190019"
        self.frame_color = "#2B124C"
        self.button_color = "#DFB6B2"
        self.button_border_color = "#4B0082"
        self.text_light = "#FBE4D8"
        self.text_dark = "#522B5B"
        self.label_color = "#FFC0CB"

        # Variables globales
        self.songs = []
        self.current_song_index = -1
        self.is_playing = False
        self.current_duration = 0

        # Crear la interfaz
        self.create_widgets()
        self.load_songs()

    def create_widgets(self):
        # Marco de navegación
        nav_frame = tk.Frame(self.root, bg=self.bg_color)
        nav_frame.place(x=0, y=0, width=150, height=768)

        # Imagen del logo
        logo_path = "logo1.png"  # Cambia la ruta si es necesario
        if os.path.exists(logo_path):
            logo_img = Image.open(logo_path).resize((120, 120))
            logo_img = ImageTk.PhotoImage(logo_img)
            logo_label = tk.Label(self.root, image=logo_img, bg=self.bg_color)
            logo_label.image = logo_img
            logo_label.place(x=10, y=10)

        # Botón Config en la parte superior derecha
        config_button = tk.Button(
            self.root,
            text="Config",
            bg=self.frame_color,
            fg=self.text_light,
            font=("Arial", 12, "bold"),
            highlightbackground=self.button_border_color,
            highlightthickness=2,
            command=self.open_profile  # Método que abre la ventana de Configuración
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
        album1_image_path = "album1.jpg"  # Cambia la ruta si es necesario
        if os.path.exists(album1_image_path):
            album1_img = Image.open(album1_image_path).resize((200, 200))
            album1_img = ImageTk.PhotoImage(album1_img)
            album1_label = tk.Label(self.root, image=album1_img, bg=self.bg_color)
            album1_label.image = album1_img
            album1_label.place(x=180, y=45)     
        # Descripción del álbum y artista
        album_description = (
            "Artista: Pink Floyd\n"
            "Álbum: The Dark Side of the Moon\n"
            "Lanzamiento: 1 de marzo de 1973\n"
            "Género: Rock progresivo, psicodélico\n"
            "Duración: 42:49\n"
            "\n"
            "Uno de los álbumes más icónicos de la historia, incluye temas como "
            "'Money', 'Time' y 'Us and Them'. Es conocido por sus letras profundas "
            "y su innovador diseño sonoro."
        )
        description_label = tk.Label(
            self.root, text=album_description, bg=self.bg_color,
            fg=self.text_light, font=("Arial", 12), justify="left", wraplength=400
        )
        description_label.place(x=400, y=50)

        tk.Button(
            nav_frame,
            text="Back",                                                                           
            bg=self.frame_color,
            fg=self.text_light,
            font=("Arial", 10),
            command=self.open_inicio,  # Llama al método para abrir Artistas
        ).place(x=10, y=145, width=130, height=40)      
        
        # Botones de navegación
        tk.Button(
            nav_frame,
            text="Library",
            bg=self.frame_color,
            fg=self.text_light,
            font=("Arial", 10),
            highlightbackground=self.button_border_color,
            highlightthickness=2,
            command=self.open_library,  # Método que abre la interfaz de biblioteca
        ).place(x=10, y=195, width=130, height=40)

        tk.Button(
            nav_frame,
            text="Artists",
            bg=self.frame_color,
            fg=self.text_light,
            font=("Arial", 10),
            command=self.open_artists,  # Llama al método para abrir Artistas
        ).place(x=10, y=245, width=130, height=40)   

        tk.Button(
            nav_frame,
            text="News",
            bg=self.frame_color,
            fg=self.text_light,
            font=("Arial", 10),
            command=self.open_news,  # Llama al método para abrir Artistas
        ).place(x=10, y=295, width=130, height=40) 
        
        tk.Button(
            nav_frame,
            text="System",
            bg=self.frame_color,
            fg=self.text_light,
            font=("Arial", 10),
            command=self.open_System,  # Llama al método para abrir Artistas
        ).place(x=10, y=345, width=130, height=40)
        
        tk.Button(
            nav_frame,
            text="Albums",
            bg=self.frame_color,
            fg=self.text_light,
            font=("Arial", 10),
            command=self.open_Albums,  # Llama al método para abrir Artistas
        ).place(x=10, y=395, width=130, height=40)
        
        buttons = [ "Browse"]
        y_offset = 445
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

        album1_image_path = "album1.png"  # Cambia la ruta si es necesario
        if os.path.exists(album1_image_path):
            album1_img = Image.open(album1_image_path).resize((200, 200))
            album1_img = ImageTk.PhotoImage(album1_img)
            album1_label = tk.Label(self.root, image=album1_img, bg=self.bg_color)
            album1_label.image = album1_img
            album1_label.place(x=180, y=45)    
        # Lista de canciones
        frame_songs = tk.Frame(self.root, bg=self.frame_color)
        frame_songs.place(x=180, y=250, width=1000, height=300)

        self.listbox_songs = tk.Listbox(frame_songs, bg=self.frame_color, fg=self.text_light, font=("Arial", 10))
        self.listbox_songs.place(x=10, y=10, width=975, height=250)

        # Controles de reproducción
        self.create_controls()

    def create_controls(self):
        # Barra de progreso
        self.progress_bar = ttk.Scale(self.root, from_=0, to=100, orient="horizontal", length=1000)
        self.progress_bar.place(x=160, y=580, width=1000, height=20)
        self.progress_bar.bind("<Button-1>", self.seek_song)

        self.elapsed_time_label = tk.Label(self.root, text="0:00", bg=self.bg_color, fg=self.label_color, font=("Arial", 10))
        self.elapsed_time_label.place(x=160, y=580, width=50, height=20)

        self.total_time_label = tk.Label(self.root, text="0:00", bg=self.bg_color, fg=self.label_color, font=("Arial", 10))
        self.total_time_label.place(x=1165, y=580, width=50, height=20)

        self.song_label = tk.Label(self.root, text="No Song Playing", bg=self.bg_color, fg=self.label_color, font=("Arial", 12))
        self.song_label.place(x=160, y=610, width=1000, height=30)

        # Controles de volumen
        volume_label = tk.Label(self.root, text="Volume:", bg=self.bg_color, fg=self.label_color, font=("Arial", 10))
        volume_label.place(x=160, y=660, width=80, height=30)

        volume_slider = ttk.Scale(self.root, from_=0, to=100, orient="horizontal", length=200, command=self.adjust_volume)
        volume_slider.set(50)
        volume_slider.place(x=250, y=660, width=200, height=30)

        # Botones de reproducción
        self.create_playback_buttons()

    def create_playback_buttons(self):
        tk.Button(self.root, text="<< 10s", bg=self.button_color, fg=self.text_dark, command=lambda: self.seek_song_manual(-10)).place(x=20, y=660, width=100, height=40)
        tk.Button(self.root, text="10s >>", bg=self.button_color, fg=self.text_dark, command=lambda: self.seek_song_manual(+10)).place(x=130, y=660, width=100, height=40)
        tk.Button(self.root, text="Play", bg=self.button_color, fg=self.text_dark, command=self.play_selected_song).place(x=580, y=660, width=100, height=40)
        tk.Button(self.root, text="Pause", bg=self.button_color, fg=self.text_dark, command=self.pause_song).place(x=690, y=660, width=100, height=40)
        tk.Button(self.root, text="Stop", bg=self.button_color, fg=self.text_dark, command=self.stop_song).place(x=800, y=660, width=100, height=40)
        tk.Button(self.root, text="Next", bg=self.button_color, fg=self.text_dark, command=self.play_next_song).place(x=910, y=660, width=100, height=40)
        tk.Button(self.root, text="Previous", bg=self.button_color, fg=self.text_dark, command=self.play_previous_song).place(x=470, y=660, width=100, height=40)
   
    def open_inicio(self): 
         """Abre la ventana de Perfil."""
         self.root.destroy()  # Oculta la ventana actual
         from interfaz import MusicPlayer  # Importa la clase Perfil desde el archivo correspondiente
         search_window = tk.Tk()  # Crea una nueva ventana secundaria
         MusicPlayer(search_window)  # Inicializa la clase Perfil con la nueva ventana
         search_window.mainloop()   
         
    # Métodos para botones y reproducción se mantienen iguales
    def open_Search(self): 
         """Abre la ventana de Perfil."""
         self.root.destroy()  # Oculta la ventana actual
         from buscar import FolderExplorer  # Importa la clase Perfil desde el archivo correspondiente
         search_window = tk.Tk()  # Crea una nueva ventana secundaria
         FolderExplorer(search_window)  # Inicializa la clase Perfil con la nueva ventana
         search_window.mainloop()        
        
    def open_profile(self):
         """Abre la ventana de Perfil."""
         self.root.destroy()  # Oculta la ventana actual
         from conectar import PerfilApp  # Importa la clase PerfilApp
         profile_window = tk.Tk()
         PerfilApp(profile_window)  # Inicializa la clase con la ventana
         profile_window.mainloop()
         
    def open_library(self):
        """Cierra esta ventana y abre la interfaz de la biblioteca."""
        self.root.destroy()  # Cierra la ventana actual
        from libreria import Biblioteca
        new_window = tk.Tk()  # Crear una nueva ventana
        Biblioteca(new_window)  # Inicializar la interfaz de Biblioteca
        new_window.mainloop()                  

    def open_artists(self):
        """Cierra esta ventana y abre la interfaz de Artistas."""
        self.root.destroy()
        from artista import Artistas  # Importación diferida
        new_window = tk.Tk()
        Artistas(new_window)
        new_window.mainloop()
        
    def open_news(self):
        """Cierra esta ventana y abre la interfaz de Artistas."""
        self.root.destroy()
        from Novedades import News  # Importación diferida
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
    def open_Perfil(self):
         """Abre la ventana de Perfil."""
         self.root.destroy()  # Oculta la ventana actual
         from principal import LoginApp  # Importa la clase PerfilApp
         Perfil_window = tk.Tk()
         LoginApp(Perfil_window)  # Inicializa la clase con la ventana
         Perfil_window.mainloop()        
    def open_Albums(self):
        """Cierra esta ventana y abre la interfaz de Artistas."""
        self.root.destroy()
        from albums import MainApp 
        new_window = tk.Tk()
        MainApp(new_window)
        new_window.mainloop()
                
    def load_songs(self):
        """Carga las canciones del álbum 'The Dark Side of the Moon'."""
        self.songs = [
            "Speak to Me.mp3",
            "Breathe.mp3",
            "On the Run.mp3",
            "Time.mp3",
            "The Great Gig in the Sky.mp3",
            "Money.mp3",
            "Us and Them.mp3",
            "Any Colour You Like.mp3",
            "Brain Damage.mp3",
            "Eclipse.mp3"
        ]
        for song in self.songs:
            self.listbox_songs.insert("end", song)

    def play_selected_song(self):
        if self.listbox_songs.curselection():
            self.current_song_index = self.listbox_songs.curselection()[0]
            self.play_song_by_index(self.current_song_index)

    def play_song_by_index(self, index):
        try:
            pygame.mixer.music.stop()
            song = self.songs[index]
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            self.is_playing = True
            self.current_duration = self.get_song_duration(song)
            self.progress_bar.config(to=self.current_duration)
            self.total_time_label.config(text=f"{self.current_duration // 60}:{self.current_duration % 60:02d}")
            self.update_progress_bar()
            self.song_label.config(text=f"Playing: {os.path.basename(song)}")
        except Exception as e:
            self.song_label.config(text=f"Error: {e}")

    def get_song_duration(self, file_path):
        try:
            audio = MP3(file_path)
            return int(audio.info.length)
        except Exception as e:
            print(f"Error getting duration: {e}")
            return 0

    def update_progress_bar(self):
        if self.is_playing:
            current_time = pygame.mixer.music.get_pos() // 1000
            self.progress_bar.set(current_time)
            self.elapsed_time_label.config(text=f"{current_time // 60}:{current_time % 60:02d}")
            if current_time < self.current_duration:
                self.root.after(1000, self.update_progress_bar)

    def seek_song_manual(self, seconds):
        if self.is_playing:
            current_time = pygame.mixer.music.get_pos() // 1000
            new_time = max(0, min(current_time + seconds, self.current_duration))
            pygame.mixer.music.set_pos(new_time)
            self.progress_bar.set(new_time)
            self.elapsed_time_label.config(text=f"{new_time // 60}:{new_time % 60:02d}")

    def seek_song(self, event):
        if self.is_playing:
            new_time = int(self.progress_bar["to"] * event.x / self.progress_bar.winfo_width())
            pygame.mixer.music.set_pos(new_time)
            self.progress_bar.set(new_time)
            self.elapsed_time_label.config(text=f"{new_time // 60}:{new_time % 60:02d}")

    def pause_song(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False

    def resume_song(self):
        if not self.is_playing:
            pygame.mixer.music.unpause()
            self.is_playing = True

    def stop_song(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.song_label.config(text="Music Stopped")
        self.progress_bar.set(0)

    def play_next_song(self):
        if self.current_song_index < len(self.songs) - 1:
            self.current_song_index += 1
            self.play_song_by_index(self.current_song_index)

    def play_previous_song(self):
        if self.current_song_index > 0:
            self.current_song_index -= 1
            self.play_song_by_index(self.current_song_index)

    def adjust_volume(self, val):
        volume = float(val) / 100
        pygame.mixer.music.set_volume(volume)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.songs.append(file_path)
            self.listbox_songs.insert("end", os.path.basename(file_path))
            


# Bloque principal
if __name__ == "__main__":
    root = tk.Tk()
    app = PinkFloydApp(root)
    root.mainloop()
