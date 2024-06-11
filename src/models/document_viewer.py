

from datetime import datetime
from libs.enums import DocumentStateEnum
from database.base_model import BaseModel
from playhouse.postgres_ext import (
    BigAutoField,
    CharField,
    DateTimeField,
    BigIntegerField,
    ForeignKeyField,
    TextField,
    BooleanField
)
from models.user import User
from models.document import Document


class DocumentViewer(BaseModel):
    user = ForeignKeyField(User, backref='document_viewers')
    document = ForeignKeyField(Document, backref='document_viewers')

    class Meta:
        table_name = "document_viewers"
        
        
        