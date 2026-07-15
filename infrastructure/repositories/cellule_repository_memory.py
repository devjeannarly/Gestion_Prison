from domain.entities.cellule import Cellule
from application.interfaces.cellule_repository import CelluleRepository


class CelluleRepositoryMemory(CelluleRepository):
    """
    Implémentation en mémoire du CelluleRepository.
    """

    def __init__(self):
        self._donnees: dict[int, Cellule] = {}
        self._prochain_id = 1

    def ajouter(self, cellule: Cellule) -> Cellule:
        cellule.id = self._prochain_id
        self._donnees[cellule.id] = cellule
        self._prochain_id += 1
        return cellule

    def obtenir_par_id(self, cellule_id: int) -> Cellule | None:
        return self._donnees.get(cellule_id)

    def mettre_a_jour(self, cellule: Cellule) -> None:
        if cellule.id not in self._donnees:
            raise ValueError(f"Aucune cellule avec l'id {cellule.id} à mettre à jour.")
        self._donnees[cellule.id] = cellule

    def lister_tous(self) -> list[Cellule]:
        return list(self._donnees.values())