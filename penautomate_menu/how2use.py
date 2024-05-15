import customtkinter
import subprocess
import json
import os
from PIL import Image, ImageTk

# Empêche la résolution automatique de Windows
customtkinter.deactivate_automatic_dpi_awareness()

# Chemin des images
icon_path = os.path.join("penautomate_images", "penautomate.ico")
image_path = os.path.join("penautomate_images", "penautomate.png")
back_path = os.path.join("penautomate_menu", "menu2.py")

# Fenêtre root
root = customtkinter.CTk()
root.geometry("500x500")
root.title("Terms of use")
root.iconbitmap(icon_path)
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

# Fonction Back pour revenu au main.py
def back():
    root.destroy()
    subprocess.run(["python", back_path])

# TXT des conditions d'utilisation
terms_text = """

"""
# Affichage du texte dans un menu déroulant    
text = customtkinter.CTkTextbox(master=root, width=500, height = 460, corner_radius=0, activate_scrollbars=True)
text.grid(row=0, column=0)
text.insert("0.0", terms_text)
text.configure(state="disabled")


# BOUTON BACK
button = customtkinter.CTkButton(master=root, text="Back", command=back, font=("Lato", 14, "bold"), fg_color="#22B14C", hover_color="#1A873A")
button.place(relx=0.5, rely=0.96, anchor="center")

# Main Loop
root.mainloop()