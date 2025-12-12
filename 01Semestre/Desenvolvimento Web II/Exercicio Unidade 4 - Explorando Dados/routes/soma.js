const express = require("express");
const router = express.Router();

/*
Essa rota é ativada quando o usuário acessa:
http://localhost:3000/soma?a=5&b=3
*/
router.get("/soma", (req, res) => {
  // Pegamos os valores enviados pela query string
  const a = Number(req.query.a);
  const b = Number(req.query.b);

  // Calcula a soma
  const soma = a + b;

  // Retorna a resposta em JSON
  res.json({
    valorA: a,
    valorB: b,
    resultado: soma,
  });
});

module.exports = router;
