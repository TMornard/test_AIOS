# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 14:05:22 2023

@author: Thomas MORNARD

Définition de la classe Date
"""

# TODO : Faire la vérification de l'exactitude de la date en fonction de la date
#        complète (prendre en compte la variabilité du numéro du dernier jour 
#        du mois)
#        ==> Faire une méthode privée supplémentaire dans la classe

# Définition des classes

class Date:
    """Cette classe permet de définir une date sous la forme JJ/MM/AAAA
    
    Attributs :
        - jour  : int - Le jour est un entier positif compris entre 1 et 31
        - mois  : int - Le mois est un entier positif compris entre 1 et 12
        - annee : int - Pour des raisons pratiques, on supposera que l'année 
                        est un entier positif compris entre 0 et 9999
        
    Méthodes :
        - __init__        : Constructeur de la classe
        - __verif_valeurs : Vérifie que les valeurs passées en entrée du 
                            constructeur sont cohérentes
        - lecture_date    : Renvoie la date sous la forme d'une chaine de 
                            caractères dans le format JJ/MM/AAAA
    """
    
    def __init__(self, p_jour, p_mois, p_annee):
        """Création d'une date dans le format JJ/MM/AAAA
        
        Entrées :
            - p_jour  : int - Numéro du jour dans le mois
            - p_mois  : int - Numéro du mois dans l'année
            - p_annee : int - Numéro de l'année
            
        Sorties :
            N/A
        """
        # On vérifie que les valeurs passées en entrée respectent bien les
        # propriétés attendues
        self.__verif_valeurs(p_jour, p_mois, p_annee)
        
        # Création de l'objet de type Date
        self.jour  = p_jour
        self.mois  = p_mois
        self.annee = p_annee
        
    def __verif_valeurs(self, p_jour, p_mois, p_annee):
        """Vérifie que les valeurs passées en entrée du constructeur respectent
           les propriétés suivantes :
               1. Le jour est un entier compris entre 1 et 31
               2. Le mois est un entier compris entre 1 et 12
               3. L'année est un entier positif compris entre 0 et 9999
               4. La date respecte bien le calendrier grégorien (on ne peut pas
                  avoir de 31 février par exemple)
               
        #################################################################
        # Exceptions pouvant être levées :
        #    - TypeError (erreur sur le type d'une variable en entrée)
        #    - ValueError (erreur sur la valeur d'une variable en entrée)
        #################################################################
        
        Entrées :
            - p_jour  : int - Numéro du jour dans le mois
            - p_mois  : int - Numéro du mois dans l'année
            - p_annee : int - Numéro de l'année
            
        Sorties :
            N/A
        """
        # On vérifie que les données en entrée sont bine du type attendu
        if(type(p_jour) != int):
            raise TypeError("Le jour doit être un entier strictement positif !")
            
        if(type(p_mois) != int):
            raise TypeError("Le mois doit être un entier strictement positif !")
            
        if(type(p_annee) != int):
            raise TypeError("L'annee doit être un entier strictement positif !")
        
        # On vérifie que les données en entrée sont bien dans l'intervalle attendu
        if(p_jour < 1 or p_jour > 31):
            raise TypeError("La date donnée est incorrecte !")
            
        if(p_mois < 1 or p_mois > 12):
            raise TypeError("La date donnée est incorrecte !")
            
        if(p_annee < 0 and p_annee > 9999):
            raise TypeError("La date donnée est incorrecte !")
        
    
    def lecture_date(self):
        """Renvoie la date au format JJ/MM/AAAA telle qu'elle est stockée dans
           un objet de type Date. Le résultat est présenté sous la forme d'une
           chaîne de caractères.
        
        Entrées :
            N/A
            
        Sorties :
            - sting - La date dans le format JJ/MM/AAAA sous la forme d'une 
                      chaine de caractères
        """
        return(str(self.jour) + "/" + str(self.mois) + "/" + str(self.annee))


#-----------------------------------------------------------------------------

# Partie principale du programme

if(__name__ == "__main__"):
    print("Test des fonctionnalitées du fichier date.py :", end="\n\n")
    
    print("Test des méthodes de la classe Date :", end="\n\n")
    
    # Création d'une date
    try :
        p_jour  = 1
        p_mois  = 1
        p_annee = 2000
        today   = Date(p_jour, p_mois, p_annee)
        
        # Lecture de la date
        print(today.lecture_date())
        print("Type de renvoi :",type(today.lecture_date()))
        
    except TypeError as erreur:
        print("Erreur lors de la création d'une variable de type Date :")
        print(erreur.args[0])

    except ValueError as erreur:
        print("Erreur lors de la création d'une variable de type Date :")
        print(erreur.args[0])
    
    # TODO : Faire les tests dans le cas où l'une des variable en entrée n'est
    #        pas de type int
    
    # TODO : Faire les tests dans le cas où les variables  ne sont pas dans
    #        l'intervalle défini
    
    # TODO : Faire les tests dans le cas où la date semble correcte, mais ne
    #        l'est pas (31 février par exemple)