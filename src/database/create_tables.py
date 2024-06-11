from database.db_session import db
from models.user import User
from models.document import Document
from models.document_version import DocumentVersion
from models.document_viewer import DocumentViewer
from models.shared_document import SharedDocument

def create_tables():
    try:
        db.create_tables(
            [SharedDocument]
        )
        db.close()
        print("created tables")
    except:
        print("Exception while creating table")
        raise
