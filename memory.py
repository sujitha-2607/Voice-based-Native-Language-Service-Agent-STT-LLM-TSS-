class Memory:
    def __init__(self):
        self.data = {
            "intent": None,
            "age": None,
            "education": None,
            "gender": None,
            "applied": None
        }

    def update(self, key, value):
        self.data[key] = value

    def get(self):
        return self.data

    def detect_contradiction(self, key, new_value):
        old = self.data.get(key)
        if old is not None and old != new_value:
            return True
        return False
