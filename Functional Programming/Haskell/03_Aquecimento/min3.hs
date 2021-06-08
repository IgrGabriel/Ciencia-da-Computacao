min3 a b c
    | a < b && b <= c = a
    | b < a && a <= c = b
    | c < a && a <= b = c
    | otherwise = a
