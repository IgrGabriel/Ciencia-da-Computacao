<template>
  <div class="col-sm-5 align-self-end">
    <p
      class="values"
      v-bind:class="tipo === 'receita' ? 'receita-value' : 'despesa-value'"
    >
      R$ {{ valor }}
    </p>
  </div>
</template>

<script>
export default {
  props: {
    valor: Number,
    tipo: String,
  },
};
</script>
