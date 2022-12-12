let messagesContainer = document.getElementById("messages");

function dismissAlert(){
    let firstChild = messagesContainer.querySelector(".message");
    if (firstChild){
        firstChild.style.transition = "0.5s";
        firstChild.style.opacity = "0";
        firstChild.addEventListener("transitionend",(event)=>{
            console.log("Ending animation")
            try {
                firstChild.remove()
            } catch (error) {}
        })
        
        // firstChild.remove()
    }
}