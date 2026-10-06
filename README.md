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