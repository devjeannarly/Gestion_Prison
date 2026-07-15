from enum import Enum


class StatutPrisonnier(Enum):
    """Représente l'état actuel d'un prisonnier dans le système."""
    INCARCERE = "incarcéré"
    LIBERE = "libéré"
    TRANSFERER = "transférer"
    EVADER = "évader"


class StatutCellule(Enum):
    """Représente l'état d'occupation d'une cellule."""
    LIBRE = "libre"
    OCCUPÉE = "occupée"
    PLEINE = "pleine"
    HORS_SERVICE = "hors_service"


class Poste(Enum):
    """Représente le poste assigné à un gardien."""
    SURVEILLANCE = "surveillance"
    ADMINISTRATION = "administration"
    SECURITÉ = "securité"