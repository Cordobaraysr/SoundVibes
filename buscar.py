import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import pygame
from mutagen.mp3 import MP3


class FolderExplorer:
    def __init__(self, root):
        self.root = root
        self.root.title("Folder Explorer")
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

        # Variables
        self.songs = []
        self.current_song_index = -1
        self.is_playing = False
        self.current_duration = 0

        # Crear la interfaz
        self.create_widgets()

        # Detectar y listar carpetas al iniciar
        self.list_folders()

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
            ("Home", self.go_back_to_music_player),
            ("Library", self.open_library),
            ("Artist", self.open_artist),
            ("News", self.open_news ),
            ("System", self.open_System),
            ("Albums", self.open_Albums),
            ("Browse", lambda: print("Like clicked")),
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

        # Campo de búsqueda
        search_label = tk.Label(self.root, text="Busca una carpeta:", font=("Arial", 16), bg="#190019", fg="#FFC0CB")
        search_label.place(x=200, y=20)

        self.search_var = tk.StringVar()
        search_entry = tk.Entry(self.root, textvariable=self.search_var, font=("Arial", 14), width=60)
        search_entry.place(x=400, y=20)

        search_button = tk.Button(
            self.root,
            text="Buscar",
            font=("Arial", 14),
            bg="#DFB6B2",
            fg="#190019",
            command=self.perform_search,
        )
        search_button.place(x=900, y=15, width=100, height=40)

        # Frame para carpetas
        folders_frame = tk.Frame(self.root, bg="#2B124C")
        folders_frame.place(x=200, y=100, width=450, height=300)

        folders_label = tk.Label(
            folders_frame, text="Carpetas detectadas:", font=("Arial", 14), bg="#2B124C", fg="#FBE4D8"
        )
        folders_label.place(x=10, y=10)

        self.folders_listbox = tk.Listbox(folders_frame, bg="#522B5B", fg="#FBE4D8", font=("Arial", 12))
        self.folders_listbox.place(x=10, y=50, width=430, height=220)

        self.folders_listbox.bind("<<ListboxSelect>>", self.open_folder)

        # Frame para archivos
        files_frame = tk.Frame(self.root, bg="#2B124C")
        files_frame.place(x=700, y=100, width=500, height=300)

        files_label = tk.Label(
            files_frame, text="Archivos en carpeta:", font=("Arial", 14), bg="#2B124C", fg="#FBE4D8"
        )
        files_label.place(x=10, y=10)

        self.files_listbox = tk.Listbox(files_frame, bg="#522B5B", fg="#FBE4D8", font=("Arial", 12))
        self.files_listbox.place(x=10, y=50, width=480, height=220)

        self.files_listbox.bind("<<ListboxSelect>>", self.play_selected_file)

        # Controles de reproducción
        self.create_playback_controls()

        # Barra de progreso
        self.progress_bar = ttk.Scale(self.root, from_=0, to=100, orient="horizontal", length=1000, command=self.seek_song)
        self.progress_bar.place(x=200, y=420, width=1000, height=20)

        self.elapsed_time_label = tk.Label(self.root, text="0:00", bg="#190019", fg="#FFC0CB", font=("Arial", 10))
        self.elapsed_time_label.place(x=200, y=420, width=50, height=20)

        self.total_time_label = tk.Label(self.root, text="0:00", bg="#190019", fg="#FFC0CB", font=("Arial", 10))
        self.total_time_label.place(x=1150, y=420, width=50, height=20)

        # Controles de volumen
        volume_label = tk.Label(self.root, text="Volume:", bg="#190019", fg="#FFC0CB", font=("Arial", 10))
        volume_label.place(x=200, y=460, width=80, height=30)

        self.volume_slider = ttk.Scale(self.root, from_=0, to=100, orient="horizontal", length=200, command=self.adjust_volume)
        self.volume_slider.set(50)
        self.volume_slider.place(x=280, y=460, width=200, height=30)
        
    def create_playback_controls(self):
        tk.Button(self.root, text="<< 10s", bg=self.button_color, fg=self.text_dark, command=lambda: self.seek_song_manual(-10)).place(x=20, y=660, width=100, height=40)
        tk.Button(self.root, text="10s >>", bg=self.button_color, fg=self.text_dark, command=lambda: self.seek_song_manual(+10)).place(x=130, y=660, width=100, height=40)
        tk.Button(self.root, text="Play", bg=self.button_color, fg=self.text_dark, command=self.play_selected_song).place(x=580, y=660, width=100, height=40)
        tk.Button(self.root, text="Pause", bg=self.button_color, fg=self.text_dark, command=self.pause_song).place(x=690, y=660, width=100, height=40)
        tk.Button(self.root, text="Stop", bg=self.button_color, fg=self.text_dark, command=self.stop_song).place(x=800, y=660, width=100, height=40)
        tk.Button(self.root, text="Next", bg=self.button_color, fg=self.text_dark, command=self.play_next_song).place(x=910, y=660, width=100, height=40)
        tk.Button(self.root, text="Previous", bg=self.button_color, fg=self.text_dark, command=self.play_previous_song).place(x=470, y=660, width=100, height=40)

    def update_progress_bar(self):
        """Actualiza la barra de progreso cada segundo."""
        if self.is_playing:
            current_time = pygame.mixer.music.get_pos() // 1000
            self.progress_bar.set(current_time)
            self.elapsed_time_label.config(text=f"{current_time // 60}:{current_time % 60:02d}")
            if current_time < self.current_duration:
                self.root.after(1000, self.update_progress_bar)     
                
    def adjust_volume(self, val):
        """Ajusta el volumen de la reproducción."""
        volume = float(val) / 100
        pygame.mixer.music.set_volume(volume)                   

    def list_folders(self):
        """Lista todas las carpetas en el directorio actual."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        folders = [f for f in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, f))]

        self.folders_listbox.delete(0, tk.END)
        if folders:
            for folder in folders:
                self.folders_listbox.insert(tk.END, folder)
        else:
            self.folders_listbox.insert(tk.END, "No se encontraron carpetas.")

    def perform_search(self):
        """Filtra las carpetas por el término de búsqueda."""
        search_term = self.search_var.get().lower()
        self.folders_listbox.delete(0, tk.END)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        folders = [f for f in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, f))]

        results = [folder for folder in folders if search_term in folder.lower()]
        if results:
            for folder in results:
                self.folders_listbox.insert(tk.END, folder)
        else:
            self.folders_listbox.insert(tk.END, "No se encontraron carpetas.")

    def open_folder(self, event):
        """Lista los archivos de una carpeta seleccionada en la aplicación."""
        selected_index = self.folders_listbox.curselection()
        if selected_index:
            folder_name = self.folders_listbox.get(selected_index)
            current_dir = os.path.dirname(os.path.abspath(__file__))
            folder_path = os.path.join(current_dir, folder_name)

            if os.path.exists(folder_path):
                self.files_listbox.delete(0, tk.END)
                files = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]

                if files:
                    for file in files:
                        self.files_listbox.insert(tk.END, os.path.join(folder_path, file))
                else:
                    self.files_listbox.insert(tk.END, "No hay archivos .mp3 en esta carpeta.")
            else:
                messagebox.showerror("Error", "La carpeta seleccionada no existe.")

    def play_selected_file(self,event=None):
        """Reproduce el archivo seleccionado en la lista."""
        selected_index = self.files_listbox.curselection()
        if selected_index:
             self.current_song_index = selected_index[0]
             file_path = self.files_listbox.get(selected_index)
             
             if os.path.exists(file_path):
                 
                try:
                    pygame.mixer.music.load(file_path)
                    pygame.mixer.music.play()
                    self.is_playing = True

                    # Obtener la duración de la canción
                    self.current_duration = self.get_song_duration(file_path)
                    self.progress_bar.config(to=self.current_duration)
                    self.total_time_label.config(
                        text=f"{self.current_duration // 60}:{self.current_duration % 60:02d}"
                    )

                    # Actualizar la barra de progreso
                    self.update_progress_bar()
                    print(f"Reproduciendo: {file_path}")
                except Exception as e:
                    print(f"Error al reproducir el archivo: {e}")
        else:
            messagebox.showerror("Error", "El archivo seleccionado no existe.")
            
    def go_back_to_music_player(self):
        self.root.destroy()
        from interfaz import MusicPlayer
        new_window = tk.Tk()
        MusicPlayer(new_window)
        new_window.mainloop()       
    
    def open_library(self):
        """Abre la biblioteca."""
        self.root.destroy()
        from libreria import Biblioteca
        library_window = tk.Tk()
        Biblioteca(library_window)
        library_window.mainloop()     
     
    def open_artist(self):
        """Abre la ventana de Artistas."""
        self.root.destroy()
        from artista import Artistas
        artist_window = tk.Tk()
        Artistas(artist_window)
        artist_window.mainloop()   
        
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
                                    
    def open_news(self):
        """Abre la ventana de Novedades."""
        self.root.destroy()
        from Novedades import News
        news_window = tk.Tk()
        News(news_window)
        news_window.mainloop()

    # Métodos de reproducción de audio

    def play_selected_song(self):
        """Reproduce la canción seleccionada."""
        if self.songs:
        # Obtener la canción seleccionada en la lista
            self.current_song_index = self.songs_listbox.curselection()[0]
            song_path = self.songs[self.current_song_index]

            try:
                pygame.mixer.music.load(song_path)
                pygame.mixer.music.play()
                self.is_playing = True
    
                # Obtener la duración de la canción
                self.current_duration = self.get_song_duration(song_path)
                self.progress_bar.config(to=self.current_duration)
                self.total_time_label.config(
                    text=f"{self.current_duration // 60}:{self.current_duration % 60:02d}"
                )

                print(f"Reproduciendo: {song_path}")
            except Exception as e:
                print(f"Error al reproducir la canción: {e}")

    def pause_song(self):
        """Pausa la canción."""
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            print("Canción pausada.")

    def resume_song(self):
        """Reanuda la reproducción de la canción."""
        if not self.is_playing:
            pygame.mixer.music.unpause()
            self.is_playing = True
            self.update_progress_bar()
            print("Reproducción reanudada.")

    def stop_song(self):
        """Detiene la reproducción."""
        pygame.mixer.music.stop()
        self.is_playing = False
        self.progress_bar.set(0)
        self.elapsed_time_label.config(text="0:00")
        print("Reproducción detenida.")

    def play_next_song(self):
        """Reproduce la siguiente canción."""
        if self.current_song_index < len(self.songs) - 1:
            self.current_song_index += 1
            self.files_listbox.select_set(self.current_song_index)
            self.play_selected_file()
            print("Siguiente canción.")

    def play_previous_song(self):
        """Reproduce la canción anterior."""
        if self.current_song_index > 0:
            self.current_song_index -= 1
            self.files_listbox.select_set(self.current_song_index)
            print("Canción anterior.")
            
    def seek_song_manual(self, seconds):
        if self.is_playing:
            current_time = pygame.mixer.music.get_pos() // 1000
            new_time = max(0, min(current_time + seconds, self.current_duration))
            pygame.mixer.music.set_pos(new_time)
            self.progress_bar.set(new_time)
            self.elapsed_time_label.config(text=f"{new_time // 60}:{new_time % 60:02d}")
            print(f"Posición ajustada a: {new_time} segundos.")       
            

    def seek_song(self, event):
        if self.is_playing:
            new_time = int(self.progress_bar["to"] * event.x / self.progress_bar.winfo_width())
            pygame.mixer.music.set_pos(new_time)
            self.progress_bar.set(new_time)
            self.elapsed_time_label.config(text=f"{new_time // 60}:{new_time % 60:02d}")
    def update_progress_bar(self):
        """Actualiza la barra de progreso cada segundo."""
        if self.is_playing:
            current_time = pygame.mixer.music.get_pos() // 1000
            self.progress_bar.set(current_time)
            self.elapsed_time_label.config(text=f"{current_time // 60}:{current_time % 60:02d}")
            if current_time < self.current_duration:
                self.root.after(1000, self.update_progress_bar)        

    def adjust_volume(self, val):
        """Ajusta el volumen de la reproducción."""
        volume = float(val) / 100
        pygame.mixer.music.set_volume(volume)
        print(f"Volumen ajustado a: {volume * 100}%")

    def get_song_duration(self, file_path):
        """Obtiene la duración de una canción en segundos."""
        try:
            audio = MP3(file_path)
            return int(audio.info.length)
        except Exception as e:
            print(f"Error al obtener la duración de la canción: {e}")
            return 0



# Bloque principal para pruebas
if __name__ == "__main__":
    root = tk.Tk()
    FolderExplorer(root)
    root.mainloop()

