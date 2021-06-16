sequencia :: Int -> Int -> [Int]
sequencia 0 _ = []
sequencia 1 y = [y]
sequencia x y = y : (sequencia (x-1) (y+1))