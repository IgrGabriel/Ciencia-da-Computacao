myrepeat x = x:myrepeat x

main = do
    print $ take 3 (myrepeat 4) == [4,4,4]
    print $ take 2 (myrepeat 5) == [5,5]