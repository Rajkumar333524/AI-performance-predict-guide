document.addEventListener("DOMContentLoaded", () => {

    const sendBtn = document.getElementById("sendBtn");
    const messageInput = document.getElementById("message");
    const chatBox = document.getElementById("chatBox");

    sendBtn.addEventListener("click", async () => {

        const message = messageInput.value.trim();

        if (!message) {
            alert("Enter message");
            return;
        }

        chatBox.innerHTML += `
            <div class="user-msg">
                <b>You:</b> ${message}
            </div>
        `;

        try {

            const response = await fetch("/chat-api", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    message: message
                })
            });

            const data = await response.json();

            chatBox.innerHTML += `
                <div class="bot-msg">
                    <b>AI:</b> ${data.response}
                </div>
            `;

            messageInput.value = "";

        } catch (error) {

            chatBox.innerHTML += `
                <div class="bot-msg">
                    <b>AI:</b> Error connecting server
                </div>
            `;
        }
    });

});