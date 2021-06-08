min3 a b c
    | a < b && b <= c = a
    | b < a && a <= c = b
    | c < a && a <= b = c
    | otherwise = a
    
{- 
	--IN : Três números, x, y e z
	--OUT: Menor valor entre x, y e z
	
	min3 1 2 3 == 1
	min3 2 1 3 == 1
	min3 3 4 2 == 2
	min3 2 5 4 == 2
-}
