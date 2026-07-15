from abc import ABC, abstractmethod

from domain.entities.gardien import Gardien


class GardienRepository(ABC):
    """
    Contrat que toute implémentation de stockage des gardiens doit respecter.
    """

    @abstractmethod
    def ajouter(self, gardien: Gardien) -> Gardien:
        """Ajoute un nouveau gardien et retourne l'objet avec son id assigné."""
        ...

    @abstractmethod
    def obtenir_par_id(self, gardien_id: int) -> Gardien | None:
        """Retourne le gardien correspondant, ou None s'il n'existe pas."""
        ...

    @abstractmethod
    def mettre_a_jour(self, gardien: Gardien) -> None:
        """Sauvegarde les changements faits sur un gardien existant."""
        ...

    @abstractmethod
    def lister_tous(self) -> list[Gardien]:
        """Retourne la liste de tous les gardiens enregistrés."""
        ...