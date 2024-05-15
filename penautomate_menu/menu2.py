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
pentestreport = os.path.join("penautomate_menu", "pentestreport", "pentestreport.py")
howtouse = os.path.join("penautomate_menu", "how2use.py")

# Fenêtre root
root = customtkinter.CTk()
root.geometry("500x500")
root.title("PenAutomate")
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

# Apparence
customtkinter.set_appearance_mode(config["appearance_mode"])
customtkinter.set_default_color_theme("dark-blue")

# Fonctions du menu
# CREATE A PENTEST REPORT
def pentest_report():
    root.withdraw()
    subprocess.Popen(["python", pentestreport])

# HOW TO USE
def how2use():
    root.withdraw()
    subprocess.Popen(["python", howtouse])

# BACK
def back():
    root.destroy()
    subprocess.run(["python", "main.py"])

# Frame
frame = customtkinter.CTkFrame(master=root, corner_radius=10)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Titre de la frame
label = customtkinter.CTkLabel(master=frame, text="\U0001f47e   PenAutomate   \U0001f47e", font=("Lato", 24, "bold"))
label.pack(pady=12, padx=10)

# Boutons pour le menu dans la frame
# BOUTON CREATE A PENTEST REPORT
button = customtkinter.CTkButton(master=frame, text="\u25fe Pentest Report \u25fe", command=pentest_report, font=("Lato", 14, "bold"), fg_color="#05213A", hover_color="#051d32")
button.pack(pady=12, padx=10, fill=("both"))

# BOUTON WHAT TO KNOW
button = customtkinter.CTkButton(master=frame, text="\u25fe How to use \u25fe", command=how2use, font=("Lato", 14, "bold"), fg_color="#05213A", hover_color="#051d32")
button.pack(pady=12, padx=10, fill=("both"))

# BOUTON BACK
button = customtkinter.CTkButton(master=frame, text="Back", command=back, font=("Lato", 14, "bold"), fg_color="#A66520", hover_color="#8A541B")
button.pack(pady=12, padx=10,fill=("both"))

# Main Loop
root.mainloop()
