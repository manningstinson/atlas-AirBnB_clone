from models.base_model import BaseModel

class User(BaseModel):
    """User class inheriting from BaseModel."""
    
    def __init__(self, *args, **kwargs):
        """Initialize User instance."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
