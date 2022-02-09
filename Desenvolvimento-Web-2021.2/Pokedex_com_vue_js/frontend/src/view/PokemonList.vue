<script setup lang="ts">
import { computed } from "@vue/runtime-core";
import { useStore } from "vuex";
import Navbar from "../components/Navbar.vue";
import PokemonCard from "../components/PokemonCard.vue";

const store = useStore();
const pokemons = computed(() => store.state.pokemons);
</script>

<template>
  <div>
    <Navbar />
    <div class="container">
      <div class="row">
        <PokemonCard
          v-for="pokemon in pokemons"
          :key="pokemon.id"
          :id="pokemon.id"
          :nome="pokemon.nome"
          :imagem="pokemon.imagem"
          :tipos="pokemon.tipo"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.container {
  margin-top: 25px;
}
</style>
