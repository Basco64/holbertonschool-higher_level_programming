const Url = "https://swapi-api.hbtn.io/api/films/?format=json";
const list = document.getElementById("list_movies");

fetch(Url)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    for (let i = 0; i < data.count; i++) {
      const newElement = document.createElement("li");
      newElement.textContent = data.results[i].title;
      list.append(newElement);
    }
  })
  .catch((error) => {
    console.error("Error fetching:", error);
  });
