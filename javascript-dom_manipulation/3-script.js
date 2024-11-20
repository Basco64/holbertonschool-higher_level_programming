const header = document.querySelector("header");
const btn = document.getElementById("toggle_header");

btn.addEventListener("click", () => {
  if (header.classList.contains("red")) {
    header.classList.remove("red");
    header.classList.add("green");
  } else {
    header.classList.remove("green");
    header.classList.add("red");
  }
});
