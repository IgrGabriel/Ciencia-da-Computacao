isPalind xs = if reverse xs == xs then True else False

teste = do
    print $ isPalind "ana"   == True
    print $ isPalind "123aa321" == True
    print $ isPalind "cachorro" == False