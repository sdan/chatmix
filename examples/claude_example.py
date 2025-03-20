#!/usr/bin/env python3
"""
Example script demonstrating the Claude parser functionality.
"""

import os
import sys
import json

# Add the parent directory to the path so we can import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from chatmix.parsers import ClaudeParser

def main():
    # Parse from a URL
    url = sys.argv[1] if len(sys.argv) > 1 else "https://claude.ai/share/d8c56ef2-044e-4d31-a71e-8c8081bc5f00"
    
    print(f"No URL provided, using example: {url}" if len(sys.argv) <= 1 else f"Parsing conversation from: {url}")
    
    # Initialize the parser
    parser = ClaudeParser()
    
    # Parse the conversation
    conversation = parser.parse_from_url(url)
    
    # Print conversation details
    print(f"\nTitle: {conversation.title}")
    print(f"URL: {conversation.url}")
    print(f"Messages: {len(conversation.messages)}")
    
    print("\nConversation:\n")
    
    # Print each message
    for i, message in enumerate(conversation.messages):
        print(f"--- Message {i+1} ({message.role.value}) ---")
        content_preview = message.content[:100] + "..." if len(message.content) > 100 else message.content
        print(content_preview)
        print()
    
    # Export to JSON
    with open("claude_conversation.json", "w") as f:
        json_data = {
            "title": conversation.title,
            "url": conversation.url,
            "messages": [
                {
                    "role": message.role.value,
                    "content": message.content
                }
                for message in conversation.messages
            ]
        }
        json.dump(json_data, f, indent=2)
    
    print("Conversation exported to claude_conversation.json")

if __name__ == "__main__":
    main()
