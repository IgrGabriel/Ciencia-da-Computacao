tails [] = [[]]
tails (x:xs) = [x:xs] ++ tails xs 

teste = do
  print $ tails [1] == [[1],[]]
  print $ tails [1,3,5] == [[1,3,5],[3,5],[5],[]] 
  print $ tails [5,3,4] == [[5,3,4],[3,4],[4],[]]