elemento n xs = xs !! n'
    where
        tam = length xs
        n'= if n < 0 then n + tam else n