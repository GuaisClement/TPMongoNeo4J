# TP Mongo Neo4J

API sur la base de données movie

## Pré-requis

- Python : 3.11

## Installation

1. Cloner le projet
2. utliser  la commande suivante pour installer les packages requis

```bash
pip install 'fastapi[all]' 'pymongo[srv]' python-dotenv neo4j
```
3. Renseigner les informations de la base de données dans le fichier .env
4. Dans le terminal se rendre dans le dossier fastapi-movies et lancer l'application avec la commande suivante

```bash
python -m uvicorn main:app --reload
```


