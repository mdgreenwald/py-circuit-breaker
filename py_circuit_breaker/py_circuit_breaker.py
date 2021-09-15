import time
import datetime
import http.client

class CircuitBreaker(object):

    def __init__(self, http_client, error_threshold, time_window):
        self.http_client = http_client
        self.error_threshold = error_threshold
        self.time_window = time_window
        self.error_count = 0
        self.last_error_time = None
        self.state = 'closed'

    def __call__(self, f):
        def wrapped_f(*args):
            if self.state == 'open':
                print("CircuitOpenError: Circuit open for {0} seconds.".format(self.time_window))
                time.sleep(time_window)
                self.state = 'closed'

            try:
                f(*args)
            
            except Exception as e:
                print(e)
                self.error()

        return wrapped_f

    def error(self):
        self.error_count += 1
        if self.error_count >= self.error_threshold:
            self.last_error_time = datetime.datetime.utcnow()
            self.state = 'open'

    def success(self):
        self.state = 'closed'
        self._failure_count = 0
        self.last_error_time = None

http_client = None
error_threshold = 2
time_window = 5
host = "localhost"
port = 8080

@CircuitBreaker(http_client, error_threshold, time_window)
def http_request(host, port):
  conn = http.client.HTTPConnection(host, port)
  conn.request("GET", "/")
  response = conn.getresponse()
  print(response.status, response.reason)

if __name__ == "__main__":
    while True:
        time.sleep(0.25)
        http_request(host, port)