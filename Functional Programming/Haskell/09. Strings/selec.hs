selec y xs = [y !! x | x <- xs]

teste = do
    print $ selec "abcdef" [0,3,2,3] == "adcd"