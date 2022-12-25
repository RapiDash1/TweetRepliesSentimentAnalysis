import json

class EnvHandler:

    handler = None
    env = None

    def __init__(self):
        raise SystemError("Cannot instantiate a singelton using its constructor, please use instance method")

    @classmethod
    def instance(cls):
        if cls.handler == None:
            cls.handler = cls.__new__(cls)
            with open("env.json") as envFile:
                cls.handler.env = json.load(envFile)
        
        return cls.handler

        
    def getValue(self, key):
        if key in self.env:
            return self.env[key]

        raise KeyError("{key} not present in environment variables")