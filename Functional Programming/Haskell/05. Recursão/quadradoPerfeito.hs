quadradoPerfeitoquadperf':: Int -> Int -> Bool
quadperf' x i
          | i * i == x = True
          | i * i > x = False
          | otherwise = quadperf' x (i+1)

quadperf x = quadperf' x 1