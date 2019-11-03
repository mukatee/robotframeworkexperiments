__author__ = 'teemu kanstren'

from robot.running import TestSuiteBuilder
from robot.api import ResultWriter

#https://robot-framework.readthedocs.io/en/3.0/autodoc/robot.running.html
suite = TestSuiteBuilder().build("./hello.robot")
result = suite.run(output="test_output.xml")
#ResultWriter(result).write_results(report='report.html', log="log.html")
ResultWriter("test_output.xml").write_results(report='report.html', log="log.html")

