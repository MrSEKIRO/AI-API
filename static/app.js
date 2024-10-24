// Listen for the form submission
document.getElementById('input-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the form from submitting the traditional way

    // Get the user's input from the form
    const userInput = document.getElementById('user-input').value;

    // Send a POST request to the /predict endpoint
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input_text: userInput }),  // Send the input text as JSON
    })
    .then(response => response.json())
    .then(data => {
        // Display the result in the result-text paragraph
        document.getElementById('result-text').textContent = data.result;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
