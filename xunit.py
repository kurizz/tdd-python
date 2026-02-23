class WasRun:

    def __init__(self, name):
        self.wasRun = None

    def testMethod(self):
        self.wasRun = 1


test = WasRun("testMeshod")
print(test.wasRun)
test.testMethod()
print(test.wasRun)

print("---8<---8<---8<---")
