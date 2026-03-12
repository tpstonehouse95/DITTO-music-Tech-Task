from dataclasses import dataclass

@dataclass(frozen=True)
class AppConfig:
    base_url: str = "https://dittomusic.com"
    auth_url: str = "https://login.dittomusic.com"