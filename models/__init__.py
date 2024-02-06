# models/__init__.py

from models.engine.file_storage import FileStorage
from models.user import User  # Import the User class

storage = FileStorage()
storage.reload()
