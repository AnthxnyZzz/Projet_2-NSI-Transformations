import os, sys
from PIL import Image, ImageOps, ImageTk #python3-pil.imagetk python3-imaging-tk

def symetrie_hor():
    imgOri=Image.open('vegeta.jpg',mode='r')
    img=imgOri
    dim=img.size
    lar=dim[0]
    hau=dim[1]

    #charger l'image en une matrice de pixels
    imgmatrice=img.load()

    imgnew= Image.new('RGB',(dim[0],dim[1]))


    for i in range (dim[0]):
        for j in range (dim[1]):
            imgnew.putpixel((i,j),img.getpixel((lar-i-1,j)))

    imgnew.show()


def symetrie_ver():

    imgOri=Image.open('vegeta.jpg','r')
    img=imgOri
    dim=img.size
    lar=dim[0]
    hau=dim[1]

    #charger l'image en une matrice de pixels
    imgmatrice=img.load()

    imgnew= Image.new('RGB',(dim[0],dim[1]))


    for i in range (dim[0]):
        for j in range (dim[1]):
            imgnew.putpixel((i,j),img.getpixel((i,hau-j-1)))

    imgnew.show()

def symetrie_cent():

    imgOri=Image.open('vegeta.jpg','r')
    img=imgOri
    dim=img.size
    lar=dim[0]
    hau=dim[1]

    #charger l'image en une matrice de pixels
    imgmatrice=img.load()

    imgnew= Image.new('RGB',(dim[0],dim[1]))


    for i in range (dim[0]):
        for j in range (dim[1]):
            imgnew.putpixel((i,j),img.getpixel((lar-i-1,hau-j-1)))

    imgnew.show()

def defil_hor(nbre):
    imgOri=Image.open('vegeta.jpg','r')
    img=imgOri
    dim=img.size
    lar=dim[0]
    hau=dim[1]

    #charger l'image en une matrice de pixels
    imgmatrice=img.load()


    imgnew= Image.new('RGB',(dim[0],dim[1]))

    for i in range(dim[0]):
        for j in range(dim[1]):
            if i+nbre>=lar-1:
                add=i+nbre-lar-1
                imgnew.putpixel((add,j),img.getpixel((i,j)))
            else:
                imgnew.putpixel((i+nbre,j),img.getpixel((i,j)))
    imgnew.show()

def defil_ver(nbre):
    imgOri=Image.open('vegeta.jpg','r')
    img=imgOri
    dim=img.size
    lar=dim[0]
    hau=dim[1]

    #charger l'image en une matrice de pixels
    imgmatrice=img.load()

    imgnew= Image.new('RGB',(dim[0],dim[1]))

    for i in range(dim[0]):
        for j in range(dim[1]):
            if j+nbre>=hau-1:
                add=j+nbre-hau-1
                imgnew.putpixel((i,add),img.getpixel((i,j)))
            else:
                imgnew.putpixel((i,j+nbre),img.getpixel((i,j)))

    imgnew.show()

def browser(): #recherche de l'image sur l'ordinateur
    global img, imgfile

    imgfile = filedialog.askopenfilename() #importation de l'image
    img=Image.open(imgfile) #ouverture de l'image
    img.thumbnail((350,350)) #définition de la zone d'affichage de l'image
    img=ImageTk.PhotoImage(img) #changement du type
    lbl.configure(image=img) #configuration du label
    lbl.image=img #définition de l'image au label


import tkinter

fenetre=tkinter.Tk() #création de la fenêtre


m = tkinter.Menu ()
Symetrie = tkinter.Menu ()
Defil = tkinter.Menu ()


lbl= tkinter.Label(fenetre, text="Menus transformations")


bou1 = Button(fenetre,text='Symétrie Horizontale',command=symetrie_hor)
bou1.place(relx=1, rely=5)
bou1.pack()

bou2 = Button(fenetre,text='Symétrie Verticale',command=symetrie_ver)
bou2.place(relx=1, rely=5)
bou2.pack()

bou3 = Button(fenetre,text='Défilement',command=defil)
bou1.place(relx=1, rely=5)
bou1.pack()

bou1 = Button(fenetre,text='Symétrie Horizontale',command=symetrie_hor)
bou1.place(relx=1, rely=5)
bou1.pack()

boufin = Button(fenetre,text='Quitter',command=fenetre.destroy) #Bouton Quitter
boufin.place(relx=1, rely=5, anchor=SE)
boufin.pack()


fenetre.title("Transformations d'image")
fenetre.mainloop()
