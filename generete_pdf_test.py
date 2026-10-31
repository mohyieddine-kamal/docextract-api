from reportlab.pdfgen import canvas

c = canvas.Canvas("test.pdf")
c.setFont("Helvetica", 10)

lignes = [
    "LIDL",
    "123 Rue de la République",
    "38000 Grenoble",
    "Tel: 04 76 00 00 00",
    "",
    "Ticket de caisse",
    "Date: 31/10/2026  18:25",
    "",
    "Pain complet            1.29",
    "Lait demi-ecreme 1L     0.89",
    "Pommes golden 1kg       1.99",
    "Yaourt nature x8        1.45",
    "Cafe moulu 250g         3.49",
    "",
    "TOTAL EUR               8.11",
    "",
    "CB SANS CONTACT",
    "Merci de votre visite",
]

y = 800
for ligne in lignes:
    c.drawString(50, y, ligne)
    y -= 15

c.save()