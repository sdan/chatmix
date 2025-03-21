/**
 * Example script demonstrating the Claude parser functionality.
 */

import { ClaudeParser } from '../src/parsers/claude';

async function main() {
  // Parse from a URL
  const url = process.argv[2] || "https://claude.ai/share/d8c56ef2-044e-4d31-a71e-8c8081bc5f00";
  
  console.log(process.argv.length <= 2 ? `No URL provided, using example: ${url}` : `Parsing conversation from: ${url}`);
  
  // Initialize the parser
  const parser = new ClaudeParser();
  
  try {
    // Parse the conversation
    const conversation = await parser.parseFromUrl(url);
    
    // Print conversation details
    console.log(`\nTitle: ${conversation.title}`);
    console.log(`URL: ${conversation.url}`);
    console.log(`Messages: ${conversation.messages.length}`);
    
    console.log("\nConversation:\n");
    
    // Print each message
    for (let i = 0; i < conversation.messages.length; i++) {
      const message = conversation.messages[i];
      console.log(`--- Message ${i+1} (${message.role}) ---`);
      const contentPreview = message.content.length > 100 ? message.content.substring(0, 100) + "..." : message.content;
      console.log(contentPreview);
      console.log();
    }
    
    // Export to JSON
    const fs = require('fs');
    const jsonData = {
      title: conversation.title,
      url: conversation.url,
      messages: conversation.messages.map(message => ({
        role: message.role,
        content: message.content
      }))
    };
    
    fs.writeFileSync("claude_conversation.json", JSON.stringify(jsonData, null, 2));
    console.log("Conversation exported to claude_conversation.json");
  } catch (error) {
    console.error("Error parsing conversation:", error);
  }
}

main();
