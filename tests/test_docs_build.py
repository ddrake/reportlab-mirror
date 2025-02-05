__version__ = '3.3.0'
"""Tests that all manuals can be built.
"""
from reportlab.lib.testutils import (setOutDir, SecureTestCase, printLocation)
import os
import sys
import unittest

setOutDir(__name__)


class ManualTestCase(SecureTestCase):
    "Runs all 3 manual-builders from the top."

    def test0(self):
        "Test if all manuals buildable from source."
        from reportlab.lib.testutils import testsFolder
        try:
            docsFolder = os.path.join(os.path.dirname(testsFolder), 'docs')
        except Exception:
            print(testsFolder)
            raise
        cwd = os.getcwd()
        os.chdir(docsFolder)
        try:
            if os.path.isfile('reportlab-userguide.pdf'):
                os.remove('reportlab-userguide.pdf')
            # if os.path.isfile('reportlab-reference.pdf'):
            #    os.remove('reportlab-reference.pdf')

            os.system('"%s" genAll.py -s' % sys.executable)

            assert os.path.isfile('reportlab-userguide.pdf'), (
                'genAll.py failed to generate reportlab-userguide.pdf!')
            # assert os.path.isfile('reportlab-reference.pdf'), (
            #   'genAll.py failed to generate reportlab-reference.pdf!'
        finally:
            os.chdir(cwd)


def makeSuite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(ManualTestCase))
    return suite


# noruntests
if __name__ == "__main__":
    unittest.TextTestRunner().run(makeSuite())
    printLocation()
