import { ClaudeParser } from '../src/parsers/claude';
import { Role } from '../src/models';

describe('ClaudeParser', () => {
  let parser: ClaudeParser;

  beforeEach(() => {
    parser = new ClaudeParser();
  });

  describe('parseFromHtml', () => {
    it('should parse HTML content and extract conversation', () => {
      // Sample HTML content from Claude
      const html = `
        <main>
          <header>Redirecting Domains with DNS Records</header>
          <div>
            <p>what domain record to redirect to a different domain?</p>
          </div>
          <div>
            <p>It looks like you're trying to set up a DNS record to redirect from one domain to another.</p>
            <ol>
              <li>Change the record type from "A - Address record" to "CNAME - Canonical name"</li>
              <li>In the "Host" field, enter the subdomain you want to redirect</li>
              <li>In the "Answer / Value" field, enter the full target domain</li>
              <li>Keep your TTL as needed (600 seconds is fine)</li>
            </ol>
          </div>
        </main>
      `;
      
      const url = 'https://claude.ai/share/example';
      
      const conversation = parser.parseFromHtml(html, url);
      
      // Check conversation properties
      expect(conversation.url).toBe(url);
      expect(conversation.title).toBe('Redirecting Domains with DNS Records');
      
      // Check messages
      expect(conversation.messages.length).toBe(2);
      
      // Check first message (user)
      expect(conversation.messages[0].role).toBe(Role.USER);
      expect(conversation.messages[0].content).toContain('domain record');
      
      // Check second message (assistant)
      expect(conversation.messages[1].role).toBe(Role.ASSISTANT);
      expect(conversation.messages[1].content).toContain('DNS record');
    });
  });
});
