__author__ = 'teemu kanstren'

from robot.running import TestSuiteBuilder
from robot.api import ResultWriter

#https://robot-framework.readthedocs.io/en/3.0/autodoc/robot.running.html
suite = TestSuiteBuilder().build("./noncritical.robot")
result = suite.run(noncritical="non-crit")
ResultWriter(result).write_results(report='report.html', log="log.html")
