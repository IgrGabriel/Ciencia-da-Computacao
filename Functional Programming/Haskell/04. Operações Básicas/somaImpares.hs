-- Versão 01
soma [] = 0
soma lista = (head lista) + (somaImpares(tail lista))
somaImpares x = soma $ filter odd x

-- Versão 02
--somaImpares x = sum ([x| x <- x, mod x 2 == 1])

{-
somaImpares [2,3,1,5] == 9
somaImpares [1,1,4,2] == 2
somaImpares [3,2,4,6,5,7,8,0,1] == 16
somaImpares [2,3,1,5,2,2] == 9
somaImpares [1,1,1,1] == 4
-}