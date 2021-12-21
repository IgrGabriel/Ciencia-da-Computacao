import { listar_pokemons } from "./services/listar_pokemons";
import { createServer, IncomingMessage, ServerResponse } from "http";
import { AddressInfo } from "net";

const server = createServer((req: IncomingMessage, res: ServerResponse) => {

    if(req.url === '/'){
        const list_pokemons = new listar_pokemons();
        const pokemons = list_pokemons.getPokemons();

        let content = "";
        for(let i in pokemons) {
            let line = `<tr><th>${pokemons[i].id}</th>
                        <th><img src="${pokemons[i].imagem}" alt="${pokemons[i].nome}" /><br>
                        ${pokemons[i].nome}</th>
                        <th>${pokemons[i].pvMax}</th>
                        <th>${pokemons[i].ataque}</th>
                        <th>${pokemons[i].defesa}</th>
                        <th>${pokemons[i].ataqueEspecial}</th>
                        <th>${pokemons[i].defesaEspecial}</th>
                        <th>${pokemons[i].velocidade}</th>`;
                        
            content += line + "</tr>";
        }

        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.end(`
            <html>
                <head>
                    <title>Lista de Pokemons</title>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
                </head>
                <body>
                    <table>
                        <caption>Pokedex</caption>
                        <thead>
                            <tr>
                                <th>Id</th>                               
                                <th>Nome</th>
                                <th>PV Max</th>
                                <th>Ataque</th>
                                <th>Defesa</th>
                                <th>Ataque Especial</th>
                                <th>Defesa Especial</th>
                                <th>Velocidade</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${content}
                        </tbody>
                    </table>
                </body>
            </html>  
        `);
    } else {
        console.log(`Não sei responder ${req.url}`);
    }
});

server.listen(8080, "localhost", () => {
    const { address, port } = server.address() as AddressInfo;
    console.log(`Server listening on http://${address}:${port}`);
});