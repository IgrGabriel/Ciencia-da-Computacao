import * as path from "path";
import express from "express";
import morgan from "morgan";
import favicon from "serve-favicon";
import { router as pokemonRouter } from "./routes/pokemons";
import { engine } from 'express-handlebars'

const PORT = 8080;
const app = express();

app.engine('hbs', engine({
    layoutsDir: __dirname + '/../views/layouts',
    extname: '.hbs'
}));

app.set('view engine', 'hbs');
app.set('views', './views');

app.use(favicon(path.join(__dirname, '../',"public", "favicon.png")));
app.use(morgan('tiny'));
app.use(express.static('./public'));
app.use('/pokemons', pokemonRouter);

app.get('/', (req, res) => {
    res.redirect('/pokemons');
})

app.listen(PORT, () => {
    console.log(`Server listening on http://localhost:${PORT}`);
});