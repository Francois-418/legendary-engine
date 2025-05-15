#region Imports
# Import des librairies externes.
from random import randrange

#Import des fichiers internes.
import AppelBase
import GlobalVariables
import Models
#endregion Imports

# Méthode pour dire bonjour.
async def bonjour(context):
  await context.send(f"{GlobalVariables.MESSAGE_ACCUEIL_DEBUT}{context.author}{GlobalVariables.MESSAGE_ACCUEIL_FIN}")

# Méthode pour dire bonjour à un nouveau joueur.
async def accueilNouveauJoueur(context):
  await context.author.send(f"{GlobalVariables.MESSAGE_NOUVEAU_JOUEUR_DEBUT}{context.author}{GlobalVariables.MESSAGE_NOUVEAU_JOUEUR_FIN}")
  await context.author.send(f"{context.author.id}")

# Méthode pour chercher un utilisateur par son pseudo.
async def cherche_utilisateur(context):
  utilisateur = AppelBase.cherche_utilisateur_name(context.author.name)
  if(utilisateur is not None):
    await context.send(f"Utilisateur {context.author.name} trouvé")
    return utilisateur

# Méthode pour chercher un utilisateur par son UUID Discord.
async def cherche_utilisateur_UUID(context):
  if(AppelBase.cherche_utilisateur_UUID(context.author.name) is not None):
    await context.send(f"Utilisateur {context.author.name} trouvé")

# Méthode pour récupérer les infos d'un utilisateur.
async def infosJoueur(context):
  infos: Models.User = cherche_utilisateur(context.author.name)
  if(infos is None):
    await context.send(f"{GlobalVariables.MESSAGE_UTILISATEUR_INCONNU}")
  else:
    await context.send(f"Voici tes infos : \n - Ton pseudo : {infos['UserName']} \n - Ton niveau : {infos['Level']} \n - Ton XP : {infos['XP']} \n - Et tu es actuellement en train de te promener dans : {infos['Location']}")

# Méthode pour répéter un message si l'utilisateur est admin.
async def repetitionAdmin(context, args):
  if (context.author.id == int(GlobalVariables.MJ_ID)):
    await context.send(f"Coco a entendu et si j'ai bien compris tu as dit {args}")
  else:
    await context.send(f"Coco n'entend que ses maitres et {context.author} n'est pas dans la liste")

# Méthode pour lancer un dé.
async def lanceDe(context, nombreFaces: int):
  limiteMaximale = int(nombreFaces) + 1
  resultat = randrange(1, limiteMaximale)

  if (resultat == limiteMaximale - 1):
    await context.send(f"{GlobalVariables.MESSAGE_REUSSITE_CRITIQUE_DEBUT}{resultat}{GlobalVariables.MESSAGE_REUSSITE_CRITIQUE_FIN}")
  elif (resultat == 1):
    await context.send(GlobalVariables.MESSAGE_ECHEC_CRITIQUE)
  else:
    await context.send(f"{GlobalVariables.MESSAGE_RESULTAT_DE}{resultat}")

# Méthode pour afficher le message d'aide.
async def aide(context):
  await context.send(f"{GlobalVariables.MESSAGE_AIDE_DEBUT}{context.author.name}\n{GlobalVariables.MESSAGE_AIDE_CORPS}")