export enum Role {
  USER = 'user',
  ASSISTANT = 'assistant'
}

export interface Message {
  role: Role;
  content: string;
  rawHtml?: string;
}

export interface Conversation {
  messages: Message[];
  url: string;
  title?: string;
}
