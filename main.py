from infrastructure.repositories.prisonnier_repository_memory import PrisonnierRepositoryMemory
from infrastructure.repositories.cellule_repository_memory import CelluleRepositoryMemory
from infrastructure.repositories.gardien_repository_memory import GardienRepositoryMemory

from application.use_cases.incarcerer_prisonnier import IncarcererPrisonnier
from application.use_cases.liberer_prisonnier import LibererPrisonnier
from application.use_cases.transferer_cellule import TransfererCellule
from application.use_cases.assigner_gardien import AssignerGardien

from domain.entities.cellule import Cellule
from domain.entities.gardien import Gardien
from domain.entities.enums import Poste

from presentation.cli import CLI


def creer_donnees_de_test(cellule_repo: CelluleRepositoryMemory, gardien_repo: GardienRepositoryMemory) -> None:
    """Ajoute quelques cellules et gardiens pour pouvoir tester le programme direct."""
    cellule_repo.ajouter(Cellule(id=0, numéro="A1", capacité=10))
    cellule_repo.ajouter(Cellule(id=0, numéro="A2", capacité=10))
    cellule_repo.ajouter(Cellule(id=0, numéro="A3", capacité=10))
    gardien_repo.ajouter(Gardien(id=1, nom="Voltaire",   prenom="Peterly",  matricule="G001", poste=Poste.SURVEILLANCE))
    gardien_repo.ajouter(Gardien(id=2, nom="Louizias",   prenom="Venksy" ,  matricule="G002", poste=Poste.SURVEILLANCE))
    gardien_repo.ajouter(Gardien(id=3, nom="Lesperance", prenom="Brunny",   matricule="G003", poste=Poste.SURVEILLANCE))

def main() -> None:
    # 1. Infrastructure : les implémentations concrètes des repositories
    prisonnier_repo = PrisonnierRepositoryMemory()
    cellule_repo = CelluleRepositoryMemory()
    gardien_repo = GardienRepositoryMemory()

    creer_donnees_de_test(cellule_repo, gardien_repo)

    # 2. Application : les use cases, injectés avec les repositories
    incarcerer = IncarcererPrisonnier(prisonnier_repo, cellule_repo)
    liberer = LibererPrisonnier(prisonnier_repo, cellule_repo)
    transferer = TransfererCellule(prisonnier_repo, cellule_repo)
    assigner_gardien = AssignerGardien(gardien_repo, cellule_repo)

    # 3. Presentation : le CLI, injecté avec les use cases + repositories (pour les listes)
    cli = CLI(
        incarcerer=incarcerer,
        liberer=liberer,
        transferer=transferer,
        assigner_gardien=assigner_gardien,
        prisonnier_repo=prisonnier_repo,
        cellule_repo=cellule_repo,
        gardien_repo=gardien_repo,
    )

    cli.demarrer()


if __name__ == "__main__":
    main()