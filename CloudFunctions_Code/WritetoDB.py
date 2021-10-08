# Please note this code lives in Google Cloud Functions,
# and thus does not work out of GitHub without additional authentication.

from google.cloud import firestore

db = firestore.Client()


def whatsappbot(request):
    """To write new messages to my Firestore DB"""
    db = firestore.Client()
    doc_ref = db.collection('whatsapp-bot').document()

    doc_ref.set(request.get_json())

    return {"status": "ok cool."}
