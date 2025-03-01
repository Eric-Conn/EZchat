/*
    This file contains:
    - model definitions
    - service definitions
*/

// model definitions
// ===================

// stringable base class
export interface Base {
    toString: () => string;
}

// for chat and control message distinction (union)
export enum MessageType {
    CHAT = 'CHAT',
    CONTROL = 'CONTROL',
}

// generic message
export interface Message extends Base {
    id: string;
    value: string;
    type: MessageType;
}

// operation enum
export enum ChatOperation {
    DELETE_MESSAGE = 'DELETE_MESSAGE',
    EDIT_MESSAGE = 'EDIT_MESSAGE',
    HIDE_MESSAGE = 'HIDE_MESSAGE',
}

// control message (union with chat message)
export interface ChatControlMessage extends Message {
    operation: ChatOperation;
}

// chat message user
export interface User extends Base {
    id: string;
    name: string;
}

// chat message (union with control message)
export interface ChatMessage extends Message {
    from: User;
    to: User;
    timestamp: Date;
}

interface args {
    a: number;
    b: number;
    c: number;
}

// service definitions
// ===================

export type WebSocketEvent = string

// general message definitions
// ---------------------------
export type SendMessageResult = boolean;
export type sendMessage = (message: Message) => SendMessageResult;

export type ReceiveMessageResult = Message;
export type receiveMessage = (event: WebSocketEvent) => ReceiveMessageResult;

// chat message definitions
// ------------------------
export type sendChatMessage = (message: ChatMessage) => SendMessageResult;
export type receiveChatMessage = (event: WebSocketEvent) => ReceiveMessageResult;

export interface ChatMessageService {
    sendChatMessage: sendChatMessage;
    receiveChatMessage: receiveChatMessage;
    deleteChatMessage: sendMessage;
    editChatMessage: sendMessage;
}