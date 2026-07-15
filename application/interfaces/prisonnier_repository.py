from abc import ABC, abstractmethod

from domain.entities.prisonnier import Prisonnier


class PrisonnierRepository(ABC):
    """
    Contrat que toute implémentation de stockage des prisonniers doit respecter.
    Peu importe si c'est en mémoire, en SQLite, ou en MySQL derrière.
    """

    @abstractmethod
    def ajouter(self, prisonnier: Prisonnier) -> Prisonnier:
        """Ajoute un nouveau prisonnier et retourne l'objet avec son id assigné."""
        ...

    @abstractmethod
    def obtenir_par_id(self, prisonnier_id: int) -> Prisonnier | None:
        """Retourne le prisonnier correspondant, ou None s'il n'existe pas."""
        ...

    @abstractmethod
    def mettre_a_jour(self, prisonnier: Prisonnier) -> None:
        """Sauvegarde les changements faits sur un prisonnier existant."""
        ...

    @abstractmethod
    def lister_tous(self) -> list[Prisonnier]:
        """Retourne la liste de tous les prisonniers enregistrés."""
        ...