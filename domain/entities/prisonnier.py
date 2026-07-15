from datetime import date
from domain.entities.enums import StatutPrisonnier


class Prisonnier:
    """
    Représente un prisonnier incarcéré (ou l'ayant été).

    Règles métier :
    - Un prisonnier libéré ne peut pas être transféré.
    - Un prisonnier ne peut être libéré que s'il est actuellement incarcéré.
    """

    def __init__(
        self,
        id: int,
        nom: str,
        prenom: str,
        date_naissance: date,
        matricule: str,
        date_incarceration: date,
        cellule_id: int | None = None,
    ):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.matricule = matricule
        self.date_incarceration = date_incarceration
        self.cellule_id = cellule_id
        self.statut = StatutPrisonnier.INCARCERE

    def transferer(self, nouvelle_cellule_id: int) -> None:
        if self.statut != StatutPrisonnier.INCARCERE:
            raise ValueError("Impossible de transférer un prisonnier non incarcéré.")

        self.cellule_id = nouvelle_cellule_id
        self.statut = StatutPrisonnier.TRANSFERER

    def liberer(self) -> None:
        if self.statut not in (StatutPrisonnier.INCARCERE, StatutPrisonnier.TRANSFERER):
            raise ValueError("Ce prisonnier ne peut pas être libéré depuis son statut actuel.")

        self.cellule_id = None
        self.statut = StatutPrisonnier.LIBERE