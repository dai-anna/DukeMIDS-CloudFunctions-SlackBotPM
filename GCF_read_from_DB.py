from google.cloud import firestore
import random

db = firestore.Client()

def whatsappbot(request):
    db = firestore.Client()
    col_ref = db.collection('whatsapp-bot')
    docs = col_ref.stream()
    results = []
    for doc in docs:
        results.append(doc.to_dict().get("Message", "Hmm doesnt make sense"))
    result = random.choice(results)
    return {
        "response_type": "in_channel",
        "text": result
    }