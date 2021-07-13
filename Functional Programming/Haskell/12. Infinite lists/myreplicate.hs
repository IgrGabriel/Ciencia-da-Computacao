myreplicate x y = take x $ myrepeat y
    where myrepeat y = y:myrepeat y

main = do
    print $ myreplicate 4 0 == [0, 0, 0, 0]
    print $ myreplicate 2 True == [True, True]
    print $ myreplicate 3 [5] == [[5],[5],[5]]