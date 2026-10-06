import os
import sys
import json
from datetime import datetime

class GenerateurRapport:
    def __init__(self,cible, type_analyse="audit"):
        self.cible = cible
        self.dossier = "reports"

        horodatage = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        nom_fichier = f"{cible}_{type_analyse}_{horodatage}.txt"

        self.fichier_path = os.path.join(self.dossier, nom_fichier)
        self.stdout_original = sys.stdout
        self.fichier = None

    def __enter__ (self):
            if not os.path.exists(self.dossier):
                os.makedirs(self.dossier)

            self.fichier = open(self.fichier_path,"w", encoding="utf-8")
            sys.stdout = self
            return self

    def write(self, data):
            self.stdout_original.write(data)
            self.fichier.write(data)

    def flush(self):
            self.stdout_original.flush()
            self.fichier.flush()

    def __exit__(self, exc_type, exc_val, exc_tb):
            sys.stdout = self.stdout_original
            if self.fichier:
                self.fichier.close()
            print(f"\n[+] Rapport Sauvegarde dans : {self.fichier_path}")

def creer_rapport_json(cible, ip, ports_ouvert, statut_web, https, en_tetes_encore):
    donnes = {
    "target" : cible,
    "ip" : ip,
    "ports_ouvert" : ports_ouvert,
    "web_serveur" : statut_web,
    "https" : https,
    "security_headers" : en_tetes_encore
    }

    nom_fichier = f"reports/{cible}.json"
    with open(nom_fichier, "w", encoding="utf-8") as f:
        json.dump(donnes, f, indent=4)


def afficher_summary(cible, ip, nb_ports_ouvert, web_serveur, https_statut, score_headers, nom_rapport):
   print("=========================================\n"
            " SUMMARY \n"
         "=========================================")
   print(f"Target         : {cible}")
   print(f"IP             : {ip}")
   print(f"Ports ouvert   : {nb_ports_ouvert}")
   print(f"Web serveur    : {web_serveur}")
   print(f"HTTPS statut   : {https_statut}")
   print(f"Score headers  : {score_headers}")
   print(f"Nom rapport    : {nom_rapport}")
   print("===============================================")