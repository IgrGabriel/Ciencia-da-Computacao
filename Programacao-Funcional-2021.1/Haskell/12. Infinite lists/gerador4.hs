import Data.List

gerador4 x = takeWhile (>0) $ iterate (`div` 2) x