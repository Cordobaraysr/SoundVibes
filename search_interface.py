import tkinter as tk
from tkinter import ttk

class SearchInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Búsqueda")
        self.root.configure(bg='#121212')
        
        # Navigation bar
        self.create_nav_bar()
        
        # Categories bar
        self.create_categories()
        
        # Main content
        self.create_main_content()
        
        # Songs list
        self.create_songs_list()
        
    def create_nav_bar(self):
        nav_frame = tk.Frame(self.root, bg='#282828')
        nav_frame.pack(fill='x', pady=(0, 20))
        
        home_btn = tk.Button(nav_frame, text="🏠", bg='#282828', fg='white')
        home_btn.pack(side='left', padx=10)
        
        search_entry = tk.Entry(nav_frame, bg='#404040', fg='white')
        search_entry.insert(0, "eduardo")
        search_entry.pack(side='left', fill='x', expand=True, padx=10, pady=10)
        
    def create_categories(self):
        categories_frame = tk.Frame(self.root, bg='#121212')
        categories_frame.pack(fill='x', padx=20)
        
        categories = ['Todo', 'Canciones', 'Artistas', 'Listas', 'Álbumes', 
                     'Pódcasts y programas', 'Perfiles']
        
        for category in categories:
            btn = tk.Button(categories_frame, text=category, bg='#282828', fg='white',
                          relief='flat', padx=15)
            btn.pack(side='left', padx=5)
            
    def create_main_content(self):
        main_frame = tk.Frame(self.root, bg='#121212')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Main result section
        tk.Label(main_frame, text="Resultado principal", fg='white', bg='#121212',
                font=('Arial', 20, 'bold')).pack(anchor='w')
        
        result_frame = tk.Frame(main_frame, bg='#282828')
        result_frame.pack(fill='x', pady=10)
        
        # Album art (placeholder)
        art_label = tk.Label(result_frame, bg='#404040', width=15, height=8)
        art_label.pack(side='left', padx=10, pady=10)
        
        # Song info
        info_frame = tk.Frame(result_frame, bg='#282828')
        info_frame.pack(side='left', padx=10)
        
        tk.Label(info_frame, text="La Mujer Que No Soñe", fg='white', bg='#282828',
                font=('Arial', 16, 'bold')).pack(anchor='w')
        tk.Label(info_frame, text="Canción • Eduardo Capetillo", fg='gray',
                bg='#282828').pack(anchor='w')
        
    def create_songs_list(self):
        songs_frame = tk.Frame(self.root, bg='#121212')
        songs_frame.pack(fill='both', expand=True, padx=20)
        
        tk.Label(songs_frame, text="Canciones", fg='white', bg='#121212',
                font=('Arial', 18, 'bold')).pack(anchor='w')
        
        songs = [
            ("La Mujer Que No Soñe", "Eduardo Capetillo"),
            ("contenta,", "Ed Maverick"),
            ("Polvos En Paris", "Eduardo Soto"),
            ("Solo en Mi Habitación", "Eduardo Soto")
        ]
        
        for song, artist in songs:
            song_frame = tk.Frame(songs_frame, bg='#282828')
            song_frame.pack(fill='x', pady=2)
            
            tk.Label(song_frame, text=song, fg='white', bg='#282828').pack(side='left', padx=10)
            tk.Label(song_frame, text=artist, fg='gray', bg='#282828').pack(side='left')

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = SearchInterface(root)
    root.mainloop()