from domain.entities.gardien import Gardien
from application.interfaces.gardien_repository import GardienRepository
from application.interfaces.cellule_repository import CelluleRepository


class AssignerGardien:
    """
    Use case : assigner un gardien à une cellule.

    Règles orchestrées :
    - Le gardien doit exister.
    - La cellule doit exister.
    - Pas de double assignation (gérée par l'entité Gardien elle-même).
    """

    def __init__(self, gardien_repo: GardienRepository, cellule_repo: CelluleRepository):
        self.gardien_repo = gardien_repo
        self.cellule_repo = cellule_repo

    def executer(self, gardien_id: int, cellule_id: int) -> Gardien:
        gardien = self.gardien_repo.obtenir_par_id(gardien_id)
        if gardien is None:
            raise ValueError(f"Aucun gardien trouvé avec l'id {gardien_id}.")

        cellule = self.cellule_repo.obtenir_par_id(cellule_id)
        if cellule is None:
            raise ValueError(f"Aucune cellule trouvée avec l'id {cellule_id}.")

        gardien.assigner_cellule(cellule_id)
        self.gardien_repo.mettre_a_jour(gardien)

        return gardien