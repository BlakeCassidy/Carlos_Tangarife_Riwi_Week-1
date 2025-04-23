# Modulo-1---Semana-1

Conceptos :

🔵 Fundamentos

¿Qué es programar?: 

- Desde mi perspectiva es darle instrucciones claras a un sistema para que ejecute algo en especifico, pueden ser cálculos, mostrar resultados, controlar cosas. Seria en si, escribir instrucciones en un lenguaje que la computadora o el sistema los entienda.

¿Qué es Python y para qué sirve?: 

- Es un lenguaje de mediano y alto nivel muy intuitivo para el desarrollo de múltiples cosas: crear juegos, paginas web, analizar datos y demás.

¿Qué es un programa y cómo se ejecuta?:

- Un programa es una serie de instrucciones escritas en determinado lenguaje que sirven para solucionar una necesidad y para que puedan llevarse a cabo, es necesario utilizar un “interprete” para que las lea y pueda ejecutarlas.

¿Qué es una variable?:

- Es el lugar donde almacenamos datos o información. Las variables deben de identificarse con un nombre y lo que se almacena dentro de ellas puede mutar.

Tipos de datos básicos:

- Texto (str): Son todos aquellos alfanuméricos, suelen ser palabras o frases.

- Número entero (int): Son los números sin decimales, positivos y negativos.

- Número decimal (float): Son los números decimales, positivos y negativos.

- Verdadero/falso (bool): Suelen conocerse como datos de expresión, solo pueden tener dos valores, True ó False.

Operaciones básicas con números:

- (+, -, *, /) : Son aquellas que nos permiten operar los números, un detalle, es que la división siempre da como resultado un decimal.

- Mostrar información en pantalla: print() : Sirve para manifestar o escribir algo en la pantalla.

- Pedir información al usuario: input() : Es una funcionalidad que permite dar una información y recolectar otra. Suele ser utilizada para pedir información al ususario.







Convertir tipos de datos: 

int() : Convierte algo a un número entero (si es posible). Ejemplo: int("10") da el número 10.

float() : Convierte algo a un número decimal (si es posible). Ejemplo: float("3.14") da el número 3.14.

str() : Convierte algo a texto. Ejemplo: str(25) da el texto "25".

¿Qué es un error?

- Un error es cuando ese “interprete” o la computadora no pueden entender las instrucciones. Los errores mas comunes son los de sintaxis, llamado de variables y operaciones que no pueden ser posibles.


🔵 Lógica de programación

- Comparar datos: (==, !=, <, >, <=, >=): Son como las formas de preguntar si algo es igual, diferente, menor, mayor, y demás, el resultado de estas preguntas o comparaciones siempre es True o False.

- Tomar decisiones: if, else, elif : Nos permiten hacer que el programa haga diferentes cosas dependiendo de si una condición es verdadera o falsa. Algo así como: 

if (si): Si esta condición es verdadera, haz esto.

else (si no): Si la condición del if no es verdadera, haz esto otro.

elif (sino si): Si la condición del if no es verdadera, pero esta otra condición sí lo es, haz esto. Puedes tener varios elif.

Combinar condiciones: 

- and: Se ejecuta cuando las condiciones se cumplen.

- or: Se ejecuta cuando al menos una de las condiciones se cumple.

- not : Sirve para invertir el valor de una condición.


- Cómo escribir comentarios en el código (# comentario): Se utiliza la almohadilla para denotar que lo que vendrá en el código es un comentario.

¿Qué es la indentación y por qué es tan importante en Python?

- La indentación son los espacios o tabulaciones que dejamos al principio de las líneas de código. En Python, la indentación es parte de la estructura del lenguaje. Esto indica qué bloques de código pertenecen a un if, else, elif, un bucle, etc. Si la indentación no es correcta, Python mostrará un error.


- Buenas prácticas al nombrar variables (nombres claros, sin espacios): Las variables deben de ser descriptivas y entendibles, por ejemplo es mejor usar “nombre_usuario” en lugar de “nombre”.

¿Qué hacer cuando algo no funciona? (buscar, leer errores, no frustrarse): Interpretar el error, buscar en internet, revisar la lectura del código. Auto-gestionar el problema e intentar solucionarlos.


🔵 Estructuras de control


Repetir acciones con bucles: 

- for : Se usa para repetir un número específico de veces o para recorrer elementos de una colección (como una lista de números).

- while : Se usa para repetir un bloque de código mientras una condición sea verdadera.

- Salir de un bucle antes de tiempo:

break : Detiene la ejecución del bucle por completo y sale de él.

continue : Detiene la iteración actual del bucle y pasa a la siguiente.

Manejo básico de errores: 

- try-except: Es cuando el código o una parte de él podría tener un error, con try-except podría ejecutarse ese código y si ocurre el error, en lugar de que la ejecución se detenga, se hará algo en especifico, por ejemplo, mostrar un mensaje de error.
