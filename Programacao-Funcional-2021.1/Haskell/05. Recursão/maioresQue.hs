-- Usando Filter 
maioresQue n xs = filter (>n) xs

-- Usando compreensão de lista
maioresQue' n xs = [x | x <- xs, x > n]
