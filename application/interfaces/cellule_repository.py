from abc import ABC, abstractmethod

from domain.entities.cellule import Cellule


class CelluleRepository(ABC):
    """
    Contrat que toute implémentation de stockage des cellules doit respecter.
    """

    @abstractmethod
    def ajouter(self, cellule: Cellule) -> Cellule:
        """Ajoute une nouvelle cellule et retourne l'objet avec son id assigné."""
        ...

    @abstractmethod
    def obtenir_par_id(self, cellule_id: int) -> Cellule | None:
        """Retourne la cellule correspondante, ou None si elle n'existe pas."""
        ...

    @abstractmethod
    def mettre_a_jour(self, cellule: Cellule) -> None:
        """Sauvegarde les changements faits sur une cellule existante."""
        ...

    @abstractmethod
    def lister_tous(self) -> list[Cellule]:
        """Retourne la liste de toutes les cellules enregistrées."""
        ...