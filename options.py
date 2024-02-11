import customtkinter
import subprocess
import os
import json
from PIL import Image, ImageTk

# Empêche la résolution automatique de Windows
customtkinter.deactivate_automatic_dpi_awareness()

# Chemin des images
icon_path = os.path.join("penautomate_images", "penautomate.ico")
image_path = os.path.join("penautomate_images", "penautomate.png")


# Fenêtre root
root = customtkinter.CTk()
root.geometry("500x500")
root.title("PenAutomate")
root.iconbitmap(icon_path)
root.resizable(width=False, height=False)

# Centrez la fenêtre au lancement
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

# Apparence
customtkinter.set_appearance_mode(config["appearance_mode"])
customtkinter.set_default_color_theme("dark-blue")

# Frame
frame = customtkinter.CTkFrame(master=root, corner_radius=10, width=200, height=200)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Titre de la frame
label = customtkinter.CTkLabel(master=frame, text="   Options   ", font=("Lato", 24, "bold"))
label.pack(pady=12, padx=10)

# Fonctions du menu
# THEMES
def themes(mode):
    # Change le thème dans themes.json avec le choix de l'utilisateur en minuscule
    config["appearance_mode"] = mode.lower()
    with open('themes.json', 'w') as file:
        json.dump(config, file)

    # Applique les modifications
    customtkinter.set_appearance_mode(mode.lower())

# BACK
def back():
    root.destroy()
    subprocess.run(["python", "main.py"])


# MENU DEROULANT THEMES
optionmenu_var = customtkinter.StringVar(value="Choose your theme")
combobox = customtkinter.CTkOptionMenu(master=frame,
                                       values=["Light", "Dark"],
                                       command=themes,
                                       variable=optionmenu_var)
combobox.pack(padx=20, pady=10)

# BOUTON BACK
button = customtkinter.CTkButton(master=frame, text="Back", command=back, font=("Lato", 14, "bold"), fg_color="#22B14C", hover_color="#1A873A")
button.pack(pady=12, padx=10)


# Main Loop
root.mainloop()