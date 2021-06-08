iguais a b c
            | a == b && b == c = 3
            | a == b && b /= c || b == c && b /= a || a == c &&a /= b = 2
            | otherwise  = 0