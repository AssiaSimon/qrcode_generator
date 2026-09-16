______________ Projet: 

Générateur de QR Code développé en Python permettant de convertir un texte en image QR Code à l’aide de la bibliothèque qrcode, utilisée pour générer et personnaliser le QR Code, et du module os, permettant de gérer les chemins de fichiers et d’enregistrer automatiquement l’image dans le répertoire du script.



______________ Arborescence du projet: 

quiz-pokemon/
|___ generate-qrcode.py
|___ generate-qrcode_color.py
|___ generate-qrcode_color.py
|___ README.txt



______________ Description des 2 fichiers:

Le projet contient deux fichiers Python permettant de générer un QR Code à partir d’un texte.

	- 1er fichier : utilise directement la méthode standard qrcode.make() pour créer un QR Code, mais malgré sa simplicité et sa rapidité elle offre peu de possibilités de personnalisation.

	- 2eme fichier : utilise la classe qrcode.QRCode() afin de créer et personnaliser davantage le QR Code. Il permet notamment de définir la couleur de l’arrière-plan et celle des modules du QR Code grâce aux paramètres back_color et fill_color.



______________ Utilisation des modules:

	- qrcode : bibliothèque Python utilisée pour générer et personnaliser le QR Code; 
	- os : module standard permettant d'interagir avec le système d'exploitation, notamment pour gérer les dossiers et les chemins de fichiers.
	
	
	
______________ Explication du code:


    . __file__ -> contient le chemin du script Python actuellement exécuté.
    . os.path.abspath(__file__) -> transforme le chemin du script en chemin absolu.
    . os.path.dirname(...) -> récupère le dossier dans lequel se trouve le script.
    . os.path.join(...) -> construit correctement le chemin vers le fichier qrcode_color.png.
    . qrcode.QRCode() -> crée un objet QR Code permettant de le personnaliser.
    . add_data(texte) -> ajoute le texte à encoder.
    . make_image(...) -> génère l'image du QR Code avec les couleurs choisies.
    . img.save(...) -> sauvegarde le QR Code au format PNG.


