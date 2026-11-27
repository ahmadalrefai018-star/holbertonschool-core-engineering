const form = document.querySelector("#chat");
const input = document.querySelector("#message");
const sendButton = document.querySelector("#send");
const status = document.querySelector("#status");
const messages = document.querySelector("#messages");

const endpoint = new URL("/ws", window.location.href);
endpoint.protocol = window.location.protocol === "https:" ? "wss:" : "ws:";
const socket = new WebSocket(endpoint);

socket.addEventListener("open", () => {
    status.textContent = "Connected";
    sendButton.disabled = false;
});

socket.addEventListener("message", (event) => {
    const message = document.createElement("li");
    message.textContent = event.data;
    messages.append(message);
    messages.scrollTop = messages.scrollHeight;
});

socket.addEventListener("close", () => {
    status.textContent = "Disconnected";
    sendButton.disabled = true;
});

form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (socket.readyState !== WebSocket.OPEN) {
        return;
    }

    socket.send(input.value);
    input.value = "";
    input.focus();
});
