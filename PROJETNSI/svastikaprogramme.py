import os, sys
from PIL import Image, ImageOps, ImageTk #python3-pil.imagetk python3-imaging-tk



def svastika():
    imgOri=Image.open('vegeta.jpg')
    img=imgOri
    dim=img.size
    lar=dim[0]
    hau=dim[1]

    #charger l'image en une matrice de pixels
    imgmatrice=img.load()
    #les prochaines dimensions de l'image que je vais créer...
    largeur=dim[0]*2
    hauteur=dim[1]*2

    #je crée une image vide qui pourra accueillir les 4 images que je vais effectuer
    imgnew= Image.new('RGB',(largeur,hauteur))

    premier= img.rotate(-90, expand=True)
    deuxieme= img.rotate(180,expand=True)
    troisieme= img.rotate(90, expand=True)

    liste=[(0,0),(lar,0),(lar,hau),(0,hau)]
    liste2=[img,premier,deuxieme,troisieme]


    #je recopie les pixels de chaque partition que j'ai faite précedement à leurs place sur la nouvelle image
    for num in range (len(liste2)):
        for i in range (dim[0]):
            for j in range (dim[1]):
                imgnew.putpixel((i+liste[num][0],j+liste[num][1]),liste2[num].getpixel((i,j)))
        imgnew.show()

