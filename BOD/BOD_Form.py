from acva.Template_Admin import Template_Admin
from z_board import getBOD, updateBOD

class BOD_Form (Template_Admin):
    def title(self):
        return 'Update Board of Directors'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            updateBOD(qs)
            self.response().sendRedirect('Index')

        else:
            bod = getBOD()
            wr('<table><tr><th>Title<th>Name<th>Email<th>Year')
            wr('<form method="POST" action="BOD_Form">')
            for a in ['President', 'President-Elect', 'Past-President', 'Executive Secretary', 'Region 1', 'Region 2', 'Region 3', 'Region 4', 'Region 5', 'At-Large_1', 'At-Large_2', 'At-Large_3', 'AVBS Representative', 'AVBS Alternate']:
                ad = bod.get(a)
                wr('<tr><td>%s' % (a))
                wr('<td><input type="text" name="%s" value="%s">' % (a, ad.get('name')))
                wr('<td><input type="text" name="%s" value="%s">' % (a, ad.get('email')))
                wr('<td><input type="text" name="%s" value="%s" size="5">' % (a, ad.get('year')))
            wr('<tr><td><td colspan="3"><input type="submit" value="Save Board Info">')
            wr('<input type="button" value="Cancel" onClick="javascript:history.go(-1)">')
            wr('</form>')
            wr('</table>')
