import unittest
# import re
# import codecs
from reportlab.pdfbase import pdfdoc
from reportlab import rl_config
from reportlab.lib.testutils import (setOutDir, makeSuiteForClasses, printLocation,
                                     NearTestCase)
# from reportlab.lib.testutils import outputfile

setOutDir(__name__)


class PdfdocTestCase(NearTestCase):
    """Tests of expected Unicode and encoding behaviour
    """
    def setUp(self):
        self.pdfMultiLine = rl_config.pdfMultiLine
        self.pdfComments = rl_config.pdfComments
        rl_config.pdfMultiLine = 0
        rl_config.pdfComments = 0

    def tearDown(self):
        rl_config.pdfMultiLine = self.pdfMultiLine
        rl_config.pdfComments = self.pdfComments

    def testPDFText(self):
        self.assertEqual(pdfdoc.PDFText(b'Hello World').format(self.doc),
                         b'<48656c6c6f20576f726c64>')

    def testPDFString(self):
        self.assertEqual(pdfdoc.PDFString(b'Hello World').format(self.doc),
                         b'(Hello World)')
        self.assertEqual(pdfdoc.PDFString(b'Hello\xc2\xa2World', 0).format(self.doc),
                         b'(Hello\xa2World)')
        self.assertEqual(
            pdfdoc.PDFString(b'Hello\xc2\xa0World', 0).format(self.doc),
            b'(\xfe\xff\x00H\x00e\x00l\x00l\x00o\x00\xa0\x00W\x00o\x00r\x00l\x00d)')
        self.assertEqual(
            pdfdoc.PDFString(b'Hello\xc2\xa0World', 1).format(self.doc),
            b'(\\376\\377\\000H\\000e\\000l\\000l\\000o\\000\\240\\000W\\000o\\000r\\000l\\000d)')  # noqa
        self.assertEqual(
            pdfdoc.PDFString(u'Hello\xa0World'.encode('utf8'), 1).format(self.doc),
            b'(\\376\\377\\000H\\000e\\000l\\000l\\000o\\000\\240\\000W\\000o\\000r\\000l\\000d)')  # noqa
        self.assertEqual(
            pdfdoc.PDFString(u'Hello\xa0World'.encode('utf8'), 0).format(self.doc),
            b'(\xfe\xff\x00H\x00e\x00l\x00l\x00o\x00\xa0\x00W\x00o\x00r\x00l\x00d)')

    def testPDFArray(self):
        self.assertEqual(pdfdoc.PDFArray([1, 2, 3, 4]).format(self.doc),
                         b'[ 1 2 3 4 ]')

    def testPDFIndirectObject(self):
        doc = self.doc
        doc.Reference(pdfdoc.PDFArray([0, 1, 2, 3]),
                      pdfdoc.PDFName('abracadabra')[1:])
        self.assertEqual(pdfdoc.PDFIndirectObject(
            'abracadabra', pdfdoc.PDFArray([3, 2, 1, 0])).format(doc),
            b'2 0 obj\n[ 3 2 1 0 ]\nendobj\n')

    def testPDFDictionary(self):
        self.assertEqual(
            pdfdoc.PDFDictionary(dict(A=pdfdoc.PDFArray([1, 2, 3, 4])))
            .format(self.doc), b'<<\n/A [ 1 2 3 4 ]\n>>')

    def testPDFPageLabels(self):
        doc = self.doc
        PL = pdfdoc.PDFPageLabels()
        PL.addPageLabel(0, pdfdoc.PDFPageLabel('D', 0, 'AA'))
        self.assertEqual(PL.format(doc), b'<<\n/Nums [ 0 2 0 R ]\n>>')

    @property
    def doc(self):
        return pdfdoc.PDFDocument()


def makeSuite():
    return makeSuiteForClasses(
        PdfdocTestCase,
        )


# noruntests
if __name__ == "__main__":
    unittest.TextTestRunner().run(makeSuite())
    printLocation()
