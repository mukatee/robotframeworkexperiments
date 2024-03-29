__author__ = 'teemu kanstren'

from robot.running import TestSuiteBuilder
from robot.api import ResultWriter

#https://robot-framework.readthedocs.io/en/3.0/autodoc/robot.running.html
suite = TestSuiteBuilder().build("./noncritical.robot")
#this tag does not exist in the given suite, so no critical tests should be listed in report
result = suite.run(noncritical="non")
ResultWriter(result).write_results(report='report.html', log="log.html")
