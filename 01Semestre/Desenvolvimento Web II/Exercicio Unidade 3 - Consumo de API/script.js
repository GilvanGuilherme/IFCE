async function carregarImagens() {
  const resposta = await fetch("https://picsum.photos/v2/list?limit=50");
  const dados = await resposta.json();
  return dados;
}

async function main() {
  const imagens = await carregarImagens();
  const galeria = document.getElementById("gallery");

  imagens.forEach((imagem) => {
    const img = document.createElement("img");
    img.src = imagem.download_url;
    galeria.appendChild(img);
  });
}

main();
