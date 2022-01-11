import { Pokemon } from '../models/Pokemon';
import * as fs from 'fs';
import * as path from 'path';

const dbPath = path.join(__dirname, '../../db/pokedex-light.json');

export class listar_pokemons {
    private _pokemons: Pokemon[] = [];

    getPokemons(): Pokemon[] {
        if(this._pokemons.length == 0) {
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
                const img = obj.pokemons[i].sprites.front_default;

                const peso = obj.pokemons[i].weight;
                const altura = obj.pokemons[i].height;
                const tipo = obj.pokemons[i].types[0].type.name;

                if(obj.pokemons[i].types.length > 1) {
                    const tipo2 = obj.pokemons[i].types[1].type.name;
                    this._pokemons.push(new Pokemon(id, nome, pvMax, ataque, defesa, ataqueEspecial, defesaEspecial, velocidade, img, peso, altura, tipo, tipo2));
                } else {
                    this._pokemons.push(new Pokemon(id, nome, pvMax, ataque, defesa, ataqueEspecial, defesaEspecial, velocidade, img, peso, altura, tipo, ''));
                }   
            }
        }
        return this._pokemons;
    }

    delete(id: number) {
        return this._pokemons.splice(id, 1).length === 1;
    }
}