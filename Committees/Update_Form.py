from acva.Template_Admin import Template_Admin
from z_committees import STANDING_KEYS, ADHOC_KEYS, OTHER_KEYS, ANNUAL_KEYS, getCommittees, updateCommittees

class Update_Form (Template_Admin):
    def title(self):
        return 'Update Committees'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            updateCommittees(qs)
            self.response().sendRedirect('Index')
        else:
            coms = getCommittees()
#            wr(coms)
            wr('<form method="POST" action="Update_Form">')
            for keyset in (STANDING_KEYS, ANNUAL_KEYS, ADHOC_KEYS, OTHER_KEYS):
                for K in keyset:
                    wr('<table><tr><td colspan="4"><h2>%s</h2>' % (K))
                    K = K.replace('ACVAA', 'ACVA') # name change
                    wr('<tr><th>Key<th>Title<th>Name<th>Year')
                    rrs, rre = 1, 11
                    if K == 'Exam Committee': rrs, rre = 1,16
                    for n in range(rrs, rre):
                        posnkey = '%s_%s' % (K, n)
                        posndict = coms.get(posnkey, {})
                        wr('<tr><td>%s' % (n))
#                        wr('<tr><td>%s' % (posnkey))
                        wr('<td><input type="text" name="%s" value="%s">' % (posnkey, posndict.get('title', ' ')))
                        wr('<td><input type="text" name="%s" value="%s">' % (posnkey, posndict.get('name', ' ')))
                        wr('<td><input type="text" name="%s" value="%s" size="5">' % (posnkey, posndict.get('year', ' ')))
                    wr('</table>')

            wr('<tr><td><td colspan="3"><input type="submit" value="Save Committees\' Info">')
            wr('<input type="button" value="Cancel" onClick="javascript:history.go(-1)">')
            wr('</form>')
