-- Opção 01
frequencia::Int->[Int]->Int
frequencia _ [] = 0
frequencia n xs = length (filter (==n) xs)

-- Opção 02
frequencia' _ [] = 0
frequencia' n xs = length [x | x <- xs, x == n]