const messageContainer = document.querySelector('.js-messageContainer');
const inputForm = document.querySelector('.js-inputForm');
const inputField = document.querySelector('.js-inputField');
const dots = document.querySelector('.js-dots');

// Event listener for form submission
inputForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const userMessage = inputField.value;

    if (!userMessage) return;

    // Clear the input field
    inputField.value = '';

    // Make a request to the GPT-3.5 Turbo API
    const response = await fetch('/chatbot', {
        method: 'POST',
        body: JSON.stringify({ user_input: userMessage }),
        headers: {
            'Content-Type': 'application/json'
        }
    });

    if (response.ok) {
        // Extract the chatbot's response from the API response
        const chatbotResponse = await response.text();

        // Add the user's message and chatbot's response to the chat interface
        addMessageToChat(userMessage, true);
        addMessageToChat(chatbotResponse);
    } else {
        console.error('Error fetching chatbot response.');
    }
});

// Function to add a message to the chat container
function addMessageToChat(message, isUserMessage = false) {
    const messageDiv = document.createElement('div');
    const messageClass = isUserMessage ? 'Chat-message--user' : 'Chat-message--bot';
    const messageBubble = `<span class="Chat-bubble">${message}</span>`;
    
    messageDiv.classList.add('Chat-message', messageClass);
    messageDiv.innerHTML += messageBubble;

    messageContainer.insertBefore(messageDiv, dots);
}
