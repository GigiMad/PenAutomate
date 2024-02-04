from CTkMessagebox import CTkMessagebox
import customtkinter
from PIL import Image, ImageTk

# Apparence
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Fenêtre root
root = customtkinter.CTk()
root.geometry("660x410")
root.title("PenAutomate")
root.iconbitmap("penautomate.ico")
root.resizable(width=False, height=False)

# Chargement de l'image
image_name = "penautomate.png"
image = Image.open(image_name)
tk_image = ImageTk.PhotoImage(image)

# Image PenAutomate + fond gris
canvas = customtkinter.CTkCanvas(master=root, width=800, height=500, background="#333", highlightthickness=0)
canvas.pack()

# Affichage PenAutomate
canvas.create_image(0, 0, anchor="nw", image=tk_image)

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
frame = customtkinter.CTkFrame(master=canvas)
frame.place(relx=0.78, rely=0.5, anchor="center")  

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

# Main Loop
root.mainloop()
