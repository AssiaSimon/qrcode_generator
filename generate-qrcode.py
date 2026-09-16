import qrcode  
import os 

texte = "Bonjour ! Ceci est un QR code contenant du texte."

script_dir = os.path.dirname(os.path.abspath(__file__))
texte_qrcode = os.path.join(script_dir, "qrcode.png")

img = qrcode.make(texte)
img.save(texte_qrcode)

print("QR code créé avec succès.")

# os module interaction avec le système d'opération
# __file__ est une variable spéciale qui contient le chemin du script en cours d'exécution
# abspath() transforme un chemin en chemin absolu
# dirname() extrait le dossier contenant le fichier