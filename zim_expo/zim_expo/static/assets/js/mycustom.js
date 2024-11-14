
/* Destinations Js*/

document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll(".province-filters button");
    const destinations = document.querySelectorAll(".destination-item");

    buttons.forEach(button => {
        button.addEventListener("click", () => {
            const province = button.getAttribute("data-province");

            destinations.forEach(destination => {
                if (province === "all" || destination.getAttribute("data-province") === province) {
                    destination.style.display = "block";
                } else {
                    destination.style.display = "none";
                }
            });
        });
    });
});



            // JavaScript for handling the chatbot functionality
            document.getElementById("askButton").addEventListener("click", function() {
                const question = document.getElementById("questionInput").value.trim();
                const chatDisplay = document.getElementById("chatDisplay");
    
                if (question === "") {
                    alert("Please enter a question.");
                    return;
                }
    
                // Display user question
                chatDisplay.innerHTML += `<div class="chat-message user-message">You: ${question}</div>`;
    
                // Clear the input field
                document.getElementById("questionInput").value = "";
    
                // Fetch the response from OpenAI API
                fetch("https://api.openai.com/v1/completions", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                      /*  "Authorization": "Bearer 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"*/
                        },
                    body: JSON.stringify({
                    model: "text-ada-001",
                    prompt: question,
                    max_tokens: 150,
                    temperature: 0.7
                    })
                })
                .then(response => response.json())
                .then(data => {
                    // Show response from the chatbot
                    const botResponse = data.choices[0].text.trim();
                    chatDisplay.innerHTML += `<div class="chat-message bot-message">Chatbot: ${botResponse}</div>`;
                    
                    // Scroll to the bottom
                    chatDisplay.scrollTop = chatDisplay.scrollHeight;
                })
                .catch(error => {
                    console.error("Error:", error);  // Log more information about the error
                    if (error.response) {
                        // The request was made and the server responded with a status code
                        console.error("Response error:", error.response);
                    } else if (error.request) {
                        // The request was made but no response was received
                        console.error("Request error:", error.request);
                    } else {
                        // Something else went wrong
                        console.error("Error message:", error.message);
                    }

                    chatDisplay.innerHTML += `<div class="chat-message bot-message">Error: Unable to reach chatbot service. Please try again later.</div>`;
                });
            });


            // Chat functionality (For demonstration purposes, messages are shown in the browser console)
            function sendMessage() {
                var message = document.getElementById('chat-input').value;
                if (message.trim() !== "") {
                    var chatBox = document.getElementById('chat-box');
                    var newMessage = document.createElement('p');
                    newMessage.textContent = "You: " + message;
                    chatBox.appendChild(newMessage);
                    document.getElementById('chat-input').value = ""; // Clear input box
                    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
                }
            }

