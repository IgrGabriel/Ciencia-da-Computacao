import Debug.Trace ( trace )
import Data.Function ( (&) )

data Car = Car  { pass :: Int
                , maxPass :: Int
                , gas :: Int
                , maxGas :: Int
                , km :: Int
                } deriving (Eq, Show, Read)


data Op = Op { name :: String
             , result :: Bool
             } deriving (Eq, Show, Read)

data Info = Info { car :: Car
                 , op  :: Op
                 } deriving (Eq, Show, Read)


toString (Info (Car pass maxPass gas maxGas km) (Op name result)) =
                "Car pass: " ++ show pass ++ "/" ++ show maxPass
                 ++ " gas: " ++ show gas  ++ "/" ++ show maxGas
                 ++  " km: " ++ show km
                 ++ " Operation: " ++ name ++ " Result: " ++ show result

resume :: Info -> Info
resume info = trace (toString info) info

-- cria um carro passando maxPass e maxGas - retorna sempre true.
createCar :: Int -> Int -> Info
createCar maxP maxG = Info (Car {pass = 0, maxPass = maxP, gas = 0, maxGas = maxG, km = 0}) (Op {name = "createCar", result = True})

-- enche o tanque passando a qtd de gas. Retorna falso apenas se o tanque já estiver completamente cheio.
fuel :: Int -> Info -> Info
fuel g (Info (Car pass maxPass gas maxGas km) _) = if gas < maxGas then
        if (g + gas) < maxGas then Info (Car pass maxPass (g + gas) maxGas km) (Op {name = "fuel", result = True})
        else Info (Car pass maxPass maxGas maxGas km) (Op {name = "fuel", result = True})
    else Info (Car pass maxPass gas maxGas km) (Op {name = "fuel", result = False})
     
-- Faz entrar uma pessoa no carro. Retorna false se já estiver lotado.
embark :: Info -> Info 
embark (Info (Car pass maxPass gas maxGas km) _) = if pass < maxPass 
    then Info (Car (pass + 1) maxPass gas maxGas km) (Op {name = "embark", result = True})
    else Info (Car pass maxPass gas maxGas km) (Op {name = "embark", result = False})

-- Retira uma pessoa do carro, retorna false se não tiver ninguém no carro
disembark :: Info -> Info
disembark (Info (Car pass maxPass gas maxGas km) _) = if pass > 0 
    then Info (Car (pass - 1) maxPass gas maxGas km) (Op {name = "disembark", result = True})
    else Info (Car pass maxPass gas maxGas km) (Op {name = "disembark", result = False})

-- dirige diminuindo a gasolina e aumentando km. 
-- Só é possível dirigir se houver alguém no carro e houver alguma gasolina.
-- Aumenta a km da gasolina gasta.
-- retorna false se não há ninguém no carro ou se não tinha gasolina para completar a viagem.
drive :: Int -> Info -> Info 
drive km' (Info (Car pass maxPass gas maxGas km) _) = if pass > 0 && gas > 0 && gas > km' 
    then Info (Car pass maxPass (gas - km') maxGas (km + km')) (Op {name = "drive", result = True}) 
    else Info (Car pass maxPass gas maxGas km) (Op {name = "drive", result = False})

-- main = print $ resume . embark . resume. embark . resume $ createCar 2 50
main = do 
    let res = createCar 2 50 
            & resume & embark
            & resume & disembark
            & resume & disembark
            & resume & drive 10
            & resume & embark
            & resume & embark
            & resume & embark
            & resume & drive 10
            & resume & fuel 30
            & resume & fuel 30
            & resume & fuel 30
            & resume & drive 30
            & resume & drive 30
            & resume
    print res
