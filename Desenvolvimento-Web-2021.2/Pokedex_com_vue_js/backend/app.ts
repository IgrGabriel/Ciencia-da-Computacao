import * as path from "path";
import express from "express";
import morgan from "morgan";
import favicon from "serve-favicon";
import { router as pokemonRouter } from "./routes/pokemons";
import cors from 'cors';

const PORT = 8082;
const app = express();

app.use(favicon(path.join(__dirname, '../',"public", "favicon.png")));
app.use(morgan('tiny'));
app.use(express.static('./public'));

app.use(cors({
    origin: 'http://localhost:3000',
}));

app.use('/pokemons', pokemonRouter);

app.get('/', (req, res) => {
    res.redirect('/pokemons');
})

app.listen(PORT, () => {
    console.log(`Server listening on http://localhost:${PORT}`);
});