
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("classifier-form");
    const textarea = document.getElementById("message");
    const charCount = document.getElementById("char-count");

    const sampleButton = document.getElementById("sample-button");
    const pasteButton = document.getElementById("paste-button");
    const clearButton = document.getElementById("clear-button");

    const analyzeButton = document.getElementById("analyze-button");
    const buttonContent = document.getElementById("button-content");
    const loadingContent = document.getElementById("loading-content");

    const sampleEmail = `Congratulations! You have been selected
to receive a FREE $1,000 gift card!

You are our lucky winner. Claim your exclusive
reward immediately by clicking the link below.

Limited time offer! Act now before your prize
expires. Click here to claim your reward today!`;

    function updateCharacterCount() {
        charCount.textContent = textarea.value.length;
    }

    textarea.addEventListener("input", updateCharacterCount);

    sampleButton.addEventListener("click", () => {
        textarea.value = sampleEmail;
        updateCharacterCount();
        textarea.focus();
    });

    clearButton.addEventListener("click", () => {
        textarea.value = "";
        updateCharacterCount();
        textarea.focus();
    });

    pasteButton.addEventListener("click", async () => {
        try {
            if (!navigator.clipboard?.readText) {
                throw new Error("Clipboard access is unavailable.");
            }

            const text = await navigator.clipboard.readText();

            if (!text) {
                alert("Your clipboard is empty.");
                return;
            }

            textarea.value = text.slice(0, 20000);
            updateCharacterCount();
            textarea.focus();
        } catch (error) {
            alert(
                "Clipboard access was blocked. Please paste your " +
                "email directly into the text area using Ctrl + V."
            );
        }
    });

    form.addEventListener("submit", () => {
        if (!textarea.value.trim()) {
            return;
        }

        analyzeButton.disabled = true;
        buttonContent.hidden = true;
        loadingContent.hidden = false;
    });

    updateCharacterCount();
});
