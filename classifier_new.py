from gmail import connect_gmail, search_messages, apply_label

# Dictionnaire des catégories avec leurs mots-clés
CATEGORIES = {
    "Confirmation Candidatures": ["nous avons bien reçu", "accusé de réception", "candidature enregistrée"],
    "Refus Candidatures": ["nous avons le regret", "n'a pas été retenue", "malheureusement"],
    "Réponses Positives": ["félicitations", "entretien", "retenue", "convocation", "plaisir"],
    "Newsletters": ["se désinscrire", "newsletter", "actualités", "abonnement", "bulletin"]
}

def classify_new_emails():
    print("Connexion à Gmail...")
    service = connect_gmail()

    for label, keywords in CATEGORIES.items():
        print(f"\nTraitement : {label}")
        for keyword in keywords:
            query = f"in:inbox is:unread {keyword}"
            message_ids = search_messages(service, "me", query)
            print(f"🔍 {keyword} → {len(message_ids)} mails non lus trouvés")
            for msg_id in message_ids:
                apply_label(service, "me", msg_id, label)

    print("\nClassification des nouveaux mails terminée.")

if __name__ == "__main__":
    classify_new_emails()
