#region Imports
# Import des librairies externes.
from fastapi import HTTPException, status
from typing import List

#Import des fichiers internes.
import GlobalVariables
import Models
#endregion Imports

# Méthodes pour chercher si un utilisateur est dans la base de données par son pseudo
@GlobalVariables.router.get("/",
                            response_description="Cherche un utilisateur par son pseudo",
                            response_model=Models.User)
def cherche_utilisateur_name(username: str):
  if (utilisateur := GlobalVariables.app.database["Users"].find_one({"UserName": username})) is not None:
    return utilisateur
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Utilisateur {username} non trouvé")

# Méthodes pour chercher si un utilisateur est dans la base de données avec son UUID Discord
@GlobalVariables.router.get("/",
                            response_description="Cherche un utilisateur par son ID Discord",                                  response_model=Models.User)
def cherche_utilisateur_UUID(context):
  if (utilisateur := GlobalVariables.app.database["Users"].find_one({"DiscordID": str(context.author.id)})) is not None:
    return True
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Utilisateur {context.author} non trouvé")

# Récupère tous les utilisateurs
@GlobalVariables.router.get("/",
            response_description="Récupère tous les utilisateurs",
            response_model=List[Models.User])
def liste_utilisateur():
  utilisateurs = list(GlobalVariables.app.database["Users"].find(limit=100))
  print(utilisateurs)
