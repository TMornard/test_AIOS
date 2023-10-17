# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:09:04 2023

@author: Thomas MORNARD

Création de la classe ListeCommande et résliation des fonctionnalitées demandées
"""

# Imports effectués

from commande     import Commande
from date         import Date
from destinataire import Destinataire


#-----------------------------------------------------------------------------

# Définition des classes

class ListeCommande:
    """Cette classe permet de définir une liste de commandes et d'effectuer les
       actions suivantes :
           - Consulter une commande
           - Ajouter une commande à la liste
           - Modifier une commande dans la liste
           - Supprimer une commande de la liste
           
    Attributs :
        - liste_commandes : list - Liste de toutes les commandes
        
    Méthodes de la liste :
        - __init__         : constructeur de la classe
        - __list_num_com   : Renvoie la liste de tous les numéros de commandes
        - lecture_commande : Lecture d'une commande dans la liste
        - ajout_commande   : Ajout d'une commande dans la liste
        - modif_commande   : Modifie une commande dans la liste
        - supp_commande    : Supprime une commande de la liste
    """
    
    def __init__(self):
        """Création d'une liste vide destinée à contenir toutes les commandes.
        
        Entrées :
            N/A
            
        Sorties :
            N/A
        """
        self.liste_commandes = []
        
    
    def __list_num_com(self):
        """Renvoie la liste de tous les numéros de commande présents dans la
           liste des commandes.
           
        Entrées :
            N/A
            
        Sorties :
            list_num_com : list - Liste des numéros de commande
        """
        return [t.num_commande for t in self.liste_commandes]
        
        
    def ajout_commande(self, p_destinataire, p_date, p_quantite):
        """Ajoute une commande dans la liste.
        
        #################################################################
        # Exceptions pouvant être levées :
        #    - TypeError (erreur sur le type d'une variable en entrée)
        #    - ValueError (erreur sur la valeur d'une variable en entrée)
        #################################################################
        
        Entrées :
            - p_destinataire : Destinataire - Destinataire de la commande
            - p_date         : Date         - Date de livraison
            - p_quantite     : int          - Quantité de bananes commandées
            
        Sorties :
            N/A
        """
        # Le numéro de la nouvelle commande est obtenue en ajoutant 1 au plus
        # grand numéro de commande présent dans la liste
        # Si la liste des numérs de commande est vide on démarre à 1
        liste = self.__list_num_com()
        
        if(len(liste) == 0):
            p_num_commande = 1
        else:
            liste.sort()
            p_num_commande = liste[-1] + 1        
        
        # On tente de créer une commande et de l'ajouter dans la liste
        try:
            com = Commande(p_num_commande, p_destinataire, p_date, p_quantite)
            self.liste_commandes.append(com)
            
        except TypeError as erreur:
            print("Ajout commande : erreur lors de la création d'une commande :")
            print(erreur.args[0])
            
        except ValueError as erreur:
            print("Ajout commande : erreur lors de la création d'une commande :")
            print(erreur.args[0])
        
        
    def lecture_commande(self, p_num_commande):
        """Lit les données composant la commande référencée par son numéro de
           commande et affiche les informations sur le terminal.
        
        ################################################
        # Exceptions pouvant être levées :
        #   - ValueError (erreur sur une valeur donnée)
        ################################################
        
        Entrées :
            - p_num_commande : int - Numéro de la commande à lire
            
        Sortie :
            N/A
            
        Dans le cas où le numéro de commande fourni n'apparait pas dans la liste
        des commandes, on lèvera une erreur de type ValueError.
        """
        # On reagrde si le numéro de commande donné fait partie de ceux qui sont
        # présents dans la liste
        liste_num = self.__list_num_com()
        
        # Si le numéro de commande n'apparait pas, on lève une erreur
        if not (p_num_commande in liste_num):
            raise ValueError("Le numéro de commande est incorrect !")
            
        # Si le numérode commande apparait, on récupère les données qui sont à
        # la même position dans la liste des commandes
        indice = liste_num.index(p_num_commande)
        com = self.liste_commandes[indice]
        
        # On affiche les données présentes dans la commande
        donnees_dest = com.destinataire.lecture_dest()
        
        print("Numéro de commande       :", com.num_commande)
        print("Nom du destinataire      :", donnees_dest[0])
        print("Adresse destinataire     :", donnees_dest[1])
        print("Code postal destinataire :", donnees_dest[2])
        print("Ville destinataire       :", donnees_dest[3])
        print("Pays destinataire        :", donnees_dest[4])
        print("Date de livraison        :", com.date.lecture_date())
        print("Quantité commandée       :", com.quantite)
        print("Prix à payer             :", com.prix, end="\n\n")
    
    
    def modif_commande(self, p_num_commande, p_destinataire, p_date, p_quantite):
        """Modifie une commande présente dans la liste. La commande est référencée
           par son numéro de commande.
           
        ####################################################
        # Exceptions pouvant être levées :
        #   - TypeError (erreur sur le type d'une variable)
        #   - ValueError (erreur sur une valeur donnée)
        ####################################################
          
        Entrées :
            - p_num_commande : int          - Numéro de la commande
            - p_destinataire : Destinataire - Destinataire
            - p_date         : Date         - Date de livraison
            - p_quantite     : int          - Quantité commandée
            
        Sortie :
            N/A
            
        NB : Dans la version actuelle du programme, il faut refournir tous les
        éléments pour reconsttuer la commande depuis 0. A terme, il faudrait
        plusieurs fonctions qui permettraient de modifier seulement un paramètre
        (seulement l'adresse de livraison par exemple)
         
        On vérifiera que le numérode commande donné est bien associé à une
        commande déjà existante. Dans le cas contraire, on lèvera une exception
        de type ValueError.
        """
        # on vérifie que le numéro de commande est valide
        if(type(p_num_commande) != int):
            raise TypeError("Le numéro de commande doit être un entier strictement positif !")
        
        liste_num = self.__list_num_com()
        if not (p_num_commande in liste_num):
            raise ValueError("Le numéro de commande donné n'est pas valide !")
        
        # Si il est valide, on retient l'emplacement de la commande dans la liste 
        # et on recréé une nouvelle commande avec les bons paramètres
        indice_commade = liste_num.index(p_num_commande)
        com            = Commande(p_num_commande, p_destinataire, p_date, p_quantite)
        self.liste_commandes[indice_commade] = com
    
    
    def supp_commande(self, p_num_commande):
        """Supprime la commande correspondant au numéro de commande de la liste.

        ####################################################
        # Exceptions pouvant être levées :
        #   - TypeError (erreur sur le type d'une variable)
        #   - ValueError (erreur sur une valeur donnée)
        ####################################################
        
        Entrée :
            - p_num_commande : int - Numéro de la commande à supprimer
            
        Sortie :
            N/A
        """
        # On vérifie que le numéro de commande fourni est valide
        if(type(p_num_commande) != int):
            raise TypeError("Le numéro de commande doit être un entire strictement positif !")
            
        liste_num = self.__list_num_com()
        if not(p_num_commande in liste_num):
            raise ValueError("Le numéro de commande n'est pas valide !")
            
        # Si le numéro de commande est valide, on récupère l'indice de la
        # commande correspondante dans la liste et on la supprime
        self.liste_commandes.pop(liste_num.index(p_num_commande))


#-----------------------------------------------------------------------------

# Partie principale du programme

if(__name__ == "__main__"):
    print("Test des fonctionnalitées implémentées dans le fichier fonctions.py :", end="\n\n")
    
    print("Test de la création de la liste des commandes :", end="\n\n")
    
    liste_commandes = ListeCommande()
    print("List obtenue après création :", liste_commandes.liste_commandes, end="\n\n")
    
    print("Test de l'ajout d'une commande à la liste :", end="\n\n")
    
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
        
    # Ajout d'une commande dans la liste des commandes
    p_quantite = 100
    liste_commandes.ajout_commande(p_destinataire, p_date, p_quantite)
    
    print("Contenu de la liste après ajout de la commande :", liste_commandes.liste_commandes, end="\n\n")
    
    print("Test de la fonction de lecture d'une commande par rapport à son numéro de commande :", end="\n\n")
    
    try:
        num_commande = 2
        liste_commandes.lecture_commande(num_commande)
        
    except ValueError as erreur:
        print(str(num_commande) + " n'est pas un numéro de commande valide !", end="\n\n")
        
    try:
        num_commande = 1
        liste_commandes.lecture_commande(num_commande)
        
    except ValueError as erreur:
        print(str(num_commande) + "n'est pas un numéro de commande valide !", end="\n\n")
        
        
    print("Test de la fonction de modification d'une commande :", end="\n\n")
    
    print("Test de la fonction de suppression d'une commande dans la liste :", end="\n\n")