from livre import Livre 
from livre_dao import LivreDAO 

def afficher_menu(): 
    print("\n--- Menu Gestion des Livres ---") 
    print("1. Ajouter un livre") 
    print( "2. Afficher tous les livres" ) 
    print("3. Modifier un livre") 
    print("4. Supprimer un livre") 
    print("5. Rechercher un livre par ID") 
    print("6. Afficher les livres dont le prix est supérieur à un seuil") 
    print("7. Compter le nombre de livres") 
    print("8. Afficher le livre le plus cher") 
    print("9. Quitter") 
    choix = input("Entrez votre choix: ") 
    return choix 

def main(): 
    livre_dao = LivreDAO() 

    while True: 
        choix = afficher_menu() 

        if choix == '1': 
            titre = input("Entrez le titre du livre: ") 
            auteur = input("Entrez l'auteur du livre: ") 
            try: 
                prix = float(input("Entrez le prix du livre: ")) 
                livre = Livre(titre=titre, auteur=auteur, prix=prix) 
                livre_dao.ajouter(livre) 
            except ValueError: 
                print("Prix invalide. Veuillez entrer un nombre.") 

        elif choix == '2': 
            livres = livre_dao.afficher() 
            if livres: 
                for livre in livres: 
                    print(livre) 
            else: 
                print("Aucun livre à afficher.") 

        elif choix == '3': 
            try: 
                id_livre = int(input("Entrez l'ID du livre à modifier: ")) 
                livre_existant = livre_dao.rechercher(id_livre) 
                if livre_existant: 
                    nouveau_titre = input(f"Entrez le nouveau titre (actuel: {livre_existant.titre}): ") or livre_existant.titre 
                    nouvel_auteur = input(f"Entrez le nouvel auteur (actuel: {livre_existant.auteur}): ") or livre_existant.auteur 
                    nouveau_prix_str = input(f"Entrez le nouveau prix (actuel: {livre_existant.prix}): ") 
                    nouveau_prix = float(nouveau_prix_str) if nouveau_prix_str else livre_existant.prix 

                    livre_modifie = Livre(id=id_livre, titre=nouveau_titre, auteur=nouvel_auteur, prix=nouveau_prix) 
                    livre_dao.modifier(livre_modifie) 
                else: 
                    print(f"Livre avec l'ID {id_livre} non trouvé.") 
            except ValueError: 
                print("ID ou prix invalide. Veuillez entrer un nombre.") 

        elif choix == '4': 
            try: 
                id_livre = int(input("Entrez l'ID du livre à supprimer: ")) 
                livre_dao.supprimer(id_livre) 
            except ValueError: 
                print("ID invalide. Veuillez entrer un nombre.") 

        elif choix == '5': 
            try: 
                id_livre = int(input("Entrez l'ID du livre à rechercher: ")) 
                livre = livre_dao.rechercher(id_livre) 
                if livre: 
                    print("Livre trouvé:", livre) 
                else: 
                    print(f"Aucun livre trouvé avec l'ID {id_livre}.") 
            except ValueError: 
                print("ID invalide. Veuillez entrer un nombre.") 

        elif choix == '6': 
            try: 
                prix_seuil = float(input("Afficher les livres dont le prix est supérieur à: ")) 
                livres = livre_dao.afficher_prix_superieur(prix_seuil) 
                if livres: 
                    for livre in livres: 
                        print(livre) 
                else: 
                    print(f"Aucun livre trouvé avec un prix supérieur à {prix_seuil}.") 
            except ValueError: 
                print("Prix invalide. Veuillez entrer un nombre.") 

        elif choix == '7': 
            count = livre_dao.compter_livres() 
            print(f"Nombre total de livres: {count}") 

        elif choix == '8': 
            livre_plus_cher = livre_dao.produit_le_plus_cher() 
            if livre_plus_cher: 
                print("Livre le plus cher:", livre_plus_cher) 
            else: 
                print("Aucun livre trouvé.") 

        elif choix == '9': 
            print("Au revoir!") 
            break 

        else: 
            print("Choix invalide. Veuillez réessayer.") 

if __name__ == "__main__": 
    main()
