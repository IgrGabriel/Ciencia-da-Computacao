import express from 'express';
import { listar_pokemons } from "../services/listar_pokemons";

export const router = express.Router();
const list_pokemons = new listar_pokemons();

router.get('/', (req, res) => {
    const pokemons = list_pokemons.getPokemons();
    res.render('index', { 
        pageTitle: 'Pokedex',
        pokemons: pokemons 
    });
});

router.get('/:id', (req, res) => {
    const id = parseInt(req.params.id) - 1;
    const pokemons = list_pokemons.getPokemons();

    res.render('detalhesPokemon', { 
        pageTitle: 'Pokedex',
        pokemons: pokemons,
        nome: pokemons[id].nome,
        tipo: pokemons[id].tipo,
        tipo2: pokemons[id].tipo2,
        imagem: pokemons[id].imagem,
        peso: pokemons[id].peso,
        altura: pokemons[id].altura,
        pvMax: pokemons[id].pvMax,
        ataque: pokemons[id].ataque,
        defesa: pokemons[id].defesa,
        ataqueEspecial: pokemons[id].ataqueEspecial,
        defesaEspecial: pokemons[id].defesaEspecial,
        velocidade: pokemons[id].velocidade,
        idP: id
    });
});

router.post('/', (req, res) => {
    res.status(200).send('TODO');
});

router.get('/:id', (req, res) => {
    const id = req.params.id;
    res.status(200).send(`TODO ${id}`);
});

router.put('/:id', (req, res) => {
    const id = req.params.id;
    res.status(200).send(`TODO ${id}`);
});

router.delete('/:id', (req, res) => {
    const id = req.params.id;
    if(list_pokemons.delete(Number(id))){
        res.status(200).send(`Pokemon ${id} removido`);
    }else {
        res.status(404).send(`Pokemon ${id} não encontrado`);
    }
    res.status(200).send(`TODO ${id}`);
});