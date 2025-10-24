# Microservicio Factorial

Este microservicio fue hecho con **Flask** y permite calcular el **factorial de un número** recibido por la URL.  
Devuelve una respuesta en formato **JSON** con:

- El número recibido  
- Su factorial  
- Si el factorial es par o impar  

---

## Cómo funciona

La ruta principal del servicio es:

```
/fact/<n>
```

Por ejemplo, si entramos a:

```
http://127.0.0.1:5000/fact/5
```

el servicio responde:

```json
{
  "input": 5,
  "factorial": "120",
  "paridad_factorial": "par"
}
```

Si probamos con 0 o 1, el resultado será "impar".

---

## Cómo ejecutarlo

1. Instalar las dependencias:
   ```
   pip install flask
   ```

2. Ejecutar el programa:
   ```
   python Factorial.py
   ```

3. Abrir en el navegador:
   ```
   http://127.0.0.1:5000/fact/5
   ```

---

## Ejemplo rápido

| Entrada | Resultado JSON |
|----------|----------------|
| `/fact/0` | {"input": 0, "factorial": "1", "paridad_factorial": "impar"} |
| `/fact/1` | {"input": 1, "factorial": "1", "paridad_factorial": "impar"} |
| `/fact/4` | {"input": 4, "factorial": "24", "paridad_factorial": "par"} |

---

## Análisis

Si este microservicio tuviera que conectarse con otro servicio que **guarde el historial de cálculos en una base de datos externa**,  
se podrían hacer algunos cambios en el diseño:

- Agregar una **variable de entorno** con la URL del otro servicio (por ejemplo `HISTORY_URL`).  
- Luego, después de calcular el factorial, mandar una petición HTTP `POST` con los datos al otro servicio.  
  Esto se puede hacer con la librería `requests`.

Ejemplo de cómo se podría enviar:

```python
import requests

data = {
  "input": n,
  "factorial": str(fact),
  "paridad": parity
}
requests.post("http://history-service/historial", json=data)
```

También se podría usar un sistema de mensajería como RabbitMQ o Redis si se quisiera guardar el historial sin afectar el tiempo de respuesta del usuario.  
Así el microservicio seguiría funcionando rápido, aunque el otro servicio esté ocupado o lento.

---

#
