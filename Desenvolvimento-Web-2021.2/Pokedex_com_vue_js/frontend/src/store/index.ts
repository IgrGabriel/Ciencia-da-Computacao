import { createStore } from 'vuex'
import Axios from 'axios'

const state = {
    pokemons: [],
    pokemon: null,
}

const mutations = {
    setPokemons(state, pokemons) {
        state.pokemons = pokemons
    },
    setPokemon(state, pokemon) {
        state.pokemon = pokemon
    }
}

const actions = {
    async getPokemons({ commit }) {
        try {
            const response = await axios.get('/pokemons')
            commit('setPokemons', response.data)
        } catch (err) {
            console.log(err)
        }
    },
    async getPokemon({ commit }, id) {
        try {
            const response = await axios.get(`/pokemons/${id}`)
            commit('setPokemon', response.data)
        } catch (err) {
            console.log(err)
        }
    }
}

const getters = {
    numberOfPokemons(state){
        return state.pokemons.length
    }
}

export const store = createStore({
    state: state,
    mutations: mutations,
    actions: actions,
    getters: getters
})

export const axios = Axios.create({
    baseURL: 'http://localhost:8082/',
    timeout: 1000,
    headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
    }
}) 