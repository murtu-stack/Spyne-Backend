
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
class Document(BaseModel):
    id = BigAutoField(primary_key=True)
    title = CharField()
    content = TextField()
    user = ForeignKeyField(User, backref='documents')
    is_private = BooleanField(default=False)
    state = CharField(default='draft')

    class Meta:
        table_name = 'documents'