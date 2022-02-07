<template>
  <div class="col-sm-5 align-self-end">
    <p
      class="borda subtitle"
      v-bind:class="tipo === 'receita' ? 'borda-verde' : 'borda-vermelha'"
    >
      {{ subtitle }}
    </p>
  </div>
</template>

<script>
export default {
  props: {
    subtitle: String,
    tipo: String,
  },
};
</script>
