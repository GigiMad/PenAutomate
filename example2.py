
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json
import os

json_path = os.path.join("penautomate_menu", "pentestreport", "pentestreport.json")

def generate_pdf(filename, data):
    c = canvas.Canvas(filename, pagesize=letter)
    y_position = 750
    for key, value in data.items():
        text = f"{key}: {value}"
        c.drawString(100, y_position, text)
        y_position -= 30  # Move to the next line
    c.save()

if __name__ == "__main__":
    with open(json_path, 'r') as file:
        json_data = json.load(file)
    generate_pdf("pentestreport.pdf", json_data)
