
const message = document.getElementById("message");
const charCount = document.getElementById("char-count");
const clearButton = document.getElementById("clear-button");

function updateCount() {
    charCount.textContent = `${message.value.length} characters`;
}

message.addEventListener("input", updateCount);

clearButton.addEventListener("click", () => {
    message.value = "";
    updateCount();
    message.focus();
});

updateCount();
