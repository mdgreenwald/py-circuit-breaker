from py_circuit_breaker import CircuitBreaker

http_client = ' '
time_window = 5
error_threshold = 2

breaker = CircuitBreaker(http_client, error_threshold, time_window)

def test_error(capsys):
    with capsys.disabled():
        assert breaker.state == 'closed'
        breaker.error()
        breaker.error()
        assert breaker.state == 'open'

def test_success(capsys):
    with capsys.disabled():
        assert breaker.state == 'open'
        breaker.success()
        assert breaker.state == 'closed'