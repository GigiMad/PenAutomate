from CTkMessagebox import CTkMessagebox
import customtkinter
from PIL import Image, ImageTk
import subprocess
import emoji

customtkinter.deactivate_automatic_dpi_awareness()

# Apparence
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Fenêtre root
root = customtkinter.CTk()
root.geometry("500x500")
root.title("PenAutomate")
root.iconbitmap("penautomate.ico")
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

# Frame
frame = customtkinter.CTkFrame(master=root, corner_radius=10, width=200, height=200)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Titre de la frame
label = customtkinter.CTkLabel(master=frame, text="   Options   ", font=("Lato", 24, "bold"))
label.pack(pady=12, padx=10)

def languages(choice):
    print("test")

def themes(choice):
    print("test")

def back():
    root.destroy()
    subprocess.run(["python", "main.py"])


# Boutons pour le menu dans la frame
button = customtkinter.CTkButton(master=frame, text="\u25fe   Languages   \u25fe", command=languages, font=("Lato", 14, "bold"))
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="\u25fe   Themes   \u25fe", command=themes, font=("Lato", 14, "bold"))
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Back", command=back, font=("Lato", 14, "bold"), fg_color="#22B14C", hover_color="#1A873A")
button.pack(pady=12, padx=10)


# Main Loop
root.mainloop()