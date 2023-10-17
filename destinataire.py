# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 13:45:49 2023

@author: Thomas MORNARD

Définition de la classe Destinataire
"""

# Définition des classes

class Destinataire:
    """Cette classe permet de définir les éléments qui contituent un destinataire
    
    Attributs :
        - nom         : string
        - adresse     : string
        - code postal : int - Le code postal est un entier positif à cinq chiffres
        - ville       : string
        - pays        : string
        
    Méthodes de la classe :
        - __init__        : Constructeur de la classe
        - __verif_valeurs : Vérifie que les valeurs passées en entrée du 
                            constructeur sont cohérentes
        - lecture_dest    : Renvoie la valeur des attributs d'un objet de type 
                            Destinataire
    """
    
    def __init__(self, p_nom, p_adresse, p_cp, p_ville, p_pays):
        """Création d'un destinataire.
        
        Entrées :
            - p_nom     : string - nom du destinataire sous la forme d'une 
                                   chaine de caractères
            - p_adresse : string - adresse du destinataire sous la forme d'une 
                                   chaine de caractères
            - p_cp      : int    - code postal du destinataire sur cinq chiffres
            - p_ville   : string - ville du destinataire sous la forme d'une 
                                   chaine de caractères
            - p_pays    : string - pays du destinataire sous la forme d'une 
                                   chaine de caractères
                                   
        Sorties :
            N/A
        """
        # On vérifie que les données passées en entrée respectent bien les
        # propriétés attendues
        self.__verif_valeurs(p_nom, p_adresse, p_cp, p_ville, p_pays)
        
        # création de l'objet
        self.nom     = p_nom
        self.adresse = p_adresse
        self.cp      = p_cp
        self.ville   = p_ville
        self.pays    = p_pays
        
        
    def __verif_valeurs(self, p_nom, p_adresse, p_cp, p_ville, p_pays):
        """Vérifie que les données passées en entrée du constructeur de la classe
           respectent les propriétés suivantes :
               1. Les valeurs données sont de type attendu (ceci inclus le cas
                  où la variable est null / de type NoneType)
               2. Le code postal est bien un entier positif entre 0 et 99999
               
        #################################################################
        # Exceptions pouvant être levées :
        #    - TypeError (erreur sur le type d'une variable en entrée)
        #    - ValueError (erreur sur la valeur du code postal)
        #################################################################
        
        Entrées :
            - p_nom     : string - nom du destinataire sous la forme d'une 
                                   chaine de caractères
            - p_adresse : string - adresse du destinataire sous la forme d'une 
                                   chaine de caractères
            - p_cp      : int    - code postal du destinataire sur cinq chiffres
            - p_ville   : string - ville du destinataire sous la forme d'une 
                                   chaine de caractères
            - p_pays    : string - pays du destinataire sous la forme d'une 
                                   chaine de caractères
                                   
        Sorties :
            N/A
        """
        # On  vérifie que les variables en entrée sont bien du type attendu
        if(type(p_nom) != str):
            raise TypeError("Le nom doit être une chaine de caractères !")
            
        if(type(p_adresse) != str):
            raise TypeError("L'adresse doit être une chaine de caractères !")
            
        if(type(p_cp) != int):
            raise TypeError("Le code postal doit être un entier positif entre 0 et 99999 !")
            
        if(type(p_ville) != str):
            raise TypeError("La ville doit être une chaine de caractères !")
            
        if(type(p_pays) != str):
            raise TypeError("Le pays doit être une chaine de caractères !")
            
        # On vérifie que le code postal est bien un nombre positif à cinq chiffres
        if(p_cp < 0 or p_cp > 99999):
            raise ValueError("Le code postal doit être compris entre 0 et 99999 !")
        
        
    def lecture_dest(self):
        """Renvoie un tuple contenant l'ensemble des attributs d'objets dans
           l'ordre : nom, adresse, cp, ville, pays.
           
        Entrées :
            N/A
              
        Sorties :
            - tuple - Tuple contenant la valeur des attributs de l'objet dans
                      l'ordre indiqué ci-dessus
        """
        return(self.nom, self.adresse, self.cp, self.ville, self.pays)
    
    
#-----------------------------------------------------------------------------

# Partie principale du programme

if(__name__ == "__main__"):
    print("Test des éléments qui composent le fichier destinataire.py :", end="\n\n")
    print("Test des méthodes de la classe Destinataire :", end="\n\n")
    
    # Construction d'un objet de la classe Destinataire
    try:
        p_nom     = "Nom destinataire"
        p_adresse = "Adresse destinataire"
        p_cp      = 0
        p_ville   = "Ville destinataire"
        p_pays    = "Pays destinataire"
        d         = Destinataire(p_nom, p_adresse, p_cp, p_ville, p_pays)
        
        # Lecture des données ainsi créées
        print("Contenu du destinataire que l'on a créé")
        t = d.lecture_dest()
        for elem in t:
            print(elem)
    
    except TypeError as erreur:
        print("Erreur lors de la création d'un objet de type Destinataire :")
        print(erreur.args[0])
        
    except ValueError as erreur:
        print("Erreur lors de la création d'un objet de type Destinataire :")
        print(erreur.args[0])
        
    # TODO : Faire les tests dans le cas où les paramètres donnés ne sont pas du
    #        bon type
    
    # TODO : Faire les tests dans le cas où le code postal est inférieur à 0
    #        ainsi que dans le cas où il est plus grand que 100000