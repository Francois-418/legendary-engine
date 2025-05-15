#region Imports
# Import des librairies externes.
import os
from dotenv import dotenv_values
from fastapi import FastAPI, APIRouter
#endregion Imports

# Variables d'OS.
token = os.environ['TOKEN']
DB_URL = os.environ['DB_ACCESS']
DB_NAME = os.environ['DB_NAME']
MJ_ID = os.environ['MJ_ID']

# Connexion à la base de données
config = dotenv_values(".env")
app = FastAPI()
router = APIRouter()

# Retour à la ligne.
RETOUR_LIGNE = "\n"

# Message de nouveau joueur.
MESSAGE_NOUVEAU_JOUEUR_DEBUT = "Bienvenue " # A faire suivre du nom de l'utilisateur
MESSAGE_NOUVEAU_JOUEUR_FIN =  "!" + RETOUR_LIGNE + "Pour créer ton personnage les organisateurs vont avoir besoin de ton identifiant discord, le voici : "

# Message d'accueil.
MESSAGE_ACCUEIL_DEBUT = "Bonjour à toi "# A faire suivre du nom de l'utilisateur
MESSAGE_ACCUEIL_FIN = ", heureux que tu sois avec nous, ensemble nous serons plus forts !" + RETOUR_LIGNE + "Si tu veux de l'aide, n'hésite pas à faire !Help"

# Message d'aide.
MESSAGE_AIDE_DEBUT = "Tu es perdu ? Ne t'en fait pas je suis là pour t'aider " # A faire suivre du nom de l'utilisateur
MESSAGE_AIDE_CORPS = "." + RETOUR_LIGNE + "Ici tu peux utiliser les commandes:" + RETOUR_LIGNE + " - !SalutAToi : Si tu veux un message d'accueil" + RETOUR_LIGNE + " - !GagneNiveau : Si tu veux monter d'un niveau" + RETOUR_LIGNE + " - !Combat : Si tu veux lancer un D20" + RETOUR_LIGNE + "- !Help : Si tu veux afficher cette aide à nouveau" + RETOUR_LIGNE + ""

# Message d'utilisateur non reconnu.
MESSAGE_UTILISATEUR_INCONNU = "T'es qui toi ?"

# Message de connection à la BdD réussi.
MESSAGE_CONNECTION_BDD = "Connection à la base de données réussi !"

# Message résultat lancé dé.
MESSAGE_RESULTAT_DE = "Le dé a fait "

# Message réussite critique.
MESSAGE_REUSSITE_CRITIQUE_DEBUT = "C'est un magnifique "
MESSAGE_REUSSITE_CRITIQUE_FIN = ", réussite critique !"

# Message échec critique.
MESSAGE_ECHEC_CRITIQUE = "C'est un pas très fantastique 1, échec critique ! Dommage ! Mais ne t'en fait pas, on brule ce dé et on en prendra un autre pour les prochains lancés !"