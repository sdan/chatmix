/**
 * Example script demonstrating the ChatGPT parser functionality.
 */

import { ChatGPTParser } from '../src/parsers/chatgpt';

async function main() {
  // Parse from a URL
  const url = process.argv[2] || "https://chatgpt.com/share/67db5526-1ddc-8013-9824-145459e33171";
  
  console.log(process.argv.length <= 2 ? `No URL provided, using example: ${url}` : `Parsing conversation from: ${url}`);
  
  // Initialize the parser
  const parser = new ChatGPTParser();
  
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
    
    fs.writeFileSync("chatgpt_conversation.json", JSON.stringify(jsonData, null, 2));
    console.log("Conversation exported to chatgpt_conversation.json");
  } catch (error) {
    console.error("Error parsing conversation:", error);
  }
}

main();
