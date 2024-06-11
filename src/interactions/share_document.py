

from models.document import Document
from models.user import User
from models.document_version import DocumentVersion
from fastapi import HTTPException
from playhouse.shortcuts import model_to_dict
from models.document import Document
from models.document_version import DocumentVersion
from models.shared_document import SharedDocument



def share_document(request, user_name):
    document = Document.get_or_none(id=request.get("document_id"))
    user = User.select().where(User.user_name == user_name).first()
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    if user.user_name != document.user.user_name:
        raise HTTPException(status_code=403, detail="You do not have permission to share this document")

    user_to_share = User.get_or_none(id=request.get("user_id"))
    if user_to_share is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if the document is already shared with the user
    existing_share = SharedDocument.get_or_none(document=document, user=user_to_share)
    if existing_share is not None:
        raise HTTPException(status_code=400, detail="Document is already shared with this user")

    # Share the document with the user
    shared_document = SharedDocument.create(document=document, user=user_to_share)
    return model_to_dict(shared_document)