

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
class DocumentVersion(BaseModel):
    document = ForeignKeyField(Document, backref='versions')
    title = CharField()
    content = TextField()
    
    
    class Meta:
        table_name = 'document_versions'