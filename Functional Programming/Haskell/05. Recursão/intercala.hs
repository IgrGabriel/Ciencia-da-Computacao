intercal :: [Integer] -> [Integer] -> [Integer]
intercal [] [] = []
intercal x [] = x
intercal [] y = y
intercal (x:xs) (y:ys) = (x:y:[]) ++ intercal xs ys   