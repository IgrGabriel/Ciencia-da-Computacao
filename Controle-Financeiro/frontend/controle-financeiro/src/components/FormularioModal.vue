<template>
  <!-- Fomulário Modal -->
  <div
    class="modal fade"
    id="staticBackdrop"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    tabindex="-1"
    aria-labelledby="staticBackdropLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <!-- Modal Header -->
        <slot></slot>

        <!-- Formulario -->
        <div class="modal-body">
          <form autocomplete="off" @submit="createTransation">
            <!-- Valor da transação -->
            <div class="input-box">
              <label for="valor" class="labelInput">
                <i class="bx bx-calculator"></i>
              </label>

              <input
                type="text"
                name="valor"
                id="valor"
                v-model="valor"
                class="input-user"
                placeholder="R$ 0,00"
                required
              />
            </div>

            <!-- Descrição da transação -->
            <div class="input-box">
              <label for="descricao" class="labelInput">
                <i class="bx bx-detail"></i>
              </label>
              <input
                type="text"
                name="descricao"
                id="descricao"
                class="input-user"
                placeholder="Descrição"
                v-model="descricao"
                required
              />
            </div>

            <!-- Opções de categoria para receita -->
            <div class="input-box">
              <label for="categoria">
                <i class="bx bx-category"></i>
              </label>
              <select id="categoria" name="categoria" v-model="categoria">
                <option selected disabled>Categoria</option>
                <option value="salario">Salário</option>
                <option value="investimento">Investimentos</option>
                <option value="servicos">Serviços</option>
                <option value="vendas">Vendas</option>
              </select>
            </div>

            <!-- Data da transação -->
            <div class="data-container">
              <input
                type="date"
                name="data"
                id="data"
                v-model="data"
                required
              />
            </div>

            <!-- Escolher o tipo da transação -->
            <div class="input-box">
              <label for="tipo">
                <i class="bx bx-dollar"></i>
              </label>
              <select v-model="tipo" id="tipo" name="tipo">
                <option selected disabled>Tipo</option>
                <option value="receita">Receita</option>
                <option value="despesa">Despesa</option>
              </select>
            </div>

            <hr />
            <input
              class="btn btn-primary"
              type="submit"
              name="submit"
              id="submit"
            />
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      valor: null,
      descricao: null,
      categoria: null,
      data: null,
      tipo: String,
    };
  },
  methods: {
    async createTransation(e) {
      e.preventDefault();

      const transacao = {
        valor: this.valor,
        descricao: this.descricao,
        categoria: this.categoria,
        data: this.data,
        tipo: this.tipo,
      };

      console.log(transacao);

      // axios
      //   .post("http://localhost:8080/financas", transacao)
      //   .then((response) => {
      //     console.log(response);
      //   });

      //limpar os campos do formulário
      this.valor = "";
      this.descricao = "";
      this.categoria = "";
      this.data = "";
    },
  },
};
</script>
