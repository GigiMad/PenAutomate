import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

json_input_path = os.path.join("penautomate_menu", "pentestreport", "pentestreport.json")


# Charger les données JSON
with open(json_input_path, 'r') as file:
    data = json.load(file)

# Créer un fichier PDF
pdf_report = SimpleDocTemplate("pentest_report.pdf", pagesize=letter)
flowables = []
styles = getSampleStyleSheet()

# Titre du document
title = Paragraph('Pentest Report', styles['Title'])
flowables.append(title)
flowables.append(Spacer(1, 12))

# Ajouter des données de base
base_data = [
    ["IP Address", data["ip_address"]],
    ["Hostname", data["hostname"]],
    ["Location", f'{data["city"]}, {data["region"]}, {data["country"]}'],
    ["Organization", data["organization"]],
    ["Timezone", data["timezone"]]
]
table = Table(base_data, style=TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.gray),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
]))
flowables.append(table)
flowables.append(Spacer(1, 12))

# Information sur les sous-domaines
subdomain_data = [["Subdomain", "IP Address"]]
subdomain_data.extend([[sd["subdomain"], sd["ip"]] for sd in data["subdomain_details"]])
table = Table(subdomain_data, style=TableStyle([
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
]))
flowables.append(table)

# Enregistrer le PDF
pdf_report.build(flowables)
print("Le rapport PDF a été créé avec succès.")
