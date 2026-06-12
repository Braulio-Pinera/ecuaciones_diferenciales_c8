# Aproximación de una Ecuación Diferencial con el Método de Euler

## Problema

Se resuelve la ecuación diferencial ordinaria:

dy/dt = y,  con condición inicial y(0)=1

Primero se obtiene la solución analítica mediante separación de variables, y posteriormente se aproxima la solución usando el método numérico de Euler en el intervalo [0,1] con paso h = 0.2.

## Solución analítica

Separando variables:

dy/y = dt

Integrando:

ln(y) = t + C

Aplicando la condición inicial:

y(t) = e^t

## Método numérico (Euler)

La aproximación se realiza con la fórmula:

y_{n+1} = y_n + h y_n

## Resultados

Se comparan los valores obtenidos por el método de Euler con la solución exacta y se grafica la diferencia.

## Tecnologías usadas

- Python
- NumPy
- Matplotlib

## Ejecución

Instalar dependencias:
