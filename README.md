# 🏛️ Gestion d'une Prison

Un mini-projet Python illustrant la mise en pratique de la **Clean Architecture** à travers un système de gestion de prison en ligne de commande (CLI).

---

## 📖 Description

Ce projet simule la gestion basique d'un établissement pénitentiaire : incarcération, libération et transfert de prisonniers, gestion des cellules et assignation de gardiens. L'objectif n'est pas de produire une application prête pour la production, mais de servir de **support d'apprentissage** pour comprendre comment structurer une application Python selon les principes de la Clean Architecture (Robert C. Martin / "Uncle Bob").

---

## 🎯 Objectif du projet

L'objectif principal est pédagogique : apprendre à **séparer les responsabilités** d'une application en couches indépendantes, où :

- La logique métier (règles de gestion d'une prison) ne dépend **d'aucun framework, base de données ou interface utilisateur**.
- Chaque couche ne connaît que les couches situées **plus au centre** qu'elle — jamais l'inverse.
- On peut remplacer une technologie (ex: passer du stockage en mémoire à une vraie base de données) **sans toucher à la logique métier**.

Ce projet démontre concrètement pourquoi cette séparation est utile : elle rend le code **testable, évolutif et maintenable** sur le long terme.

---

## 🧠 Pourquoi la Clean Architecture est importante

Dans un projet classique, la logique métier finit souvent mélangée avec le code de base de données ou d'interface utilisateur. Résultat : le moindre changement technique (changer de base de données, ajouter une API) oblige à réécrire une partie du cœur métier.

La Clean Architecture répond à ce problème en imposant une règle simple :

> **Les dépendances ne pointent que vers l'intérieur.**

Concrètement, ça veut dire que :
- Le domaine métier (`domain`) ne sait rien du monde extérieur.
- Les couches externes (bases de données, CLI, API) dépendent du domaine — jamais l'inverse.

Cette approche apporte plusieurs bénéfices directs :
- **Testabilité** : la logique métier se teste sans base de données ni interface.
- **Flexibilité technologique** : changer de stockage (mémoire → SQLite → MySQL) ne demande que quelques lignes dans `main.py`.
- **Clarté** : chaque fichier a un rôle précis, ce qui facilite la lecture et la maintenance du code, même après plusieurs mois.

---

## 🛠️ Technologies utilisées

| Élément | Technologie |
|---|---|
| Langage | Python 3.14 |
| Interface | CLI (ligne de commande, module `input()` natif) |
| Stockage | Dictionnaires Python en mémoire (aucune base de données externe pour l'instant) |
| Typage | Type hints natifs Python (`str`, `int`, `list[...]`, `X \| None`) |
| Architecture | Clean Architecture (Domain / Application / Infrastructure / Presentation) |
| Gestion de version | Git & GitHub |

Aucune dépendance externe n'est requise pour faire tourner le projet — tout repose sur la bibliothèque standard de Python.

---

## 🏗️ Structure du projet

```
gestion_prison/
│
├── domain/                          # Cœur métier — aucune dépendance externe
│   └── entities/
│       ├── prisonnier.py            # Entité Prisonnier + règles (transfert, libération)
│       ├── gardien.py               # Entité Gardien + règles (assignation de cellules)
│       ├── cellule.py               # Entité Cellule + règles (capacité, occupation)
│       └── enums.py                 # StatutPrisonnier, StatutCellule, Poste
│
├── application/                     # Règles applicatives — orchestrent le domaine
│   ├── use_cases/
│   │   ├── incarcerer_prisonnier.py
│   │   ├── liberer_prisonnier.py
│   │   ├── transferer_cellule.py
│   │   └── assigner_gardien.py
│   └── interfaces/                  # Contrats abstraits (ports)
│       ├── prisonnier_repository.py
│       ├── cellule_repository.py
│       └── gardien_repository.py
│
├── infrastructure/                   # Implémentations concrètes des interfaces
│   └── repositories/
│       ├── prisonnier_repository_memory.py
│       ├── cellule_repository_memory.py
│       └── gardien_repository_memory.py
│
├── presentation/                     # Interface utilisateur (CLI)
│   └── cli.py
│
├── main.py                          # Composition root — assemble toutes les couches
├── requirements.txt
└── README.md
```

---

## ⚙️ Comment le système fonctionne

### Les 4 couches, de l'intérieur vers l'extérieur

**1. Domain (Entities)**
Contient les objets métier purs : `Prisonnier`, `Gardien`, `Cellule`. Chaque entité protège ses propres règles — par exemple, une `Cellule` refuse d'accueillir un prisonnier si elle est pleine. Cette couche ne dépend de rien d'autre dans le projet.

**2. Application (Use Cases & Interfaces)**
Les *use cases* (ex: `IncarcererPrisonnier`) orchestrent une action métier complète : ils vérifient les règles, appellent les entités, et persistent les changements. Ils ne dépendent que des *interfaces* (contrats abstraits comme `PrisonnierRepository`), jamais d'une implémentation concrète.

**3. Infrastructure (Repositories)**
Implémente concrètement les interfaces définies dans `application`. Actuellement, le stockage se fait en mémoire via des dictionnaires Python (`{id: objet}`), avec un compteur auto-incrémenté simulant une clé primaire de base de données.

**4. Presentation (CLI)**
Le menu interactif que l'utilisateur manipule. Il ne contient **aucune règle métier** — il se contente de récupérer les entrées utilisateur, d'appeler le use case correspondant, et d'afficher le résultat.

### Le flux d'exécution

```
Utilisateur → CLI → Use Case → Entités (règles métier) → Repository → Stockage
```

Exemple concret avec l'incarcération d'un prisonnier :
1. L'utilisateur choisit l'option "Incarcérer un prisonnier" dans le CLI.
2. Le CLI récupère les infos saisies et appelle `IncarcererPrisonnier.executer(...)`.
3. Le use case vérifie que la cellule existe et n'est pas pleine.
4. Une nouvelle entité `Prisonnier` est créée et sauvegardée via `PrisonnierRepository`.
5. La cellule est mise à jour pour refléter le nouvel occupant.
6. Le résultat est renvoyé au CLI, qui l'affiche à l'utilisateur.

### Le point d'assemblage : `main.py`

C'est le seul fichier du projet qui connaît **toutes** les couches à la fois. Il instancie les repositories concrets, les injecte dans les use cases, puis injecte les use cases dans le CLI. C'est ce qu'on appelle la **composition root** — et c'est ce qui permet, par exemple, de remplacer le stockage en mémoire par une vraie base de données en ne modifiant que ce fichier.

---

## ▶️ Lancer le projet

```bash
python3 main.py
```

Un menu interactif s'affiche, permettant d'incarcérer, libérer, transférer des prisonniers, d'assigner des gardiens, et de lister les prisonniers/cellules enregistrés.

---

## 🔮 Évolutions possibles

- Remplacer le stockage en mémoire par une vraie base de données (SQLite/MySQL) sans modifier `domain/`, `application/` ni `presentation/`.
- Ajouter une API REST (FastAPI) en parallèle du CLI, en réutilisant les mêmes use cases.
- Ajouter des tests unitaires sur les entités et use cases (facilité justement par cette architecture).
