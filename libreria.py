import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from tkinter import *
import pygame
from tkinter import ttk
from PIL import Image, ImageTk  # Necesario para trabajar con imágenes


# Inicializar pygame para el manejo de audio
pygame.mixer.init()

# Lista de canciones (puedes agregar más canciones aquí)
songs = [

]

# Playlist
playlists = {}  # Las playlists serán un diccionario vacío inicialmente
liked_songs = []  # Lista de "Me gusta"
favorite_artists = []  # Lista de artistas favoritos

# Definir los colores
BACKGROUND_COLOR = "#190019"
SIDEBAR_COLOR = "#2B124C"
BUTTON_COLOR = "#522B5B"
BUTTON_HOVER_COLOR = "#854F6C"
LABEL_COLOR = "#DFB6B2"
PROGRESSBAR_COLOR = "#FBE4D8"

class Biblioteca:
    def __init__(self, root):  # Constructor correctamente definido
        self.root = root
        self.root.title("Mi Biblioteca Musical")
        self.root.geometry("1040x550")
        self.root.config(bg=BACKGROUND_COLOR)  # Fondo oscuro

        # Crear el panel lateral
        self.sidebar = tk.Frame(self.root, bg=SIDEBAR_COLOR, width=200, height=700, relief="sunken")
        self.sidebar.grid(row=0, column=0, rowspan=2, sticky="nsew")

        # Llamada al método que carga la imagen
        self.load_sidebar_image("logo.jpg")  # Ruta de la imagen que deseas mostrar

        # Título "Tu Biblioteca" en el panel lateral
        self.title_label_sidebar = tk.Label(self.sidebar, text="Tu Biblioteca", font=("Helvetica", 24), fg=LABEL_COLOR, bg=SIDEBAR_COLOR)
        self.title_label_sidebar.pack(pady=20)
        
        self.return_button = tk.Button(
            self.sidebar,
            text="Volver",
            width=20,
            height=2,
            bg=BUTTON_COLOR,
            fg="white",
            font=("Helvetica", 12),
            command=self.go_back_to_music_player,
        )
        self.return_button.pack(pady=10)
        
        # Botones del panel lateral
        self.create_playlist_button = tk.Button(self.sidebar, text="Crear Playlist", width=20, height=2, bg=BUTTON_COLOR, fg="white", font=("Helvetica", 12), command=self.create_playlist)
        self.create_playlist_button.pack(pady=10)

        self.tus_me_gusta_button = tk.Button(self.sidebar, text="Tus Me Gusta", width=20, height=2, bg=BUTTON_COLOR, fg="white", font=("Helvetica", 12), command=self.show_liked_songs)
        self.tus_me_gusta_button.pack(pady=10)

        self.artists_button = tk.Button(self.sidebar, text="Artistas", width=20, height=2, bg=BUTTON_COLOR, fg="white", font=("Helvetica", 12), command=self.show_artists)
        self.artists_button.pack(pady=10)

        self.playlists_frame = tk.Frame(self.sidebar, bg=SIDEBAR_COLOR)  # Contenedor para las playlists
        self.playlists_frame.pack(pady=10)

        # Crear el área principal para las canciones
        self.main_area = tk.Frame(self.root, bg=BACKGROUND_COLOR, width=600, height=500)
        self.main_area.grid(row=0, column=1, sticky="nsew")

        # Lista de canciones
        self.song_listbox = tk.Listbox(self.main_area, width=50, height=15, bg="#9b59b6", fg="white", font=("Helvetica", 12), selectmode=tk.SINGLE)
        self.song_listbox.pack(pady=20)

        # Si no hay canciones, mostrar un mensaje
        if not songs:
            self.song_listbox.insert(tk.END, "No hay canciones disponibles.")

        # Botón para agregar una canción
        self.add_song_button = tk.Button(self.main_area, text="+", width=5, height=2, bg=BUTTON_COLOR, fg="white", font=("Helvetica", 16), command=self.add_song)
        self.add_song_button.pack(pady=10)

        # Reproductor en la parte inferior
        self.player_frame = tk.Frame(self.root, bg=SIDEBAR_COLOR, height=100)
        self.player_frame.grid(row=1, column=1, sticky="nsew")

        # Botones del reproductor
        self.like_button = tk.Button(self.player_frame, text="❤", width=5, height=2, bg=BUTTON_COLOR, fg="white", command=self.like_song)
        self.like_button.pack(side=tk.LEFT, padx=20)

        self.rewind_button = tk.Button(self.player_frame, text="<< 10s", width=8, height=2, bg=BUTTON_COLOR, fg="white", command=self.rewind_song)
        self.rewind_button.pack(side=tk.LEFT, padx=20)

        self.play_button = tk.Button(self.player_frame, text="Play", width=8, height=2, bg=BUTTON_COLOR, fg="white", command=self.toggle_play)
        self.play_button.pack(side=tk.LEFT, padx=20)

        self.forward_button = tk.Button(self.player_frame, text="10s >>", width=8, height=2, bg=BUTTON_COLOR, fg="white", command=self.forward_song)
        self.forward_button.pack(side=tk.LEFT, padx=20)

        # Barra de progreso
        self.progress = ttk.Progressbar(self.player_frame, length=200, mode="determinate", value=0)
        self.progress.pack(side=tk.LEFT, padx=20)
        self.progress.config(style="TProgressbar")

        # Control de volumen
        self.volume_label = tk.Label(self.player_frame, text="Volumen", bg=SIDEBAR_COLOR, fg="white")
        self.volume_label.pack(side=tk.LEFT, padx=10)

        self.volume_slider = tk.Scale(self.player_frame, from_=0, to=100, orient=tk.HORIZONTAL, bg=SIDEBAR_COLOR, fg="white", command=self.set_volume)
        self.volume_slider.set(50)
        self.volume_slider.pack(side=tk.LEFT, padx=10)

        self.current_song = None
        self.is_playing = False
        
    def go_back_to_music_player(self):
        """Cierra la ventana actual y abre MusicPlayer."""
        self.root.destroy()  # Cierra la ventana actual
        from interfaz import MusicPlayer
        new_window = tk.Tk()  # Crear una nueva ventana
        MusicPlayer(new_window)  # Inicializa MusicPlayer
        new_window.mainloop()

    def load_sidebar_image(self, image_path):
        """Carga la imagen y la muestra en la barra lateral."""
        try:
            image = Image.open(image_path)
            image = image.resize((100, 100))  # Ajustar el tamaño de la imagen
            image = ImageTk.PhotoImage(image)
            self.image_label = tk.Label(self.sidebar, image=image, bg=SIDEBAR_COLOR)
            self.image_label.pack(pady=20)
            self.image_label.image = image  # Mantener la referencia a la imagen para evitar que se elimine
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

    def add_song(self):
        """Agregar una nueva canción."""
        title = simpledialog.askstring("Título de la Canción", "Ingresa el título de la canción:")
        artist = simpledialog.askstring("Artista", "Ingresa el nombre del artista:")
        if not title or not artist:
            messagebox.showwarning("Error", "Debes ingresar tanto el título como el artista.")
            return
        
        # Solicitar al usuario que seleccione el archivo de la canción
        file_path = filedialog.askopenfilename(title="Selecciona el archivo de la canción", filetypes=[("Archivos MP3", "*.mp3")])
        if not file_path:
            messagebox.showwarning("Error", "Debes seleccionar un archivo de audio.")
            return

        # Añadir la canción a la lista
        new_song = {'title': title, 'artist': artist, 'file': file_path}
        songs.append(new_song)

        # Actualizar la lista de canciones en la interfaz
        self.update_song_listbox()

    def update_song_listbox(self):
        """Actualizar la lista de canciones en la interfaz."""
        # Limpiar la lista de canciones actual
        self.song_listbox.delete(0, tk.END)

        # Si no hay canciones, mostrar un mensaje
        if not songs:
            self.song_listbox.insert(tk.END, "No hay canciones disponibles.")
        else:
            for song in songs:
                self.song_listbox.insert(tk.END, f"{song['title']} - {song['artist']}")

    def like_song(self):
        """Agregar canción a 'Tus Me Gusta' o a una playlist."""
        selected_index = self.song_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Seleccionar canción", "Por favor, selecciona una canción.")
            return
        song_title = self.song_listbox.get(selected_index)
        song_title = song_title.split(" - ")[0]  # Obtener solo el título de la canción
        song = next((s for s in songs if s['title'] == song_title), None)

        if song:
            # Mostrar una ventana con dos botones: "Tus Me Gusta" y "Playlist"
            destination_window = tk.Toplevel(self.root)
            destination_window.title("¿Dónde deseas guardar la canción?")

            # Botón para agregar a "Tus Me Gusta"
            button_liked = tk.Button(destination_window, text="Agregar a Tus Me Gusta", command=lambda: self.add_to_liked_songs(song))
            button_liked.pack(pady=10)

            # Botón para agregar a una Playlist
            button_playlist = tk.Button(destination_window, text="Agregar a Playlist", command=lambda: self.add_to_playlist(song))
            button_playlist.pack(pady=10)

    def add_to_liked_songs(self, song):
        """Agregar la canción a la lista de Me Gusta."""
        if song not in liked_songs:
            liked_songs.append(song)
            messagebox.showinfo("Agregado a Me Gusta", f"{song['title']} ha sido agregado a 'Tus Me Gusta'.")
        else:
            messagebox.showinfo("Ya agregado", f"{song['title']} ya está en 'Tus Me Gusta'.")

    def add_to_playlist(self, song):
        """Agregar la canción a una playlist."""
        playlist_name = simpledialog.askstring("Nombre de la Playlist", "Ingresa el nombre de la playlist:")
        if not playlist_name:
            messagebox.showwarning("Error", "Debes ingresar un nombre para la playlist.")
            return
        
        # Verificar si la playlist ya existe, si no, crearla
        if playlist_name not in playlists:
            playlists[playlist_name] = {"songs": [], "image": None}
        
        # Agregar la canción a la playlist
        playlists[playlist_name]["songs"].append(song)
        messagebox.showinfo("Agregado a Playlist", f"{song['title']} ha sido agregado a la playlist '{playlist_name}'.")

    def show_liked_songs(self):
        """Mostrar las canciones de 'Tus Me Gusta'."""
        liked_songs_window = tk.Toplevel(self.root)
        liked_songs_window.title("Tus Me Gusta")

        listbox = tk.Listbox(liked_songs_window, width=50, height=15, bg="#9b59b6", fg="white", font=("Helvetica", 12))
        listbox.pack(pady=20)

        if liked_songs:
            for song in liked_songs:
                listbox.insert(tk.END, f"{song['title']} - {song['artist']}")
        else:
            listbox.insert(tk.END, "No tienes canciones en 'Tus Me Gusta'.")
    
    def show_artists(self):
        """Mostrar los artistas favoritos."""
        artists_window = tk.Toplevel(self.root)
        artists_window.title("Artistas Favoritos")

        listbox = tk.Listbox(artists_window, width=50, height=15, bg="#9b59b6", fg="white", font=("Helvetica", 12))
        listbox.pack(pady=20)

        if favorite_artists:
            for artist in favorite_artists:
                listbox.insert(tk.END, artist)
        else:
            listbox.insert(tk.END, "No tienes artistas favoritos.")
        
    def create_playlist(self):
        """Crear una nueva playlist con opción de agregar imagen."""
        playlist_name = simpledialog.askstring("Crear Playlist", "Ingresa el nombre de la nueva playlist:")
        if playlist_name:
            # Opción para agregar una imagen
            image_path = filedialog.askopenfilename(title="Seleccionar imagen de la playlist", filetypes=[("Archivos de imagen", ".png;.jpg;.jpeg;.gif")])
            
            if image_path:  # Si se selecciona una imagen
                playlists[playlist_name] = {"songs": [], "image": image_path}
            else:
                playlists[playlist_name] = {"songs": [], "image": None}

            self.update_playlist_buttons()

    def update_playlist_buttons(self):
        """Actualizar los botones de las playlists en la interfaz, mostrando la imagen si está disponible."""
        for widget in self.playlists_frame.winfo_children():
            widget.destroy()

        for playlist_name, playlist_info in playlists.items():
            # Crear un contenedor para cada playlist
            playlist_frame = tk.Frame(self.playlists_frame, bg=SIDEBAR_COLOR)
            playlist_frame.pack(pady=5)

            # Si hay imagen, mostrarla
            if playlist_info["image"]:
                image = Image.open(playlist_info["image"])
                image = image.resize((50, 50))  # Ajustar el tamaño de la imagen
                image = ImageTk.PhotoImage(image)
                image_label = tk.Label(playlist_frame, image=image, bg=SIDEBAR_COLOR)
                image_label.image = image  # Mantener la referencia a la imagen
                image_label.pack(side=tk.LEFT, padx=10)

            # Botón para la playlist
            button = tk.Button(playlist_frame, text=playlist_name, width=20, height=2, bg=BUTTON_COLOR, fg="white", font=("Helvetica", 12), command=lambda name=playlist_name: self.show_playlist(name))
            button.pack(side=tk.LEFT, padx=10)

    def show_playlist(self, playlist_name):
        """Mostrar las canciones de una playlist seleccionada, junto con su imagen si existe."""
        playlist_window = tk.Toplevel(self.root)
        playlist_window.title(f"Playlist: {playlist_name}")
        playlist_window.geometry("400x400")

        # Mostrar la imagen de la playlist si tiene una
        playlist_info = playlists[playlist_name]
        if playlist_info["image"]:
            image = Image.open(playlist_info["image"])
            image = image.resize((100, 100))  # Ajustar tamaño
            image = ImageTk.PhotoImage(image)
            image_label = tk.Label(playlist_window, image=image, bg=BACKGROUND_COLOR)
            image_label.image = image  # Mantener la referencia
            image_label.pack(pady=10)

        playlist_listbox = tk.Listbox(playlist_window, width=50, height=15, bg="#9b59b6", fg="white", font=("Helvetica", 12), selectmode=tk.SINGLE)
        playlist_listbox.pack(pady=20)

        if playlist_info["songs"]:
            for song in playlist_info["songs"]:
                playlist_listbox.insert(tk.END, f"{song['title']} - {song['artist']}")
        else:
            playlist_listbox.insert(tk.END, "Esta playlist está vacía.")
        
        # Opción para eliminar la playlist
        button_delete_playlist = tk.Button(playlist_window, text="Eliminar Playlist", width=20, height=2, bg=BUTTON_COLOR, fg="white", font=("Helvetica", 12), command=lambda: self.delete_playlist(playlist_name, playlist_window))
        button_delete_playlist.pack(pady=10)

    def delete_playlist(self, playlist_name, window):
        """Eliminar una playlist."""
        del playlists[playlist_name]
        window.destroy()  # Cerrar la ventana de la playlist
        self.update_playlist_buttons()  # Actualizar la lista de playlists en la interfaz

    def toggle_play(self):
        """Reproducir o pausar la canción."""
        if not self.is_playing:
            self.play_current_song()
        else:
            pygame.mixer.music.pause()
            self.is_playing = False
            self.play_button.config(text="Play")

    def play_current_song(self):
        """Reproducir la canción seleccionada."""
        selected_index = self.song_listbox.curselection()
        if selected_index:
            song_title = self.song_listbox.get(selected_index)
            song_title = song_title.split(" - ")[0]  # Obtener solo el título de la canción
            song = next((s for s in songs if s['title'] == song_title), None)
            
            if song:
                pygame.mixer.music.load(song['file'])
                pygame.mixer.music.play()
                self.is_playing = True
                self.play_button.config(text="Pausar")
                self.update_progress_bar()

    def update_progress_bar(self):
        """Actualizar la barra de progreso mientras suena la canción."""
        if self.is_playing:
            current_pos = pygame.mixer.music.get_pos() / 1000  # Convertir de milisegundos a segundos
            total_length = pygame.mixer.Sound(pygame.mixer.music.get_filename()).get_length()
            progress_percentage = (current_pos / total_length) * 100
            self.progress['value'] = progress_percentage
            self.root.after(1000, self.update_progress_bar)  # Actualizar cada segundo

    def rewind_song(self):
        """Retroceder 10 segundos en la canción."""
        current_pos = pygame.mixer.music.get_pos() / 1000  # Convertir a segundos
        new_pos = max(0, current_pos - 10)  # Evitar retroceder más allá del principio
        pygame.mixer.music.set_pos(new_pos)

    def forward_song(self):
        """Avanzar 10 segundos en la canción."""
        current_pos = pygame.mixer.music.get_pos() / 1000
        new_pos = current_pos + 10
        pygame.mixer.music.set_pos(new_pos)

    def set_volume(self, volume):
        """Ajustar el volumen."""
        pygame.mixer.music.set_volume(int(volume) / 100)

# Crear la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Biblioteca(root)
    root.mainloop()