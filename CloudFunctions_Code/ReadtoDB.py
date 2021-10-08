# Please note this code lives in Google Cloud Functions,
# and thus does not work out of GitHub without additional authentication.

from google.cloud import firestore
import random

db = firestore.Client()


def whatsappbot(request):
    """To pull a random message from my Firestore DB"""
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
