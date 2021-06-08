min2 a b
    | a > b = b
    | otherwise = a
    
{-
	--IN : Dois números, x e y
	--OUT: Menor valor entre x e y
	
	min2 3 4 == 3
	min2 4 1 == 1
	min2 2 2 == 2
	min2 4 -1 == -1
-}
