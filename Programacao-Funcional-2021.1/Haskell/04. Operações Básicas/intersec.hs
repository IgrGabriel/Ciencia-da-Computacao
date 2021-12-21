intersec xs ys = zs ++ [x | x <- xs, elem x ys]
        where zs = []
