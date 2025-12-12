// Importa apenas o sistema de rotas do Express
const express = require("express");

// Cria um objeto de rotas
const router = express.Router();

/*
Essa rota é ativada quando o usuário digita no navegador:
http://localhost:3000/saudacao/NOME

O ":nome" significa que o valor será recebido dinamicamente
*/
router.get("/saudacao/:nome", (req, res) => {
  // Aqui estamos pegando o valor enviado na URL
  // Exemplo: /saudacao/Ana → nome = "Ana"
  const nome = req.params.nome;

  // Envia a resposta para o navegador
  res.send(`Olá, ${nome}!`);
});

// Exporta a rota para o server.js usar
module.exports = router;
