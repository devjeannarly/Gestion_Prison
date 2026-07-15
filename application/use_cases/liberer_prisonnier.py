from application.interfaces.prisonnier_repository import PrisonnierRepository
from application.interfaces.cellule_repository import CelluleRepository


class LibererPrisonnier:
    """
    Use case : libérer un prisonnier.

    Règles orchestrées :
    - Le prisonnier doit exister.
    - Il est retiré de sa cellule actuelle, s'il en a une.
    """

    def __init__(self, prisonnier_repo: PrisonnierRepository, cellule_repo: CelluleRepository):
        self.prisonnier_repo = prisonnier_repo
        self.cellule_repo = cellule_repo

    def executer(self, prisonnier_id: int) -> None:
        prisonnier = self.prisonnier_repo.obtenir_par_id(prisonnier_id)
        if prisonnier is None:
            raise ValueError(f"Aucun prisonnier trouvé avec l'id {prisonnier_id}.")

        if prisonnier.cellule_id is not None:
            cellule = self.cellule_repo.obtenir_par_id(prisonnier.cellule_id)
            if cellule is not None:
                cellule.retirer_prisonnier(prisonnier.id)
                self.cellule_repo.mettre_a_jour(cellule)

        prisonnier.liberer()
        self.prisonnier_repo.mettre_a_jour(prisonnier)