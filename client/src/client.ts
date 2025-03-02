export default class WebSocketClient {
    private webSocket: WebSocket;
    private url: string;

    openHandler: (event: Event) => any;
    messageHandler: (event: Event) => any;
    closeHandler: (event: Event) => any;
    errorHandler: (event: Event) => any;

    constructor(url: string) {
        this.webSocket = null;
        this.url = url;

        this.openHandler = this.defaultHandler;
        this.messageHandler = this.defaultHandler;
        this.closeHandler = this.defaultHandler;
        this.errorHandler = this.defaultHandler;
    }

    defaultHandler(event: Event) {
        console.log(event);
    }

    onConnect(handler: (event: Event) => any) {
        this.openHandler = handler;
    }
    onDisconnect(handler: (event: Event) => any) {
        this.closeHandler = handler;
    }
    onMessageReceived(handler: (event: Event) => any) {
        this.messageHandler = handler;
    }
    onError(handler: (event: Event) => any) {
        this.errorHandler = handler;
    }

    sendMessage(message: string) {
        if (!this.webSocket || this.webSocket.readyState !== WebSocket.OPEN) {
            throw new Error('WebSocket is not connected. Call connect() first.');
        }
        this.webSocket.send(message);
    }

    async connect() {
        this.webSocket = new WebSocket(this.url);

        // return promise that resolves when the connection is established
        const connectPromise = new Promise((resolve, reject) => {
            this.webSocket.onopen = (event: Event) => {
                this.openHandler(event);
                resolve(event);
            };
            this.webSocket.onerror = (event: Event) => {
                this.errorHandler(event);
                reject(event);
            };
            this.webSocket.onclose = (event: Event) => {
                this.closeHandler(event);
                reject(event);
            }
            this.webSocket.onmessage = (event: Event) => {
                this.messageHandler(event);
            }
        });

        return connectPromise;
    }
}