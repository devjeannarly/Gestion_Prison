from application.interfaces.prisonnier_repository import PrisonnierRepository
from application.interfaces.cellule_repository import CelluleRepository


class TransfererCellule:
    """
    Use case : transférer un prisonnier vers une nouvelle cellule.

    Règles orchestrées :
    - Le prisonnier doit exister et être incarcéré.
    - La nouvelle cellule doit exister et avoir de la place.
    """

    def __init__(self, prisonnier_repo: PrisonnierRepository, cellule_repo: CelluleRepository):
        self.prisonnier_repo = prisonnier_repo
        self.cellule_repo = cellule_repo

    def executer(self, prisonnier_id: int, nouvelle_cellule_id: int) -> None:
        prisonnier = self.prisonnier_repo.obtenir_par_id(prisonnier_id)
        if prisonnier is None:
            raise ValueError(f"Aucun prisonnier trouvé avec l'id {prisonnier_id}.")

        nouvelle_cellule = self.cellule_repo.obtenir_par_id(nouvelle_cellule_id)
        if nouvelle_cellule is None:
            raise ValueError(f"Aucune cellule trouvée avec l'id {nouvelle_cellule_id}.")

        if nouvelle_cellule.est_pleine():
            raise ValueError("Impossible de transférer : nouvelle cellule pleine.")

        ancienne_cellule_id = prisonnier.cellule_id
        if ancienne_cellule_id is not None:
            ancienne_cellule = self.cellule_repo.obtenir_par_id(ancienne_cellule_id)
            if ancienne_cellule is not None:
                ancienne_cellule.retirer_prisonnier(prisonnier.id)
                self.cellule_repo.mettre_a_jour(ancienne_cellule)

        prisonnier.transferer(nouvelle_cellule_id)
        nouvelle_cellule.ajouter_prisonnier(prisonnier.id)

        self.prisonnier_repo.mettre_a_jour(prisonnier)
        self.cellule_repo.mettre_a_jour(nouvelle_cellule)