from datetime import date

from domain.entities.prisonnier import Prisonnier
from application.interfaces.prisonnier_repository import PrisonnierRepository
from application.interfaces.cellule_repository import CelluleRepository


class IncarcererPrisonnier:
    """
    Use case : incarcérer un nouveau prisonnier dans une cellule donnée.

    Règles orchestrées :
    - La cellule doit exister.
    - La cellule ne doit pas être pleine.
    """

    def __init__(self, prisonnier_repo: PrisonnierRepository, cellule_repo: CelluleRepository):
        self.prisonnier_repo = prisonnier_repo
        self.cellule_repo = cellule_repo

    def executer(
        self,
        nom: str,
        prenom: str,
        date_naissance: date,
        matricule: str,
        cellule_id: int,
    ) -> Prisonnier:
        cellule = self.cellule_repo.obtenir_par_id(cellule_id)
        if cellule is None:
            raise ValueError(f"Aucune cellule trouvée avec l'id {cellule_id}.")

        if cellule.est_pleine():
            raise ValueError("Impossible d'incarcérer : cellule pleine.")

        nouveau_prisonnier = Prisonnier(
            id=0,  # sera assigné par le repository
            nom=nom,
            prenom=prenom,
            date_naissance=date_naissance,
            matricule=matricule,
            date_incarceration=date.today(),
            cellule_id=cellule_id,
        )

        prisonnier_sauvegarde = self.prisonnier_repo.ajouter(nouveau_prisonnier)

        cellule.ajouter_prisonnier(prisonnier_sauvegarde.id)
        self.cellule_repo.mettre_a_jour(cellule)

        return prisonnier_sauvegarde