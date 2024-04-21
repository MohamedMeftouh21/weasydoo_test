# Contact Travel
## Contexte

Contact Travel est un module Odoo destiné à la gestion des voyages pour les contacts.

## Installation et configuration 
Bienvenue dans ce dépôt ! Ici, vous trouverez le code source du test disponible à l'adresse suivante : [Contact Travel](https://github.com/MohamedMeftouh21/weasydoo_test/tree/main/custom_addons/contact_travel).


Dans ce test, j'ai configuré un environnement Docker pour exécuter l'application (module) Odoo version 16. Vous trouverez ici le code source ainsi que les fichiers de configuration nécessaires.
### Testé avec :
   - Odoo 16.0 (docker image)
   - PostgreSQL 13 (docker image)
   - Docker version 24.0.5  (Macos intel)
  


Pour démarrer l'application Odoo à l'aide de Docker, suivez ces étapes :

1. Assurez-vous d'avoir [Docker](https://docs.docker.com/get-docker/) et 
[Docker-Compose](https://docs.docker.com/compose/install/) installés sur votre système.
2. Clonez ce dépôt sur votre machine.
3. Accédez au répertoire du projet.
4. Utilisez la commande suivante pour démarrer les conteneurs Docker :
   ```bash
   docker-compose up -d



____________


### Recommandation

Utiliser la technique [multi-stage](https://medium.com/@pranaymate/multi-stage-docker-build-streamlining-your-python-app-deployment-a8185601666f)  est recommandé pour réduire la taille des images Docker, ce qui peut améliorer les performances de déploiement et réduire la consommation de ressources système.

____
