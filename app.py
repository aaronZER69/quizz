def sio_orientation():
    print("Bienvenue dans le quiz d'orientation BTS SIO !")
    print("Répondez aux questions en choisissant 'A' ou 'B'.\n")

    questions = [
        "Quel type de tâche préférez-vous ?\nA) Développement d'applications\nB) Gestion des réseaux et systèmes",
        "Comment vous imaginez-vous travailler dans une entreprise ?\nA) Créer des logiciels\nB) Assurer le bon fonctionnement des infrastructures",
        "Quels outils aimez-vous le plus utiliser ?\nA) Langages de programmation\nB) Outils d’administration réseau",
        "Qu’est-ce qui vous motive le plus ?\nA) Résoudre des problèmes avec du code\nB) Configurer et optimiser des réseaux",
        "Avez-vous déjà une expérience ou une préférence ?\nA) Création de logiciels ou sites web\nB) Configuration matérielle ou réseau",
        "Quelle notion vous intéresse le plus ?\nA) Bases de données et interfaces utilisateur\nB) Sécurité informatique et administration système",
        "Quelle situation vous semble la plus satisfaisante ?\nA) Voir un logiciel fonctionner\nB) Voir une infrastructure réseau fonctionner sans faille",
        "Préférez-vous travailler sur :\nA) Un projet de développement sur le long terme\nB) Des tâches techniques variées",
        "Lors de vos études précédentes, qu'avez-vous préféré ?\nA) Les projets en programmation\nB) Les projets en réseau ou matériel",
        "Que pensez-vous de la programmation ?\nA) J’adore ça\nB) Je préfère travailler sur l’aspect matériel et réseau"
    ]

    scores = {"A": 0, "B": 0}

    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question}")
        while True:
            choix = input("Votre choix (A/B) : ").upper()
            if choix in ["A", "B"]:
                scores[choix] += 1
                break
            else:
                print("Veuillez entrer 'A' ou 'B'.")

    print("\nRésultats du quiz :")
    if scores["A"] > scores["B"]:
        print("Vous êtes fait pour l'option SLAM (Solutions Logicielles et Applications Métier) !")
        print("Vous aimez concevoir, coder et améliorer des applications et logiciels.")
    else:
        print("Vous êtes fait pour l'option SISR (Solutions d’Infrastructure, Systèmes et Réseaux) !")
        print("Vous préférez travailler sur les infrastructures, les réseaux et la sécurité informatique.")
    print("-" * 50)

# Lancer le quiz
sio_orientation()
