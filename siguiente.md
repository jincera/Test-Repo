# Fuentes de Información

## Examen parcial - Sección práctica

#### Mayo, 2020

### 1. Hadoop

Conéctese a nuestro servidor de Hadoop.  En la carpeta `/home/jincera/MaterialExParcial` encontrará el archivo `u2.data`.  Es un archivo con 100,000 evaluaciones de películas de cine.

1. Cree una nueva carpeta en su directorio local llamada ExParcial.
2. **Cambie los permisos para que sólo usted pueda accederla** (`chmod 700 ExParcial`)
3. Ingrese a esa carpeta y copie el archivo `u2.data`.

Cada registro tiene cuatro campos: 

* El identificador del evaluador

* El identificador de la película

* La evaluación

* El momento en que se hizo la evaluación

  

Con código que utilice **el paradigma MapReduce** y que se ejecute **en HDFS** (no puede limitar su respuesta a la ejecución con pipes de Unix), responda a las siguientes preguntas:

*  ¿Cuántos evaluadores hay?
* ¿Cuántas películas fueron evaluadas?

Trate de que el segundo resultado se ejecute con dos tareas Reduce. Verifique que se incluyeron todos los registros (deben sumar 100,000).

Puede reutilizar las plantillas EjMapper y EjReducer con las que ha trabajado en las prácticas anteriores.

**Envíe sus resultados a jincera@itam.mx y deje su código en la carpeta `ExParcial`. El profesor lo revisará posteriormente**.

### 2. Pig


Mediante un script de Pig identifique:

* ¿Cuál es el promedio de evaluación de cada película? Debe guardar el resultado en un archivo sólo con los campos del identificador de la película y de su evaluación promedio.
* ¿Cuáles son los diez evaluadores que califican peor las películas?  

**Envíe sus resultados y las líneas de su script a jincera@itam.mx**



#### Pregunta opcional.

(*Sólo haga este ejercicio si le sobra tiempo, lo desea o si la quiere utlizar como rescate para tener puntos adicionales*).

El archivo `u2.item` en la carpeta `/home/jincera/MaterialExParcial`  tiene los nombres de las películas. Está formado por tres campos:

* El identificador de la película
* El nombre de la película
* La fecha de publicación

Con ayuda de Pig haga un script para identificar:

* Cuáles son las diez películas mejor evaluadas y qué promedio tuvo cada una de ellas.  Debe responder a esta pregunta con el nombre de las películas
* Quiénes son los tres evaluadores que evaluaron más películas. Cuántas evaluó cada uno de esos tres evaluadores.

### 3. Fiware

En nuestro Orion Context Broker se han registrado instancias de entidades que simulan estaciones para renta de bicicletas (como las EcoBicis).  su tipo es `BikeHireDockingStation`.  Se ha registrado una estación con las siglas de su nombre y apellido. Por ejemplo, hay una estación con el identificador EstacionAA para Alexis Arroyo.

1. Identifique qué atributos y qué valores tiene su entidad
2. Identifique todas las entidades que tienen más de 15 bicicletas disponibles
3. Modifique el nombre de la compañía que administra la estación.

**POR FAVOR NO MODIFIQUE LOS ATRIBUTOS DE NÚMERO DE BICLETAS Y SLOTS LIBRES PARA NO AFECTAR A SUS COMPAÑEROS**



**Envíe el resultado obtenido y el URL con que hizo la consulta en cada caso a jincera@itam.mx**.  No es necesario que envíe capturas de pantalla.

