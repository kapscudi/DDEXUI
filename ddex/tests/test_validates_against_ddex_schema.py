import lxml.etree as ET
from DDEXUI.ddex.ddex import DDEX
from DDEXUI.ddex.release import Release, ReleaseId
from DDEXUI.ddex.party import Party
from DDEXUI.ddex.deal import Deal
from datetime import date
import unittest

class DDEXSchemaValidation(unittest.TestCase):
	@unittest.skip("work in progress")
	def test_created_ddex_files_validate_against_ddex_xsd(self):
		#helpped by http://alex-sansom.info/content/validating-xml-against-xml-schema-python
		release = (Release(
			"Bad",
			"copyright MJ",
			"Published by MJ",
			1987,
			"R0",
			ReleaseId(1,"1234567898764"),
			"Album",
			"Michael Jackson",
			"Epic",
			True))

		deal = Deal("PayAsYouGoModel", "PermenantDownload", "FR", date(2012,1,3))

		release.add_deal(deal)

		DDEX(Party('derwwfefw', 'Sony'),release).write()
		
		tree = ET.parse('file.xml')
#		tree = ET.parse('/home/will/Documents/python/DDEXUI/ddex/tests/resources/ddex-sample.xml')
		schema = ET.XMLSchema(file="http://ddex.net/xml/ern/341/release-notification.xsd")
		schema.assertValid(tree)
