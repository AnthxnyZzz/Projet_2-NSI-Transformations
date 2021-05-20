import os, sys
from PIL import Image, ImageOps, ImageTk #python3-pil.imagetk python3-imaging-tk
import tkinter.font as tkFont
import tkinter.messagebox

def symetrie_hor():
    imgOri=Image.open(choix.get(),mode='r')
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

    imgOri=Image.open(choix.get(),'r')
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

    imgOri=Image.open(choix.get(),'r')
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

def defil():
    imgOri=Image.open(choix.get(),'r')
    img=imgOri
    dim=img.size
    lar=dim[0]
    hau=dim[1]

    #charger l'image en une matrice de pixels
    imgmatrice=img.load()

    newnbre=nbre.get()
    newnbre=newnbre%512
    imgnew= Image.new('RGB',(dim[0],dim[1]))

    for i in range(dim[0]):
        for j in range(dim[1]):
            if i+newnbre>=lar-1:
                add=i+newnbre-lar-1
                imgnew.putpixel((add,j),img.getpixel((i,j)))
            else:
                imgnew.putpixel((i+newnbre,j),img.getpixel((i,j)))

    newnbre2=nbre2.get()
    newnbre2=newnbre2%512

    imgnew2= Image.new('RGB',(dim[0],dim[1]))

    for i in range(dim[0]):
        for j in range(dim[1]):
            if j+newnbre2>=hau-1:
                add=j+newnbre2-hau-1
                imgnew2.putpixel((i,add),imgnew.getpixel((i,j)))
            else:
                imgnew2.putpixel((i,j+newnbre2),imgnew.getpixel((i,j)))

    imgnew2.show()

def svastika():
    imgOri=Image.open(choix.get(),'r')
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

    imgtempo.show()



from tkinter import*
from PIL import Image,ImageOps, ImageTk
import tkinter.font as tkFont
import tkinter.messagebox

def accueil():
    #pour clear
    for c in fenetre.winfo_children():
        if c != menubar:
            c.destroy()

    Label(fenetre,text="Projet 2 : Transformation d'images",foreground='red',anchor='center',font=("Comics Sans MS", 50)).pack()
    Label(fenetre,text="Ce programme s'appelle le Ansteleen. (Anthony, Steban et Kathleen)",font=("Comics Sans MS", 16)).pack()




    Label(fenetre,text="Programmes disponibles :",foreground='blue',anchor='nw',pady=30,font=("Comics Sans MS", 25)).pack()
    Label(fenetre,text="- Symétrie horizontale",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
    Label(fenetre,text="- Symétrie verticale",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
    Label(fenetre,text="- Symétrie centrale",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
    Label(fenetre,text="- Défilement horizontal",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
    Label(fenetre,text="- Défilement vertical",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
    Label(fenetre,text="- Svastika (Semi-fonctionnel",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()

#selection d'images
def select():
    #pour clear
    for c in fenetre.winfo_children():
        if c != menubar:
            c.destroy()



    Label(fenetre,text="Le nombre de pixels en hauteur et en largeur de chaque image est pair.",foreground='red',anchor='nw',pady=30,font=("Comics Sans MS", 25)).pack()
    Label(fenetre,text="Chaque image a pour dimension:  512×512",foreground='blue',anchor='nw',pady=30,font=("Comics Sans MS", 16)).pack()

    Button(fenetre, text ="Steban",pady=15, command = Steban).pack()
    Button(fenetre, text ="Anthoo", pady=15,command = Anthoo).pack()
    Button(fenetre, text ="Flash", pady=15,command = flash).pack()
    Button(fenetre, text ="Vegeta", pady=15,command = vegeta).pack()
    Button(fenetre, text ="Kindasama", pady=15,command = kinda).pack()
    Button(fenetre, text ="Dinausaures", pady=15,command = dino).pack()
    Button(fenetre, text ="Aventador", pady=15,command = lambo).pack()



    Label(fenetre,text=message.get(),foreground='green',anchor='nw',pady=30,font=("Comics Sans MS", 16)).pack()




#les changements de choix
def Steban():
    choix.set('Steban.jpg')
    message.set("L'image choisi est :  "+choix.get())
    selection.set('Amazing')
    select()
def Anthoo():
    choix.set('Anthoo.jpg')
    message.set("L'image choisi est :  "+choix.get())
    selection.set('Amazing')
    select()
def flash():
    choix.set('flash.jpg')
    message.set("L'image choisi est :  "+choix.get())
    selection.set('Amazing')
    select()
def vegeta():
    choix.set('vegeta.jpg')
    message.set("L'image choisi est :  "+choix.get())
    selection.set('Amazing')
    select()
def kinda():
    choix.set('kindasama.jpg')
    message.set("L'image choisi est :  "+choix.get())
    selection.set('Amazing')
    select()
def dino():
    choix.set('dinosaure.jpg')
    message.set("L'image choisi est :  "+choix.get())
    selection.set('Amazing')
    select()
def lambo():
    choix.set('aventador.jpg')
    message.set("L'image choisi est :  "+choix.get())
    selection.set('Amazing')
    select()


def symetries():
    #pour clear
    for c in fenetre.winfo_children():
        if c != menubar:
            c.destroy()

    #je vais essayer de mettre un prévisualisation de l'image sélectionnée

    if selection.get()!='Rien':
        #symétrie horizontale
        Label(fenetre,text="Symétrie horizontale:",foreground='blue',anchor='nw',pady=30,font=("Comics Sans MS", 25)).pack()
        Label(fenetre,text="Ce programme a pour but de reproduire une image à l'identique par rapport à un axe. Et dans le cas de la symétrie horizontale, on inverse l'axe des abscisses.",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
        bou1=Button(fenetre, text ="Symétrie horizontale", pady=15, command = symetrie_hor)
        bou1.pack()

        #symétrie verticale
        Label(fenetre,text="Symétrie verticale:",foreground='blue',anchor='nw',pady=30,font=("Comics Sans MS", 25)).pack()
        Label(fenetre,text="C'est le même principe que la symétrie horizontale sauf que on inverse l'axe des ordonnées.",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
        bou2=Button(fenetre, text ="Symétrie verticale", pady=15, command = symetrie_ver)
        bou2.pack()

        #symétrie centrale
        Label(fenetre,text="Symétrie centrale:",foreground='blue',anchor='nw',pady=30,font=("Comics Sans MS", 25)).pack()
        Label(fenetre,text="C'est un mélange entre la symétrie horizontale et la symétrie verticale.",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
        bou3=Button(fenetre, text ="Symétrie centrale", pady=15, command = symetrie_cent)
        bou3.pack()

    else:
        #symétrie horizontale inutilisable
        Label(fenetre,text="Symétrie horizontale:",foreground='blue',anchor='nw',pady=30,font=("Comics Sans MS", 25)).pack()
        Label(fenetre,text="Ce programme a pour but de reproduire une image à l'identique par rapport à un axe. Et dans le cas de la symétrie horizontale, on inverse l'axe des abscisses.",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
        bou1=Button(fenetre, text ="Symétrie horizontale", pady=15,state = DISABLED, command= test)
        bou1.pack()

        #symétrie verticale inutilisable
        Label(fenetre,text="Symétrie verticale:",foreground='blue',anchor='nw',pady=30,font=("Comics Sans MS", 25)).pack()
        Label(fenetre,text="C'est le même principe que la symétrie horizontale sauf que on inverse l'axe des ordonnées.",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
        bou2=Button(fenetre, text ="Symétrie verticale", pady=15,state = DISABLED, command = test)
        bou2.pack()

        #symétrie centrale inutilisable
        Label(fenetre,text="Symétrie centrale:",foreground='blue',anchor='nw',pady=30,font=("Comics Sans MS", 25)).pack()
        Label(fenetre,text="C'est un mélange entre la symétrie horizontale et la symétrie verticale.",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
        bou3=Button(fenetre, text ="Symétrie centrale", pady=15,state = DISABLED, command = test)
        bou3.pack()
        tkinter.messagebox.showerror ( title = "Une erreur" , message = "N'oubliez pas de choisir une image avant dans l'onglet « Sélection » ! \n" )



def svas():
    #pour clear
    for c in fenetre.winfo_children():
        if c != menubar:
            c.destroy()

    if selection.get()!='Rien':
        #svastika
        Label(fenetre,text="Svastika (semi-fonctionnel):",foreground='blue',anchor='nw',pady=30,font=("Comics Sans MS", 25)).pack()
        Label(fenetre,text="C'est un programme est une transformation qui permet de passer d'une image de base à cette même image\n séparée en quatre mais dont chaque face est retournée à 90° de la précédente",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
        bou15=Button(fenetre, text ="Svastika", pady=15, command = svastika)
        bou15.pack()
    else:
        #svastika inutilisable
        Label(fenetre,text="Svastika (semi-fonctionnel):",foreground='blue',anchor='nw',pady=30,font=("Comics Sans MS", 25)).pack()
        Label(fenetre,text="C'est un programme est une transformation qui permet de passer d'une image de base à cette même image\n séparée en quatre mais dont chaque face est retournée à 90° de la précédente",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
        bou15=Button(fenetre, text ="Svastika", pady=15,state=DISABLED, command = svastika)
        bou15.pack()



def defilements():
    global selection

    #pour clear
    for c in fenetre.winfo_children():
        if c != menubar:
            c.destroy()

    if selection.get()!='Rien':
        #défilement horizontal
        Label(fenetre,text="Défilement horizontal:",foreground='blue',anchor='nw',pady=30,font=("Comics Sans MS", 25)).pack()
        Label(fenetre,text="Ce programme est une transformation qui consiste à déplacer des colonnes de pixels d’une image vers la droite.\n L'utilisateur doit indiquer le nombre de déplacement qu'il souhaite mais le nombre doit être inférieur au nombre de pixel en largeur.\n Quand une colonne de pixels est en dehors de l'image, elle est replacée à gauche.",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
        scale1=Scale(fenetre, from_=0,to=1000,command=affectation)
        scale1.pack()

        Label(fenetre,text="-----------------------",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
        nbre.set(scale1.get())
        bou10=Button(fenetre, text ="Défilement", pady=15, command = defil)
        bou10.pack()
        Label(fenetre,text="Les deux transformations fonctionnent ensemble...",foreground='black',anchor='nw',font=("Comics Sans MS", 16)).pack()
        Label(fenetre,text="-----------------------",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()

        #défilement vertical
        Label(fenetre,text="Défilement vertical:",foreground='blue',anchor='nw',pady=30,font=("Comics Sans MS", 25)).pack()
        Label(fenetre,text="Ce programme est une transformation qui consiste à déplacer des lignes de pixels d’une image vers le bas.\n L'utilisateur doit indiquer le nombre de déplacement qu'il souhaite mais le nombre doit être inférieur au nombre de pixel en hauteur.\n Quand une ligne de pixels est en dehors de l'image, elle est replacée au sommet.",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
        scale2=Scale(fenetre, from_=0,to=1000,command=affectation2)
        scale2.pack()


    else:
        Label(fenetre,text="Défilement horizontal:",foreground='blue',anchor='nw',pady=30,font=("Comics Sans MS", 25)).pack()
        Label(fenetre,text="Ce programme est une transformation qui consiste à déplacer des colonnes de pixels d’une image vers la droite.\n L'utilisateur doit indiquer le nombre de déplacement qu'il souhaite mais le nombre doit être inférieur au nombre de pixel en largeur.\n Quand une colonne de pixels est en dehors de l'image, elle est replacée à gauche.",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
        scale1=Scale(fenetre, from_=0,to=1000,state=DISABLED,command=affectation)
        scale1.pack()

        Label(fenetre,text="-----------------------",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
        nbre.set(scale1.get())
        bou10=Button(fenetre, text ="Défilement", pady=15,state=DISABLED, command = defil)
        bou10.pack()
        Label(fenetre,text="Les deux transformations fonctionnent ensemble...",foreground='black',anchor='nw',font=("Comics Sans MS", 16)).pack()
        Label(fenetre,text="-----------------------",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()

        #défilement vertical
        Label(fenetre,text="Défilement vertical:",foreground='blue',anchor='nw',pady=30,font=("Comics Sans MS", 25)).pack()
        Label(fenetre,text="Ce programme est une transformation qui consiste à déplacer des lignes de pixels d’une image vers le bas.\n L'utilisateur doit indiquer le nombre de déplacement qu'il souhaite mais le nombre doit être inférieur au nombre de pixel en hauteur.\n Quand une ligne de pixels est en dehors de l'image, elle est replacée au sommet.",foreground='green',anchor='nw',font=("Comics Sans MS", 16)).pack()
        scale2=Scale(fenetre, from_=0,to=1000,state=DISABLED,command=affectation2)
        scale2.pack()
        tkinter.messagebox.showerror ( title = "Une erreur" , message = "N'oubliez pas de choisir une image avant dans l'onglet « Sélection » ! \n" )



def affectation(x):
    nbre.set(x)

def affectation2(x):
    nbre2.set(x)

def info():
    #pour clear
    for c in fenetre.winfo_children():
        if c != menubar:
            c.destroy()

    Label(fenetre,text="Contributeurs :",foreground='red',anchor='center',font=("Comics Sans MS", 50)).pack()
    Label(fenetre,text="--------------------------------",anchor='center',font=("Comics Sans MS", 30)).pack()
    Label(fenetre,text="Anthony PAMPHILE a travaillé sur :",pady=20,anchor='center',font=("Comics Sans MS", 25)).pack()
    Label(fenetre,text="- La symétrie horizontale",anchor='center',font=("Comics Sans MS", 18)).pack()
    Label(fenetre,text="- La symétrie verticale",anchor='center',font=("Comics Sans MS", 18)).pack()
    Label(fenetre,text="- Le défilement horizontal",anchor='center',font=("Comics Sans MS", 18)).pack()
    Label(fenetre,text="- Le défilement vertical",anchor='center',font=("Comics Sans MS", 18)).pack()
    Label(fenetre,text="- La réalisation du Github",anchor='center',font=("Comics Sans MS", 18)).pack()
    Label(fenetre,text="- L'interface graphique tkinter'",anchor='center',font=("Comics Sans MS", 18)).pack()

    Label(fenetre,text="Steban BREDAS a travaillé sur:",pady=20,anchor='center',font=("Comics Sans MS", 25)).pack()
    Label(fenetre,text="- La symétrie horizontale",anchor='center',font=("Comics Sans MS", 18)).pack()
    Label(fenetre,text="- Le défilement vertical",anchor='center',font=("Comics Sans MS", 18)).pack()
    Label(fenetre,text="- La symétrie centrale",anchor='center',font=("Comics Sans MS", 18)).pack()


    Label(fenetre,text="Kathleen RADIGUET a travaillé sur:",pady=20,anchor='center',font=("Comics Sans MS", 25)).pack()
    Label(fenetre,text="- La symétrie centrale",anchor='center',font=("Comics Sans MS", 18)).pack()
    Label(fenetre,text="- La symétrie verticale",anchor='center',font=("Comics Sans MS", 18)).pack()
    Label(fenetre,text="- La réalisation du Github",anchor='center',font=("Comics Sans MS", 18)).pack()






fenetre= Tk()

#barre des menus
menubar=Menu(fenetre)


#créa des menus
menuaccueil=Menu(menubar)
menuselec=Menu(menubar)
menutrans=Menu(menubar)
menuinfo=Menu(menubar)

#ajout dans menu
menubar.add_cascade(label="Réception",menu=menuaccueil)
menubar.add_cascade(label="Sélection de l'image",command=select)
menubar.add_cascade(label="Transformations",menu=menutrans, background='red')
menubar.add_cascade(label="Informations",command=info)

#menuaccueil
accueil()



menuaccueil.add_command(label="Accueil",command=accueil)
menuaccueil.add_command(label="Quitter",command=fenetre.destroy)

#menuchoix
choix=StringVar()
choix.set('Rien')

selection=StringVar()
selection.set('Rien')


message = StringVar()
message.set("L'image choisi est :  "+choix.get())


nbre=IntVar()
nbre2=IntVar()

#menutransformation
menutrans.add_command(label="Symétries",command=symetries)
menutrans.add_command(label="Défilements",command=defilements)
menutrans.add_command(label="Svastika",command=svas)

fenetre.config(menu=menubar)
fenetre.wm_state(newstate="zoomed")
fenetre.title('Ansteleen')
fenetre.mainloop()
