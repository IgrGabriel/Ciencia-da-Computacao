import Data.List

-- com list comprehension
gerador3 = [x | x <- [1..], x `mod` 2 == 0] 
-- sem list comprehension
gerador3' = iterate (*2) 1