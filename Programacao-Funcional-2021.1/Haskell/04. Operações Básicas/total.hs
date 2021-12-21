--caso 1
total a = sum (map (\x -> 1) a)

--caso 2
total2 [] = 0
total2 (_:xs) = 1 + total2 xs

--caso 3
total3 l = foldl (\x y -> 1+x) 0 l
