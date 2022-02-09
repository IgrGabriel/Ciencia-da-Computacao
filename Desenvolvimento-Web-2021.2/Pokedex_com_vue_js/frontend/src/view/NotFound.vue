<script setup lang="ts">
const props = defineProps<{
  msg: string;
}>();
</script>

<template>
  <div class="container">
    <div class="row align-justify-center">
      <h1>Ocorreu um erro</h1>
      <h2 v-if="msg != undefined" class="text-muted">
        {{ msg }}
      </h2>

      <router-link to="/pokemons" replace>
        <button type="button" class="btn btn-md btn-outline-primary">
          <i class="bx bx-left-arrow-alt"></i>
          Voltar
        </button>
      </router-link>
    </div>
  </div>
</template>
