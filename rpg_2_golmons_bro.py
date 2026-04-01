class chr_politiques :
    def __init__( self, name, pv, attack, skill) :
        self.name = name
        self.pv = pv
        self.attack = attack
        self.skill = skill

class chr_vidgames :
    def __init__( self, name, pv, attack, skill) :
        self.name = name
        self.pv = pv
        self.attack = attack
        self.skill = skill

class chr_anime :
    def __init__( self, name, pv, attack, skill ) :
        self.name = name
        self.pv = pv
        self.attack = attack
        self.skill = skill

class chr_historical :
    def __init__( self, name, pv, attack, skill ) :
        self.name = name
        self.pv = pv
        self.attack = attack
        self.skill = skill

class chr_richmen :
    def __init__( self, name, pv, attack, skill ) :
        self.name = name
        self.pv = pv
        self.attack = attack
        self.skill = skill

brigitte_macron = chr_politiques("Brigitte Macron", 80, ["Attaque de la Première Dame de France"], ["Esquive sur talons"])
steve_minecraft = chr_vidgames("Steve de Minecraft", 100, ["Coup d'épée"], ["Manger"])
senku_ishigami = chr_anime("Senku Ishigami", 90, ["Acide sulfurique"], ["Poison"])
joseph_staline = chr_historical("Joseph Staline", 100, ["Goulag"], ["Taxes étatiques"])
bill_gates = chr_richmen("Bill Gates", 90,["Flambée des prix"], ["Fenêtre bouclier"]) #defenestration tu checkeras l'orthographe enculé


def tutorial() :
    print("ceci est le tutoriel")

def pre_rpg() :
    print("""
Bienvenu dans ce rpg de tordus : un monde dans lequel les crossovers sont infinis.
Voulez-vous démarrer le tutoriel pour apprendre à jouer au jeu ou bien voulez-vous directement combattre? :
Sur votre clavier, appuyez sur 'O' pour dire oui ou bien sur 'N' pour dire non. 
          """)
    if action == "O" :
        tutorial()
        return "choix_tuto_positif"
    elif action == "N" :
        rpg()
        return "choix_tuto_negatif"
    else :
        return "erreur touche"

def rpg():
     print("cela sera bientôt le rpg ;)")
    



pre_rpg()


while True :
    action = input()
    if action == "exit" :
        print("Ben alors? Vous partez déjà?")
        break
    elif case == "erreur touche" :
        print("Mauvaise touche, recommencez.")
    elif case == "choix_tuto_negatif" :
        rpg()
    elif case == "choix_tuto_positif" :
        tutorial()

        