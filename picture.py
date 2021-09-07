from dataclasses import dataclass
from statusnaked import StatusNaked


@dataclass
class HentaiPicture:
    id: int
    censorship: bool
    status_naked: StatusNaked
    bdsm: bool
    people: int
    anime: bool
    parents: []
    celebritiy: bool
    artist: str