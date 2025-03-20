import unittest
from chatmix.parsers import ClaudeParser, Message, Conversation, Role
from bs4 import BeautifulSoup


class TestClaudeParser(unittest.TestCase):
    def test_parse_from_html(self):
        # Sample HTML content from Claude
        html = """
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
        """
        
        parser = ClaudeParser()
        conversation = parser.parse_from_html(html, "https://claude.ai/example")
        
        # Check conversation properties
        self.assertEqual(conversation.url, "https://claude.ai/example")
        
        # Check messages
        self.assertEqual(len(conversation.messages), 2)
        
        # Check first message (user)
        self.assertEqual(conversation.messages[0].role, Role.USER)
        self.assertIn("domain record", conversation.messages[0].content)
        
        # Check second message (assistant)
        self.assertEqual(conversation.messages[1].role, Role.ASSISTANT)
        self.assertIn("DNS record", conversation.messages[1].content)


if __name__ == "__main__":
    unittest.main()
