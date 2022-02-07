<script setup>
import Container from "../components/Container.vue";
import Saldo from "../components/home/Saldo.vue";
import Titulo from "../components/Titulo.vue";
import Subtitulo from "../components/home/Subtitulo.vue";
import Financas from "../components/home/Financas.vue";
import TituloSaldo from "../components/home/TituloSaldo.vue";
import DespesasDiaria from "../components/home/DespesasDiaria.vue";
</script>

<template>
  <div>
    <!-- Saldo da Conta -->
    <Container>
      <TituloSaldo title="Saldo da Conta" />
      <Saldo :saldo="saldoTotal.toFixed(2)" />
    </Container>

    <!-- Visão geral -->
    <Container>
      <Titulo title="Visão geral" />
      <!-- Receita -->
      <Subtitulo subtitle="Receitas" tipo="receita" />
      <Financas :valor="valorReceita.toFixed(2)" tipo="receita" />
      <!-- Despesa -->
      <Subtitulo subtitle="Despesas" tipo="despesa" />
      <Financas :valor="valorDespesa.toFixed(2)" tipo="despesa" />
    </Container>

    <!-- Despesas Diarias-->
    <Container>
      <Titulo title="Despesas de hoje" />
      <DespesasDiaria :despesasDiarias="despesasDiarias" />
    </Container>
  </div>
</template>

<script>
import financas from "../service/financas";

export default {
  data() {
    return {
      saldoTotal: 0,
      valorReceita: 0,
      valorDespesa: 0,
      dataAtual: new Date().toLocaleDateString("en-GB"),
      despesasDiarias: null,
    };
  },
  mounted() {
    financas.listar().then((resposta) => {
      this.transacoes = resposta.data;

      /* Calcular o valor total saldo */
      this.saldoTotal = this.transacoes.reduce((total, item) => {
        if (item.tipo === "receita") {
          return total + parseFloat(item.valor);
        } else {
          return total - parseFloat(item.valor);
        }
      }, 0);

      /* Calcular o valor total das receitas */
      this.valorReceita = this.transacoes.reduce((total, item) => {
        if (item.tipo === "receita") {
          return total + parseFloat(item.valor);
        } else {
          return total;
        }
      }, 0);

      /* Calcular o valor total das despesas */
      this.valorDespesa = this.transacoes.reduce((total, item) => {
        if (item.tipo === "despesa") {
          return total + parseFloat(item.valor);
        } else {
          return total;
        }
      }, 0);

      /* Filtra apenas as depesas */
      this.despesas = this.transacoes.filter((item) => {
        return item.tipo === "despesa";
      });

      /*Filtra apenas as depesas que foram feitas no "diaAtual"*/
      this.despesasDiarias = this.despesas.filter((item) => {
        return item.data === this.dataAtual;
      });
    });
  },
};
</script>
