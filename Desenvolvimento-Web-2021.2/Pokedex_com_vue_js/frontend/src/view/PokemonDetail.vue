<script setup lang="ts">
import { computed } from "@vue/runtime-core";
import { useStore } from "vuex";
import { useRoute, onBeforeRouteUpdate } from "vue-router";

const props = defineProps<{
  id: string;
}>();

const store = useStore();
const route = useRoute();

store.dispatch("getPokemon", route.params.id);

onBeforeRouteUpdate((to, from) => {
  if (to.params.id !== from.params.id) {
    store.dispatch("getPokemon", to.params.id);
  }
});

const pokemon = computed(() => store.state.pokemon);

const numberOfPokemons = computed(() => store.getters.numberOfPokemons);
</script>

<template>
  <div class="container" v-if="pokemon">
    <div class="row align-items-center">
      <div class="col-md-2">
        <router-link :to="`/pokemons/${Math.max(1, Number(id) - 1)}`">
          <button
            type="button"
            class="btn btn-md btn-outline-primary"
            :class="{ disabled: Number(id) === 1 }"
          >
            <i class="bx bx-left-arrow-alt"></i>
          </button>
        </router-link>
      </div>
      <div class="col">
        <div class="card">
          <div class="col-sm-4 col-md-3 col-lg-3">
            <img
              :src="pokemon.imagem"
              class="card-img-top"
              :alt="pokemon.nome"
            />
          </div>
          <div class="col-sm-8 col-md-8 col-lg-8">
            <div class="card-body">
              <div class="row">
                <div class="col-auto">
                  <h5 class="card-title">{{ pokemon.nome }}</h5>
                </div>
                <div class="col-4">
                  <span
                    class="badge bg-secondary"
                    v-for="(tipo, i) in pokemon.tipo"
                    :key="i"
                  >
                    {{ tipo }}
                  </span>
                </div>
              </div>

              <h6 class="card-subtitle text-muted fw-bold">
                Peso {{ pokemon.peso }} Ibs
              </h6>
              <h6 class="card-text text-muted fw-bold">
                Altura {{ pokemon.altura }}"
              </h6>
              <h6 class="card-text text-muted fw-bold">Base stats</h6>

              <hr />

              <div class="row">
                <div class="col-sm-6 col-md-4 col-lg-3">
                  <h6 class="card-text text-muted fw-bold">PvMax:</h6>
                </div>
                <div class="col-sm-6 col-md-8 col-lg-9">
                  <div class="progress">
                    <div
                      class="progress-bar text-start"
                      role="progressbar"
                      :style="{ width: `${pokemon.pvMax}%` }"
                      :aria-valuenow="pokemon.pvMax"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    >
                      {{ pokemon.pvMax }}
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-sm-6 col-md-4 col-lg-3">
                  <h6 class="card-text text-muted fw-bold">Ataque:</h6>
                </div>
                <div class="col-sm-6 col-md-8 col-lg-9">
                  <div class="progress">
                    <div
                      class="progress-bar text-start"
                      role="progressbar"
                      :style="{ width: `${pokemon.ataque}%` }"
                      :aria-valuenow="pokemon.ataque"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    >
                      {{ pokemon.ataque }}
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-sm-6 col-md-4 col-lg-3">
                  <h6 class="card-text text-muted fw-bold">Defesa:</h6>
                </div>
                <div class="col-sm-6 col-md-8 col-lg-9">
                  <div class="progress">
                    <div
                      class="progress-bar text-start"
                      role="progressbar"
                      :style="{ width: `${pokemon.defesa}%` }"
                      :aria-valuenow="pokemon.defesa"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    >
                      {{ pokemon.defesa }}
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-sm-6 col-md-4 col-lg-3">
                  <h6 class="card-text text-muted fw-bold">Ataque Esp.:</h6>
                </div>
                <div class="col-sm-6 col-md-8 col-lg-9">
                  <div class="progress">
                    <div
                      class="progress-bar text-start"
                      role="progressbar"
                      :style="{ width: `${pokemon.ataqueEspecial}%` }"
                      :aria-valuenow="pokemon.ataqueEspecial"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    >
                      {{ pokemon.ataqueEspecial }}
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-sm-6 col-md-4 col-lg-3">
                  <h6 class="card-text text-muted fw-bold">Defesa Esp.:</h6>
                </div>
                <div class="col-sm-6 col-md-8 col-lg-9">
                  <div class="progress">
                    <div
                      class="progress-bar text-start"
                      role="progressbar"
                      :style="{ width: `${pokemon.defesaEspecial}%` }"
                      :aria-valuenow="pokemon.defesaEspecial"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    >
                      {{ pokemon.defesaEspecial }}
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-sm-6 col-md-4 col-lg-3">
                  <h6 class="card-text text-muted fw-bold">Velocidade:</h6>
                </div>
                <div class="col-sm-6 col-md-8 col-lg-9">
                  <div class="progress">
                    <div
                      class="progress-bar text-start"
                      role="progressbar"
                      :style="{ width: `${pokemon.velocidade}%` }"
                      :aria-valuenow="pokemon.velocidade"
                      aria-valuemin="0"
                      aria-valuemax="100"
                    >
                      {{ pokemon.velocidade }}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-2">
        <router-link
          :to="`/pokemons/${Math.min(Number(id) + 1, numberOfPokemons)}`"
        >
          <button
            type="button"
            class="btn btn-md btn-outline-primary"
            :class="{ disabled: Number(id) === numberOfPokemons }"
          >
            <i class="bx bx-right-arrow-alt"></i>
          </button>
        </router-link>
      </div>
    </div>

    <div class="centralizar">
      <router-link to="/pokemons">
        <button
          type="button"
          class="btn btn-lg btn-outline-primary"
          :class="{ disabled: Number(id) === numberOfPokemons }"
        >
          <i class="bx bx-home"></i>
          Página principal
        </button>
      </router-link>
    </div>
  </div>
</template>

<style>
/* centralizar a div */
.centralizar {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px auto;
}
</style>
