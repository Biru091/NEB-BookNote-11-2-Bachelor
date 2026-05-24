function toggleMenu() {
    const navLinks = document.getElementById('navLinks');
    navLinks.classList.toggle('active');
}
function showLoks() {
    document.querySelector(".bire").classList.add("blur-bg");
    document.getElementById("overlay").style.display = "block";
    document.querySelector(".loksewa_choice").style.display = "block";
}

function closeLoks() {
    document.querySelector(".bire").classList.remove("blur-bg");
    document.getElementById("overlay").style.display = "none";
    document.querySelector(".loksewa_choice").style.display = "none";
}
document.getElementById("openBot").onclick = () =>
    document.getElementById("botPopup").style.display = "block";

document.getElementById("closeBot").onclick = () =>
    document.getElementById("botPopup").style.display = "none";

function escapeHtml(text) {
    const map = { '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#039;' };
    return text.replace(/[&<>"']/g, m => map[m]);
}

document.getElementById("botForm").addEventListener("submit", function(e){
    e.preventDefault();

    const question = document.getElementById("question").value.trim();
    const resultBox = document.getElementById("resultBox");
    const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;

    if(!question){
        resultBox.innerHTML = "Please enter a question.";
        return;
    }

    resultBox.innerHTML = "Loading...";

    fetch("", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": csrf,
            "X-Requested-With": "XMLHttpRequest"
        },
        body: "title=" + encodeURIComponent(question)
    })
    .then(res => res.json())
    .then(data => {
        // Your Django view returns only {"reply": "..."}
        resultBox.innerHTML = `<p>${escapeHtml(data.reply)}</p>`;
    })
    .catch(err => {
        resultBox.innerHTML = "Fetch error: " + escapeHtml(err);
    });
});