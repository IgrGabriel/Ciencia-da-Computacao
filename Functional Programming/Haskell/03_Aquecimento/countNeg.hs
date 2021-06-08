countNeg x = length (filter (\x -> x < 0) x)

{-
netlist [] == 0
countNeg [1,2,3,4,5] == 0
countNeg [1,-1,2,-3,4] == 2
countNeg [2,-2] == 1
countNeg [1,-1] == 1
countNeg [1,-3,-4,3,4,-5] == 3
-}
