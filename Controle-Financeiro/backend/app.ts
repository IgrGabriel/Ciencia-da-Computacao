import express from "express";
import morgan from "morgan";
import cors from 'cors';
import {router as financaRouter } from "././routes/financas";

const PORT = 8080;
const app = express();

app.use(morgan("tiny"));
app.use(express.static("./public"));

app.use(
  cors({
    origin: "http://localhost:3000",
  })
);

app.use("/financas", financaRouter);

app.get("/", (req, res) => {
  res.redirect("/financas");
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
