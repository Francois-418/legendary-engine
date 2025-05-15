import os
import discord
import GlobalVariables as GV
from discord.ext import commands
from random import randrange
from fastapi import FastAPI, APIRouter, Body, Request, Response, HTTPException, status
from dotenv import dotenv_values
from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder
from typing import List
import Models

# Méthode pour chercher si un utilisateur est dans la base de données
@GV.router.get("/",
            response_description="Cherche un utilisateur par son pseudo",
            response_model=Models.User)
def cherche_utilisateur(username: str):
  if (utilisateur := app.database["Users"].find_one({"UserName": username})) is not None:
    return utilisateur
  else:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Utilisateur {username} non trouvé")