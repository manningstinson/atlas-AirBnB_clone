from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

def get_storage():
    return storage