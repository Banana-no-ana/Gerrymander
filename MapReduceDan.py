class MapReduceDan:
    def __init__(self):
        self.intermediate = {}
        self.result = []

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value)

    def execute(self, data, mapper, reducer, final):
        for key in data:
            mapper(key)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        final()
	return self.result

    def reset(self):
	self.intermediate = {}
	self.result = []
