import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class MusicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music App")
        self.root.configure(bg='#121212')
        
        # Configure grid weights
        root.grid_columnconfigure((0,1,2), weight=1)
        
        # Top navigation bar
        self.nav_frame = tk.Frame(root, bg='#282828')
        self.nav_frame.grid(row=0, column=0, columnspan=3, sticky='ew', pady=(0,20))
        
        # Home button
        self.home_btn = tk.Button(self.nav_frame, text="🏠", bg='#282828', fg='white', 
                                relief='flat', font=('Arial', 16))
        self.home_btn.pack(side='left', padx=10)
        
        # Search entry
        self.search_entry = tk.Entry(self.nav_frame, bg='#404040', fg='white',
                                   insertbackground='white', relief='flat')
        self.search_entry.insert(0, "¿Qué quieres reproducir?")
        self.search_entry.pack(side='left', fill='x', expand=True, padx=10, pady=10)
        
        # Category cards
        categories = [
            ("Música", "#E91E63"),
            ("Pódcasts", "#00796B"),
            ("Eventos en directo", "#9C27B0"),
            ("Novedades", "#689F38"),
            ("Feliz Navidad", "#C62828"),
            ("MEXCLA", "#FF3D00"),
            ("Latina", "#E91E63"),
            ("Éxitos en pódcasts", "#2196F3"),
            ("Podcast New Releases", "#9575CD")
        ]
        
        # Create category cards
        row, col = 1, 0
        for title, color in categories:
            self.create_category_card(title, color, row, col)
            col += 1
            if col > 2:
                col = 0
                row += 1
    
    def create_category_card(self, title, color, row, col):
        card = tk.Frame(self.root, bg=color, height=150)
        card.grid(row=row, column=col, padx=10, pady=10, sticky='nsew')
        card.grid_propagate(False)
        
        # Category title
        label = tk.Label(card, text=title, bg=color, fg='white',
                        font=('Arial', 14, 'bold'), anchor='w')
        label.pack(side='left', padx=15, pady=15)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x600")
    app = MusicApp(root)
    root.mainloop()