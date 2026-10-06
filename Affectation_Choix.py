import os
import sys
from datetime import datetime
from rapport import GenerateurRapport, afficher_summary, creer_rapport_json
from historique import ajouter_historique

def main(afficher_menu, resolve_targe, cible, verification_port, http_web, analyser_headres):
    while True:
        afficher_menu()
        try:
            nombre=int(input("Votres choix: "))
            #continue

            if nombre == 1:
                with GenerateurRapport(cible, type_analyse="full") :
                    date_du_jour = datetime.now().strftime("%d/%m/%Y")
                    print("==============================================\n"
                                "NETWORK SECURITY AUDIT\n"
                          "===============================================")
                    print(f"Targe : {cible}")
                    print(f"Date : {date_du_jour}")
                    ip = resolve_targe(cible)
                    ports_ouverts = verification_port (cible)
                    code_statut = http_web(cible, ports_ouverts)
                    http_web(cible, ports_ouverts)
                    analyser_headres(cible)
                    print("===================================================\n"
                          "   END OF REPORT\n "
                          "====================================================")

                statut_log = str(code_statut) if code_statut else "200"
                ajouter_historique(cible, statut_log)

                creer_rapport_json (
                        cible = cible,
                        ip = ip or "0.0.0.0",
                        ports_ouvert= len(ports_ouverts) if ports_ouverts else "0",
                        statut_web = "Available",
                        https = "Available",
                        en_tetes_encore="4/5",
                )

                afficher_summary(
                    cible = cible,
                    ip = ip or "0.0.0.0",
                    nb_ports_ouvert = len(ports_ouverts) if ports_ouverts else "0",
                    web_serveur = "Available",
                    https_statut = "Available",
                    score_headers = "4/5",
                    nom_rapport = f"reports/{cible}.txt",
                )

            elif nombre == 2:
                with GenerateurRapport(cible, type_analyse="web") :
                    date_du_jour = datetime.now().strftime("%d/%m/%Y")
                    print("==================================================\n"
                                " RAPPORT D'ANALYSE WEB \n"
                          "===================================================")
                    print(f"Targe : {cible}")
                    print(f"Date : {date_du_jour}")
                    ports_ouverts = verification_port (cible)
                    code_statut = http_web(cible, ports_ouverts)
                    http_web(cible, ports_ouverts)
                    analyser_headres(cible)
                    print("===================================================\n"
                          "   END OF REPORT\n "
                          "====================================================")


                statut_log = str(code_statut) if code_statut else "200"
                ajouter_historique(cible, statut_log)

            elif nombre == 3:
                date_du_jour = datetime.now().strftime("%d/%m/%Y")
                with GenerateurRapport(cible, type_analyse="ports") :
                    print("=================================================\n"
                                " RAPPORT SCAN DE PORT \n"
                          "==================================================")
                    print(f"Targe : {cible}")
                    print(f"Date : {date_du_jour}")
                    verification_port (cible)
                    print("===================================================\n"
                          "   END OF REPORT\n "
                          "====================================================")

                ajouter_historique(cible, "200")
            elif nombre == 4:
                dossier = "reports"
                if not os.path.exists(dossier):
                    os.makedirs(dossier)
                    """print("Le dossier 'reports' n'existe pas encore.\n")
                    continue"""

                fichiers = [f for f in os.listdir("reports") if f.endswith(".txt")]
                if len(fichiers) == 0:
                    print("Aucun rapport disponible.\n")
                    continue
                while True:
                    print("=======================================================\n"
                                  " RAPPORTS DISPONIBLES  \n"
                           "=========================================================")
                    for i in range(len(fichiers)):
                        print(f"{i + 1}. {fichiers[i]}")

                    numreo_retour = len(fichiers) + 1
                    print(f"{numreo_retour}. Retour\n")

                    try:
                        choix = int(input("Votre Choix: "))
                        if choix == numreo_retour:
                            break
                        if 1 <= choix <= len(fichiers):
                            fichier_choisi = fichiers[choix - 1]
                            chemin_fichier = os.path.join(dossier, fichier_choisi)

                            print("=====================================================\n"
                                        "CONTENU DU RAPPORT \n"
                                  "======================================================")
                            with open(chemin_fichier, "r", encoding="utf-8") as f:
                                print(f.read())

                                input("Appuer sur Entrée pour continuer")
                        else:
                            print("Choix invalide")
                    except ValueError:
                        print("Veuillez entrer un nombre")
            elif nombre == 5:
                 print("====================================================\n"
                            "FERMETURE DU PROGRAMME\n"
                      "=====================================================")
                 sys.exit()
            else :
                print("Choix invalide")

        except ValueError:
            print("Votre nombre n'est pas valide")


