import os
from datetime import datetime

def ajouter_historique(cible, statut="200"):
    date_jour = datetime.now().strftime("%d/%m/%Y")
    ligne = f"{date_jour} |{cible} |{statut} \n"

    with open("history.txt", "a", encoding="utf-8") as file:
        file.write(ligne)