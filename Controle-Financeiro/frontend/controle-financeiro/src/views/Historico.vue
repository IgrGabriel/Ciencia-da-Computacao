<script setup>
import Container from "../components/Container.vue";
import TabelaTransacoes from "../components/historico/TabelaTransacoes.vue";
import Titulo from "../components/Titulo.vue";
</script>

<template>
  <div>
    <Container>
      <Titulo title="Histórico de Transações" />
      <TabelaTransacoes :transacoes="transacoes" />
    </Container>
  </div>
</template>

<script>
import financas from "../service/financas";

export default {
  data() {
    return {
      transacoes: null,
    };
  },
  mounted() {
    financas.listar().then((resposta) => {
      this.transacoes = resposta.data;
    });
  },
};
</script>
