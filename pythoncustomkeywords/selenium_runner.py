from robot.running import TestSuiteBuilder
import robot

#result = robot.run("./search_flights.robot")
#print(result)

#https://robot-framework.readthedocs.io/en/3.0/autodoc/robot.running.html
suite = TestSuiteBuilder().build("./google_search.robot")
result = suite.run()

