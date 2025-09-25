let questions = [];
let userAnswers = [];
let reviewMode = false;
let currentIndex = 0;

const qList = document.getElementById("question-list");
const qContainer = document.getElementById("question-container");
const resultBox = document.getElementById("result");

// Load questions from JSON
fetch("questions.json")
  .then(res => res.json())
  .then(data => {
    questions = data;
    userAnswers = new Array(questions.length).fill(null);
    renderSidebar();
    loadQuestion(0);
  });

// Create sidebar links
function renderSidebar() {
  qList.innerHTML = "";
  questions.forEach((q, i) => {
    const div = document.createElement("div");
    div.className = "question-link";
    div.textContent = `Question ${i + 1}`;
    div.onclick = () => loadQuestion(i);
    qList.appendChild(div);
  });
}

// Load question to main area
function loadQuestion(index) {
  currentIndex = index;
  const q = questions[index];
  qContainer.innerHTML = `
    <div class="question">
      <h3>${q.text}</h3>
      <div class="answers">
        ${q.options.map((opt, i) => `
          <label>
            <input type="radio" name="q${index}" value="${i}" 
              ${userAnswers[index] === i ? "checked" : ""}
              ${reviewMode ? "disabled" : ""}
            >
            ${opt}
          </label>
        `).join("")}
      </div>
    </div>
    <div class="navigation">
      <button onclick="prevQuestion()" ${index === 0 ? "disabled" : ""}>Previous</button>
      <button onclick="nextQuestion()" ${index === questions.length - 1 ? "disabled" : ""}>Next</button>
    </div>
  `;

  // Answer selection listener
  if (!reviewMode) {
    qContainer.querySelectorAll("input").forEach(input => {
      input.addEventListener("change", (e) => {
        userAnswers[index] = parseInt(e.target.value);
        markDone(index);
      });
    });
  } else {
    highlightReview(index);
  }
}

// Navigation buttons
function nextQuestion() {
  if (currentIndex < questions.length - 1) {
    loadQuestion(currentIndex + 1);
  }
}

function prevQuestion() {
  if (currentIndex > 0) {
    loadQuestion(currentIndex - 1);
  }
}

// Mark sidebar question as done
function markDone(index) {
  const links = document.querySelectorAll(".question-link");
  if (userAnswers[index] !== null) {
    links[index].classList.add("done");
  }
}

// Submit quiz
function submitQuiz() {
  let score = 0;
  questions.forEach((q, i) => {
    if (userAnswers[i] === q.answer) {
      score++;
    }
  });
  alert(`You got ${score}/${questions.length} correct!`);
  resultBox.innerHTML = `<h3>Your Score: ${score}/${questions.length}</h3><p>You can now review your answers.</p>`;
  reviewMode = true;
  loadQuestion(0);
}

// Highlight correct/wrong answers in review
function highlightReview(index) {
  const q = questions[index];
  const labels = qContainer.querySelectorAll("label");
  labels.forEach((label, i) => {
    if (i === q.answer) {
      label.classList.add("correct");
    }
    if (userAnswers[index] === i && userAnswers[index] !== q.answer) {
      label.classList.add("wrong");
    }
  });
}
