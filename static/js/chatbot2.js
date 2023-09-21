const messageContainer = document.querySelector('.js-messageContainer')
const inputForm = document.querySelector('.js-inputForm')
const inputField = document.querySelector('.js-inputField')
const dots = document.querySelector('.js-dots')

// clear chat window with clear

inputForm.addEventListener('submit', (e) => {
    e.preventDefault()
    
    const userMessage = inputField.value    
    const messageDiv = document.createElement('div')
    const messageBubble = `<span class="Chat-bubble">${userMessage}</span>`

    if (!userMessage) return
    
    messageDiv.classList.add('Chat-message', 'Chat-message--user')
    messageDiv.innerHTML += messageBubble

    messageContainer.insertBefore(messageDiv, dots)
    messageContainer.classList.add('Chat-messages--typing')

    e.preventDefault()
    inputForm.reset()
})