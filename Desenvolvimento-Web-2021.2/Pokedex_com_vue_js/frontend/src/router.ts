import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    { 
        path: '/', 
        component: import('./view/PokemonList.vue'),
        alias: '/pokemons'
    },
    {
        path: '/pokemons/:id',
        component: () => import('./view/PokemonDetail.vue'),
        props: true
    },
    {
        path: '/404',
        component: import('./view/NotFound.vue'),
        name: 'NotFound',
        props: true
    }
]

export const router = createRouter({
    history: createWebHistory(),
    routes
})