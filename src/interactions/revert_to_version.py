


from models.document import Document
from models.document_version import DocumentVersion
from fastapi import HTTPException
from playhouse.shortcuts import model_to_dict
from models.user import User
from interactions.get_current_user import get_current_user
from fastapi import Depends
from models.shared_document import SharedDocument

def revert_to_version(request, user_name):
    
    document = Document.get_or_none(id=request.get("document_id"))
    user = User.select().where(User.user_name == user_name).first()
    shared_users = SharedDocument.select(SharedDocument.user).where(SharedDocument.document.id == request.get("id"))
    shared_user_ids = {user.get("id"): user.get("access_type") for user in model_to_dict(shared_users)}
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    if user.id != document.user.id  and not (document.user.id in shared_user_ids.keys() and shared_user_ids[document.user.id]=='editor'):
        raise HTTPException(status_code=403, detail="You do not have permission to revert this document")

    version = DocumentVersion.get_or_none(id=request.GET("version_id"))
    if version is None or version.document.id != request.get("document_id"):
        raise HTTPException(status_code=400, detail="Invalid version id")

    # Revert to the specified version
    document.title = version.title
    document.content = version.content
    document.save()

    return model_to_dict(document)