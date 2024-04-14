DARIO

Pregunta 1)
Los cuatro algoritmos clásicos para encontrar ceros de funciones no lineales son:

1. **Método de Bisección**: Divide iterativamente el intervalo que contiene la raíz a la mitad y selecciona el subintervalo donde cambia de signo la función. Repite este proceso hasta alcanzar la precisión deseada.

2. **Método de Newton-Raphson**: Utiliza la derivada de la función para aproximar la raíz, utilizando la fórmula de Newton-Raphson: \( x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \). Este método converge rápidamente si la suposición inicial es cercana a la raíz y si la función es suave.

3. **Método de Secante**: Similar al método de Newton-Raphson, pero en lugar de usar la derivada exacta, utiliza una aproximación a través de una secante entre dos puntos cercanos. La fórmula de iteración es \( x_{n+1} = x_n - \frac{f(x_n)(x_n - x_{n-1})}{f(x_n) - f(x_{n-1})} \).

4. **Método de Regula Falsi**: Similar al método de bisección, pero en lugar de dividir el intervalo a la mitad, la división se hace proporcional a la interpolación lineal entre los extremos del intervalo. Esto acelera la convergencia en comparación con la bisección.

Estos métodos son fundamentales en la resolución numérica de ecuaciones no lineales y se eligen según la función específica y los requisitos de precisión y velocidad de convergencia.

Pregunta 2)
a) Los criterios de parada comunes al implementar un método para encontrar ceros de funciones no lineales son:

1. **Convergencia**: Detener el algoritmo cuando la diferencia entre dos iteraciones sucesivas es menor que una cierta tolerancia predefinida, lo que indica que se ha alcanzado la convergencia.

2. **Número máximo de iteraciones**: Establecer un límite en el número de iteraciones permitidas para evitar que el algoritmo se ejecute indefinidamente, lo que puede ocurrir en casos de convergencia lenta o divergencia.

b) Se utilizarían estos criterios por las siguientes razones:

1. **Convergencia**: Este criterio garantiza que el algoritmo se detenga una vez que se haya alcanzado una solución lo suficientemente cercana al valor real de la raíz. Ayuda a evitar el desperdicio de recursos computacionales en iteraciones adicionales cuando la solución ya es lo suficientemente precisa para el propósito deseado.

2. **Número máximo de iteraciones**: Es importante establecer un límite en el número de iteraciones para evitar que el algoritmo se ejecute indefinidamente, especialmente en casos donde la función puede ser complicada o no converger hacia una raíz. Esto garantiza que el algoritmo finalice incluso si no alcanza la convergencia dentro de un número razonable de iteraciones.

Pregunta 4)
a) **Justificación de la afirmación**:

El método de la secante se puede ver como una modificación del método de Newton porque utiliza una aproximación de la derivada en lugar de la derivada exacta. En el método de Newton, se utiliza la derivada exacta de la función en cada iteración para calcular la pendiente de la recta tangente, mientras que en el método de la secante se estima esta pendiente mediante una secante entre dos puntos cercanos en la función. Por lo tanto, el método de la secante es una aproximación del método de Newton que no requiere el cálculo explícito de la derivada.

Por otro lado, el método de Newton se puede considerar una modificación del método de la secante al utilizar la derivada exacta en lugar de una aproximación. El método de Newton mejora la velocidad de convergencia al utilizar información más precisa sobre la función en cada iteración.

b) **Argumentación sobre si el método de la secante puede ser considerado como un Newton++ o un Newton--**:

El método de la secante puede considerarse como un "Newton--" en el sentido de que es una simplificación del método de Newton al no requerir el cálculo explícito de la derivada. Sin embargo, también se puede ver como un "Newton++" en el sentido de que generalmente converge más lentamente que el método de Newton, pero es más robusto en ciertos casos donde la función puede no ser diferenciable o la derivada puede ser difícil de calcular.

c) **Elección del "mejor" método**:

La elección entre el método de Newton y el método de la secante depende de la naturaleza de la función y los requisitos específicos del problema. En general, el método de Newton tiende a converger más rápidamente si se dispone de la derivada y si la función es suave. Sin embargo, el método de la secante puede ser preferible en casos donde calcular la derivada es costoso o la función no es diferenciable en ciertos puntos. Por lo tanto, no hay un método "mejor" en todos los casos, sino que la elección depende del contexto específico.

Pregunta 5)
a) **Biblioteca o lenguaje**:

1. **Biblioteca SciPy de Python**
2. **Matlab**

b) **Funciones para encontrar ceros de funciones**:

1. **SciPy de Python**:
   - Función: `scipy.optimize.root`
   - Descripción: Esta función encuentra una raíz de una función dada utilizando diversos métodos de optimización. Se puede especificar el método deseado mediante el argumento `method`, que puede incluir métodos como Newton-Raphson, Broyden, Powell, entre otros.

2. **Matlab**:
   - Función: `fzero`
   - Descripción: La función `fzero` encuentra un cero de una función mediante métodos iterativos. Se le pasa como argumento la función a la que se desea encontrar el cero y un valor inicial aproximado. Además, se puede especificar una tolerancia para la precisión deseada.

Pregunta Secreta)
Un método para comparar dos algoritmos para encontrar el cero de una función podría ser el siguiente:

1. **Definir un conjunto de funciones de prueba**: Seleccionar un conjunto diverso de funciones de prueba que representen diferentes características, como funciones lineales, cuadráticas, trigonométricas, polinomiales de grado variable, funciones con múltiples raíces, etc. Esto ayudará a evaluar cómo se comportan los algoritmos en una variedad de situaciones.

2. **Definir un criterio de comparación**: Establecer un criterio cuantitativo para comparar la eficiencia y la precisión de los algoritmos. Esto podría incluir medidas como el número de iteraciones requeridas para converger a la solución, el tiempo de ejecución, la precisión de la solución obtenida en relación con una solución de referencia (si está disponible), o una combinación de estos factores.

3. **Implementar los algoritmos y ejecutarlos en las funciones de prueba**: Implementar los dos algoritmos que se desean comparar en un entorno de programación, utilizando las funciones de prueba definidas anteriormente. Ejecutar los algoritmos con diferentes configuraciones de parámetros (si es posible) y registrar los resultados obtenidos.

4. **Analizar los resultados y realizar comparaciones**: Analizar los resultados obtenidos en términos del criterio de comparación definido anteriormente. Comparar el rendimiento de los algoritmos en términos de su eficiencia (número de iteraciones, tiempo de ejecución) y precisión (diferencia con la solución de referencia, si está disponible).

5. **Considerar la robustez y la escalabilidad**: Además de la eficiencia y la precisión, es importante considerar la robustez y la escalabilidad de los algoritmos. Evaluar cómo se comportan los algoritmos en situaciones difíciles, como funciones con múltiples raíces o funciones mal condicionadas. También considerar cómo se escalan los algoritmos con respecto al tamaño del problema, es decir, si mantienen un rendimiento aceptable para funciones más grandes o más complejas.

6. **Conclusión y recomendaciones**: Basándose en los resultados obtenidos, sacar conclusiones sobre qué algoritmo es más adecuado para qué tipo de funciones y situaciones. Proporcionar recomendaciones sobre cuándo y cómo utilizar cada algoritmo en función de sus fortalezas y debilidades observadas durante la comparación.

Pregunta 7)
Claro, aquí tienes:

**Scipy de Python**:
- Nombre del algoritmo: `scipy.optimize.root`
- Descripción breve: Esta función de la biblioteca Scipy implementa varios algoritmos para encontrar raíces de funciones no lineales. Algunos de los métodos disponibles son 'hybr', 'lm', 'broyden1', 'broyden2', 'anderson', 'linearmixing', 'diagbroyden', entre otros. La función permite especificar el método deseado mediante el argumento `method` y proporciona opciones adicionales para ajustar la tolerancia, el número máximo de iteraciones y otros parámetros.

**Matlab**:
- Nombre del algoritmo: `fzero`
- Descripción breve: La función `fzero` en Matlab encuentra ceros de funciones no lineales utilizando un método iterativo similar al método de la secante. La sintaxis de uso es simple: `x = fzero(fun,x0)`, donde `fun` es la función que se quiere analizar y `x0` es el punto inicial de la búsqueda del cero. `fzero` es una función versátil y ampliamente utilizada en Matlab para encontrar raíces de funciones de forma eficiente.

Pregunta 8)
Para deducir el método de Newton para sistemas de ecuaciones no lineales, partiendo de una solución inicial \( x_0 \), podemos utilizar el desarrollo en serie de Taylor de la función \( F(x + h) \) alrededor del punto \( x \):

El desarrollo en serie de Taylor de \( F(x + h) \) alrededor de \( x \) se expresa como:

\[ F(x + h) = F(x) + J(x) \cdot h + O(||h||^2) \]

Donde:
- \( F(x) \) es la función vectorial \( F : \mathbb{R}^n \rightarrow \mathbb{R}^n \).
- \( J(x) \) es la matriz jacobiana de \( F \) evaluada en \( x \), es decir, \( J(x) = \frac{\partial F}{\partial x} \).
- \( h \) es un vector pequeño que representa un cambio en \( x \).
- \( O(||h||^2) \) denota términos de orden superior, que pueden ser ignorados si \( ||h|| \) es lo suficientemente pequeño.

Si establecemos \( F(x + h) = 0 \) y despreciamos los términos de orden superior, obtenemos:

\[ F(x) + J(x) \cdot h = 0 \]

Queremos encontrar \( h \) tal que \( F(x + h) = 0 \), por lo que podemos tomar \( h \) como el paso a seguir para acercarnos a la solución. Entonces, podemos despejar \( h \):

\[ J(x) \cdot h = -F(x) \]

Finalmente, el paso \( h \) se puede encontrar resolviendo este sistema de ecuaciones lineales para \( h \):

\[ h = -[J(x)]^{-1} \cdot F(x) \]

Por lo tanto, el método de Newton para sistemas de ecuaciones no lineales consiste en actualizar iterativamente \( x \) utilizando la siguiente fórmula:

\[ x_{n+1} = x_n - [J(x_n)]^{-1} \cdot F(x_n) \]

Donde \( x_n \) es la solución en la n-ésima iteración. Este proceso se repite hasta que se alcanza una solución aceptable, es decir, hasta que \( ||F(x_n)|| \) es lo suficientemente pequeño.

Pregunta 9)Ver .py

Pregunta 10)
El método de Newton para sistemas converge a un punto \( \xi \in \mathbb{R}^n \) tal que \( F(\xi) = 0 \) bajo las siguientes condiciones:

1. **Continuidad de \( F \)**: La función \( F : \mathbb{R}^n \rightarrow \mathbb{R}^n \) debe ser continua en un vecindario alrededor del punto \( x_0 \).

2. **Diferenciabilidad de \( F \)**: La función \( F \) debe ser diferenciable en el vecindario alrededor de \( x_0 \).

3. **Invertibilidad de \( J(x) \)**: La matriz jacobiana \( J(x) \) de \( F \) en el punto \( x \) debe ser invertible en el vecindario alrededor de \( x_0 \).

4. **Condiciones iniciales cercanas a la solución**: El punto inicial \( x_0 \) debe estar lo suficientemente cerca de la solución \( \xi \) para que el método de Newton pueda converger.

Bajo estas condiciones, el teorema del método de Newton establece que si \( x_0 \) está lo suficientemente cerca de la solución \( \xi \), entonces el método de Newton converge a \( \xi \) con al menos una tasa cuadrática de convergencia. Esto significa que el error en la solución se reduce al cuadrado en cada iteración, siempre y cuando se cumplan las condiciones de continuidad, diferenciabilidad e invertibilidad mencionadas anteriormente.

Pregunta Secreta)
El desarrollo en serie de Taylor de \( F(x + h) \) alrededor del punto \( x \) para una función \( F : \mathbb{R}^n \rightarrow \mathbb{R}^n \) se puede expresar como:

\[ F(x + h) = F(x) + J(x) \cdot h + \frac{1}{2!} H(x) \cdot h \cdot h + \cdots \]

Donde:
- \( F(x) \) es la función vectorial evaluada en \( x \).
- \( J(x) \) es la matriz jacobiana de \( F \) evaluada en \( x \), es decir, \( J(x) = \frac{\partial F}{\partial x} \).
- \( H(x) \) es el tensor hessiano de \( F \) evaluado en \( x \), es decir, \( H(x) = \frac{\partial^2 F}{\partial x^2} \).
- \( h \) es un vector pequeño que representa un cambio en \( x \).

Este desarrollo en serie de Taylor proporciona una aproximación de \( F(x + h) \) alrededor del punto \( x \) en términos de los valores de \( F(x) \), \( J(x) \) y \( H(x) \). Dependiendo de la precisión deseada, se pueden considerar más términos del desarrollo en serie de Taylor, pero en la práctica, a menudo se trabaja con una aproximación lineal utilizando solo el término de primer orden \( F(x) + J(x) \cdot h \).

Pregunta 11)
a) **Descripción de las variantes del método de Newton para sistemas**:

1. **Newton Amortiguado**:
   - En el método de Newton amortiguado, se introduce un parámetro de amortiguamiento (a menudo denotado como \( \alpha \)) que controla el tamaño del paso que se toma en cada iteración. En lugar de tomar el paso completo calculado por el método de Newton estándar, se toma un paso reducido multiplicado por \( \alpha \). Este parámetro puede ser constante o variable, y se ajusta para evitar pasos excesivamente grandes que puedan llevar a divergencia.
   
2. **Variante de Whittaker**:
   - La variante de Whittaker, también conocida como el método de Newton modificado o el método de Newton relajado, es una modificación del método de Newton que introduce un término de relajación para controlar la convergencia. En lugar de actualizar directamente \( x \) con el paso calculado por el método de Newton, se agrega un término de relajación que reduce el tamaño del paso. Este término de relajación ayuda a garantizar la convergencia en casos donde el método de Newton estándar puede ser inestable o divergente.

b) **Problema que busca resolver cada una**:

1. **Newton Amortiguado**:
   - El método de Newton amortiguado busca resolver problemas de divergencia o inestabilidad que pueden surgir en el método de Newton estándar cuando se toman pasos excesivamente grandes. Introduciendo el parámetro de amortiguamiento \( \alpha \), se controla la magnitud de los pasos tomados en cada iteración, lo que ayuda a garantizar la convergencia del método incluso en situaciones donde el método de Newton estándar podría fallar.

2. **Variante de Whittaker**:
   - La variante de Whittaker busca resolver problemas de convergencia en el método de Newton estándar, especialmente en casos donde la función \( F(x) \) puede ser altamente no lineal o donde pueden surgir condiciones de mal condicionamiento. Al introducir un término de relajación, se ralentiza la velocidad de convergencia del método de Newton, lo que puede ayudar a evitar oscilaciones o divergencia y mejorar la estabilidad del algoritmo.

VPregunta 12)
a) En el método de bisección, las dos formas de calcular el punto medio del intervalo \( p_n \) son matemáticamente equivalentes, pero desde el punto de vista numérico, es preferible la primera expresión \( p_n = \frac{a_n + b_n}{2} \). Esto se debe a que en esta expresión se realiza una suma y una división, operaciones numéricamente estables que minimizan los errores de redondeo. En cambio, la segunda expresión \( p_n = a_n + \frac{b_n - a_n}{2} \) implica primero una resta seguida de una división, lo que podría introducir errores de cancelación y pérdida de precisión numérica, especialmente cuando \( a_n \) y \( b_n \) son valores muy cercanos entre sí.

b) En el método de la secante, las dos formas equivalentes de calcular el siguiente punto son:
- \( p_{n+1} = \frac{a_n \cdot f(b_n) - b_n \cdot f(a_n)}{f(b_n) - f(a_n)} \)
- \( p_{n+1} = a_n - \frac{(b_n - a_n) \cdot f(a_n)}{f(b_n) - f(a_n)} \)

La segunda forma es numéricamente superior a la primera. Esto se debe a que en la segunda expresión, el término \( (b_n - a_n) \cdot f(a_n) \) es menos propenso a errores de cancelación que en la primera expresión, donde este término se encuentra en el numerador. Por lo tanto, la segunda expresión tiende a ser más estable numéricamente y menos susceptible a la pérdida de precisión debido a la cancelación de cifras significativas.

Pregunta 13)Para cada uno de los métodos mencionados:

a) El error absoluto en el paso i-ésimo del algoritmo se puede definir como la diferencia absoluta entre la aproximación actual y el valor verdadero del cero de la función.

b) El error relativo en el paso i-ésimo del algoritmo se puede definir como el error absoluto dividido por el valor verdadero del cero de la función, todo esto multiplicado por 100 para expresarlo como un porcentaje.

c) Los errores absoluto y relativo se pueden estimar comparando la aproximación actual con la anterior. El error absoluto se calcula como la diferencia entre la aproximación actual y la anterior, mientras que el error relativo se calcula como la división del error absoluto entre la aproximación actual.

d) La convergencia del algoritmo hacia un cero de la función se puede asegurar bajo ciertas condiciones, como la continuidad de la función en el intervalo considerado, la existencia de un cambio de signo en la función dentro del intervalo inicial para el método de la bisección, la existencia de la derivada en el intervalo y que la derivada no sea cero en el método de Newton-Raphson, y condiciones similares para los otros métodos. Además, la convergencia puede depender de la elección adecuada de los parámetros iniciales y la función de iteración en los métodos iterativos como el de la secante y el de punto fijo.

Pregunta 14)
**a) Demuestre que en cada paso del algoritmo se agrega una cifra significativa correcta binaria:**

En cada iteración del algoritmo de bisección, el intervalo [a, b] se divide por la mitad. Esto significa que el número de bits necesarios para representar la longitud del intervalo se reduce a la mitad en cada paso. Como resultado, en cada iteración se agrega una cifra significativa correcta binaria al intervalo, ya que se está refinando la aproximación al cero de la función.

**b) ¿En una computadora que use el formato “double” del estándar 754 de la IEEE, ¿cuál es el número máximo de iteraciones que tiene sentido hacer?**

En el estándar IEEE 754 de doble precisión, un número "double" utiliza 64 bits para representar el número. Dado que en cada iteración del algoritmo de bisección se agrega una cifra significativa correcta binaria, el número máximo de iteraciones tendría sentido sería 64 (ya que no tendría sentido seguir dividiendo el intervalo más allá de la precisión del número double).

**c) Dado un error absoluto ε, determine cuántas iteraciones debe realizar el algoritmo para hallar una solución que tenga un error absoluto menor que ε, si se comienza con el intervalo [a0, b0].**

El número de iteraciones necesarias para alcanzar un error absoluto menor que ε se puede calcular utilizando la fórmula:

\[ \text{Número de iteraciones} = \frac{\log_2 \left(\frac{b_0 - a_0}{\epsilon}\right)}{\log_2(2)} \]

Donde \( b_0 - a_0 \) es la longitud del intervalo inicial y \( \epsilon \) es el error absoluto deseado.

**d) Dado un número entero r, determine cuántas iteraciones debe hacer el algoritmo para encontrar una solución con r cifras significativas correctas.**

El número de iteraciones necesarias para alcanzar r cifras significativas correctas se puede calcular utilizando la fórmula:

\[ \text{Número de iteraciones} = \lceil \log_2 \left(\frac{b_0 - a_0}{10^{-r}}\right) \rceil \]

Donde \( \lceil x \rceil \) es la función techo, que redondea hacia arriba al número entero más cercano.

Pregunta 15)
**a) Resolución utilizando una iteración de punto fijo:**

Para resolver las ecuaciones no lineales dadas utilizando el método de punto fijo, primero necesitamos reorganizarlas en la forma \(x = g(x)\).

Para la primera ecuación: \(e^{-x} + 1 - x^2 = 0\), podemos despejar \(x\) como \(x = e^{-x} + 1\).

Para la segunda ecuación: \(e^x - 4x^2 = 0\), podemos despejar \(x\) como \(x = \sqrt{e^x/4}\).

Ahora podemos elegir una función \(g(x)\) para cada ecuación y usar el método de punto fijo para iterar hasta converger a la solución.

**b) Función \(g(x)\) y intervalo [a, b] para asegurar la convergencia:**

Para la primera ecuación: \(x = e^{-x} + 1\), podemos elegir \(g(x) = e^{-x} + 1\) y el intervalo [0, 2], ya que la función \(g(x)\) es creciente en este intervalo y \(g(x)\) se mantiene dentro del intervalo [0, 2] para \(x \in [0, 2]\).

Para la segunda ecuación: \(x = \sqrt{e^x/4}\), podemos elegir \(g(x) = \sqrt{e^x/4}\) y el intervalo [0, 2], ya que la función \(g(x)\) es creciente en este intervalo y \(g(x)\) se mantiene dentro del intervalo [0, 2] para \(x \in [0, 2]\).

Por lo tanto, con estas elecciones de función \(g(x)\) y intervalo [a, b], podemos asegurar la convergencia al cero de la función utilizando la iteración de punto fijo.

PS
Correcto, es importante tener en cuenta que en la práctica, es muy raro (si no imposible) conocer el valor exacto de los errores absoluto y relativo al encontrar el cero de una función numéricamente. Esto se debe a que generalmente no conocemos la solución exacta de la ecuación y, por lo tanto, no podemos calcular directamente el error absoluto o relativo.

En su lugar, utilizamos métodos numéricos para encontrar una aproximación de la solución. Estas aproximaciones tienen cierto grado de error asociado, que depende de varios factores, como la precisión de los cálculos, la elección del algoritmo, la tolerancia establecida para la convergencia, entre otros.

Por lo tanto, en lugar de intentar calcular los errores absolutos y relativos exactos, nos centramos en controlar y minimizar estos errores dentro de ciertos límites aceptables para obtener una solución lo más precisa posible dadas las limitaciones computacionales y numéricas. Esto se logra estableciendo criterios de convergencia adecuados y ajustando los parámetros del algoritmo según sea necesario.

Pregunta 16)
a) La función de iteración de punto fijo que convergerá más rápido a la solución es aquella cuya derivada en valor absoluto sea menor que 1 en la vecindad de la solución. Esto se debe a que la convergencia en el método de iteración de punto fijo está relacionada con la magnitud de la derivada de la función de iteración en la vecindad de la solución. Si la derivada es menor que 1, la convergencia será más rápida.

b) En la práctica, la teoría puede no cumplirse completamente debido a diversos factores, como errores de redondeo, truncamiento y condiciones iniciales lejanas de la solución. Además, la convergencia rápida en la teoría puede no ser garantía de convergencia rápida en situaciones reales. Por lo tanto, mientras que la teoría proporciona una guía útil, es importante realizar pruebas empíricas para verificar la convergencia en casos específicos.

Pregunta 17)
Para determinar el orden de convergencia y la constante asintótica de cada uno de los algoritmos para buscar ceros de funciones, podemos analizar cada uno por separado:

a) Bisección:
El método de bisección es conocido por su convergencia lineal. El orden de convergencia es 1 y la constante asintótica es 0.5.

Demostración:
Sea \( r \) la raíz de la función y \( x_n \) la aproximación en la iteración \( n \). El método de bisección reduce el intervalo que contiene la raíz a la mitad en cada iteración. Esto implica que el error se reduce a la mitad en cada paso.

Si \( e_n \) es el error en la iteración \( n \), entonces \( e_{n+1} = \frac{1}{2} e_n \).
Entonces, podemos escribir:
\[ \lim_{n \to \infty} \frac{e_{n+1}}{(e_n)^1} = \lim_{n \to \infty} \frac{\frac{1}{2} e_n}{e_n} = \frac{1}{2} \]
Por lo tanto, el orden de convergencia es 1 y la constante asintótica es 0.5.

b) Iteración de punto fijo:
El orden de convergencia de la iteración de punto fijo depende de la derivada de la función de iteración en el punto fijo. Si esta derivada es menor que 1 en valor absoluto, la convergencia es lineal. Si es igual a 1, la convergencia es superlineal. Si es mayor que 1, la convergencia puede ser oscilatoria o divergente.

Demostración:
Sea \( g(x) \) la función de iteración. Si \( r \) es la raíz de \( f(x) \), entonces \( r = g(r) \). Supongamos que \( g(x) \) es continuamente diferenciable en la vecindad de \( r \) y que \( |g'(r)| < 1 \).

Entonces, el error en la iteración \( n+1 \) es \( e_{n+1} = g(r) - g(x_n) \approx g'(r) (x_n - r) \).

Esto implica que \( \lim_{n \to \infty} \frac{e_{n+1}}{(e_n)^1} = |g'(r)| \).

Por lo tanto, el orden de convergencia es 1 y la constante asintótica es \( |g'(r)| \).

c) Método de Newton:
El método de Newton tiene una convergencia cuadrática cuando la raíz es simple y las condiciones iniciales están suficientemente cerca de la raíz.

Demostración:
Supongamos que \( r \) es la raíz de \( f(x) \) y \( x_n \) es la aproximación en la iteración \( n \). Entonces, por la fórmula de Newton, \( x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)} \).

Si \( e_n \) es el error en la iteración \( n \), entonces el error en la iteración \( n+1 \) es \( e_{n+1} = x_{n+1} - r \).
Desarrollando en serie de Taylor alrededor de \( r \), obtenemos:
\[ e_{n+1} \approx \frac{f''(r)}{2f'(r)} (e_n)^2 \]

Por lo tanto, el orden de convergencia es 2 y la constante asintótica es \( \frac{f''(r)}{2f'(r)} \).

Estas son las demostraciones de los órdenes de convergencia y las constantes asintóticas para los tres métodos mencionados.

Pregunta Secreta)

Una función se dice que es continuamente diferenciable en un intervalo si su derivada existe y es continua en todo ese intervalo. Esto implica que la función no solo es diferenciable en cada punto del intervalo, sino que la derivada cambia de manera continua a lo largo de todo el intervalo. En otras palabras, la función tiene una curva suave y sin saltos en el intervalo dado.

Pregunta Secreta)
Pregunta: ¿Cuál es el método más eficiente para encontrar la raíz de una función no lineal en un intervalo dado? 

Respuesta: Uno de los métodos más eficientes es el método de Newton-Raphson. Este método utiliza una aproximación inicial y luego converge rápidamente hacia la raíz de la función mediante sucesivas iteraciones, utilizando la derivada de la función en cada paso para ajustar la aproximación.

Pregunta 18)
Para demostrar que la iteración de punto fijo definida por \( g(x) \) converge para cualquier \( x_0 \) tal que \( |x_0 - \xi| \leq \varepsilon \), donde \( \xi \) es el punto fijo de \( g(x) \), y \( g(x) \) es continuamente diferenciable en algún intervalo abierto que contiene a \( \xi \) con \( |g'(\xi)| < 1 \), podemos usar el teorema del punto fijo y el teorema del valor medio.

Por el teorema del valor medio, sabemos que para cualquier \( x \) en el intervalo \( (x_0, \xi) \), existe \( \xi_x \) tal que:

\[ g(\xi) - g(x) = g'(\xi_x)(\xi - x) \]

Dado que \( |g'(\xi)| < 1 \), podemos elegir \( \delta > 0 \) suficientemente pequeño para que \( |g'(\xi_x)| < 1 \) para todo \( \xi_x \) en el intervalo \( (x_0, \xi) \).

Entonces, para \( x \) en \( (x_0, \xi) \):

\[ |g(\xi) - g(x)| = |g'(\xi_x)| \cdot |\xi - x| < |\xi - x| \]

Esto implica que \( g(x) \) es una contracción en el intervalo \( (x_0, \xi) \).

Ahora, el teorema del punto fijo establece que si \( g(x) \) es una contracción en un intervalo \( [a, b] \), entonces tiene un único punto fijo \( \xi \) en ese intervalo, y la secuencia \( x_{n+1} = g(x_n) \) converge a \( \xi \) para cualquier \( x_0 \) en \( [a, b] \).

Como \( g(x) \) es una contracción en \( (x_0, \xi) \) y \( \xi \) es el punto fijo, la iteración de punto fijo converge para cualquier \( x_0 \) tal que \( |x_0 - \xi| \leq \varepsilon \), donde \( \varepsilon \) es un valor positivo que satisface las condiciones de convergencia.

Pregunta 19)
1. **Canción para el método de Bisección: "Stairway to Heaven" de Led Zeppelin**
   - Justificación: "Stairway to Heaven" es una canción que gradualmente construye una atmósfera y una melodía ascendente, similar al método de bisección que divide iterativamente un intervalo en dos partes iguales hasta encontrar la raíz de una función. Al igual que la canción que progresa paso a paso, el método de bisección avanza de manera lenta pero segura hacia la solución.

2. **Canción para el método de Newton: "Bohemian Rhapsody" de Queen**
   - Justificación: "Bohemian Rhapsody" es una canción que presenta cambios bruscos de ritmo y tonalidad, así como diferentes secciones que se conectan de manera fluida pero no lineal. Esto se asemeja al método de Newton, que utiliza la derivada de la función para encontrar la raíz de manera más rápida y directa, pero puede ser más susceptible a oscilaciones y divergencias si la derivada no es representativa de la función en ciertas regiones. La canción también refleja la naturaleza no lineal y emocionante del método de Newton.

Pregunta 20)

a) Para demostrar que el orden de convergencia de la iteración de punto fijo es 2 cuando \( g'(\xi) = 0 \) y \( g''(\xi) \neq 0 \), primero necesitamos aplicar la definición del orden de convergencia de una iteración de punto fijo. Sea \( e_k = \xi - x_k \), donde \( \xi \) es la solución exacta y \( x_k \) es la aproximación en la k-ésima iteración. Entonces, tenemos:

\[ e_{k+1} = \xi - x_{k+1} = \xi - g(x_k) = g(\xi) - g(x_k) + \frac{g''(\xi)}{2}(\xi - x_k)^2 + O((\xi - x_k)^3) \]

Usando la expansión de Taylor de primer y segundo orden alrededor de \( \xi \), y suponiendo que \( g(\xi) = \xi \) (ya que estamos buscando un punto fijo), y que \( g'(\xi) = 0 \), la expresión se simplifica a:

\[ e_{k+1} = \frac{g''(\xi)}{2}(\xi - x_k)^2 + O((\xi - x_k)^3) \]

Como \( g''(\xi) \neq 0 \), podemos decir que \( e_{k+1} \) es proporcional a \( e_k^2 \), lo que indica un orden de convergencia de 2.

b) Para demostrar que el método de Newton tiene un orden de convergencia de 2 cuando \( f'(\xi) \neq 0 \), podemos usar el resultado del ejercicio anterior. Sabemos que el método de Newton se puede expresar como una iteración de punto fijo \( x_{k+1} = x_k - \frac{f(x_k)}{f'(x_k)} \). Aquí, \( g(x) = x - \frac{f(x)}{f'(x)} \). 

Si derivamos \( g(x) \), obtenemos:

\[ g'(x) = 1 - \frac{f'(x)f'(x) - f(x)f''(x)}{(f'(x))^2} = 1 - \frac{f'(x)}{f'(x)} = 0 \]

Y si derivamos nuevamente:

\[ g''(x) = -\frac{f''(x)f'(x) + (f'(x))^2 - (f'(x))^2 - f(x)f'''(x)}{(f'(x))^2} = -\frac{f''(x)f'(x) - f(x)f'''(x)}{(f'(x))^2} \]

Dado que estamos interesados en \( g'(\xi) = 0 \) y \( g''(\xi) \neq 0 \), lo que es el caso cuando \( f'(\xi) \neq 0 \), podemos aplicar el resultado del ejercicio anterior para concluir que el método de Newton tiene un orden de convergencia de 2.

Pregunta 21)
Para demostrar las cotas de error, primero necesitamos las siguientes condiciones:

1. Supongamos que \( g(x) \) es diferenciable en un intervalo que contiene a \( \xi \), el punto fijo de la iteración \( x_{n+1} = g(x_n) \).
2. Existe una constante \( K \) tal que \( |g'(x)| \leq K \) para todo \( x \) en el intervalo que contiene a \( \xi \).
3. \( g(\xi) = \xi \), lo que significa que \( \xi \) es un punto fijo de \( g(x) \).

a) Para la cota \( |e_n| = |\xi - x_n| \leq \frac{K^n}{1-K}|x_1 - x_0| \), usamos el Teorema del Valor Medio en el intervalo \( [x_n, \xi] \):

\[ |e_n| = |\xi - x_n| = |g(\xi) - g(x_n)| = |g'(\xi^*)||\xi - x_n| \leq K|\xi - x_n| \]

Entonces, \( |e_n| \leq K|e_{n-1}| \leq \dots \leq K^n |x_1 - x_0| \). Por lo tanto, \( |e_n| \leq \frac{K^n}{1-K}|x_1 - x_0| \).

b) Para la cota \( |e_n| = |\xi - x_n| \leq \frac{K}{1 - K}|x_{n} - x_{n-1}| \), usamos el Teorema del Valor Medio en el intervalo \( [x_n, x_{n-1}] \):

\[ |e_n| = |\xi - x_n| = |g(\xi) - g(x_{n-1})| = |g'(\xi^*)||\xi - x_{n-1}| \leq K|\xi - x_{n-1}| \]

Entonces, \( |e_n| \leq K|e_{n-1}| \leq \dots \leq K^n |x_1 - x_0| \). Por lo tanto, \( |e_n| \leq \frac{K}{1 - K}|x_{n} - x_{n-1}| \).

c) El menor valor de \( K \) para el que se cumplen las cotas es aquel que garantiza la convergencia de la iteración de punto fijo. Para que la iteración converja, necesitamos que \( |g'(\xi)| < 1 \). Por lo tanto, el menor valor de \( K \) se obtiene cuando \( K = |g'(\xi)| \).

Pregunta 22)
a) El algoritmo más eficiente para encontrar todas las raíces de un polinomio con coeficientes reales es el método de Durand-Kerner. Este método es iterativo y utiliza la fórmula de recurrencia para calcular las raíces del polinomio. Es eficiente tanto desde el punto de vista algorítmico como numérico, ya que converge rápidamente a las raíces del polinomio.

b) Sí, tiene sentido preguntar por el orden de convergencia del método de Durand-Kerner. Este método tiene un orden de convergencia lineal. El orden de convergencia de un algoritmo es importante porque nos dice qué tan rápido se acerca a la solución exacta a medida que aumenta el número de iteraciones. En el caso del método de Durand-Kerner, su orden de convergencia lineal significa que la cantidad de dígitos correctos en la aproximación de la raíz se duplica en cada iteración.

Pregunta 23)
a) Un método para hallar el cero de una función no lineal con un orden de convergencia mayor estricto que 2 es el método de Halley. Este método es una extensión del método de Newton y utiliza la segunda y tercera derivada de la función para mejorar la convergencia. La fórmula de recurrencia para el método de Halley es:

\[ x_{n+1} = x_n - \frac{2f(x_n)f'(x_n)}{2[f'(x_n)]^2 - f(x_n)f''(x_n)} \]

b) Para demostrar que el orden de convergencia del método de Halley es mayor estricto que 2, podemos calcular la secuencia de errores \( e_{n+1} \) en términos de \( e_n \) utilizando la definición del orden de convergencia. Luego, podemos mostrar que el límite de \( \frac{e_{n+1}}{(e_n)^p} \) donde \( p \) es el orden de convergencia, es menor que cero, lo que indica que el orden de convergencia es mayor estricto que 2.

c)Ver .py

d) Para mostrar las ventajas del método de Halley sobre otros métodos con un menor orden de convergencia, podemos comparar el número de iteraciones necesarias para alcanzar una cierta tolerancia en la solución. En general, el método de Halley debería converger más rápido que métodos con un orden de convergencia menor, como el método de Newton.

e) Podemos realizar pruebas comparativas entre el método de Halley y otros métodos como el método de Newton o el método de la secante, utilizando diversas funciones de prueba y observando el número de iteraciones necesarias para alcanzar una cierta precisión. Esto demostrará empíricamente las ventajas del método de Halley en términos de eficiencia de convergencia.
