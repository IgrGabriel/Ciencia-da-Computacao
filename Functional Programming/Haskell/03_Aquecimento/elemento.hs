--elemento 0 (x:xs) = x
--elemento ind (x:xs)  -- elemento (ind - 1) xs
           -- | ind < 0 = ind + (length xs)
           -- | otherwise = elemento (ind - 1) xs

        --where len = length xs
             -- ind' = if ind' < 0 then ind + len else ind 

--elemento ind (x:xs)
           -- | ind > 0 = elemento (ind - 1) xs
           -- | ind < 0 = elemento (ind - 1) xs
 
elemento ind xs = let
        


--elemento 2 [2,7,3,9] == 3
--elemento 0 [2,7,3,9] == 2
--elemento -1 [2,7,3,9] == 9
--elemento -2 [2,7,3,9] == 3