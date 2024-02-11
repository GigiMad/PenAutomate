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
    subprocess.run(["python", "main.py"])

# TXT des conditions d'utilisation
terms_text = """
**PenAutomate Automated Penetration Testing Tool - Terms of Use**

**1. Acceptance of Terms**

By using the PenAutomate Automated Penetration Testing Tool ("PenAutomate" or "the Tool"), you agree to comply with and be bound by the following terms and conditions of use. If you do not agree to these terms, please refrain from using the Tool.

**2. Ethical Hacking**

PenAutomate is intended solely for ethical hacking and penetration testing purposes. Users are strictly prohibited from engaging in any illegal or malicious activities. The Tool must be used in compliance with all applicable laws and regulations.

**3. Limitation of Liability**

PenAutomate is provided "as is," without any warranty or guarantee of any kind, either expressed or implied. PenAutomate, its developers, and affiliated parties (collectively referred to as "PenAutomate") disclaim all warranties, including but not limited to the implied warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall PenAutomate be liable for any direct, indirect, incidental, special, or consequential damages arising out of or in any way connected with the use of the Tool.

**4. Responsibility of the User**

Users are solely responsible for their use of PenAutomate. This includes ensuring that the Tool is used only for ethical hacking purposes and in compliance with all relevant laws and regulations. Users are also responsible for any actions taken using PenAutomate and any consequences that may arise.

**5. Ethical Use**

Users must use PenAutomate in an ethical and responsible manner. Unauthorized access to systems or networks is strictly prohibited. Users must obtain explicit permission before conducting penetration testing on any system, network, or application.

**6. Compliance with Laws**

Users agree to comply with all local, national, and international laws and regulations while using PenAutomate. This includes, but is not limited to, laws related to hacking, data protection, and computer security.

**7. Updates and Modifications**

PenAutomate may be updated or modified at the discretion of PenAutomate developers. Users are encouraged to regularly check for updates to ensure they are using the latest version of the Tool.

**8. Indemnification**

Users agree to indemnify and hold PenAutomate harmless from any claims, damages, or liabilities arising out of their use of the Tool. This includes, but is not limited to, legal fees and expenses.

**9. Governing Law**

These terms of use shall be governed by and construed in accordance with the laws of [jurisdiction], without regard to its conflict of law principles.

By using PenAutomate, you acknowledge that you have read, understood, and agree to these terms of use. If you do not agree with any part of these terms, refrain from using PenAutomate. PenAutomate reserves the right to modify these terms at any time without prior notice.
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