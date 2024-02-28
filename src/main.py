from tkinter import *
from tkinter import messagebox  # Importation du module messagebox pour afficher des messages à l'utilisateur
import ast  # Importation du module ast pour l'évaluation littérale des chaînes de caractères

# Création de la fenêtre principale
window = Tk()
window.title("Inscription")  # Définition du titre de la fenêtre
window.geometry("925x500+300+200")  # Définition de la taille et de la position de la fenêtre
window.configure(bg="#fff")  # Définition de la couleur de fond de la fenêtre
window.resizable(False, False)  # Rendre la fenêtre non redimensionnable

# Fonction pour gérer le processus d'inscription
def signup():
    # Récupération du nom d'utilisateur, du mot de passe et du mot de passe confirmé à partir des champs de saisie
    username = user.get()
    password = code.get()
    conform_password = conform_code.get()

    # Vérification si le mot de passe correspond au mot de passe confirmé
    if password == conform_password:
        try:
            # Ouverture du fichier datasheet.txt en mode lecture
            file = open("datasheet.txt", "r")
            # Lecture du contenu du fichier
            d = file.read()
            # Évaluation du contenu de la chaîne comme une expression littérale (dictionnaire)
            r = ast.literal_eval(d)

            # Création d'une entrée de dictionnaire pour le nouvel utilisateur
            dict2 = {username: password}
            # Mise à jour du dictionnaire avec les nouvelles données utilisateur
            r.update(dict2)
            # Troncature du fichier pour supprimer son contenu
            file.truncate(0)
            # Fermeture du fichier
            file.close()

            # Réouverture du fichier en mode écriture
            file = open("datasheet.txt", "w")
            # Écriture du contenu du dictionnaire mis à jour dans le fichier
            w = file.write(str(r))
            # Fermeture du fichier
            file.close()

            # Affichage d'un message de succès avec le nombre de caractères écrits dans le fichier
            messagebox.showinfo("Succès", f"Compte créé avec succès. {w} caractères écrits dans le fichier.")

        except:
            # Gestion du cas où il n'y a pas de fichier datasheet.txt
            file = open("datasheet.txt", "w")
            pp = str({username: password})
            file.write(pp)
            file.close()

    else:
        # Affichage d'un message d'erreur lorsque les mots de passe ne correspondent pas
        messagebox.showerror("Erreur", "Le mot de passe ne correspond pas")


# Création de la disposition de la fenêtre

# Image
img = PhotoImage(file="image/login1.png")
img = img.subsample(2, 2)
Label(window, image=img, border=0, bg="white").place(x=50, y=90)

# Cadre
frame = Frame(window, width=350, height=400, bg="white")
frame.place(x=480, y=50)

# En-tête d'inscription
heading = Label(frame, text="Inscription", fg="#57a1f8", bg="white", font=("arial", 23, "bold"))
heading.place(x=100, y=5)

# Champ de saisie pour le nom d'utilisateur
user = Entry(frame, width=25, fg="black", border=0, bg="white", font=("arial", 11))
user.place(x=30, y=80)
user.insert(0, "Nom d'utilisateur")

# Champ de saisie pour le mot de passe
code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("arial", 11))
code.place(x=30, y=150)
code.insert(0, "Mot de passe")

# Champ de saisie pour la confirmation du mot de passe
conform_code = Entry(frame, width=25, fg="black", border=0, bg="white", font=("arial", 11))
conform_code.place(x=30, y=220)
conform_code.insert(0, "Confirmer le mot de passe")

# Bouton d'inscription
Button(frame, width=39, pady=7, text="S'inscrire", bg="#57a1f8", fg="white", border=0, command=signup).place(x=35, y=274)

# Étiquette "Déjà un compte ?"
label = Label(frame, text="Déjà un compte ?", bg="white", fg="black", font=("arial", 9))
label.place(x=50, y=340)

# Bouton de connexion
signin = Button(frame, width=6, text="Se connecter", border=0, bg="white", cursor="hand2", fg="#57a1f8")
signin.place(x=200, y=340)

# Exécution de la boucle principale des événements
window.mainloop()
