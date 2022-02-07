<template>
  <div class="col-sm-11 col-md-auto">
    <p class="saldo-value">R$ {{ saldo }}</p>
  </div>
</template>

<script>
export default {
  props: {
    saldo: Number,
  },
};
</script>

<style></style>
