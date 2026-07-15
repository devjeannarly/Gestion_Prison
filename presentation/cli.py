from datetime import date

from application.use_cases.incarcerer_prisonnier import IncarcererPrisonnier
from application.use_cases.liberer_prisonnier import LibererPrisonnier
from application.use_cases.transferer_cellule import TransfererCellule
from application.use_cases.assigner_gardien import AssignerGardien
from application.interfaces.cellule_repository import CelluleRepository
from application.interfaces.gardien_repository import GardienRepository
from application.interfaces.prisonnier_repository import PrisonnierRepository


class CLI:
    """
    Interface utilisateur en ligne de commande.
    Ne contient aucune logique métier : elle ne fait qu'orchestrer les inputs
    et appeler les use cases correspondants.
    """

    def __init__(
        self,
        incarcerer: IncarcererPrisonnier,
        liberer: LibererPrisonnier,
        transferer: TransfererCellule,
        assigner_gardien: AssignerGardien,
        prisonnier_repo: PrisonnierRepository,
        cellule_repo: CelluleRepository,
        gardien_repo: GardienRepository,
    ):
        self.incarcerer = incarcerer
        self.liberer = liberer
        self.transferer = transferer
        self.assigner_gardien = assigner_gardien
        self.prisonnier_repo = prisonnier_repo
        self.cellule_repo = cellule_repo
        self.gardien_repo = gardien_repo

    def demarrer(self) -> None:
        while True:
            self._afficher_menu()
            choix = input("Ton choix : ").strip()

            try:
                if choix == "1":
                    self._incarcerer_prisonnier()
                elif choix == "2":
                    self._liberer_prisonnier()
                elif choix == "3":
                    self._transferer_prisonnier()
                elif choix == "4":
                    self._assigner_gardien()
                elif choix == "5":
                    self._lister_prisonniers()
                elif choix == "6":
                    self._lister_cellules()
                elif choix == "0":
                    print("À bientôt !")
                    break
                else:
                    print("Choix invalide, réessaie.\n")
            except ValueError as erreur:
                print(f"Erreur : {erreur}\n")

    def _afficher_menu(self) -> None:
        print("\n=== GESTION D'UNE PRISON ===")
        print("1. Incarcérer un prisonnier")
        print("2. Libérer un prisonnier")
        print("3. Transférer un prisonnier")
        print("4. Assigner un gardien à une cellule")
        print("5. Lister les prisonniers")
        print("6. Lister les cellules")
        print("0. Quitter")

    def _incarcerer_prisonnier(self) -> None:
        nom = input("Nom : ").strip()
        prenom = input("Prénom : ").strip()
        matricule = input("Matricule : ").strip()
        cellule_id = int(input("Id de la cellule : ").strip())

        prisonnier = self.incarcerer.executer(
            nom=nom,
            prenom=prenom,
            date_naissance=date(2000, 1, 1),  # simplifié pour l'instant
            matricule=matricule,
            cellule_id=cellule_id,
        )
        print(f"✅ Prisonnier {prisonnier.prenom} {prisonnier.nom} incarcéré (id={prisonnier.id}).")

    def _liberer_prisonnier(self) -> None:
        prisonnier_id = int(input("Id du prisonnier à libérer : ").strip())
        self.liberer.executer(prisonnier_id)
        print("✅ Prisonnier libéré.")

    def _transferer_prisonnier(self) -> None:
        prisonnier_id = int(input("Id du prisonnier : ").strip())
        nouvelle_cellule_id = int(input("Id de la nouvelle cellule : ").strip())
        self.transferer.executer(prisonnier_id, nouvelle_cellule_id)
        print("✅ Prisonnier transféré.")

    def _assigner_gardien(self) -> None:
        gardien_id = int(input("Id du gardien : ").strip())
        cellule_id = int(input("Id de la cellule : ").strip())
        self.assigner_gardien.executer(gardien_id, cellule_id)
        print("✅ Gardien assigné.")

    def _lister_prisonniers(self) -> None:
        prisonniers = self.prisonnier_repo.lister_tous()
        if not prisonniers:
            print("Aucun prisonnier enregistré.")
            return
        for p in prisonniers:
            print(f"[{p.id}] {p.prenom} {p.nom} — statut: {p.statut.value} — cellule: {p.cellule_id}")

    def _lister_cellules(self) -> None:
        cellules = self.cellule_repo.lister_tous()
        if not cellules:
            print("Aucune cellule enregistrée.")
            return
        for c in cellules:
            print(f"[{c.id}] Cellule {c.numéro} — statut: {c.statut.value} — occupants: {len(c.prisonniers_ids)}/{c.capacité}")