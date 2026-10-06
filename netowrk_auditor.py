import sys

from port_TCP import verfication_port
from resolve_target import resolve_targe
from Affectation_Choix import main
from serveur_web import http_web
from Analyses_Haeders import analyser_headres


arguments = sys.argv[1:]

cibles = arguments

def afficher_menu():

    print("======================================\n"
                "   NETOWRK_AUDITOR   \n"
          "======================================\n")
    print("1.Analyse Compléte")
    print("2.Analyse Web")
    print("3.Verification des ports")
    print("4.Consulter les rapports")
    print("5.Quitter")


if __name__ == "__main__":
    cibles = sys.argv[1:]
    if not cibles:
        cible_saisie = ""
        while not cible_saisie.strip():
            cible_saisie = input("Entrez le nom de domaine ou l'adresse IP : ")
        cibles = [cible_saisie.strip()]
    for cible in cibles:
        print("==================================================\n"
                    " DEBUT DE L'ANALYSE \n"
              "==================================================")
        main(
            afficher_menu,
            resolve_targe,
            cible,
            verfication_port,
            http_web,
            analyser_headres,
        )