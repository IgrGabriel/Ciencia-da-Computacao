import { Financas } from "../models/Financas";
import * as fs from "fs";
import * as path from "path";

const dbPath = path.join(__dirname, "../../db/financas.json");

interface FinancasInterface {
  id: number;
  data: string;
  categoria: string;
  valor: number;
  descricao: string;
  tipo: string;
}

export class listar_financas {
  private _financas: Financas[] = [];

  loadFinancas() {
    if (this._financas.length == 0) {
      const fileContent = fs.readFileSync(dbPath, "utf8");
      const obj = JSON.parse(fileContent);

      for (let i in obj.financas) {
        const id = obj.financas[i].id;
        const data = obj.financas[i].data;
        const categoria = obj.financas[i].categoria;
        const valor = obj.financas[i].valor;
        const descricao = obj.financas[i].descricao;
        const tipo = obj.financas[i].tipo;

        this._financas.push(
          new Financas(id, data, categoria, valor, descricao, tipo)
        );
      }
    }
  }

  getFinancas(): Financas[] {
    const result: FinancasInterface[] = [];

    if(this._financas.length == 0) {  
      this.loadFinancas();
    }

    for(let financa of this._financas) {
      const {id, data, categoria, valor, descricao, tipo} = financa;
      
      result.push({
        id: id,
        data: data,
        categoria: categoria,
        valor: valor,
        descricao: descricao,
        tipo: tipo
      });
    }

    return result;
  }
};
