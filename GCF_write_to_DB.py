from google.cloud import firestore

db = firestore.Client()

def whatsappbot(request):
    db = firestore.Client()
    doc_ref = db.collection('whatsapp-bot').document()

    doc_ref.set(request.get_json())

    return {"status": "ok cool."}