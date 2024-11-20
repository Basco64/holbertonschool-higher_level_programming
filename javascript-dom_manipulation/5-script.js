const header = document.querySelector("header");
const btn = document.getElementById("update_header");

btn.addEventListener("click", () => (header.textContent = "New Header!!!"));
