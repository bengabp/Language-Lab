let messagesContainer = document.getElementById("messages");

function dismissAlert(){
    let firstChild = messagesContainer.querySelector(".message");
    if (firstChild){
        firstChild.style.transition = "0.5s";
        firstChild.style.opacity = "0";
        firstChild.addEventListener("transitionend",(event)=>{
            console.log("Ending animation");
            try {
                firstChild.remove();
            } catch (error) {}
        });
        // firstChild.remove()
    }
}

let is_connected = false;
const sendBtn = document.getElementById("send-btn");
sendBtn.addEventListener("click",sendMessageToClient);
const messageField = document.getElementById("message");

let url = `ws://${window.location.host}/chat/test`;
let chatSocket = new WebSocket(url);

function connectClient(username){
    url = `ws://${window.location.host}/chat/${username}`;
    chatSocket = new WebSocket(url);
}

function sendMessageToClient(e){
    if (is_connected){
        const messageText = messageField.value.trim();
        if (messageText.length > 0){
            chatSocket.send(JSON.stringify({
                type:"chat",
                message:messageText
            }));
        }
    }
}

// WEBSOCKET EVENT HANDLERS

// ON-MESSAGE EVENT HANDLER
chatSocket.onmessage = function(e){
    let data = JSON.parse(e.data);
    console.log("Data",data);
    let message_type = data.type;
    if (message_type === "message_received"){
        messageField.value = ""
    }
}

// ON-CONNECT HANDLER
chatSocket.onopen = function(e){
    is_connected = true;
    console.log("Connected");
}

// ON-DISCONNECT HANDLER
chatSocket.onclose = function(e){
    is_connected = false;
}



