-- Opção 01
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

-- Opção 02
fib' n
    | n == 1 || n == 2 = 1
    | otherwise = fib' (n-1) + fib' (n-2)