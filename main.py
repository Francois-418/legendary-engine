#region Imports
# Import des librairies externes.
import discord
from discord.ext import commands
from pymongo import MongoClient

#Import des fichiers internes.
import GlobalVariables
import Methodes
#endregion Imports

#region Connexion à la base de données
@GlobalVariables.app.on_event("startup")
def startup_db_client():
  GlobalVariables.app.mongodb_client = MongoClient(GlobalVariables.DB_URL)
  GlobalVariables.app.database = GlobalVariables.app.mongodb_client[
      GlobalVariables.DB_NAME]
  print(GlobalVariables.MESSAGE_CONNECTION_BDD)

@GlobalVariables.app.on_event("shutdown")
def shutdown_db_client():
  GlobalVariables.app.mongodb_client.close()
#endregion Connexion à la base de données

# Préparation du bot.
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

#region Points d'entrées depuis le bot.
# Appel pour avoir un message d'accueil
@bot.command()
async def SalutAToi(context):
  await Methodes.bonjour(context)

# Appel pour demander à jouer
@bot.command()
async def JeVeuxJouer(context):
  await Methodes.accueilNouveauJoueur(context)

# Appel pour vérifier si un utilisateur est dans la base de données.
@bot.command()
async def Estcequejexiste(context):
  await Methodes.cherche_utilisateur(context)

# Appel pour vérifier si un utilisateur est dans la base de données avec son UUID Discord.
@bot.command()
async def EstcequejexisteUUID(context):
  await Methodes.cherche_utilisateur_UUID(context)

# Appel pour récupérer les infos d'un utilisateur en base.
@bot.command()
async def MesInfos(context):
  await Methodes.infosJoueur(context)

# Appel test pour récupération d'infos dans un message et droit admin.
@bot.command()
async def Coco(context, args):
  await Methodes.repetitionAdmin(context, args)

# Appel pour lancer un dé
@bot.command()
async def De(context, args):
  await Methodes.lanceDe(context, args)

# Appel pour avoir le message d'aide
@bot.command()
async def Help(context):
  await Methodes.aide(context)
#endregion Points d'entrées depuis le bot.

# Lancement du bot.
startup_db_client()
bot.run(GlobalVariables.token)
