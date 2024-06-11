
from models.user import User
from models.document import Document
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
class SharedDocument(BaseModel):
    id = BigAutoField(primary_key = True)
    document = ForeignKeyField(Document, backref='shared_documents')
    user = ForeignKeyField(User, backref='shared_documents')
    access_type = CharField(default="viewer")

    class Meta:
        table_name = 'shared_documents'
        