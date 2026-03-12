import uuid
import time
from dataclasses import dataclass

@dataclass
class User:
    email: str
    password: str

class UserFactory:
    
    @staticmethod
    def create_test_user(password: str = "StrongPass123!") -> User:
        # Using a timestamp + short UUID to generate unique users for repeated test executions
        unique_id = f"{int(time.time())}_{uuid.uuid4().hex[:4]}"
        return User(
            email=f"qa_test_{unique_id}@gmail.com",
            password=password
        )