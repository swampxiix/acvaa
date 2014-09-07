from acva.Template_Admin import Template_Admin
from z_rez import get_one_residency, save_residency

class Program_Form (Template_Admin):
    def title(self):
        return ("Add/Edit Residency Program")

    def writeContent(self):
        wr = self.writeln
        qs = form = self.request().fields()
        rezid = qs.get('id')
        wr('<h1>%s</h1>' % (self.title()))
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            save_residency(form)
            self.response().sendRedirect('Programs')
        else:
            rezdict = {}
            wr('<form method="POST" action="Program_Form">')
            if rezid:
                wr('<input type="hidden" name="id" value="%s">' % (rezid))
                rezdict = get_one_residency(rezid)
            wr('<table>')
            wr('<tr><td>Institution:</td>')
            wr('<td><input type="text" name="institution" value="%s">' % (rezdict.get('institution', '')))
            wr('<small>This will decide where the program exists in the sorted list.</small></td></tr>')
            wr('<tr><td>Details:</td>')
            wr('<td><textarea name="listing" cols="50" rows="10">%s</textarea></td></tr>' % (rezdict.get('listing', '')))
            wr('<tr><td>Program Leader 1:</td>')
            wr('<td><input type="text" name="leader1name" value="%s"></td></tr>' % (rezdict.get('leader1name', '')))
            wr('<tr><td>Leader 1 Email:</td>')
            wr('<td><input type="text" name="leader1email" value="%s"></td></tr>' % (rezdict.get('leader1email', '')))
            wr('<tr><td>Program Leader 2:</td>')
            wr('<td><input type="text" name="leader2name" value="%s"></td></tr>' % (rezdict.get('leader2name', '')))
            wr('<tr><td>Leader 2 Email:</td>')
            wr('<td><input type="text" name="leader2email" value="%s"></td></tr>' % (rezdict.get('leader2email', '')))
            wr('<tr><td></td><td><input type="submit" value="Save Residency Program"> <input type="button" value="Cancel" onClick="javascript:history.go(-1)"></td></tr>')
            wr('</table>')
            wr('</form>')

