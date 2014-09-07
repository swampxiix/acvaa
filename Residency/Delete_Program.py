from acva.Template_Admin import Template_Admin
from z_rez import get_one_residency, delete_residency

class Delete_Program (Template_Admin):
    def title(self):
        return ("Delete Residency Program?")

    def writeContent(self):
        wr = self.writeln
        qs = form = self.request().fields()
        rezid = qs.get('id')
        wr('<h1>%s</h1>' % (self.title()))

        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            delete_residency(form.get('id'))
            self.response().sendRedirect('Programs')
        else:
            rezdict = get_one_residency(rezid)

            wr('<P>Are you sure you want to delete this program?</P>')
            wr(rezdict.get('institution', ''))
            wr('<br>')
            listing = rezdict.get('listing')
            listing = listing.replace('\r\n', '\n')
            listing = listing.replace('\n', '<br>')
            wr(listing)
            wr('<br>')
            wr(rezdict.get('leader1name', ''))
            wr(rezdict.get('leader1email', ''))
            wr('<br>')
            wr(rezdict.get('leader2name', ''))
            wr(rezdict.get('leader2email', ''))

            wr('<form method="POST" action="Delete_Program">')
            wr('<input type="hidden" name="id" value="%s">' % (rezid))
            wr('<input type="submit" value="Delete Program"> <input type="button" value="Cancel" onClick="javascript:history.go(-1)">')
            wr('</form>')
