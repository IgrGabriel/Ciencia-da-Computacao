<script setup lang="ts">
import { useStore } from "vuex";
import Footer from "./components/Footer.vue";

const store = useStore();
store.dispatch("getPokemons");
</script>

<template>
  <main>
    <router-view></router-view>
    <Footer />
  </main>
</template>
