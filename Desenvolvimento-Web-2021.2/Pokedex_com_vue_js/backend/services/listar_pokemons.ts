import { Pokemon } from '../models/Pokemon';
import * as fs from 'fs';
import * as path from 'path';

const dbPath = path.join(__dirname, '../../db/pokedex-light.json');

interface PokemonSummary {
    id: number;
    nome: string;
    pvMax: number;
    ataque: number;
    defesa: number;
    ataqueEspecial: number;
    defesaEspecial: number;
    velocidade: number;
    tipo: string[];
    imagem: string;
    peso: number;
    altura: number;

    sumary: string;
}

export class listar_pokemons {
    private _pokemons: Pokemon[] = [];

    loadPokemons(){
        const fileContent = fs.readFileSync(dbPath, 'utf8');
        const obj = JSON.parse(fileContent);
    
        for(let i in obj.pokemons) {
            const id = obj.pokemons[i].id;
            const nome = obj.pokemons[i].name;
            const pvMax = obj.pokemons[i].stats[0].base_stat;
            const ataque = obj.pokemons[i].stats[1].base_stat;
            const defesa = obj.pokemons[i].stats[2].base_stat;
            const ataqueEspecial = obj.pokemons[i].stats[3].base_stat;
            const defesaEspecial = obj.pokemons[i].stats[4].base_stat;
            const velocidade = obj.pokemons[i].stats[5].base_stat;
            const imagem = obj.pokemons[i].sprites.front_default;
    
            const peso = obj.pokemons[i].weight;
            const altura = obj.pokemons[i].height;
    
            const tipo = [];
    
            for(let j in obj.pokemons[i].types) {
                tipo.push(obj.pokemons[i].types[j].type.name);
            }
    
            this._pokemons.push(new Pokemon(id, nome, pvMax, ataque, defesa, ataqueEspecial, defesaEspecial, velocidade, imagem, peso, altura, tipo));
        }
    }

    getPokemons(): PokemonSummary[] {
        const result: PokemonSummary[] = [];

        if(this._pokemons.length == 0) {
            this.loadPokemons();
        }

        for (let pokemon of this._pokemons) {
            const { id, nome, pvMax, ataque, defesa, ataqueEspecial, defesaEspecial, velocidade, imagem, peso, altura, tipo } = pokemon;
        
            result.push({
                id: id,
                nome: nome,
                pvMax: pvMax,
                ataque: ataque,
                defesa: defesa,
                ataqueEspecial: ataqueEspecial,
                defesaEspecial: defesaEspecial,
                velocidade: velocidade,
                imagem: imagem,
                peso: peso,
                altura: altura,
                tipo: tipo,
                sumary: "",
            })
        }

        return result;
    }

    getPokemonById(id: number): Pokemon | undefined {
        if(this._pokemons.length == 0){
            this.loadPokemons();
        }
        return this._pokemons.find(pokemon => pokemon.id === id);
    }

    delete(id: number) {
        return this._pokemons.splice(id, 1).length === 1;
    }
}