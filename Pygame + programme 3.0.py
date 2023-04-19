import pygame
from random import *

pygame.init()
class Game:
    def __init__(self, screen,joueurs,argent_d):
        self.screen = screen
        self.running = True
        self.joueurs=joueurs
        for joueur in self.joueurs:
            joueur.argent=argent_d
        self.clock = pygame.time.Clock()


    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        lancer1=randint(1,6)
                        lancer2=randint(1,6)
                        screen.tour(joueurs[0],lancer1,lancer2)



    def update(self):
        pass

    def display(self):
        pygame.display.flip()




    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)

class Screen:
    def __init__(self,x,y):
        self.init=pygame.display.set_mode((x,y))
        self.dé_1=pygame.image.load("Dé_1.png").convert()
        self.dé_2=pygame.image.load("Dé_1.png").convert()
        self.plateau=pygame.image.load("monopoly.jpg").convert()
        self.pion_v=pygame.image.load("pions_vert.png").convert()
        self.pion_b=pygame.image.load("pions_bleu.png").convert()
        self.pion_r=pygame.image.load("pions_rouge.png").convert()
        self.pion_j=pygame.image.load("pions_jaune.png").convert()
        self.init.blit(self.plateau,(250,250))
        self.init.blit(self.dé_1,(550,330))
        self.init.blit(self.dé_2,(330,550))
        self.init.blit(self.pion_v,(690,690))
        self.init.blit(self.pion_b,(725,725))
        if len(joueurs)>=3:
            self.init.blit(self.pion_r,(690,725))
        if len(joueurs)==4:
            self.init.blit(self.pion_j,(725,690))

    def dé(self,lancer1,lancer2):

        if lancer1==1:
            self.dé_1=pygame.image.load("Dé_1.png").convert()
        elif lancer1==2:
            self.dé_1=pygame.image.load("Dé_2.png").convert()
        elif lancer1==3:
            self.dé_1=pygame.image.load("Dé_3.png").convert()
        elif lancer1==4:
            self.dé_1=pygame.image.load("Dé_4.png").convert()
        elif lancer1==5:
            self.dé_1=pygame.image.load("Dé_5.png").convert()
        elif lancer1==6:
            self.dé_1=pygame.image.load("Dé_6.png").convert()
        if lancer2==1:
            self.dé_2=pygame.image.load("Dé_1.png").convert()
        elif lancer2==2:
            self.dé_2=pygame.image.load("Dé_2.png").convert()
        elif lancer2==3:
            self.dé_2=pygame.image.load("Dé_3.png").convert()
        elif lancer2==4:
            self.dé_2=pygame.image.load("Dé_4.png").convert()
        elif lancer2==5:
            self.dé_2=pygame.image.load("Dé_5.png").convert()
        elif lancer2==6:
            self.dé_2=pygame.image.load("Dé_6.png").convert()
        self.init.blit(self.dé_1,(550,330))
        self.init.blit(self.dé_2,(330,550))                 #IMPORTANT: na pas oublier le point le .blit à chaque fois que l'on change d'image ou que l'on veut la déplacer

    def tour(self,joueur,lancer1,lancer2):
        """
        Permet de lancer un tour de jeu
        """

        self.dé(lancer1,lancer2)
        pygame.display.flip()
        compteur_double=0
        if joueur.compteur_prison>0:
            if lancer1==lancer2:
                joueur.compteur_prison=0
                joueur.prison=False
            else:
                joueur.compteur_prison-=1
                if joueur.compteur_prison==0:
                    if joueur.csp>=1:
                        joueur.csp-=1
                        cartes_chance.append("csp")
                        joueur.prison=false
                    else:
                        joueur.argent-=5000
                        joueur.prison=False
                else:
                    joueurA=joueurs.pop(0)
                    joueurs.append(joueurA)
        if lancer1==lancer2:
            compteur_double+=1
            if compteur_double==3:
                joueur.ncase=10
                compteur_prison=3
                joueur.prison=True
                return ("Vous allez en prison")
            joueur.ncase+=lancer1*2
            if joueur.ncase>=40:
                joueur.case=self.ncase%40
                joueur.argent+=20000
            considérer_case(joueur)
        else:
            joueur.ncase+=lancer1+lancer2
            if joueur.ncase>=40:
                joueur.ncase-=40
                joueur.argent+=20000
            considérer_case(joueur)
            joueurA=joueurs.pop(0)
            joueurs.append(joueurA)







class Case:
    def __init__(self,type,nom,ncase,x,y,couleur=None,loyer=None):
        self.nom=nom
        self.type=type
        self.couleur=couleur
        self.coordonnees=(x,y)
        if self.couleur!=None:
            self.prix=loyer
            self.nb_maison=0
        self.ncase=ncase
        self.coordonnées=(x,y)

    def mettre_une_maison(self):
        """
        Ajoute une maison sur une propriété si elle n'en possède pas déjà 4
        """
        if self.type=="Propriété":
            if self.nb_maison<4:
                self.loyer=round(self.loyer*1.5,0)
                self.nb_maison+=1
            else:
                raise IndexError('Trop de maisons')

    def poser_un_hôtel(self):
        """
        Transforme les 4 maisons en un hôtel lorsque l'on veut en poser une cinquième
        """
        if self.type=="Propriété":
            if self.nb_maison==4:
                self.loyer=round(self.loyer*2,0)
                self.nb_maison=5

class Joueur:
    def __init__(self):
        self.propriétés=[]
        self.argent=0
        self.compteur_prison=0
        self.ncase=0       #On peut rajouter les coordonnées des cases pour déplacer les pions parce qu'on sait sur quelle case on est
        self.case="départ"
        self.csp=0
        self.prison=False

    def verif_argent(self):
        """
        Permet de vérifier si un joueur est en manque d'argent pendant son tour
        """
        if self.argent<0:
            if self.propriétés==[]:
                joueurs.pop(0)
                return("Vous avez fait faillite")
            choix_vente=input("Quelle propriété voulez-vous vendre ? (Faillite pour abandonner)")
            while choix_vente not in self.propriétés.nom and choix_vente!="Faillite":
                if self.propriétés==[]:
                    joueurs.pop(0)
                    return("Vous avez fait faillite")
                choix_vente=input("Vous ne possédez pas cette propriété ou elle n'existe pas. Quelle propriété voulez-vous vendre ? (Faillite pour abandonner)")
                if choix_vente=="Faillite":
                    joueurs.pop(0)
                    return("Vous avez fait faillite")
                else:
                    for i in range (len(self.propriétés)):
                        if self.propriétés[i].nom==choix_vente:
                            propriété=self.propriétés[i]
                            break
                    vendre(self,propriété)

    def acheter(self,propriété):
        for joueur in joueurs:
            if propriété in joueur.propriétés:
                return ("Cette propriété appartient déjà à un joueur")
        if self.argent>=propriété.prix:
            self.propriétés.append(propriété)
            self.argent-=propriété.prix
        else:
            print("Vous n'avez pas assez d'argent")

    def vendre(self,propriété):
        """
        Permet de vendre une propriété, notamment lorsqu'on se trouve en manque d'argent
        """
        self.argent+=propriété.prix//2
        for pro in self.propriétés:
            if pro.nom==propriété.nom:
                self.propriétés.pop(pro)

    def tomber_chez_qqun(self,autre,propriété):
        """
        Gère lorsque le lancer de dé emmène le joueur sur la propriété d'un autre joueur
        """
        if self.argent>=propriété.loyer:
            self.argent-=propriété.loyer
            autre.argent+=propriété.loyer
        else:
            while self.argent<propriété.loyer:
                if self.propriété==[]:
                    autre.argent+=self.argent
                    self.argent=0
                    joueurs.pop(self)
                    return ("Vous avez fait faillite")
                propriété=input("Quelle propriété voulez-vous vendre ?")
                while propriété not in self.propriétés:
                    propriété=input("Cette propriété ne vous appartient pas, quelle propriété voulez-vous vendre ?")
                self.vendre()

def nb_joueurs(nb):
    j1=Joueur()
    j2=Joueur()
    joueurs.append(j1)
    joueurs.append(j2)
    if nb>=3:
        j3=Joueur()
        joueurs.append(j3)
        if nb==4:
            j4=Joueur()
            joueurs.append(j4)

def tellCase(joueur):
    """
    Donne la case sactuelle sur laquelle le joueur est présent
    """
    for prop in propriétés:
        if joueur.ncase==prop.ncase:
            return (prop)


def choix_chance(montant):
    """
    Considère la carte caisse de communauté spéciale "payer 1000 ou tirer une carte chance"
    """
    choix = input("Décidez vous de tirer une carte chance ? (Y/N)")
    if choix=="Y":
        chance(joueur)
    else:
        prime(joueur,montant)

def aller(joueur,case):
    """
    Considère les cartes chance et caisse de communauté "Allez à ... en passant par la case départ"
    """
    joueur.case=case.nom
    if joueur.ncase<case.ncase and joueur.ncase>0:
        joueur.argent+=20000
    joueur.ncase=case.ncase

def aller_sans_départ(joueur,case):
    """
    Considère les cartes chance et caisse de communauté "Allez à ... sans passer par la case départ"
    """
    joueur.case=case.nom
    joueur.ncase=case.ncase

def anniversaire(joueur):
    """
    Considère la carte caisse de communauté "C'est votre anniversaire"
    """
    for player in joueurs:
        if player is not joueur:
            player.argent-=1000
            joueur.argent+=1000

def prime(joueur,montant):
    """
    Considère les cartes chance et caisse de communauté "Vous gagnez ..."
    """
    joueur.argent+=montant

def impôts(joueur,i_maisons,i_hôtels):
    """
    Considère les cartes chance et caisse de communauté "impôts"
    """
    for propriété in joueur.propriétés:
        if propriété.nb_maisons>5:
            joueur.argent-=propriété.nb_maisons*i_maisons
        else:
            joueur.argent-=i_hôtels

def reculer(joueur,nb_cases):
    joueur.ncase-=3
    if joueur.ncase<0:
        joueur.ncase+=40
    joueur.case=propriétés[joueur.ncase].nom

def prendre_csp(joueur):
    """
    Donne une carte sortie de prison lorsque le joueur en tire une
    """
    joueur.csp+=1

def communaute(joueur):
    """
    Considère les cartes caisse de communauté
    """
    action=communautés.pop(0)
    print(action[0])
    if action[0]!="Carte sortie de prison":
        communautés.append(action)
        if "chance" in action[0]:
            choix_chance(joueur,action[1])
        elif "Gagnez" in action[0]:
            prime(joueur,action[1])
        elif "Perdez" in action[0]:
            prime(joueur,action[1])
            joueur.verif_argent()
        elif "Allez" in action[0] and (not "prison" in action[0] or "sans passer par la case départ" in action[0]):
            aller(joueur,action[1])
        elif "prison" in action[0]:
            aller_sans_départ(joueur,action[1])
        elif "Payez des réparations" in action[0]:
            impôts(joueur,action[1])
            joueur.verif_argent()
        elif "Reculez" in action[0]:
            reculer(joueur,action[1])
        elif "anniversaire" in action[0]:
            anniversaire(joueur)
    else:
        prendre_csp(joueur)

def chance(joueur):
    """
    Considère les cartes chance
    """
    action=chances.pop(0)
    print(action[0])
    if action[0]!="Carte sortie de prison":
        communautés.append(action)
        if "Gagnez" in action[0]:
            prime(joueur,action[1])
        elif "Perdez" in action[0]:
            prime(joueur,action[1])
            joueur.verif_argent()
        elif "Allez" in action[0] and not "prison" in action[0]:
            aller(joueur,action[1])
        elif "prison" in action[0]:
            aller_sans_départ(joueur,action[1])
        elif "Payez des réparations" in action[0]:
            impôts(joueur,action[1])
            joueur.verif_argent()
        elif "Reculez" in action[0]:
            reculer(joueur,action[1])
    else:
        prendre_csp(joueur)


def considérer_case(joueur):
    """
    Effectue certaines actions en fonction de la case et si c'est une propriété appartenant au joueur
    """
    prop=tellCase(joueur)
    if prop.type=="propriété":
        if prop in joueur.propriétés:
            choix=input("Voulez-vous ajouter une maison ? (Y/N)")
            if choix=="Y":
                choix2=input("Combien ?")
                if prop.nb_maison+choix2<=4:
                    for i in range(choix2):
                        prop.mettre_une_maison()
                    return ("Vous avez placé",choix2,"maison(s)")
            return ("Vous n'avez pas placé de maison")
        for player in joueurs:
            if (prop in player.propriétés and player!=joueur):
                joueur.tomber_chez_qqun(player,prop)
                return ("Vous avez payé",prop.loyer,"à",player,"...")
        achat=input("Voulez-vous acheter cette case ? (Y/N)")
        if achat=="Y":
            joueur.acheter(prop)
            return ("Vous avez acheté la propriété",prop.nom,"!")
        else:
            return ("Vous avez choisi de ne pas acheter la propriété")
    elif prop.type=="effetP":
        joueur.ncase=10
        print("Vous allez en prison pour 3 tours")
        joueur.compteur_prison=3
        joueur.prison=True
    elif prop.type=="effetI":
        joueur.argent-=20000
    elif prop.type=="effetT":
        joueur.argent-=10000
    elif prop.type=="effetC":
        if Compagnie_d_Eau in joueur.propriétés and Compagnie_d_Electricité in joueur.propriétés:
            joueur.argent-=(1000*(lancer1+lancer2))
        else:
            joueur.argent-=(400*(lancer1+lancer2))
    elif prop.type=="effetCh":
        chance(joueur)
    elif prop.type=="effetCo":
        communaute(joueur)



60)
Rue_Lecourbe=Case("propriété","Rue_Lecourbe",3,575,708,"marron",60)
Rue_de_Vaugirard=Case("propriété","Rue_de_Vaugirard",6,455,708,"bleu_clair",100)
Rue_de_Courcelles=Case("propriété","Rue_de_Courcelles",8,375,708,"bleu_clair",100)
Avenue_de_la_République=Case("propriété","Avenue_de_la_République",9,335,708,"bleu_clair",120)
Boulevard_de_la_Villette=Case("propriété","Boulevard_de_la_Villette",11,282,655,"rose",140)
Avenue_de_Neuilly=Case("propriété","Avenue_de_Neuilly",13,282,575,"rose",140)
Rue_de_Paradis=Case("propriété","Rue_de_Paradis",14,282,535,"rose",160)
Avenue_Mozart=Case("propriété","Avenue_Mozart",16,282,455,"orange",180)
Boulevard_Saint_Michel=Case("propriété","Boulevard_Saint_Michel",18,282,375,"orange",180)
Place_Pigalle=Case("propriété","Place_Pigalle",19,282,335,"orange",200)
Avenue_Matignon=Case("propriété","Avenue_Matignon",21,335,282,"rouge",220)
Boulevard_Malesherbes=Case("propriété","Boulevard_Malesherbes",23,415,282,"rouge",220)
Avenue_Henri_Martin=Case("propriété","Avenue_Henri_Martin",24,455,282,"rouge",240)
Faubourg_Saint_Honoré=Case("propriété","Faubourg_Saint_Honoré",26,535,282,"jaune",260)
Place_de_la_Bourse=Case("propriété","Place_de_la_Bourse",27,575,282,"jaune",260)
Rue_la_Fayette=Case("propriété","Rue_la_Fayette",29,655,282,"jaune",280)
Avenue_de_Breteuil=Case("propriété","Avenue_de_Breteuil",31,708,335,"vert",300)
Avenue_Foch=Case("propriété","Avenue_Foch",32,708,375,"vert",300)
Boulevard_des_Capucines=Case("propriété","Boulevard_des_Capucines",34,708,455,"vert",320)
Avenue_des_Champs_Elysées=Case("propriété","Avenue_des_Champs_Elysées",37,708,575,"bleu",350)
Rue_de_la_Paix=Case("propriété","Rue_de_la_Paix",39,708,655,"bleu",400)
Gare_Montparnasse=Case("propriété","Gare_Montparnasse",5,495,708,"gare",200)
Gare_de_Lyon=Case("propriété","Gare_de_Lyon",15,282,495,"gare",200)
Gare_du_Nord=Case("propriété","Gare_du_Nord",25,495,282,"gare",200)
Gare_Saint_Lazare=Case("propriété","Gare_Saint_Lazare",35,708,495,"gare",200)
Allez_en_Prison=Case("effetP","Allez_en_Prison",30,708,282)
Prison_SimpleVisite=Case("neutre","Prison_SimpleVisite",10,282,708)
Parc_Gratuit=Case("neutre","Parc_Gratuit",20,282,282)
Départ=Case("neutre","Départ",0,708,708)
Taxe_de_Luxe=Case("effetT","Taxe_de_Luxe",38,708,615)
Impôts=Case("effetI","Impôts",4,535,708)
Chance1=Case("effetCh","Chance",7,415,708)
Chance2=Case("effetCh","Chance",22,375,282)
Chance3=Case("effetCh","Chance",36,708,535)
Caisse_de_Communauté1=Case("effetCo","Caisse_de_Communauté",2,615,708)
Caisse_de_Communauté2=Case("effetCo","Caisse_de_Communauté",17,282,415)
Caisse_de_Communauté3=Case("effetCo","Caisse_de_Communauté",33,708,415)
Compagnie_d_Eau=Case("effetC","Compagnie_d_Eau",28,615,282)
Compagnie_d_Electricité=Case("effetC","Compagnie_d_Electricité",12,282,615)

propriétés=[
Boulevard_de_Belleville,
Rue_Lecourbe,
Rue_de_Vaugirard,
Rue_de_Courcelles,
Avenue_de_la_République,
Boulevard_de_la_Villette,
Avenue_de_Neuilly,
Rue_de_Paradis,
Avenue_Mozart,
Boulevard_Saint_Michel,
Place_Pigalle,
Avenue_Matignon,
Boulevard_Malesherbes,
Avenue_Henri_Martin,
Faubourg_Saint_Honoré,
Place_de_la_Bourse,
Rue_la_Fayette,
Avenue_de_Breteuil,
Avenue_Foch,
Boulevard_des_Capucines,
Avenue_des_Champs_Elysées,
Rue_de_la_Paix,
Gare_Montparnasse,
Gare_de_Lyon,
Gare_du_Nord,
Gare_Saint_Lazare,
Allez_en_Prison,
Prison_SimpleVisite,
Parc_Gratuit,
Départ,
Taxe_de_Luxe,
Impôts,
Chance1,
Chance2,
Chance3,
Caisse_de_Communauté1,
Caisse_de_Communauté2,
Caisse_de_Communauté3,
Compagnie_d_Eau,
Compagnie_d_Electricité
]

joueurs = []
nb_j=int(input("Combien y a-t-il de joueurs ? (de 2 à 4)"))
while nb_j<=1 or nb_j>4:
    if nb_j<=1:
        print("Il n'y a pas assez de joueurs")
    elif nb_j>4:
        print("Il y a trop de joueurs")
    nb_j=int(input("Combien y a-t-il de joueurs ? (de 2 à 4)"))
nb_joueurs(nb_j)

argent_d=int(input("Argent de départ ? (de 1500 à 3000)"))
while argent_d<1500 or argent_d>3000:
    if argent_d<1500:
        print("Somme de départ trop petite")
    elif argent_d>3000:
        print("Somme de départ trop grande")
    argent_d=int(input("Argent de départ ? (de 1500 à 3000)"))

chances=[("Gagnez 10000",10000),("Allez à la rue de la Paix",Rue_de_la_Paix),("Payez des réparations : 4000 par maison / 11500 par hôtel",(4000,11500)),("Allez en prison",Allez_en_Prison),
("Gagnez 15000",15000),("Reculez de 3 cases",3),("Allez à la case Départ",Départ),("Gagnez 5000",5000),("Allez à la Gare de Lyon",Gare_de_Lyon),("Perdez 2000",-2000),
("Perdez 1500",-1500),("Allez à l'avenue Henri-Martin",Avenue_Henri_Martin),("Payez des réparations : 2500 par maison / 10000 par hôtel",(2500,10000)),("Allez au Boulevard de la Vilette",Boulevard_de_la_Villette),
("Perdez 15000",-15000),("Carte sortie de prison")]
communautés=[("Perdez 1000 ou tirez une carte chance",-1000),("Perdez 5000",-5000),("Gagnez 10000",10000),("Gagnez 2500",2500),("Gagnez 20000",20000),
("Gagnez 10000",10000),("Carte sortie de prison"),("Allez en prison",Allez_en_Prison),("Gagnez 2000",2000),("Perdez 10000",-10000),("Gagnez 5000",5000),
("Perdez 5000",-5000),("Gagnez 1000",1000),("C'est votre anniversaire, chaque joueur vous verse 1000"),("Allez au boulevard de Belleville sans passer par la case départ",Boulevard_de_Belleville),
("Allez à la case Départ",Départ)]

screen=Screen(1000,1000)
game=Game(screen,joueurs,argent_d)
game.run()
pygame.quit()
