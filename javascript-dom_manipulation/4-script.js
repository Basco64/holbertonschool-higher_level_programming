const myList = document.querySelector(".my_list");
const btn = document.getElementById("add_item");

btn.addEventListener("click", () => {
  const newElement = document.createElement("li");
  newElement.textContent = "Item";

  myList.append(newElement);
});
