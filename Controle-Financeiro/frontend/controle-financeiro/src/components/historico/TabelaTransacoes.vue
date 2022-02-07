<template>
  <div class="row justify-content-around">
    <div class="col-12">
      <div id="paginate">
        <table class="table text-white bg-color-secondary">
          <thead>
            <tr>
              <th scope="col">Data</th>
              <th scope="col">Categoria</th>
              <th scope="col">Descrição</th>
              <th scope="col">Valor</th>
              <th scope="col">Tipo</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="transacao in transacoes" :key="transacao.id">
              <td>{{ transacao.data }}</td>
              <td>{{ transacao.categoria }}</td>
              <td>{{ transacao.descricao }}</td>
              <td>{{ transacao.valor }}</td>
              <td>{{ transacao.tipo }}</td>
            </tr>
          </tbody>
        </table>
        <!-- controles -->
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    transacoes: Array,
  },
};
</script>
