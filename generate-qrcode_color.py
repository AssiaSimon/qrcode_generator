import qrcode  
import os 

texte = "Bonjour ! Ceci est un QR code contenant du texte."

script_dir = os.path.dirname(os.path.abspath(__file__))
texte_qrcode = os.path.join(script_dir, "qrcode_color.png")

#img = qrcode.make(texte)
#img.save(texte_qrcode)

qr = qrcode.QRCode() # QRCode class
qr.add_data(texte)
img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
img.save(texte_qrcode)

print("QR code créé avec succès.")