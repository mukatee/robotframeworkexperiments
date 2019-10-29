__author__ = 'teemu kanstren'

from robot.running import TestSuiteBuilder
from robot.api import ResultWriter
from io import StringIO

#https://robot-framework.readthedocs.io/en/3.0/autodoc/robot.running.html
suite = TestSuiteBuilder().build("./include.robot")
#this tag does not exist in the given suite, so no critical tests should be listed in report
stdout = StringIO()
result = suite.run(include="*crit", stdout=stdout)
ResultWriter(result).write_results(report='report.html', log="log.html")
output = stdout.getvalue()
print(output)
