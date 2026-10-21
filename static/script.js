const form = document.getElementById("spamForm");
const textarea = document.getElementById("message");
const checkBtn = document.getElementById("checkBtn");
const clearBtn = document.getElementById("clearBtn");

// Show "Checking..." and block empty submissions
form.addEventListener("submit", function (e) {
    if (textarea.value.trim() === "") {
        e.preventDefault();
        textarea.focus();
        return;
    }
    checkBtn.textContent = "Checking...";
});

// Clear the text box and hide the old result
clearBtn.addEventListener("click", function () {
    textarea.value = "";
    const result = document.querySelector(".result");
    if (result) result.remove();
    textarea.focus();
});
