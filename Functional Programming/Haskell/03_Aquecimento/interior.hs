interior xs = take ((length xs) - 2) (drop 1 xs)

{-
interior [1,2] == []
interior [1,3,2] == [3]
interior [2,5,3,7,3] == [5,3,7]
interior [2,2,2,4] == [2,2]
interior [1,2,3,5,7,8] == [2,3,5,7]
-}