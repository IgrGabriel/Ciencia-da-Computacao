uniao xs ys = xs ++ [y | y <- ys, not (elem y xs)]
