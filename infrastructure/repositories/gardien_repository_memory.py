from domain.entities.gardien import Gardien
from application.interfaces.gardien_repository import GardienRepository


class GardienRepositoryMemory(GardienRepository):
    """
    Implémentation en mémoire du GardienRepository.
    """

    def __init__(self):
        self._donnees: dict[int, Gardien] = {}
        self._prochain_id = 1

    def ajouter(self, gardien: Gardien) -> Gardien:
        gardien.id = self._prochain_id
        self._donnees[gardien.id] = gardien
        self._prochain_id += 1
        return gardien

    def obtenir_par_id(self, gardien_id: int) -> Gardien | None:
        return self._donnees.get(gardien_id)

    def mettre_a_jour(self, gardien: Gardien) -> None:
        if gardien.id not in self._donnees:
            raise ValueError(f"Aucun gardien avec l'id {gardien.id} à mettre à jour.")
        self._donnees[gardien.id] = gardien

    def lister_tous(self) -> list[Gardien]:
        return list(self._donnees.values())