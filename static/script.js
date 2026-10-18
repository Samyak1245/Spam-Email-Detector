// ---------- Elements ----------
const message = document.getElementById("message");
const charCount = document.getElementById("char-count");
const clearButton = document.getElementById("clear-button");
const form = document.getElementById("classifier-form");
const submitButton = document.querySelector(".submit-button");

// ---------- Character counter ----------
function updateCount() {
    charCount.textContent = `${message.value.length} characters`;
}

message.addEventListener("input", updateCount);

clearButton.addEventListener("click", () => {
    message.value = "";
    updateCount();
    message.focus();
});

// ---------- Sample emails ----------
const samples = {
    spam: [
        "CONGRATULATIONS! You've won a $1,000 Walmart gift card. Click here now to claim your prize before it expires!",
        "URGENT: Your bank account has been suspended. Verify your password immediately at http://secure-bank-login.xyz",
        "Make $5000 per week working from home! No experience needed. Reply YES to get started today!!!",
        "You have been selected for a FREE iPhone 15. Just pay $1 shipping. Limited offer, act now!"
    ],
    ham: [
        "Hi Rahul, just a reminder that our project meeting is tomorrow at 10 AM. Please bring your report.",
        "Hey, are we still on for lunch on Saturday? Let me know what time works for you.",
        "Dear students, the assignment deadline has been extended to Friday. Please submit it on the portal.",
        "Thanks for your help yesterday! I've attached the notes from the lecture. Let me know if anything is unclear."
    ]
};

let lastSample = "";

function loadSample(type) {
    if (type === "random") {
        type = Math.random() < 0.5 ? "spam" : "ham";
    }

    const list = samples[type];
    let text;

    // Avoid showing the same sample twice in a row
    do {
        text = list[Math.floor(Math.random() * list.length)];
    } while (text === lastSample && list.length > 1);

    lastSample = text;
    message.value = text;
    updateCount();
    message.focus();
}

document.querySelectorAll(".sample-button").forEach(btn => {
    btn.addEventListener("click", () => loadSample(btn.dataset.type));
});

// ---------- Loading state on submit ----------
form.addEventListener("submit", () => {
    submitButton.disabled = true;
    submitButton.textContent = "Classifying...";
});

// ---------- Scroll to result after page reload ----------
const result = document.querySelector(".result");
if (result) {
    result.scrollIntoView({ behavior: "smooth", block: "nearest" });
}

// ---------- Initial setup ----------
updateCount();
