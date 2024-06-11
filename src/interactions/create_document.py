
from models.document import Document
from models.user import User
from models.document_version import DocumentVersion
from playhouse.shortcuts import model_to_dict
from fastapi.encoders import jsonable_encoder
def create_document(request,user_name):
    user = User.select().where(User.user_name == user_name).first()
    document = None
    if not user:
        return
    with Document._meta.database.atomic():
        try:
            document = Document.create(title=request.get("title"), content=request.get("content"), user=user, is_private=request.get("is_private"))
            DocumentVersion.create(document=document, title=document.title, content=document.content)
            return jsonable_encoder(model_to_dict(document))
        except:
            raise 

  