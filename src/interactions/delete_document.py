
from models.document import Document
from models.document_version import DocumentVersion
from fastapi import HTTPException
from playhouse.shortcuts import model_to_dict
from models.user import User

def delete_document(request, user_name):
    user = User.select().where(User.user_name == user_name).first()
    document = Document.get_or_none(id=request.get("document_id"))
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    if user.id != document.user.id:
        raise HTTPException(status_code=403, detail="You do not have permission to delete this document")

    document.delete_instance()
    return {"message": "Document deleted successfully"}