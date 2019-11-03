__author__ = 'teemu kanstren'

from robot.running import TestSuiteBuilder
from robot.api import ResultWriter
from io import StringIO

#https://robot-framework.readthedocs.io/en/3.0/autodoc/robot.running.html
suite = TestSuiteBuilder().build("./include.robot")
stdout = StringIO()
result = suite.run(output="test_output.xml", include="*crit", stdout=stdout)
ResultWriter("test_output.xml").write_results(report='report.html', log="log.html")
output = stdout.getvalue()
print(output)
