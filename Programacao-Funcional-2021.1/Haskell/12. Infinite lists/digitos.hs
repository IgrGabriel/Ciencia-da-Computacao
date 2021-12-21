import Data.List

digitos x = reverse $ unfoldr (\y -> if y == 0 then Nothing else Just (y `mod` 10, y `div` 10)) x