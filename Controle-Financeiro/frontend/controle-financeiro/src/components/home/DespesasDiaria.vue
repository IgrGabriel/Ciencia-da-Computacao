<template>
  <div class="col-sm-11 col-md-11">
    <table class="table text-white bg-color-secondary">
      <thead>
        <tr>
          <th scope="col">Data</th>
          <th scope="col">Categoria</th>
          <th scope="col">Descrição</th>
          <th scope="col">Valor(R$)</th>
        </tr>
      </thead>

      <tbody class="list">
        <tr v-for="item in despesasDiarias" :key="item.id">
          <td>{{ item.data }}</td>
          <td>{{ item.categoria }}</td>
          <td>{{ item.descricao }}</td>
          <td>{{ item.valor }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  props: {
    despesasDiarias: Array,
  },
};
</script>
