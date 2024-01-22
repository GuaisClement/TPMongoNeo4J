# Mutify

Appication Flutter qui permet de chercher des artistes et leurs musiques pour en écouter une partie

## Pré-requis

- Python : 3.11

## Installation

1. Cloner le projet
2. utliser  la commande suivante pour installer les packages requis

```bash
pip install 'fastapi[all]' 'pymongo[srv]' python-dotenv neo4j
```
3. Renseigner les informations de la base de donnée dans le fichier .env
4. Dans le terminal se rendre dans le dossier fastapi-movies et lancer l'application avec la commande suivante

```bash
python -m uvicorn main:app --reload
```


