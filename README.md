# Network Auditor

Un outil d'audit réseau et Web en ligne de commande (CLI) développé en Python. Il permet d'analyser la sécurité d'une ou plusieurs cibles autorisées, d'effectuer des vérifications d'infrastructure et d'évaluer la présence d'en-têtes de sécurité HTTP.

## 🎯 Objectif du programme
Ce projet permet de :
- Résoudre un nom de domaine en adresse IP.
- Scanner les ports réseau stratégiques (22, 80, 443, 8080, 8443).
- Effectuer des requêtes HTTP/HTTPS avec gestion des timeouts et un User-Agent personnalisé (`AWA-Network-Auditor/1.0`).
- Récupérer les informations clés du serveur Web (code statut, temps de réponse, type de serveur, URL finale).
- Évaluer la présence des en-têtes de sécurité HTTP essentiels (CSP, X-Frame-Options, X-Content-Type-Options, HSTS, Referrer-Policy).
- Enregistrer automatiquement les résultats dans des rapports textuels (`.txt`) et structurés (`.json`).
- Conserver un historique chronologique de toutes les analyses dans `history.txt`.

## 📦 Installation des dépendances
Le projet nécessite Python 3.x et la bibliothèque `requests`.

1. Cloner le dépôt Git :
   ```bash
   git clone <URL_DE_TON_DEPOT_GITHUB>
   cd Network_Auditor
   
2.Installer la dépendance requise:
   ```bash
   pip install requests


🚀 Comment lancer le programme

Le programme s'exécute de deux manières :

1.Sans argument (mode menu interactif):
   ```bash
      python network_auditor.py
      
2. Avec une ou plusieur cibles en paramètre :
   ```bash 
      python network_auditor.py exapmle.com google.com
      
 
⚙️ Utilisation des différentes options
Depuis le menu principal :
 1. Analyse complète : Exécute la résolution DNS, le scan de ports, l'analyse Web et l'audit des en-têtes de sécurité.
 2. Analyse Web : Teste l'accessibilité du serveur HTTP/HTTPS et vérifie les en-têtes.
 3. Vérification des ports : Effectue un balayage des ports TCP cibles (22, 80, 443, 8080, 8443).
 4. Consulter les rapports : Affiche la liste des fichiers enregistrés dans le dossier reports/ et permet de les lire.
 5. Quitter : Ferme le programme.


⚠️ Limites du programme
 Scan synchrone : Le balayage TCP s'effectue séquentiellement, ce qui peut prendre quelques secondes selon la réactivité du réseau.
 Nombre de ports restreint : Seule une liste fixée de ports d'intérêt est testée pour maintenir une rapidité d'exécution.
 Support TCP uniquement : Les services s'appuyant sur UDP ne sont pas analysés.
 Absence de détection active de vulnérabilités : L'absence d'un en-tête HTTP signale un manque de durcissement (hardening), mais ne confirme pas une faille directement exploitable.
  
   