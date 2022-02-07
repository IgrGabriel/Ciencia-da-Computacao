import { http } from "./config";

export default {
  listar: () => {
    return http.get("/financas");
  },
  salvar: (financa) => {
    return http.post("/financas", financa);
  },
};
