from robot.running import TestSuiteBuilder

suite = TestSuiteBuilder().build("./google_search.robot")
result = suite.run()

