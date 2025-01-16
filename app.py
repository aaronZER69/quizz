def orientation_quiz():
    print("Bienvenue au quiz d'orientation scolaire !")
    print("Répondez aux questions en entrant le chiffre correspondant à votre choix.")
    print("-" * 50)

    scores = {
        "scientifique": 0,
        "littéraire": 0,
        "artistique": 0,
        "technologique": 0,
        "économique": 0,
    }

    # Question 1
    print("\n1. Quelle matière préférez-vous ?")
    print("1) Mathématiques ou physique-chimie")
    print("2) Philosophie ou littérature")
    print("3) Arts plastiques ou musique")
    print("4) Informatique ou électronique")
    print("5) Économie ou gestion")
    choix = int(input("Votre choix : "))
    if choix == 1:
        scores["scientifique"] += 1
    elif choix == 2:
        scores["littéraire"] += 1
    elif choix == 3:
        scores["artistique"] += 1
    elif choix == 4:
        scores["technologique"] += 1
    elif choix == 5:
        scores["économique"] += 1

    # Question 2
    print("\n2. Quel type d'activité vous plaît le plus ?")
    print("1) Résoudre des problèmes complexes")
    print("2) Lire et écrire des textes")
    print("3) Créer des œuvres ou des projets visuels")
    print("4) Concevoir et programmer des outils")
    print("5) Analyser des données et des graphiques")
    choix = int(input("Votre choix : "))
    if choix == 1:
        scores["scientifique"] += 1
    elif choix == 2:
        scores["littéraire"] += 1
    elif choix == 3:
        scores["artistique"] += 1
    elif choix == 4:
        scores["technologique"] += 1
    elif choix == 5:
        scores["économique"] += 1

    # Question 3
    print("\n3. Comment préférez-vous travailler ?")
    print("1) En laboratoire avec des expériences")
    print("2) En bibliothèque ou en rédaction")
    print("3) En studio ou sur scène")
    print("4) Sur ordinateur ou avec des machines")
    print("5) Dans un bureau ou en équipe sur des projets d'entreprise")
    choix = int(input("Votre choix : "))
    if choix == 1:
        scores["scientifique"] += 1
    elif choix == 2:
        scores["littéraire"] += 1
    elif choix == 3:
        scores["artistique"] += 1
    elif choix == 4:
        scores["technologique"] += 1
    elif choix == 5:
        scores["économique"] += 1

    # Calcul des résultats
    domaine_recommande = max(scores, key=scores.get)

    print("\nRésultats du quiz :")
    print("Votre domaine recommandé est :", domaine_recommande.capitalize())
    print("-" * 50)

    # Suggestions spécifiques
    if domaine_recommande == "scientifique":
        print("Orientation suggérée : études en sciences, médecine, ingénierie ou recherche.")
    elif domaine_recommande == "littéraire":
        print("Orientation suggérée : études en lettres, histoire, philosophie, journalisme.")
    elif domaine_recommande == "artistique":
        print("Orientation suggérée : arts appliqués, design, musique, cinéma.")
    elif domaine_recommande == "technologique":
        print("Orientation suggérée : informatique, robotique, électronique, BTS SIO ou DUT Info.")
    elif domaine_recommande == "économique":
        print("Orientation suggérée : gestion, finance, marketing, commerce international.")

# Lancer le quiz
orientation_quiz()
