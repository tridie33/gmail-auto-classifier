from gmail import connect_gmail, search_messages, apply_label

# Dictionnaire des catégories avec leurs mots-clés respectifs
CATEGORIES = {
    "Confirmation Candidatures": ["nous avons bien reçu", "accusé de réception", "candidature enregistrée"],
    "Refus Candidatures": ["nous avons le regret", "n'a pas été retenue", "malheureusement"],
    "Réponses Positives": ["félicitations", "entretien", "retenue", "convocation", "plaisir"],
    "Newsletters": ["se désinscrire", "newsletter", "actualités", "abonnement", "bulletin"]
}

def classify_old_emails():
    print("Connexion à Gmail...")
    service = connect_gmail()

    for label, keywords in CATEGORIES.items():
        print(f"\nTraitement de la catégorie : {label}")
        # Recherche des messages contenant un des mots-clés
        for keyword in keywords:
            query = f"in:inbox {keyword}"
            message_ids = search_messages(service, "me", query)
            print(f"🔎 Mot-clé '{keyword}' → {len(message_ids)} messages trouvés")
            for msg_id in message_ids:
                apply_label(service, "me", msg_id, label)

    print("\nClassification des anciens mails terminée.")

if __name__ == "__main__":
    classify_old_emails()
