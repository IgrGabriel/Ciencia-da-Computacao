import express from 'express';
import { listar_pokemons } from "../services/listar_pokemons";

export const router = express.Router();
const list_pokemons = new listar_pokemons();

router.get('/', (req, res) => {
    const pokemons = list_pokemons.getPokemons();
    res.status(200).json(pokemons);
});

router.post('/', (req, res) => {
    res.status(200).send('TODO');
});

router.get('/:id', (req, res) => {
    const id = Number(req.params.id);
    const pokemon = list_pokemons.getPokemonById(id);

    pokemon ? res.status(200).json(pokemon) : res.status(404).json({ msg: 'Pokemon não encontrado'});
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