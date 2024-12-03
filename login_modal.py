import tkinter as tk
from tkinter import ttk

class LoginModal:
    def __init__(self, root):
        self.root = root
        self.root.title("Spotify Login")
        self.root.configure(bg='#282828')
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='#282828', padx=40, pady=40)
        main_frame.pack(expand=True, fill='both')
        
        # Image placeholder
        image_frame = tk.Frame(main_frame, bg='#404040', width=200, height=200)
        image_frame.pack(pady=20)
        image_frame.pack_propagate(False)
        
        # Title
        tk.Label(main_frame, 
                text="Empieza a escuchar\ncon una cuenta de\nSpotify gratis",
                font=('Arial', 24, 'bold'),
                fg='white',
                bg='#282828',
                justify='center').pack(pady=20)
        
        # Register button
        register_btn = tk.Button(main_frame,
                               text="Registrate gratis",
                               bg='#1DB954',
                               fg='white',
                               font=('Arial', 12, 'bold'),
                               padx=40,
                               pady=10,
                               relief='flat')
        register_btn.pack(pady=10)
        
        # Download button
        download_btn = tk.Button(main_frame,
                               text="Descargar aplicación",
                               bg='#282828',
                               fg='white',
                               font=('Arial', 12),
                               padx=40,
                               pady=10,
                               relief='flat',
                               border=1)
        download_btn.pack(pady=10)
        
        # Login link
        login_frame = tk.Frame(main_frame, bg='#282828')
        login_frame.pack(pady=20)
        
        tk.Label(login_frame,
                text="¿Ya tienes cuenta?",
                fg='gray',
                bg='#282828').pack(side='left')
        
        tk.Label(login_frame,
                text="Iniciar sesión",
                fg='white',
                bg='#282828',
                cursor='hand2').pack(side='left', padx=5)
        
        # Close button
        tk.Button(main_frame,
                 text="Cerrar",
                 bg='#282828',
                 fg='white',
                 relief='flat').pack(side='bottom', pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x700")
    app = LoginModal(root)
    root.mainloop()