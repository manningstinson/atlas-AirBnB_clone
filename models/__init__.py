# models/__init__.py

# Import necessary modules
from .engine.file_storage import FileStorage

# Initialize storage
storage = FileStorage()
storage.reload()
