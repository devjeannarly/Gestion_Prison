from domain.entities.prisonnier import Prisonnier
from application.interfaces.prisonnier_repository import PrisonnierRepository


class PrisonnierRepositoryMemory(PrisonnierRepository):
    """
    Implémentation en mémoire du PrisonnierRepository.
    Les données sont perdues à chaque redémarrage du programme.
    """

    def __init__(self):
        self._donnees: dict[int, Prisonnier] = {}
        self._prochain_id = 1

    def ajouter(self, prisonnier: Prisonnier) -> Prisonnier:
        prisonnier.id = self._prochain_id
        self._donnees[prisonnier.id] = prisonnier
        self._prochain_id += 1
        return prisonnier

    def obtenir_par_id(self, prisonnier_id: int) -> Prisonnier | None:
        return self._donnees.get(prisonnier_id)

    def mettre_a_jour(self, prisonnier: Prisonnier) -> None:
        if prisonnier.id not in self._donnees:
            raise ValueError(f"Aucun prisonnier avec l'id {prisonnier.id} à mettre à jour.")
        self._donnees[prisonnier.id] = prisonnier

    def lister_tous(self) -> list[Prisonnier]:
        return list(self._donnees.values())