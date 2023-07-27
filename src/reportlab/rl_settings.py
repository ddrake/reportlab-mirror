# Copyright ReportLab Europe Ltd. 2000-2017
# see license.txt for license details
'''default settings for reportlab

to override these drop a module rl_local_settings.py parallel to this file or
anywhere on the path.
'''
import os
import sys
__version__ = '3.3.0'
__all__ = tuple('''allowTableBoundsErrors
shapeChecking
defaultEncoding
defaultGraphicsFontName
pageCompression
useA85
defaultPageSize
defaultImageCaching
warnOnMissingFontGlyphs
verbose
showBoundary
emptyTableAction
invariant
eps_preview_transparent
eps_preview
eps_ttf_embed
eps_ttf_embed_uid
overlapAttachedSpace
longTableOptimize
autoConvertEncoding
_FUZZ
wrapA85
fsEncodings
odbc_driver
platypus_link_underline
canvas_basefontname
allowShortTableRows
imageReaderFlags
paraFontSizeHeightOffset
canvas_baseColor
ignoreContainerActions
ttfAsciiReadable
pdfMultiLine
pdfComments
debug
rtlSupport
listWrapOnFakeWidth
T1SearchPath
TTFSearchPath
CMapSearchPath
decimalSymbol
errorOnDuplicatePageLabelPage
autoGenerateMissingTTFName
allowTTFSubsetting
spaceShrinkage
underlineWidth
underlineOffset
underlineGap
strikeWidth
strikeOffset
strikeGap
hyphenationLang
uriWasteReduce
embeddedHyphenation
hyphenationMinWordLength
reserveTTFNotdef
documentLang
encryptionStrength
trustedHosts
trustedSchemes
renderPMBackend
xmlParser
textPaths
toColorCanUse'''.split())

# set to 0 to die on too large elements in tables in debug
# (recommend 1 for production use)
allowTableBoundsErrors = 1
shapeChecking = 1
# 'WinAnsi' or 'MacRoman'
defaultEncoding = 'WinAnsiEncoding'
# initializer for STATE_DEFAULTS in shapes.py
defaultGraphicsFontName = 'Times-Roman'
# default page compression mode
pageCompression = 1
# set to 0 to disable Ascii Base 85 stream filters
useA85 = 1
# default page size
defaultPageSize = 'A4'
# set to zero to remove those annoying cached images
defaultImageCaching = 0
# if 1, warns of each missing glyph
warnOnMissingFontGlyphs = 0
verbose = 0
# turns on and off boundary behaviour in Drawing
showBoundary = 0
# one of 'error', 'indicate', 'ignore'
emptyTableAction = 'error'
# produces repeatable, identical PDFs with same timestamp info (for regression testing)
invariant = 0
# set to white etc
eps_preview_transparent = None
# set to False to disable
eps_preview = 1
# set to False to disable
eps_ttf_embed = 1
# set to 1 to enable
eps_ttf_embed_uid = 0
# if set non false then adajacent flowable space after
# and space before are merged (max space is used).
overlapAttachedSpace = 1
# default do use Henning von Bargen's long table optimizations
longTableOptimize = 1
# convert internally as needed (experimental)
autoConvertEncoding = 0
# fuzz for layout arithmetic
_FUZZ = 1e-6
# set to 1 to get old wrapped line behaviour
wrapA85 = 0
# encodings to attempt utf8 conversion with
fsEncodings = ('utf8', 'cp1252', 'cp430')
# default odbc driver
odbc_driver = 'odbc'
# paragraph links etc underlined if true
platypus_link_underline = 0
# this is used to initialize the canvas; if you override to make
canvas_basefontname = 'Helvetica'
# something else you are responsible for ensuring the font is registered etc etc
# this will be used everywhere and the font family connections will be made
# if the bold/italic/bold italic fonts are also registered and defined as a family.

# allows some rows in a table to be short
allowShortTableRows = 1
# no longer in use
imageReaderFlags = 0
# if true paragraphs start at height-fontSize
paraFontSizeHeightOffset = 1
# initialize the canvas fill and stroke colors if this is set
canvas_baseColor = None
# if true then action flowables in flowable _Containers will be ignored
ignoreContainerActions = 1
# smaller subsets when set to 0
ttfAsciiReadable = 1
# use more lines in pdf etc
pdfMultiLine = 0
# put in pdf comments
pdfComments = 0
# for debugging code
debug = 0
# set to 1 to attempt import of RTL assistance eg fribidi etc etc
rtlSupport = 0

# set to 0/False to force platypus.flowables._listWrapOn to report correct widths
# else it reports minimum(required,available) width
listWrapOnFakeWidth = 1

# empty to use canvas strokeWidth or a distance or number*<letter>
underlineWidth = ''
# num * <letter> make value proportional to a font size
# P paragraph font size
# L line max font size
# f first use font size
# F max fontsize in the tag

# fraction of fontSize from baseline to draw underlines at.
underlineOffset = '-0.125*F'
# gap for double/triple underline
underlineGap = '1'

strikeWidth = ''
# fraction of fontSize from baseline to draw strike through at.
strikeOffset = '0.25*F'
# gap for double/triple strike
strikeGap = '1'

# by default typical value 0.05. may be overridden on a parastyle.
# what we use to align floats numerically
decimalSymbol = '.'
# if True will cause repeated PageLabel page numbers to raise an error.
errorOnDuplicatePageLabelPage = 0
# if true we try to auto generate any missing TTF font name
autoGenerateMissingTTFName = 0

# list of font file names that will be subsetted even when they
# have the no subsetting flag set. These should be fonts for which
# the user has explicit permission from the rights holder(s).
allowTTFSubsetting = []
# This flag could already be overcome by hacking the code.
# ReportLab takes no responsibility for the use of this setting.

# allowable space shrinkage to make lines fit
spaceShrinkage = 0.05
# if pyphen installed set this to the language of your choice
# eg 'en_GB'
hyphenationLang = ''

# split URI if we would waste 0.3 of a line or if the URI#
# would not fit on the next line; if zero then no splitting
# is attempted. suggested value = 0.3
uriWasteReduce = 0
# if true attempt hypenation of words with embedded hyphens
embeddedHyphenation = 0
# minimum length of words that can be hyphenated
hyphenationMinWordLength = 5
# if true force subset element 0 to be zero(.notdef)
# helps to fix bug in edge
reserveTTFNotdef = 0
# pdf document catalog Lang value xx-xx not ee_xx
documentLang = None
# the bits for standard encryption 40, 128 or 256 (AES)
encryptionStrength = 40

# set to a list of trusted for access hosts None means
# all are trusted glob patterns eg *.reportlab.com are
# allowed. In environment use a comma separated string.
trustedHosts = None
# these url schemes are trusted
trustedSchemes = ['file', 'rml', 'data', 'https', 'http', 'ftp']
# or '_renderPM' if available
renderPMBackend = 'rlPyCairo'
# or 'pyrxp' for preferred xml parsing
xmlParser = 'lxml'

# freetype or _renderPM or backend
# determines what code is used to create Paths from str
# see reportlab/graphics/utils.py for full horror
textPaths = 'freetype'
# change to None or 'rl_safe_eval' depending on trust
toColorCanUse = 'rl_extended_literal_eval'

# places to look for T1Font information
T1SearchPath = (
    'c:/Program Files/Adobe/Acrobat 9.0/Resource/Font',
    'c:/Program Files/Adobe/Acrobat 8.0/Resource/Font',
    'c:/Program Files/Adobe/Acrobat 7.0/Resource/Font',
    'c:/Program Files/Adobe/Acrobat 6.0/Resource/Font',  # Win32, Acrobat 6
    'c:/Program Files/Adobe/Acrobat 5.0/Resource/Font',  # Win32, Acrobat 5
    'c:/Program Files/Adobe/Acrobat 4.0/Resource/Font',  # Win32, Acrobat 4
    '%(disk)s/Applications/Python %(sys_version)s/reportlab/fonts',  # Mac?
    '/usr/lib/Acrobat9/Resource/Font',      # Linux, Acrobat 5?
    '/usr/lib/Acrobat8/Resource/Font',      # Linux, Acrobat 5?
    '/usr/lib/Acrobat7/Resource/Font',      # Linux, Acrobat 5?
    '/usr/lib/Acrobat6/Resource/Font',      # Linux, Acrobat 5?
    '/usr/lib/Acrobat5/Resource/Font',      # Linux, Acrobat 5?
    '/usr/lib/Acrobat4/Resource/Font',      # Linux, Acrobat 4
    '/usr/local/Acrobat9/Resource/Font',    # Linux, Acrobat 5?
    '/usr/local/Acrobat8/Resource/Font',    # Linux, Acrobat 5?
    '/usr/local/Acrobat7/Resource/Font',    # Linux, Acrobat 5?
    '/usr/local/Acrobat6/Resource/Font',    # Linux, Acrobat 5?
    '/usr/local/Acrobat5/Resource/Font',    # Linux, Acrobat 5?
    '/usr/local/Acrobat4/Resource/Font',    # Linux, Acrobat 4
    '/usr/share/fonts/default/Type1',       # Linux, Fedora
    '%(REPORTLAB_DIR)s/fonts',              # special
    '%(REPORTLAB_DIR)s/../fonts',           # special
    '%(REPORTLAB_DIR)s/../../fonts',        # special
    '%(CWD)s/fonts',                        # special
    '~/fonts',
    '~/.fonts',
    '%(XDG_DATA_HOME)s/fonts',
    '~/.local/share/fonts',
     )

# places to look for TT Font information
TTFSearchPath = (
    'c:/winnt/fonts',
    'c:/windows/fonts',
    '/usr/lib/X11/fonts/TrueType/',
    '/usr/share/fonts/truetype',
    '/usr/share/fonts',               # Linux, Fedora
    '/usr/share/fonts/dejavu',        # Linux, Fedora
    '%(REPORTLAB_DIR)s/fonts',        # special
    '%(REPORTLAB_DIR)s/../fonts',     # special
    '%(REPORTLAB_DIR)s/../../fonts',  # special
    '%(CWD)s/fonts',                  # special
    '~/fonts',
    '~/.fonts',
    '%(XDG_DATA_HOME)s/fonts',
    '~/.local/share/fonts',
    # mac os X - from
    # http://developer.apple.com/technotes/tn/tn2024.html
    '~/Library/Fonts',
    '/Library/Fonts',
    '/Network/Library/Fonts',
    '/System/Library/Fonts',
    )

# places to look for CMap files - should ideally merge with above
CMapSearchPath = (
    '/usr/lib/Acrobat9/Resource/CMap',
    '/usr/lib/Acrobat8/Resource/CMap',
    '/usr/lib/Acrobat7/Resource/CMap',
    '/usr/lib/Acrobat6/Resource/CMap',
    '/usr/lib/Acrobat5/Resource/CMap',
    '/usr/lib/Acrobat4/Resource/CMap',
    '/usr/local/Acrobat9/Resource/CMap',
    '/usr/local/Acrobat8/Resource/CMap',
    '/usr/local/Acrobat7/Resource/CMap',
    '/usr/local/Acrobat6/Resource/CMap',
    '/usr/local/Acrobat5/Resource/CMap',
    '/usr/local/Acrobat4/Resource/CMap',
    'C:\\Program Files\\Adobe\\Acrobat\\Resource\\CMap',
    'C:\\Program Files\\Adobe\\Acrobat 9.0\\Resource\\CMap',
    'C:\\Program Files\\Adobe\\Acrobat 8.0\\Resource\\CMap',
    'C:\\Program Files\\Adobe\\Acrobat 7.0\\Resource\\CMap',
    'C:\\Program Files\\Adobe\\Acrobat 6.0\\Resource\\CMap',
    'C:\\Program Files\\Adobe\\Acrobat 5.0\\Resource\\CMap',
    'C:\\Program Files\\Adobe\\Acrobat 4.0\\Resource\\CMap',
    '%(REPORTLAB_DIR)s/fonts/CMap',         # special
    '%(REPORTLAB_DIR)s/../fonts/CMap',      # special
    '%(REPORTLAB_DIR)s/../../fonts/CMap',   # special
    '%(CWD)s/fonts/CMap',                   # special
    '%(CWD)s/fonts',                        # special
    '~/fonts/CMap',
    '~/.fonts/CMap',
    '%(XDG_DATA_HOME)s/fonts/CMap',
    '~/.local/share/fonts/CMap',
    )

if sys.platform.startswith('linux'):
    def _findFontDirs(*ROOTS):
        R = [].append
        for rootd in ROOTS:
            for root, dirs, files in os.walk(rootd):
                if not files:
                    continue
                R(root)
        return tuple(R.__self__)
    T1SearchPath = T1SearchPath + _findFontDirs(
                        '/usr/share/fonts/type1',
                        '/usr/share/fonts/Type1',
                        )
    TTFSearchPath = TTFSearchPath + _findFontDirs(
                        '/usr/share/fonts/truetype',
                        '/usr/share/fonts/TTF',
                        )
