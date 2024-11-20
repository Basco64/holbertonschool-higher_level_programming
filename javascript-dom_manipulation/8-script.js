document.addEventListener("DOMContentLoaded", function () {
  const Url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
  const div = document.getElementById("hello");

  fetch(Url)
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      div.textContent = data.hello;
    })
    .catch((error) => {
      console.error("Error fetching:", error);
    });
});
