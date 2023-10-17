# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:07:12 2023

@author: Thomas MORNARD

Définition d'une commande en utilisant les classes Destinataire et Date
"""

# Imports effectués

from date         import Date
from destinataire import Destinataire


#----------------------------------------------------------------------------

# Définition des classes

class Commande:
    """Cette classe permet de définir les différents éléments qui constiturons
       une commande de bananes.
    
    Attributs :
        - num_commande : int
        - destinataire : Destinataire
        - date         : Date
        - quantite     : int   - La quantité de bananes commandée est un entier
                                 compris entre 25 et 10000 qui est un multiple 
                                 de 25
        - prix         : float - Calculé automatiquement lors de la création
                                 d'un objet de type Commande
        
    Méthodes de la classe
        - lecture_commande : Renvoie les éléments qui composent une commande
    """
    
    def __init__(self, p_num_commande, p_destinataire, p_date, p_quantite):
        """Création d'une commande
        
        Entrées :
            - p_num_commande : int          - Numéro de la commande
            - p_destinataire : Destinataire - Destinataire de la commande
            - p_date         : Date         - Date de la livraison
            - p_quantite     : int          - Quantité de bananes à livrer
            
        Sorties :
            N/A
        """
        # On vérifie que la quantité de bananes commandées est bien un entier
        # compris entre 25 et 10000 qui est un multiple de 25
        self.__verif_valeurs(p_num_commande, p_destinataire, p_date, p_quantite)
        
        # Création de l'objet de type Commande
        self.num_commande = p_num_commande
        self.destinataire = p_destinataire
        self.date         = p_date
        self.quantite     = p_quantite
        # Le prix à facturer est déterminé en fonction de la quantité commandée
        # Le prix est égal à 2.5 fois la valeur de p_quantite
        self.prix         = 2.5 * self.quantite
        
        
    def __verif_valeurs(self, p_num_commande, p_destinataire, p_date, p_quantite):
        """Vérifie que les valeurs passées en entrée respectent les propriétés
           suivantes :
               1. Les valeurs passées en entrée sont bien du type attendu
               2. Le numéro de commande est un entier strictement positif
               3. La quantité de bananes commandée est un nombre strictement
                  positif inférieur à 10000 et est un multiple de 25
                  
        #################################################################
        # Exceptions pouvant être levées :
        #    - TypeError (erreur sur le type d'une variable en entrée)
        #    - ValueError (erreur sur la valeur d'une variable en entrée)
        #################################################################
        
        Entrées :
            - p_num_commande : int          - Numéro de la commande
            - p_destinataire : Destinataire - Destinataire
            - p_date         : Date         - Date de livraison
            - p_quantite     : int          - Quantité de bananes commandée
            
        Sorties :
            N/A
        """
        # On vérifie que les valeurs passées en entrée sont bien du type attendu
        if(type(p_num_commande) != int):
            raise TypeError("Le numéro de commande doit être un entier strictement positif !")
        
        if(type(p_destinataire) != Destinataire):
            raise TypeError("Erreur dans les paramètres du destinataire !")
            
        if(type(p_date) != Date):
            raise TypeError("Erreur sur les paramètres qui composent la date !")
            
        if(type(p_quantite) != int):
            raise TypeError("La quantité commandée doit être un entier strictement positif !")
            
        # On vérifiera que le numérode commande est bien un entier strictement
        # positif
        if(p_num_commande < 0):
            raise ValueError("Le numéro de commande doit être un entier strcitement positif !")
        
        # On vérifie que la valeur de p_quantite est bien à la fois dans
        # l'intervalle [25;10000]
        if(p_quantite < 25 or p_quantite > 10000):
            raise ValueError("La quantité de bananes commandées doit être comprise entre 25 et 10000 !")
            
        if(p_quantite%25 != 0):
            raise ValueError("La quantité de bananes commandée doit être un multiple de 25 !")
        
        
    def lecture_commande(self):
        """Renvoie les éléments qui composent une commande sous la forme d'un
        
        Entrées :
            N/A
            
        Sorties :
            - tuple - Valeurs des attribut de l'objet de type Commande dans 
                      l'ordre suivant : destinataire, date, quantite, prix
        """
        return (self.num_commande, self.destinataire.lecture_dest(), self.date.lecture_date(), self.quantite, self.prix)


#----------------------------------------------------------------------------

# Partie principale du programme

if(__name__ == "__main__"):
    print("Test des fonctionnalitées du fichier commande.py :",end="\n\n")
    
    print("Test des méthodes de la classe Commande")
    
    # Création du destinataire de la commande
    try:
        p_nom          = "Thomas MORNARD"
        p_adresse      = "42 rue des plantes en pot"
        p_cp           = 7777
        p_ville        = "Laoujabite"
        p_pays         = "France"
        p_destinataire = Destinataire(p_nom, p_adresse, p_cp, p_ville, p_pays)
        
    except TypeError as erreur:
        print("Erreur sur le destinataire :")
        print(erreur.args[0])
        
    except ValueError as erreur:
        print("Erreur sur le destinataire :")
        print(erreur.args[0])
    
    # Création de la date de livraison
    try :
        p_jour  = 1
        p_mois  = 1
        p_annee = 2000
        p_date  = Date(p_jour, p_mois, p_annee)
    
    except TypeError as erreur:
        print("Erreur sur la date de livraison :")
        print(erreur.args[0])
        
    except ValueError as erreur:
        print("Erreur sur la date de livraison :")
        print(erreur.args[0])
    
    # Création de la commande
    try:
        p_num_commande = 1
        p_quantite = 100
        com = Commande(p_num_commande, p_destinataire, p_date, p_quantite)
        
        # Lecture de la commande
        print("Contenu de la commande")
        for elem in com.lecture_commande():
            print(elem)
        
    except TypeError as erreur:
        print("Erreur lors de la construction de la commande :")
        print(erreur.args[0])
        
    except ValueError as erreur:
        print("Erreur lors de la construction de la commande :")
        print(erreur.args[0])    