import { ChatGPTParser } from '../src/parsers/chatgpt';
import { Role } from '../src/models';

describe('ChatGPTParser', () => {
  let parser: ChatGPTParser;

  beforeEach(() => {
    parser = new ChatGPTParser();
  });

  describe('parseFromHtml', () => {
    it('should parse HTML content and extract conversation', () => {
      // Sample HTML content
      const html = `
        <html>
          <head>
            <title>Coconut compatibility with DeepSeek R1</title>
          </head>
          <body>
            <div>Sample content</div>
          </body>
        </html>
      `;
      
      const url = 'https://chatgpt.com/share/example';
      
      const conversation = parser.parseFromHtml(html, url);
      
      // Check conversation properties
      expect(conversation.url).toBe(url);
      expect(conversation.title).toBe('Coconut compatibility with DeepSeek R1');
      
      // Check messages
      expect(conversation.messages.length).toBe(2);
      
      // Check first message (user)
      expect(conversation.messages[0].role).toBe(Role.USER);
      expect(conversation.messages[0].content).toContain('DeepSeek R1');
      
      // Check second message (assistant)
      expect(conversation.messages[1].role).toBe(Role.ASSISTANT);
      expect(conversation.messages[1].content).toContain('DeepSeek R1 works well');
    });
  });
});
