export class Pokemon {
    readonly id: number;
    readonly nome: string;
    readonly pvMax: number;
    readonly ataque: number;
    readonly defesa: number;
    readonly ataqueEspecial: number;
    readonly defesaEspecial: number;
    readonly velocidade: number;
    readonly imagem: string;
    readonly peso: number;
    readonly altura: number;
    readonly tipo: string[];

    constructor(id: number, name: string, pvMax: number, ataque: number, defesa: number, ataqueEspecial: number, defesaEspecial: number, velocidade: number, imagem: string, peso: number, altura: number, tipo: string[]) {
        this.id = id;
        this.nome = name;
        this.pvMax = pvMax;
        this.ataque = ataque;
        this.defesa = defesa;
        this.ataqueEspecial = ataqueEspecial;
        this.defesaEspecial = defesaEspecial;
        this.velocidade = velocidade;
        this.imagem = imagem;
        this.peso = peso;
        this.altura = altura;
        this.tipo = tipo;
    }
}