# ChatMix

A Python library for parsing conversation history from various AI chat platforms.

## Features

- **Multi-Platform Support**: Parse conversations from different AI chat platforms:
  - ChatGPT (via share links)
  - Claude (via share links)
- **Structured Data Models**: Conversations and messages are represented as structured Python objects
- **Role Detection**: Automatically identifies user and assistant messages
- **Content Extraction**: Preserves the content structure including lists, headings, and formatted text

## Installation

```bash
pip install chatmix
```

## Usage

### Parsing from ChatGPT

```python
from chatmix.parsers import ChatGPTParser

# Initialize the parser
parser = ChatGPTParser()

# Parse from a URL
conversation = parser.parse_from_url("https://chatgpt.com/share/67db5526-1ddc-8013-9824-145459e33171")

# Access conversation data
print(f"Title: {conversation.title}")
print(f"URL: {conversation.url}")
print(f"Messages: {len(conversation.messages)}")

# Process messages
for i, message in enumerate(conversation.messages):
    print(f"\n--- Message {i+1} ({message.role.value}) ---")
    print(message.content[:100] + "..." if len(message.content) > 100 else message.content)
```

### Parsing from Claude

```python
from chatmix.parsers import ClaudeParser

# Initialize the parser
parser = ClaudeParser()

# Parse from a URL
conversation = parser.parse_from_url("https://claude.ai/share/d8c56ef2-044e-4d31-a71e-8c8081bc5f00")

# Access conversation data
print(f"Title: {conversation.title}")
print(f"URL: {conversation.url}")
print(f"Messages: {len(conversation.messages)}")

# Process messages
for i, message in enumerate(conversation.messages):
    print(f"\n--- Message {i+1} ({message.role.value}) ---")
    print(message.content[:100] + "..." if len(message.content) > 100 else message.content)
```

## Data Models

The library uses the following data models:

```python
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
```

## Platform Differences

- **ChatGPT**: Uses article elements with h5/h6 headers to identify messages
- **Claude**: Uses a different HTML structure with specific div elements for user and assistant messages

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
