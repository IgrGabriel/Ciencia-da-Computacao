indices v xs = [snd (x,y) | (x,y) <- zip xs [0..], fst (x,y) == v]
        
teste = do
  print $ indices 0 [1,0,0,0,1] == [1,2,3]
  print $ indices 5 [1,3,5,2,3,5,5] == [2,5,6]
  print $ indices 7 [1,3,5,2,3,5,5] == []
  print $ indices 3 [1,3,5,2,3,5,5] == [1,4]