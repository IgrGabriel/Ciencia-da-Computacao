-- Usando Filter
maioresQue n xs = filter (>n) xs

-- Usando comprensão de lista
maioresQue' n xs = [x | x <- xs, x > n]