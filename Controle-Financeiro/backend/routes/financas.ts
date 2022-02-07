import express from "express";
import { listar_financas } from "../services/listar_financas";


export const router = express.Router();
const list_financas = new listar_financas();

router.get("/", (req, res) => {
  const financas = list_financas.getFinancas();
  res.status(200).json(financas);
});

router.post('/', (req, res) => {
  res.status(200).json({message: 'Transacao cadastrada com sucesso'});
});
