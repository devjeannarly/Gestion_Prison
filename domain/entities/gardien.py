from domain.entities.enums import Poste


class Gardien:
    """
    Représente un gardien de prison.

    Règles métier :
    - Un gardien ne peut être assigné qu'à des cellules distinctes (pas de doublons).
    """

    def __init__(self, id: int, nom: str, prenom: str, matricule: str, poste: Poste):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.matricule = matricule
        self.poste = poste
        self.cellules_assignees_ids: list[int] = []

    def assigner_cellule(self, cellule_id: int) -> None:
        if cellule_id in self.cellules_assignees_ids:
            raise ValueError("Cette cellule est déjà assignée à ce gardien.")

        self.cellules_assignees_ids.append(cellule_id)

    def retirer_cellule(self, cellule_id: int) -> None:
        if cellule_id not in self.cellules_assignees_ids:
            raise ValueError("Cette cellule n'est pas assignée à ce gardien.")

        self.cellules_assignees_ids.remove(cellule_id)