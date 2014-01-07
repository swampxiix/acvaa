from acva.Template_Authenticated import Template_Authenticated
from acva.z_account import is_site_admin
from z_committees import STANDING_KEYS, ADHOC_KEYS, OTHER_KEYS, ANNUAL_KEYS, getCommDict

class Index (Template_Authenticated):
    def title(self):
        return 'ACVA Committees'

    def writeContent(self):
        wr = self.writeln
        IS_SITE_ADMIN = is_site_admin(self.request())
        if IS_SITE_ADMIN:
            wr('<div class="button">')
            wr('<a href="Update_Form">Edit Committees</a>')
            wr('</div>')

        wr('<a name="top"></a>')
        wr('<h1>%s</h1>' % (self.title()))

        comdict = getCommDict()

        for CTITLE, KEYSET in (('Standing Committees', STANDING_KEYS), ('Annual Committees', ANNUAL_KEYS), ('Ad Hoc Committees', ADHOC_KEYS), ('Other Positions', OTHER_KEYS)):
            wr('<h2>%s</h2>' % (CTITLE))
            wr('<table class="comm">')
            catinfo = comdict.get(CTITLE)
            for COMMITTEE in KEYSET:
                wr('<tr><th colspan="3">%s' % (COMMITTEE))
                committee_dict = catinfo.get(COMMITTEE)
                committee_keys = committee_dict.get('sorted') # already sorted
#                committee_keys = committee_dict.keys() # already sorted
                for position in committee_keys:
                    pdict = committee_dict.get(position)
                    xx, xy = pdict.get('title').replace(' ', ''), pdict.get('name').replace(' ', '')
                    if xx or xy:
                        wr('<tr><td>')
                        wr(pdict.get('title'))
                        wr('<td>')
                        wr(pdict.get('name'))
                        wr('<td>')
                        wr(pdict.get('year'))
            wr('</table>')
