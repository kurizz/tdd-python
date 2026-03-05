class TestResult:
    """Testing Framework: 実行結果をどう保持するかを定義"""

    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount = self.runCount + 1

    def testFailed(self):
        self.errorCount = self.errorCount + 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.errorCount)


class TestCase:
    """Testing Framework: テストの実行順序を制御"""

    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        result = TestResult()
        result.testStarted()
        try:
            self.setUp()
            method = getattr(self, self.name)
            method()
        except Exception:
            result.testFailed()
        self.tearDown()
        return result


class WasRun(TestCase):
    """TestCaseTest 検証用のダミー。テストダブル (Spy, Stub) の役割"""

    def setUp(self):
        self.log = "setUp "
        if self.name == "testBrokenSetup":
            raise Exception

    def testMethod(self):
        self.log = self.log + "testMethod "

    def testBrokenMethod(self):
        raise Exception

    def tearDown(self):
        self.log = self.log + "tearDown "


class TestCaseTest(TestCase):

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert "setUp testMethod tearDown " == test.log

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert "1 run, 1 failed" == result.summary()

    def testFailedSetup(self):
        test = WasRun("testBrokenSetup")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()


print(TestCaseTest("testTemplateMethod").run().summary())
print(TestCaseTest("testResult").run().summary())
print(TestCaseTest("testFailedResult").run().summary())
print(TestCaseTest("testFailedResultFormatting").run().summary())
print(TestCaseTest("testFailedSetup").run().summary())
