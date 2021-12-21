-- Opção 01 - usando elem
pertence indice x = elem indice x

-- Opção 02 - usando filter
pertence2 ind x = if (filter (\x -> x == ind) x) == [] then False else True 

-- Opçao 03 - usando recursividade
pertence3 ind [] = False
pertence3 ind (x:xs) = if ind == x then True else pertence3 ind xs