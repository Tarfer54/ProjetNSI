import pygame
import random

pygame.init()
blank=(255,255,255)
MonopolyFont=pygame.font.Font("MONOPOLY_INLINE.ttf", 30)
PropriétéFont=pygame.font.Font("MONOPOLY_INLINE.ttf", 15)
max_couleur={
        "marron":2,
        "bleu_clair":3,
        "rose":3,
        "orange":3,
        "rouge":3,
        "jaune":3,
        "vert":3,
        "bleu":2,
        "gare":4
        }

loyers={1:[2,10,30,90,160,250],
        3:[4,20,60,180,320,450],
        6:[6,30,90,270,400,550],
        8:[6,30,90,270,400,550],
        9:[8,40,100,300,450,600],
        11:[10,50,150,450,625,750],
        13:[10,50,150,450,625,750],
        14:[12,60,180,500,700,900],
        16:[14,70,200,550,750,950],
        18:[14,70,200,550,750,950],
        19:[16,80,220,600,800,1000],
        21:[18,90,250,700,875,1050],
        23:[18,90,250,700,875,1050],
        24:[20,100,300,750,925,1100],
        26:[22,110,330,800,975,1150],
        27:[22,110,330,800,975,1150],
        29:[24,120,360,850,1025,1200],
        31:[26,130,390,900,1100,1275],
        32:[26,130,390,900,1100,1275],
        34:[28,150,450,1000,1200,1400],
        37:[35,175,500,1100,1300,1500],
        39:[50,200,600,1400,1700,2000]
        }

class Game:
    def __init__(self, screen,joueurs,argent_d):
        self.screen = screen
        self.running = True
        self.joueurs=joueurs
        for joueur in self.joueurs:
            joueur.argent=argent_d
            joueur.affichage()
        self.clock = pygame.time.Clock()

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        lancer1=random.randint(1,6)
                        lancer2=random.randint(1,6)
                        screen.tour(joueurs[0],lancer1,lancer2)

    def display(self):
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_events()
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
        if nb_j>=3:
            self.init.blit(self.pion_r,(690,725))
        if nb_j==4:
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

    def tour(self,joueur,lancer1,lancer2):
        """
        Permet de lancer un tour de jeu
        """
        self.dé(lancer1,lancer2)
        if len(joueurs)==1:
            self.running=False
        if not joueur.prison:
            joueur.ncase+=lancer1+lancer2
        if joueur.ncase>=40:
            joueur.ncase-=40
            joueur.argent+=200
        self.init.fill((0,0,0))
        self.init.blit(self.plateau,(250,250))
        self.init.blit(self.dé_1,(550,330))
        self.init.blit(self.dé_2,(330,550))
        for j in joueurs:
            j.actualiser_pion(j.ncase,propriétés)
            j.affichage()
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
                        joueur.prison=False
                    else:
                        joueur.argent-=50
                        joueur.compteur_prison=0
                        joueur.prison=False
                else:
                    joueurA=joueurs.pop(0)
                    joueurs.append(joueurA)
        while lancer1==lancer2:
            if joueur.prison:
                break
            compteur_double+=1
            if compteur_double==3:
                joueur.ncase=10
                compteur_prison=3
                joueur.prison=True
                return ("Vous allez en prison")
            else:
                considérer_case(joueur,lancer1,lancer2)
                lancer1=random.randint(1,6)
                lancer2=random.randint(1,6)
                self.dé(lancer1,lancer2)
                joueur.ncase+=lancer1+lancer2
                if joueur.ncase>=40:
                    joueur.ncase-=40
                    joueur.argent+=200
                self.init.fill((0,0,0))
                self.init.blit(self.plateau,(250,250))
                self.init.blit(self.dé_1,(550,330))
                self.init.blit(self.dé_2,(330,550))
                for j in joueurs:
                    j.actualiser_pion(j.ncase,propriétés)
                    j.affichage()
                pygame.display.flip()
        considérer_case(joueur,lancer1,lancer2)
        joueurA=joueurs.pop(0)
        joueurs.append(joueurA)

class Case:
    def __init__(self,type,nom,ncase,x,y,couleur=None,loyer=None):
        self.nom=nom
        self.type=type
        self.couleur=couleur
        self.x=x
        self.y=y
        if self.couleur!=None and self.couleur!="gare" and self.couleur!="compagnie":
            self.prix=loyer
            self.loyer=loyers[ncase][0]
            self.nb_maison=0
        elif self.couleur=="gare":
            self.prix=200
        elif self.couleur=="compagnie":
            self.prix=150
        self.ncase=ncase
        self.coordonnées=(x,y)

    def mettre_une_maison(self,joueur):
        """
        Ajoute une maison sur une propriété si elle n'en possède pas déjà 4
        """
        if self.type=="propriété" and self.couleur!="gare" and self.couleur!="compagnie":
            if self.nb_maison<5:
                if self.couleur=="marron" or self.couleur=="bleu_clair":
                    argent=50
                elif self.couleur=="rose" or self.couleur=="orange":
                    argent=100
                elif self.couleur=="rouge" or self.couleur=="jaune":
                    argent=150
                elif self.couleur=="vert" or self.couleur=="bleu":
                    argent=200
                if joueur.argent-argent<0:
                    return "Vous êtes sur la paille"
                self.nb_maison+=1
                self.loyer=loyers[self.ncase][self.nb_maison]
                joueur.argent-=argent
            else:
                raise IndexError('Trop de maisons')

class Joueur:
    def __init__(self,couleur):
        self.propriétés=[]
        self.n_propriétés=[]
        self.quan_propriétés={
        "marron":0,
        "bleu_clair":0,
        "rose":0,
        "orange":0,
        "rouge":0,
        "jaune":0,
        "vert":0,
        "bleu":0,
        "gare":0,
        "compagnie":0
        }
        self.argent=0
        self.compteur_prison=0
        self.ncase=0
        self.case=Départ
        self.csp=0
        self.prison=False
        self.couleur=couleur
        if self.couleur=="vert":
            self.pion=screen.pion_v
        elif self.couleur=="bleu":
            self.pion=screen.pion_b
        elif self.couleur=="rouge":
            self.pion=screen.pion_r
        elif self.couleur=="jaune":
            self.pion=screen.pion_j

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
            self.n_propriétés.append(propriété.nom)
            self.argent-=propriété.prix
            self.quan_propriétés[propriété.couleur]+=1
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
                self.n_propriétés.pop(pro.nom)

    def tomber_chez_qqun(self,autre,propriété,lancer1,lancer2):
        """
        Gère lorsque le lancer de dé emmène le joueur sur la propriété d'un autre joueur
        """
        if propriété.couleur=="gare":
            if self.argent>=(2**(autre.quan_propriétés[propriété.couleur])-1)*25:
                self.argent-=(2**(autre.quan_propriétés[propriété.couleur])-1)*25
                autre.argent+=(2**(autre.quan_propriétés[propriété.couleur])-1)*25
                Gare_de_Lyon.loyer=25*self.quan_propriétés["gare"]
                Gare_du_Nord.loyer=25*self.quan_propriétés["gare"]
                Gare_Montparnasse.loyer=25*self.quan_propriétés["gare"]
                Gare_Saint_Lazare.loyer=25*self.quan_propriétés["gare"]
        elif propriété.couleur=="compagnie":
            if Compagnie_d_Eau in autre.propriétés and Compagnie_d_Electricité in autre.propriétés:
                self.argent-=10*(lancer1+lancer2)
                autre.argent+=10*(lancer1+lancer2)
                Compagnie_d_Eau.loyer=10*(lancer1+lancer2)
                Compagnie_d_Electricité.loyer=10*(lancer1+lancer2)
            else:
                self.argent-=4*(lancer1+lancer2)
                autre.argent+=4*(lancer1+lancer2)
                Compagnie_d_Eau.loyer=4*(lancer1+lancer2)
                Compagnie_d_Electricité.loyer=4*(lancer1+lancer2)
        else:
            if autre.quan_propriétés[propriété.couleur]==max_couleur[propriété.couleur]:
                if self.argent>=propriété.loyer*2:
                    self.argent-=propriété.loyer*2
                    autre.argent+=propriété.loyer*2
            elif self.argent>=propriété.loyer:
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

    def actualiser_pion(self,ncase,propriétés):
        for prop in propriétés:
            if ncase==prop.ncase:
                if self.couleur=="vert":
                    screen.init.blit(self.pion,(prop.x-3,prop.y-3))
                elif self.couleur=="bleu":
                    screen.init.blit(self.pion,(prop.x-3,prop.y+3))
                elif self.couleur=="rouge":
                    screen.init.blit(self.pion,(prop.x+3,prop.y-3))
                elif self.couleur=="jaune":
                    screen.init.blit(self.pion,(prop.x+3,prop.y+3))

    def affichage(self):
        if self.couleur=="vert":
            self.affichage1=MonopolyFont.render("Vert:", True, blank)
            self.affichage2=MonopolyFont.render("argent:", True, blank)
            self.affichage3=MonopolyFont.render(str(self.argent), True, blank )
            self.affichage4=MonopolyFont.render("propriétés:", True, blank)
            self.affichage5=PropriétéFont.render(str(self.n_propriétés), True, blank)
            screen.init.blit(self.affichage1,(10,10))
            screen.init.blit(self.affichage2,(120,10))
            screen.init.blit(self.affichage3,(210,10))
            screen.init.blit(self.affichage4,(10,40))
            screen.init.blit(self.affichage5,(130,50))
        elif self.couleur=="bleu":
            self.affichage1=MonopolyFont.render("Bleu:", True, blank)
            self.affichage2=MonopolyFont.render("argent:", True, blank)
            self.affichage3=MonopolyFont.render(str(self.argent), True, blank )
            self.affichage4=MonopolyFont.render("propriétés:", True, blank)
            self.affichage5=PropriétéFont.render(str(self.n_propriétés), True, blank)
            screen.init.blit(self.affichage1,(10,90))
            screen.init.blit(self.affichage2,(120,90))
            screen.init.blit(self.affichage3,(210,90))
            screen.init.blit(self.affichage4,(10,120))
            screen.init.blit(self.affichage5,(130,130))
        elif self.couleur=="rouge":
            self.pion=screen.pion_r
            self.affichage1=MonopolyFont.render("Rouge:", True, blank)
            self.affichage2=MonopolyFont.render("argent:", True, blank)
            self.affichage3=MonopolyFont.render(str(self.argent), True, blank )
            self.affichage4=MonopolyFont.render("propriétés:", True, blank)
            self.affichage5=PropriétéFont.render(str(self.n_propriétés), True, blank)
            screen.init.blit(self.affichage1,(10,750))
            screen.init.blit(self.affichage2,(120,750))
            screen.init.blit(self.affichage3,(210,750))
            screen.init.blit(self.affichage4,(10,780))
            screen.init.blit(self.affichage5,(130,790))
        elif self.couleur=="jaune":
            self.affichage1=MonopolyFont.render("Jaune:", True, blank)
            self.affichage2=MonopolyFont.render("argent:", True, blank)
            self.affichage3=MonopolyFont.render(str(self.argent), True, blank )
            self.affichage4=MonopolyFont.render("propriétés:", True, blank)
            self.affichage5=PropriétéFont.render(str(self.n_propriétés), True, blank)
            screen.init.blit(self.affichage1,(10,830))
            screen.init.blit(self.affichage2,(120,830))
            screen.init.blit(self.affichage3,(210,830))
            screen.init.blit(self.affichage4,(10,860))
            screen.init.blit(self.affichage5,(130,870))

def nb_joueurs(nb):
    j1=Joueur("vert")
    j2=Joueur("bleu")
    joueurs.append(j1)
    joueurs.append(j2)
    if nb>=3:
        j3=Joueur("rouge")
        joueurs.append(j3)
        if nb==4:
            j4=Joueur("jaune")
            joueurs.append(j4)

def tellCase(joueur):
    """
    Donne la case actuelle sur laquelle le joueur est présent
    """
    for prop in propriétés:
        if joueur.ncase==prop.ncase:
            return (prop)

def choix_chance(montant):
    """
    Considère la carte caisse de communauté spéciale "payer 10 ou tirer une carte chance"
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
    if joueur.ncase>case.ncase and joueur.ncase>0:
        joueur.argent+=200
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
            player.argent-=10
            joueur.argent+=10

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
        if propriété.nb_maison>5:
            joueur.argent-=propriété.nb_maison*i_maisons
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
    action=cartes_communautés.pop(0)
    print(action[0])
    if action[0]!="Carte sortie de prison":
        cartes_communautés.append(action)
        if "chance" in action[0]:
            choix_chance(action[1])
        elif "Gagnez" in action[0]:
            prime(joueur,action[1])
        elif "Perdez" in action[0]:
            prime(joueur,action[1])
            joueur.verif_argent()
        elif "Allez" in action[0] and (not "prison" in action[0] or "sans passer par la case départ" in action[0]):
            aller(joueur,action[1])
        elif "prison" in action[0]:
            aller_sans_départ(joueur,action[1])
            joueur.compteur_prison=3
            joueur.prison=True
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
    action=cartes_chances.pop(0)
    print(action[0])
    if action[0]!="Carte sortie de prison":
        cartes_chances.append(action)
        if "Gagnez" in action[0]:
            prime(joueur,action[1])
        elif "Perdez" in action[0]:
            prime(joueur,action[1])
            joueur.verif_argent()
        elif "Allez" in action[0] and not "prison" in action[0]:
            aller(joueur,action[1])
        elif "prison" in action[0]:
            aller_sans_départ(joueur,action[1])
            joueur.compteur_prison=3
            joueur.prison=True
        elif "Payez des réparations" in action[0]:
            impôts(joueur,action[1][0],action[1][1])
            joueur.verif_argent()
        elif "Reculez" in action[0]:
            reculer(joueur,action[1])
    else:
        prendre_csp(joueur)

def considérer_case(joueur,lancer1,lancer2):
    """
    Effectue certaines actions en fonction de la case et si c'est une propriété appartenant au joueur
    """
    prop=tellCase(joueur)
    if prop.type=="propriété":
        if prop in joueur.propriétés and prop.couleur!="gare" and prop.couleur!="compagnie":
            choix=input("Voulez-vous ajouter une maison ? (Y/N)")
            if choix=="Y" or choix=="y":
                choix2=input("Combien ?")
                if prop.nb_maison+int(choix2)<=4:
                    for i in range(int(choix2)):
                        prop.mettre_une_maison(joueur)
                    return ("Vous avez placé",choix2,"maison(s)")
            return ("Vous n'avez pas placé de maison")
        for player in joueurs:
            if (prop in player.propriétés and player!=joueur):
                joueur.tomber_chez_qqun(player,prop,lancer1,lancer2)
                return ("Vous avez payé",prop.loyer,"à",player,"...")
        achat=input("Voulez-vous acheter cette case ? (Y/N)")
        if achat=="Y" or achat=="y":
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
        joueur.argent-=200
    elif prop.type=="effetT":
        joueur.argent-=100
    elif prop.type=="effetCh":
        chance(joueur)
    elif prop.type=="effetCo":
        communaute(joueur)

Boulevard_de_Belleville=Case("propriété","Boulevard_de_Bellevile",1,655,708,"marron",60)
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
Compagnie_d_Eau=Case("propriété","Compagnie_d_Eau",28,615,282,"compagnie")
Compagnie_d_Electricité=Case("propriété","Compagnie_d_Electricité",12,282,615,"compagnie")

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

cartes_chances=[("Gagnez 100",100),("Allez à la rue de la Paix",Rue_de_la_Paix),("Payez des réparations : 40 par maison / 115 par hôtel",(40,115)),("Allez en prison",Prison_SimpleVisite),
("Gagnez 150",150),("Reculez de 3 cases",3),("Allez à la case Départ",Départ),("Gagnez 50",50),("Allez à la Gare de Lyon",Gare_de_Lyon),("Perdez 20",-20),
("Perdez 15",-15),("Allez à l'avenue Henri-Martin",Avenue_Henri_Martin),("Payez des réparations : 25 par maison / 100 par hôtel",(25,100)),("Allez au Boulevard de la Vilette",Boulevard_de_la_Villette),
("Perdez 150",-150),("Carte sortie de prison")]
cartes_communautés=[("Perdez 10 ou tirez une carte chance",-10),("Perdez 50",-50),("Gagnez 100",100),("Gagnez 25",25),("Gagnez 200",200),
("Gagnez 100",100),("Carte sortie de prison"),("Allez en prison",Prison_SimpleVisite),("Gagnez 20",20),("Perdez 100",-100),("Gagnez 50",50),
("Perdez 50",-50),("Gagnez 10",10),("C'est votre anniversaire, chaque joueur vous verse 10"),("Allez au boulevard de Belleville sans passer par la case départ",Boulevard_de_Belleville),
("Allez à la case Départ",Départ)]

random.shuffle(cartes_chances)
random.shuffle(cartes_communautés)

joueurs = []
nb_j=int(input("Combien y a-t-il de joueurs ? (de 2 à 4)"))
while nb_j<=1 or nb_j>4:
    if nb_j<=1:
        print("Il n'y a pas assez de joueurs")
    elif nb_j>4:
        print("Il y a trop de joueurs")
    nb_j=int(input("Combien y a-t-il de joueurs ? (de 2 à 4)"))


argent_d=int(input("Argent de départ ? (de 1500 à 3000)"))
while argent_d<1500 or argent_d>3000:
    if argent_d<1500:
        print("Somme de départ trop petite")
    elif argent_d>3000:
        print("Somme de départ trop grande")
    argent_d=int(input("Argent de départ ? (de 1500 à 3000)"))

screen=Screen(1000,1000)
nb_joueurs(nb_j)
game=Game(screen,joueurs,argent_d)
game.run()
pygame.quit()
