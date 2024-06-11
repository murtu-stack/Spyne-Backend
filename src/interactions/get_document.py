
from models.document import Document
from fastapi import HTTPException
from playhouse.shortcuts import model_to_dict
from models.user import User
from interactions.get_current_user import get_current_user
from fastapi import Depends
from models.shared_document import SharedDocument


def get_document(request, user_name):
    document = Document.get_or_none(id=request.get("id"))
    shared_users = SharedDocument.select(SharedDocument.user).where(SharedDocument.document.id == request.get("id"))
    shared_user_ids = [user.get("id") for user in model_to_dict(shared_users)]
    user = User.select().where(User.user_name == user_name).first()
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    if document.is_private and (user.id != document.user.id and document.user.id not in shared_user_ids):
        raise HTTPException(status_code=403, detail="You do not have access to this document")
    
    
    return model_to_dict(document)