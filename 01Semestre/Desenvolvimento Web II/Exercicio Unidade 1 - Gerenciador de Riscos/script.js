function avaliarRiscoDeCredito(rendaMensal, dividaAtual) {
  let renda = parseFloat(rendaMensal);
  let divida = parseFloat(dividaAtual);

  let te = (divida / renda) * 100;

  let risco;
  if (te < 10) {
    risco = "Risco Baixo";
  } else if (te >= 10 && te < 30) {
    risco = "Risco Moderado";
  } else {
    risco = "Risco Alto";
  }

  return `Taxa de Endividamento: ${te.toFixed(2)}% - ${risco}`;
}

function exercicio1() {
  let rendaMensal = prompt("Digite sua renda mensal:");
  let dividaAtual = prompt("Digite sua dívida atual:");

  let resultado = avaliarRiscoDeCredito(rendaMensal, dividaAtual);

  console.log("===GERENCIADOR DE RISCO FINACEIRO===");
  console.log(resultado);

  let div = document.getElementById("resultado1");
  div.innerHTML = `<strong>Resultado:</strong><br>${resultado}`;
  div.style.display = "block";
}
