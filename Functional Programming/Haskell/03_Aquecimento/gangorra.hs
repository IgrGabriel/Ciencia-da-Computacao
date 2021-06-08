gangorra p1 c1 p2 c2
        | (p1*c1) == (p2*c2) = 0
        | (p1*c1) > (p2*c2) = -1
        | otherwise = 1

{-
gangorra 30 100 60 50 == 0
gangorra 40 40 38 60 == 1
gangorra 35 80 35 75 == -1
gangorra 45 23 96 12 == 1
gangorra 74 12 65 48 == 1
gangorra 78 45 12 23 == -1
-}