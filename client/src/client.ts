import type {
    ChatMessageService,
    ChatMessage,
    SendMessageResult,
    ReceiveMessageResult,
    WebSocketEvent,
    sendMessage
} from "./declarations.d.ts";

class chatMessageService implements ChatMessageService {
    private webSocket: WebSocket;

    sendChatMessage(message: ChatMessage): SendMessageResult {
        this.webSocket.send(message.toString());
        return true;
    }

    receiveChatMessage(event: WebSocketEvent): ReceiveMessageResult {
        return this.receiveChatMessage(event.toString());
    }

    editChatMessage: sendMessage;
    deleteChatMessage: sendMessage;

    webSocketOpenHandler(event: Event) {
        console.log(event);
    }

    webSocketCloseHandler(event: Event) {
        console.log(event);
    }

    webSocketMessageHandler(event: Event) {
        return this.receiveChatMessage(event);
    }

    webSocketErrorHandler(event: Event) {
        console.log(event);
    }

    bindWebSocketEvents() {
        const eventMap = {
            open: this.webSocketOpenHandler,
            close: this.webSocketCloseHandler,
            message: this.webSocketMessageHandler,
            error: this.webSocketErrorHandler,
        };

        Object.keys(eventMap).forEach((event) => {
            this.webSocket.addEventListener(event, eventMap[event]);
        });
    }

    constructor(webSocket: WebSocket) {
        this.webSocket = webSocket;
        this.bindWebSocketEvents();
    }

    // deleteMessage: sendMessage;
    // editMessage: sendMessage;
};

export default chatMessageService;