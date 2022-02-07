
export class Financas {
  readonly id: number;
  readonly data: string;
  readonly categoria: string;
  readonly valor: number;
  readonly descricao: string;
  readonly tipo: string;

  constructor(id: number, data: string, categoria: string, valor: number, descricao: string, tipo: string) {
    this.id = id;
    this.data = data;
    this.categoria = categoria;
    this.valor = valor;
    this.descricao = descricao;
    this.tipo = tipo;
  }
}