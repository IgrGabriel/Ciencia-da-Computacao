//Resultado
let r

// Currying (Funções com apenas um parâmetro)
const soma = a => b => c => a + b + c
r = soma(1)(2)(3)
r

// Função identidade
const ID = a => a
r =  ID(9)
r

// Retorna o primeiro valor
const PRI = a => _ => a
r = PRI(4)(8)
r

// Retorna o último valor
const ULT = _ => b => b
r = ULT(5)(1) 
r

//Executa a função com os valores trocados
const TRO = f => a => b => f(b)(a)
r = TRO(PRI)(3)(7)
r

r = TRO(ULT)(3)(7)
r

// Boolean
// TRUE: PRI é retornado
// FALSE: ULT é retorndo

const T = PRI
const F = ULT

T.inspect = () => 'Verdadeiro (PRI)'
F.inspect = () => 'Falso (ULT)'

T
F

/* Álgebra Booleana*/

//NOT
const NOT = a => a(F)(T)

r = NOT(F)
r

r = NOT(T)
r

//AND
const AND = a => b => a(b)(F)

r = AND(T)(T)
r

r = AND(T)(F)
r

r = AND(F)(T)
r

r = AND(F)(F)
r

//OR
const OR = a => b => a(T)(b)

r = OR(T)(T)
r

r = OR(T)(F)
r

r = OR(F)(T)
r

r = OR(F)(F)
r
