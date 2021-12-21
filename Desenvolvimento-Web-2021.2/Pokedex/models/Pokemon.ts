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

    constructor(id: number, name: string, pvMax: number, ataque: number, defesa: number, ataqueEspecial: number, defesaEspecial: number, velocidade: number, imagem: string) {
        this.id = id;
        this.nome = name;
        this.pvMax = pvMax;
        this.ataque = ataque;
        this.defesa = defesa;
        this.ataqueEspecial = ataqueEspecial;
        this.defesaEspecial = defesaEspecial;
        this.velocidade = velocidade;
        this.imagem = imagem;
    }
}