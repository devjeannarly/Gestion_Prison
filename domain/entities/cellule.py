from domain.entities.enums import StatutCellule


class Cellule:
    """
    Représente une cellule physique de la prison.

    Règles métier :
    - Une cellule ne peut pas contenir plus de prisonniers que sa capacité.
    - Une cellule "hors service" ne peut recevoir aucun prisonnier.
    """

    def __init__(self, id: int, numéro: str, capacité: int):
        self.id = id
        self.numéro = numéro
        self.capacité = capacité
        self.prisonniers_ids: list[int] = []
        self.statut = StatutCellule.LIBRE

    def est_pleine(self) -> bool:
        return len(self.prisonniers_ids) >= self.capacité

    def ajouter_prisonnier(self, prisonnier_id: int) -> None:
        if self.statut == StatutCellule.HORS_SERVICE:
            raise ValueError("Impossible d'ajouter un prisonnier : cellule hors service.")
        if self.est_pleine():
            raise ValueError("Cellule pleine, capacité maximale atteinte.")

        self.prisonniers_ids.append(prisonnier_id)
        self.statut = StatutCellule.PLEINE if self.est_pleine() else StatutCellule.OCCUPÉE

    def retirer_prisonnier(self, prisonnier_id: int) -> None:
        if prisonnier_id not in self.prisonniers_ids:
            raise ValueError("Ce prisonnier n'est pas dans cette cellule.")

        self.prisonniers_ids.remove(prisonnier_id)
        self.statut = StatutCellule.LIBRE if not self.prisonniers_ids else StatutCellule.OCCUPÉE