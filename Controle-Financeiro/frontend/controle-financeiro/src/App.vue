<script setup>
import Footer from "./components/Footer.vue";
import Navbar from "./components/Navbar.vue";
import ModalHeader from "./components/ModalHeader.vue";
import FormularioModal from "./components/FormularioModal.vue";
</script>

<template>
  <main>
    <Navbar userName="Igor Gabriel" />
    <router-view></router-view>
    <Footer />
    <FormularioModal>
      <ModalHeader />
    </FormularioModal>
  </main>
</template>

<script></script>

<style>
/* Link de importação do Google Fontes*/
@import url("https://fonts.googleapis.com/css2?family=Dongle:wght@300;400&family=Maven+Pro&family=Roboto+Slab:wght@200;300;400;500&display=swap");

* {
  font-family: "Maven Pro", sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

:root {
  /*Cor das fontes*/
  --color-text: #fff;
  /*Cores principais*/
  --color-primary: #0f102c;
  --color-secondary: #1c1e3b;
  --color-shadow: #454764;
  /*Cores das bordas*/
  --color-green: #00ff00;
  --color-red: #ff0000;
  /*Cores dos valores*/
  --saldo-color: #4652fa;
  --receita-color: #42ac48;
  --despesa-color: #df3c30;
  /*1rem = 16px*/
  font-size: 16px;
}

body {
  height: 100vh;
  background-color: var(--color-secondary);
  color: var(--color-text);
}

main .container .title {
  font-size: 2rem;
  font-weight: 400;
  margin-bottom: 0.45rem;
}

main .container .row .subtitle {
  font-size: 1.4rem;
}

main .container .row .subtitle {
  font-size: 1.4rem;
}

main .container .row ul {
  list-style: none;
}
</style>
