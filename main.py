import customtkinter
from PIL import Image, ImageTk

# Apparence
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Fenêtre root
root = customtkinter.CTk()
root.geometry("660x415")
root.title("PenAutomate")
root.iconbitmap("penautomate.ico")
root.resizable(width=False, height=False)

# Chargement de l'image
image_name = "penautomate.png"
image = Image.open(image_name)
tk_image = ImageTk.PhotoImage(image)

# Image PenAutomate
canvas = customtkinter.CTkCanvas(master=root, width=800, height=500, background="#333", highlightthickness=0)
canvas.pack()

# Affichage PenAutomate
canvas.create_image(0, 0, anchor="nw", image=tk_image)

# Fonction du menu
def start_penautomate():
    print("=== Start with PenAutomate ===")
    # Ajoutez votre code pour le démarrage avec PenAutomate ici

def options():
    print("=== Options ===")
    # Ajoutez votre code pour les options ici

def terms_of_use():
    print("=== Terms of Use ===")
    # Ajoutez votre code pour les conditions d'utilisation ici

def credits():
    print("=== Credits ===")
    # Ajoutez votre code pour les crédits ici

def exit_app():
    root.destroy()

# Frame du menu à droite
frame = customtkinter.CTkFrame(master=canvas)
frame.place(relx=0.8, rely=0.5, anchor="center")  

# Titre de la frame
label = customtkinter.CTkLabel(master=frame, text="PenAutomate", font=("Lato", 24, "bold"))
label.pack(pady=12, padx=10)

# Boutons pour le menu
button = customtkinter.CTkButton(master=frame, text="Start", command=start_penautomate, font=("Lato", 14, "bold"))
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Options", command=options, font=("Lato", 14, "bold"))
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Terms of Use", command=terms_of_use, font=("Lato", 14, "bold"))
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Credits", command=credits, font=("Lato", 14, "bold"))
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Exit", command=exit_app, font=("Lato", 14, "bold"))
button.pack(pady=12, padx=10)

# Main Loop
root.mainloop()
