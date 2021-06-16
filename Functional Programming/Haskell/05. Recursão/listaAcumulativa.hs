listacc [] = []
listacc xs = (listacc (init xs))++[sum xs]