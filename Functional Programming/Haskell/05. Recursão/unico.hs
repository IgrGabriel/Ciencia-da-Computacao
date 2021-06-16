unico _ [] = False
unico n xs = length (filter (==n) xs) == 1 || False

unico :: Eq a => a -> [a] -> Bool
unico _ [] = False
unico n (x:xs)
  | n == x = True
  | otherwise = unico n xs  
  where if n == x then count

  --unico' _ [] = False
unico' :: Eq a => a -> a -> [a]  -> Bool
unico' n i (x:xs)
  | n == x && i == 1 = True
  | otherwise = unico' n (i+1) xs  

unico n (x:xs) = unico' n 0 (x:xs)

{-
IN : Lista u e valor x
OUT: True se x ocorre exatamente uma vez em u e false do contrário

unico 2 [2] == True
unico 2 [3,1] == False
unico 2 [1,2,3,2] == False
-} 