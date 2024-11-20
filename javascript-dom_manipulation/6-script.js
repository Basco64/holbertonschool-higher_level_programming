const Url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
const char = document.getElementById("character");

fetch(Url)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    char.textContent = data.name;
  })
  .catch((error) => {
    console.error("Error fetching:", error);
    char.textContent = "Failed to fetch";
  });
