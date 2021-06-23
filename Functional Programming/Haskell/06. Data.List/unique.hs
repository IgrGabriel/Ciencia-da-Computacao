unique [] = []
unique [u] = [u]
unique (u:us) = u : unique [x | x <- us, u /= x]

teste = do
  print $ unique [1,1,1] == [1]
  print $ unique [2,1,2,1,1,1,1,2] == [2,1]
  print $ unique [2,1,2,1,1,1,1,2,3] == [2,1,3]
  print $ unique [1,2,5,2,5,7,2,5] == [1,2,5,7]
 