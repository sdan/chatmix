from dataclasses import dataclass
from typing import List, Optional
from enum import Enum


class Role(Enum):
    USER = 'user'
    ASSISTANT = 'assistant'


@dataclass
class Message:
    role: Role
    content: str
    raw_html: Optional[str] = None


@dataclass
class Conversation:
    messages: List[Message]
    url: str
    title: Optional[str] = None

