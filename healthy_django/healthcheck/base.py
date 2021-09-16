import time
from healthy_django.exceptions import InvalidParams


class HealthCheck:

    name = ""
    title = ""
    description = ""
    health_code_pretty = {200: "All OK", 500: "Down"}

    required_params = []
    params = {}

    def __init__(self, name, **params):
        self.name = name
        for param in self.required_params:
            if param not in params:
                raise InvalidParams("Param {0} is required for checking health".format(param))
        self.params = params

    def check(self):
        raise NotImplemented()

    def health_status(self):
        cur_time = time.time()
        health_code, health_meta = self.check()
        latency = time.time() - cur_time
        return {
            "name": self.name,
            "title": self.title,
            "code": health_code,
            "message": self.health_code_pretty.get(health_code, ""),
            "latency": latency,
            "meta": health_meta,
        }
