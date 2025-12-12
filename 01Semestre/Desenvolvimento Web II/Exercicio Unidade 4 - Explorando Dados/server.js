// Importa o Express (framework para criar servidor)
const express = require("express");

// Cria a aplicação Express
// A partir daqui o "app" passa a existir
const app = express();

// Rota inicial (apenas para teste)
// Essa função responde quando alguém acessa http://localhost:3000/
app.get("/", (req, res) => {
  res.send("Servidor Express está funcionando!");
});

// Importa as rotas criadas em arquivos separados
const rotaSaudacao = require("./routes/saudacao");
const rotaSoma = require("./routes/soma");

// Usa as rotas
// Quando alguém acessar /saudacao ou /soma,
// o Express vai encaminhar para esses arquivos
app.use(rotaSaudacao);
app.use(rotaSoma);

// Define a porta do servidor
const PORT = 3000;

// Inicia o servidor
app.listen(PORT, () => {
  console.log("Servidor rodando em http://localhost:3000");
});
