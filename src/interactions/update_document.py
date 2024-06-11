

from models.document import Document
from models.document_version import DocumentVersion
from fastapi import HTTPException
from playhouse.shortcuts import model_to_dict
from models.user import User
from models.shared_document import SharedDocument

def update_document(request, user_name):
    
    user = User.select().where(User.user_name == user_name).first()
    existing_document = Document.get_or_none(id=request.get("id"))
    shared_users = SharedDocument.select(SharedDocument.user).where(SharedDocument.document.id == request.get("id"))
    shared_user_ids = {user.get("id"): user.get("access_type") for user in model_to_dict(shared_users)}
    if existing_document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    if ((user.id != existing_document.user.id) and not (existing_document.user.id in shared_user_ids.keys() and shared_user_ids[existing_document.user.id]=='editor')):
        raise HTTPException(status_code=403, detail="You do not have permission to update this document")

    # Create a new version of the document
    DocumentVersion.create(document=existing_document, title=request.get("title"), content=request.get("content"))
    
    # Update the document
    existing_document.title = request.get("title")
    existing_document.content = request.get("content")
    existing_document.save()
    
    return model_to_dict(existing_document)