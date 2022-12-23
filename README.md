# U02_DS_RestfulCommunication

El objetivo de esta práctica era realizar una simulación de una comunicacion asíncrona entre agentes con el objetivo de que acordar una mayoría en la elección de un número aleatorio.

**-Nota.** En el enunciado indica que teniamos que implementar 3 agentes y que cada uno generara un numero aleatorio hasta conseguir que dos de ellos coincidieran deteniendo el proceso, yo me he equivocado y lo he hecho para que se detenga el proceso cuando todos generan el mismo número.

Los intercambios de información entre los agentes se han realizado a través de un servidor web generado con la librería Flask, este es el encargado de procesar los datos que le llegan de los agentes y los agentes solamente generan números aleatorios que postean y preguntan al servidor web por medio de peticiones si los valores coinciden y si tiene que seguir enviando números aleatorios

**Funcionamiento**. Los agentes son un mismo programa server.py ejecutado en 3 terminales diferentes, para que el programa funcione primero hay que ejecutar con flask app.py ya que es el servidor web donde se realizan las peticiones. Primero de todo el agente pide que le asigne un id al servidor web para poder identificarse cuando suba un número aleatorio, el agente de manera indefinida pide al servidor web si tiene que enviar un nuevo aleatorio, si es que sí genera otro aleatorio y si es que no el agente avisa al servidor web que termina el proceso y acaba.
