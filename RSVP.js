let text = "Paste your text here"; // The text to be displayed
let words = text.split(" "); // Split the text into words
let i = 0; // Index for the current word
let readingSpeed = 300; // Reading speed in milliseconds
let fontSize = "20px"; // Font size
let fontColor = "black"; // Font color
let backgroundColor = "white"; // Background color

// Create a div to display the words
let div = document.createElement("div");
div.style.fontSize = fontSize;
div.style.color = fontColor;
div.style.backgroundColor = backgroundColor;
document.body.appendChild(div);s

// Function to display the next word
function displayNextWord() {
    if (i < words.length) {
        div.textContent = words[i];
        i++;
    } else {
        clearInterval(intervalId); // Stop when all words have been displayed
    }
}

// Start the RSVP
let intervalId = setInterval(displayNextWord, readingSpeed);
