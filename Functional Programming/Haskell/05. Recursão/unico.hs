-- Filter
unico _ [] = False
unico n xs = length (filter (==n) xs) == 1 || False

-- Clist
unico' n xs = length [x | x <- xs, x == n] == 1 || False
