import sys

from port_TCP import verfication_port
from resolve_target import resolve_targe
from Affectation_Choix import main
from serveur_web import http_web
from Analyses_Haeders import analyser_headres


arguments = sys.argv[1:]

def usage ():
    print("Usage: python network_auditor.py <cible> [cible2..]")
    sys.exit()

if len(arguments) == 0:
    usage()
    sys.exit()


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

    for cible in cibles:
        print("===================================================\n"
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


    #resolve_targe(cible)
    #main(afficher_menu,resolve_targe,cible, verfication_port, http_web, analyser_headres)
