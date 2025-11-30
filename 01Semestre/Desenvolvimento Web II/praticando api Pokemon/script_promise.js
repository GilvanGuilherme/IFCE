document.addEventListener("DOMContentLoaded", function () {
  let gallery = document.getElementById("gallery");

  const limit = 30;

  fetch(`https://pokeapi.co/api/v2/pokemon?limit=${limit}`)
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      data.results.forEach(function (pokemon) {
        fetch(pokemon.url)
          .then(function (response) {
            return response.json();
          })
          .then(function (details) {
            let div = document.createElement("div");
            div.style.display = "flex";
            div.style.flexDirection = "column";
            div.style.alignItems = "center";
            div.style.margin = "10px";

            let img = document.createElement("img");
            img.src = details.sprites.other["official-artwork"].front_default;
            img.alt = pokemon.name;

            let name = document.createElement("p");
            name.textContent = pokemon.name.toUpperCase();

            div.appendChild(img);
            div.appendChild(name);

            gallery.appendChild(div);
          });
      });
    })
    .catch(function (error) {
      console.error("Erro ao carregar Pokémons:", error);
    });
});
