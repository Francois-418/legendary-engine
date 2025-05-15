# Import des librairies
import os
import discord
import GlobalVariables as GV
from discord.ext import commands
from random import randrange
from fastapi import FastAPI, APIRouter, Body, HTTPException, status
from dotenv import dotenv_values
from pymongo import MongoClient
from typing import List
import Models

# Déclaration variables
token = os.environ['TOKEN']
DB_URL = os.environ['DB_ACCESS']
DB_NAME = os.environ['DB_NAME']
MJ_ID = os.environ['MJ_ID']

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Connexion à la base de données
config = dotenv_values(".env")
app = FastAPI()
router = APIRouter()

@app.on_event("startup")
def startup_db_client():
  app.mongodb_client = MongoClient(DB_URL)
  app.database = app.mongodb_client[DB_NAME]
  print("Connected to the database!")


@app.on_event("shutdown")
def shutdown_db_client():
  app.mongodb_client.close()

# Récupère tous les utilisateurs
@router.get("/",
            response_description="Récupère tous les utilisateurs",
            response_model=List[Models.User])
def liste_utilisateur():
  utilisateurs = list(app.database["Users"].find(limit=100))
  print(utilisateurs)


# Appel pour avoir un message d'accueil
@bot.command()
async def SalutAToi(v_context):
  await v_context.send(
      f"{GV.MESSAGE_ACCUEIL_DEBUT}{v_context.author}{GV.MESSAGE_ACCUEIL_FIN}")

# Appel pour demander à jouer
@bot.command()
async def JeVeuxJouer(v_context):
    await v_context.author.send(f"Bienvenue {v_context.author} !\nPour créer ton personnage les organisateurs vont avoir besoin de ton identifiant discord, le voici : ")
    await v_context.author.send(f"{v_context.author.id}")

# Méthode pour chercher si un utilisateur est dans la base de données
@router.get("/",
            response_description="Cherche un utilisateur par son pseudo",
            response_model=Models.User)
def cherche_utilisateur(username: str):
  if (utilisateur := app.database["Users"].find_one({"UserName": username})) is not None:
    return utilisateur
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Utilisateur {username} non trouvé")

# Appel pour vérifier si un utilisateur est dans la base de données.
@bot.command()
async def Estcequejexiste(context):
  cherche_utilisateur(context.author.name)
  await context.send(f"Utilisateur {context.author.name} trouvé")

# Méthode pour chercher si un utilisateur est dans la base de données
@router.get("/",
            response_description="Cherche un utilisateur par son pseudo",
            response_model=Models.User)
def cherche_utilisateur_UUID(context):  
  if (utilisateur := app.database["Users"].find_one({"DiscordID": str(context.author.id)})) is not None:
    return True
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Utilisateur {context.author} non trouvé")

# Appel pour vérifier si un utilisateur est dans la base de données avec son UUID Discord.
@bot.command()
async def EstcequejexisteUUID(context):
  if(cherche_utilisateur_UUID(context) is True):
    await context.send(f"Utilisateur {context.author.name} trouvé")

# Appel pour récupérer les infos d'un utilisateur en base.
@bot.command()
async def MesInfos(context):
  infos = cherche_utilisateur(context.author.name)
  await context.send(f"Voici tes infos : \n - Ton pseudo : {infos['UserName']} \n - Ton niveau : {infos['Level']} \n - Ton XP : {infos['XP']} \n - Et tu es actuellement en train de te promener dans : {infos['Location']}")

# Appel test pour injection données
@bot.command()
async def Coco(context, args):
  if(context.author.id == int(MJ_ID)):
    await context.send(f"Coco a entendu et si j'ai bien compris tu as dit {args}")
  else:
    await context.send(f"Coco n'entend que ses maitres et {context.author.id} n'est pas dans la liste")

#Commande pour faire gagner un niveau à un utilisateur
@router.put("/{id}", response_description="Update a user after level gain", response_model=Models.User)
def UtilisateurGagneNiveau(utilisateur: Models.User, update: Models.UserUpdate = Body(...)):
    app.database["Users"].update_one({"_id": utilisateur["_id"]}, {"Level": utilisateur["Level"] + 1})

# Appel pour gagner un niveau
@bot.command()
async def GagneNiveau(context):
  auteur = context.author.name
  if (utilisateur := app.database["Users"].find_one({"UserName": auteur})) is not None:
    UtilisateurGagneNiveau(utilisateur["_id"], )
  else:
    await context.send(GV.MESSAGE_UTILISATEUR_INCONNU)

# Appel pour lancer un combat
@bot.command()
async def Combat(context):
  D20 = randrange(1, 21)

  if (D20 == 20):
    await context.send(GV.MESSAGE_REUSSITE_CRITIQUE)
  elif (D20 == 1):
    await context.send(GV.MESSAGE_ECHEC_CRITIQUE)
  else:
    await context.send(f"Le dé a fait {D20}")


# Appel pour avoir le message d'aide
@bot.command()
async def Help(v_context):
  await v_context.send(
      f"{GV.MESSAGE_AIDE_DEBUT}{v_context.author.name}\n{GV.MESSAGE_AIDE_CORPS}"
  )


startup_db_client()
bot.run(token)
