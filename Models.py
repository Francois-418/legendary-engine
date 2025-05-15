#region Imports
# Import des librairies externes.
import uuid
from typing import Optional
from pydantic import BaseModel, Field
#endregion Imports

class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    DiscordID: str = Field(alias="DiscordID")
    Level: int = Field(alias="Level")
    XP: int = Field(alias="XP")
    Force: int = Field(alias="Force")
    Agilite: int = Field(alias="Agilite")
    Intelligence: int = Field(alias="Intelligence")
    PointsDeNotoriete: int = Field(alias="PointsDeNotoriete")
    PointsDeGloire: int = Field(alias="PointsDeGloire")
    PiecesDOr: int = Field(alias="PiecesDOr")
    Location: str = Field(alias="Location")
    De: int = Field(alias="De")
    # Voir comment gérer l'inventaire

class UserUpdate(BaseModel):
    UserName: Optional[str]
    Level: Optional[int]
    XP: Optional[int]
    Force: Optional[int]
    Agilite: Optional[int]
    Intelligence: Optional[int]
    PointsDeNotoriete: Optional[int]
    PointsDeGloire: Optional[int]
    PiecesDOr: Optional[int]
    Location: Optional[str]
    De: Optional[int]

class Config:
    schema_extra = {
        "example": {
            "UserName": "John DOE",
            "Level": "0",
            "XP": "0",
            "Force": "0",
            "Agilite": "0",
            "Intelligence": "0",
            "PointsDeNotoriete": "0",
            "PointsDeGloire": "0",
            "PiecesDOr": "0",
            "De": "4",
            "Location": "Les limbes"
        }
    }
