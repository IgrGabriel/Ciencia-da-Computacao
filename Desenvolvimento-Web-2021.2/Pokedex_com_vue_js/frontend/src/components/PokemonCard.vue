<script setup lang="ts">
const props = defineProps<{
  id: number;
  nome: string;
  imagem: string;
  tipos: String[];
}>();
</script>

<template>
  <div class="col-sm-6 col-md-4 col-lg-3">
    <router-link
      class="text-decoration-none text-reset"
      :to="`/pokemons/${id}`"
    >
      <div class="col">
        <div class="card h-100">
          <img :src="imagem" :alt="nome" class="card-img-top" />
          <div class="card-body">
            <div class="row">
              <div class="col" v-for="(tipo, i) in tipos" :key="i">
                <p class="fw-bold text-center text-white">
                  {{ tipo }}
                </p>
              </div>
            </div>
          </div>
          <div class="card-footer bg-dark bg-opacity-75">
            <p class="fs-4 text-white text-center">#{{ id }} - {{ nome }}</p>
          </div>
        </div>
      </div>
    </router-link>
  </div>
</template>

<style scoped>
.card {
  margin-bottom: 20px;
  width: 100%;
  height: 10rem;
  background-image: linear-gradient(to top, #d82f32 40%, #e9e8e9 60%);
}
</style>
