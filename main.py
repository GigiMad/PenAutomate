from CTkMessagebox import CTkMessagebox
import customtkinter
from PIL import Image, ImageTk

# Apparence
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Fonction pour déplacer l'image progressivement vers la gauche
def move_image_left(event, steps=10):
    global move_step
    if steps > 0:
        canvas.move(image_id, -move_step, 0)
        move_step += 1
        root.after(30, lambda: move_image_left(event, steps - 1))
    else:
        move_step = 0

# Fonction pour ramener l'image à sa position initiale
def reset_image_position(event):
    canvas.coords(image_id, x, y)  # Réinitialise la position de l'image

# Fenêtre root
root = customtkinter.CTk()
root.geometry("500x500")
root.title("PenAutomate")
root.iconbitmap("penautomate.ico")
root.resizable(width=False, height=False)

# Chargement de l'image et redimensionnement
image_name = "penautomate.png"
original_image = Image.open(image_name)
original_image.thumbnail((300, 300))  # Redimensionne l'image à la taille souhaitée
tk_image = ImageTk.PhotoImage(original_image)

# Image PenAutomate + fond gris
canvas = customtkinter.CTkCanvas(master=root, width=500, height=500, background="#333", highlightthickness=0)
canvas.pack()

# Calcul des coordonnées pour centrer l'image
canvas_width = canvas.winfo_reqwidth()
canvas_height = canvas.winfo_reqheight()
image_width = tk_image.width()
image_height = tk_image.height()

x = (canvas_width - image_width) // 6
y = (canvas_height - image_height) // 2

# Affichage PenAutomate
image_id = canvas.create_image(x, y, anchor="nw", image=tk_image)

# Variables pour le déplacement de l'image
move_step = 0

# Fonctions du menu
def start_penautomate():
    print("=== Start with PenAutomate ===")

def options():
    print("=== Options ===")

def terms_of_use2():
    CTkMessagebox(title="Info", message="This is a CTkMessagebox!")

def credits():
    print("=== Credits ===")

def exit_app():
    root.destroy()

# Frame du menu à droite de l'image
frame = customtkinter.CTkFrame(master=root, corner_radius=10, bg_color="#333")
frame.place(relx=0.48, rely=0.5, anchor="w")

# Titre de la frame
label = customtkinter.CTkLabel(master=frame, text="   PenAutomate   ", font=("Lato", 24, "bold"))
label.pack(pady=12, padx=10)

# Boutons pour le menu dans la frame
button = customtkinter.CTkButton(master=frame, text="Start", command=start_penautomate, font=("Lato", 14, "bold"))
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Options", command=options, font=("Lato", 14, "bold"))
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Terms of Use", command=terms_of_use2, font=("Lato", 14, "bold"))
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Credits", command=credits, font=("Lato", 14, "bold"))
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Exit", command=exit_app, font=("Lato", 14, "bold"), fg_color="#FF3355", hover_color="#FF3333")
button.pack(pady=12, padx=10)

# Lier les fonctions aux événements
canvas.tag_bind(image_id, '<Enter>', lambda event: move_image_left(event, steps=10))
canvas.tag_bind(image_id, '<Leave>', reset_image_position)

# Main Loop
root.mainloop()
