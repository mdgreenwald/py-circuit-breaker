![test](https://github.com/mdgreenwald/py-circuit-breaker/workflows/PyTest/badge.svg)

# py-circuit-breaker
*Python Circuit Breaker Library*

## Usage ##

Call the CircuitBreaker logic using a `@CircuitBreaker` decorator.

```python
@CircuitBreaker(http_client, error_threshold, time_window)
def http_request(host, port):
  conn = http.client.HTTPConnection(host, port)
  conn.request("GET", "/")
  response = conn.getresponse()
  print(response.status, response.reason)
```
When the underlying function raises an exception, CircuitBreaker opens the circuit for the duration of the `time_window`.

## Execution ##

**Note**: *Requires docker or a running instance of nginx at `localhost:8080` that can be terminated and restarted easily.*

```bash
docker-compose up -d
python3 py_circuit_breaker/py_circuit_breaker.py

#From another terminal:
docker exec -it nginx /bin/sh -c 'kill 1'
```

### Example Execution ###

```bash
% python3 py_circuit_breaker/py_circuit_breaker.py
200 OK
200 OK
200 OK
200 OK
[Errno 61] Connection refused
[Errno 61] Connection refused
CircuitOpenError: Circuit open for 5 seconds.
200 OK
200 OK
200 OK
200 OK
```

## Tests ##

```bash
python3 setup.py pytest
```

## References ##
1. [https://martinfowler.com/bliki/CircuitBreaker.html](https://martinfowler.com/bliki/CircuitBreaker.html)
