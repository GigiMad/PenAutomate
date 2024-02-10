import customtkinter
import subprocess
import emoji
import json
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk

# Empêche la résolution automatique de Windows
customtkinter.deactivate_automatic_dpi_awareness()

# Fenêtre root
root = customtkinter.CTk()
root.geometry("500x500")
root.title("PenAutomate")
root.iconbitmap("penautomate.ico")
root.resizable(width=False, height=False)

# Centre la fenêtre au lancement
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = root.winfo_width()
window_height = root.winfo_height()

x_pos = (screen_width - window_width) // 2
y_pos = (screen_height - window_height) // 2

root.geometry("+{}+{}".format(x_pos, y_pos))    

# Importe la configuration du thème Light / Dark depus le fichier themes.json
with open('themes.json', 'r') as file:
    config = json.load(file)

# Apparence du thème
customtkinter.set_appearance_mode(config["appearance_mode"])
customtkinter.set_default_color_theme("dark-blue")

# Chargement de l'image et redimensionnement
image_name = "penautomate.png"
original_image = Image.open(image_name)
original_image.thumbnail((200, 200))
tk_image = ImageTk.PhotoImage(original_image)

# Ajout du fond gris sur l'image penautomate.png
canvas = customtkinter.CTkCanvas(master=root, width=500, height=500, background="#333", highlightthickness=0)
canvas.pack()

# Positionne l'image penautomate.png
canvas_width = canvas.winfo_reqwidth()
canvas_height = canvas.winfo_reqheight()
image_width = tk_image.width()
image_height = tk_image.height()

x = (canvas_width - image_width) // 2
y = (canvas_height - image_height) // 2

# Affichage de penautomate.png
image_id = canvas.create_image(x, y, anchor="w", image=tk_image)

# Déplace l'image penautomate.png progressivement vers le haut dès que la souris la survole
move_step = 0
def move_image_up(event, steps=10):
    global move_step
    if steps > 0:
        canvas.move(image_id, 0, -move_step)
        move_step += 1
        root.after(30, lambda: move_image_up(event, steps - 1))
    else:
        move_step = 0

# Ramene l'image penautomate.png à sa position initiale dès que la souris ne la survole plus
def reset_image_position(event):
    canvas.coords(image_id, x, y)

# Lie les fonctions aux événements du déplacement de penautomate.png
canvas.tag_bind(image_id, '<Enter>', lambda event: move_image_up(event, steps=10))
canvas.tag_bind(image_id, '<Leave>', reset_image_position)

# Fonctions du menu
# START
def start_penautomate():
    root.withdraw()
    subprocess.Popen(["python", "menu2.py"])

# OPTIONS
def options():
    root.withdraw()
    subprocess.Popen(["python", "options.py"])

# TERMS OF USE
def terms_of_use():
    root.withdraw()
    subprocess.Popen(["python", "termsofuse.py"])

# CREDITS
def credits():
    print("=== Credits ===")

# EXIT
def exit_app():
    root.destroy()

# Frame du menu
frame = customtkinter.CTkFrame(master=root, corner_radius=10, bg_color="#333")
frame.place(relx=0.5, rely=0.55, anchor="center")

# Titre de la frame
label = customtkinter.CTkLabel(master=frame, text="\U0001f47e   PenAutomate   \U0001f47e", font=("Lato", 24, "bold"))
label.pack(pady=12, padx=10)

# Boutons pour le menu dans la frame
# BOUTON START
button = customtkinter.CTkButton(master=frame, text="\u25fe Start \u25fe", command=start_penautomate, font=("Lato", 14, "bold"))
button.pack(pady=12, padx=10)

# BOUTON OPTIONS
button = customtkinter.CTkButton(master=frame, text="\u25fe Options \u25fe", command=options, font=("Lato", 14, "bold"))
button.pack(pady=12, padx=10)

# BOUTON TERMS OF USE
button = customtkinter.CTkButton(master=frame, text="\u25fe Terms of Use \u25fe", command=terms_of_use, font=("Lato", 14, "bold"))
button.pack(pady=12, padx=10)

# BOUTON CREDITS
button = customtkinter.CTkButton(master=frame, text="\u25fe Credits \u25fe", command=credits, font=("Lato", 14, "bold"))
button.pack(pady=12, padx=10)

# BOUTON EXIT
button = customtkinter.CTkButton(master=frame, text="Exit", command=exit_app, font=("Lato", 14, "bold"), fg_color="#880015", hover_color="#5C000E")
button.pack(pady=12, padx=10)

# Main Loop
root.mainloop()
