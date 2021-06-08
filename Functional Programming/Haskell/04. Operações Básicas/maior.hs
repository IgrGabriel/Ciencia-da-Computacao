maior [x] = x
maior x = if maxResto > (head x) then maxResto else (head x)
          where maxResto = maior (tail x)