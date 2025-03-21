# ChatMix (TypeScript)

A TypeScript library for parsing conversation history from various AI chat platforms.

## Features

- **Multi-Platform Support**: Parse conversations from different AI chat platforms:
  - ChatGPT (via share links)
  - Claude (via share links)
- **Structured Data Models**: Conversations and messages are represented as structured TypeScript objects
- **Role Detection**: Automatically identifies user and assistant messages
- **Content Extraction**: Preserves the content structure including lists, headings, and formatted text

## Installation

```bash
npm install chatmix
```

## Usage

### Parsing from ChatGPT

```typescript
import { ChatGPTParser } from 'chatmix';

// Initialize the parser
const parser = new ChatGPTParser();

// Parse from a URL
parser.parseFromUrl("https://chatgpt.com/share/67db5526-1ddc-8013-9824-145459e33171")
  .then(conversation => {
    // Access conversation data
    console.log(`Title: ${conversation.title}`);
    console.log(`URL: ${conversation.url}`);
    console.log(`Messages: ${conversation.messages.length}`);
    
    // Process messages
    conversation.messages.forEach((message, i) => {
      console.log(`\n--- Message ${i+1} (${message.role}) ---`);
      console.log(message.content.length > 100 ? message.content.substring(0, 100) + "..." : message.content);
    });
  })
  .catch(error => console.error("Error parsing conversation:", error));
```

### Parsing from Claude

```typescript
import { ClaudeParser } from 'chatmix';

// Initialize the parser
const parser = new ClaudeParser();

// Parse from a URL
parser.parseFromUrl("https://claude.ai/share/d8c56ef2-044e-4d31-a71e-8c8081bc5f00")
  .then(conversation => {
    // Access conversation data
    console.log(`Title: ${conversation.title}`);
    console.log(`URL: ${conversation.url}`);
    console.log(`Messages: ${conversation.messages.length}`);
    
    // Process messages
    conversation.messages.forEach((message, i) => {
      console.log(`\n--- Message ${i+1} (${message.role}) ---`);
      console.log(message.content.length > 100 ? message.content.substring(0, 100) + "..." : message.content);
    });
  })
  .catch(error => console.error("Error parsing conversation:", error));
```

## Data Models

The library uses the following data models:

```typescript
enum Role {
  USER = 'user',
  ASSISTANT = 'assistant'
}

interface Message {
  role: Role;
  content: string;
  rawHtml?: string;
}

interface Conversation {
  messages: Message[];
  url: string;
  title?: string;
}
```

## Platform Differences

- **ChatGPT**: Uses article elements with h5/h6 headers to identify messages
- **Claude**: Uses a different HTML structure with specific div elements for user and assistant messages

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
