from acva.Template_Admin import Template_Admin
from z_cpe import get_raw_from, write_raw_to, LOOKUP

class Edit_Document (Template_Admin):
    def title(self):
        return 'Edit Document'


    def writeContent(self):
        wr = self.writeln
        qs = form = self.request().fields()
        wr('<h1>%s</h1>' % (self.title()))
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            filename = form.get('fn')
            filename = sanitize(filename)
            write_raw_to(filename, form.get('text'))
            destURL = LOOKUP.get(filename)
            self.response().sendRedirect(destURL)
        else:
            filename = qs.get('fn')
            filename = sanitize(filename)
            wr('<h2>%s</h2>' % (filename))
            wr('<form method="POST" action="Edit_Document">')
            wr('<input type="hidden" name="fn" value="%s">' % (filename))
            wr('<textarea name="text" cols="100" rows="40">')
            txt = get_raw_from(filename)
            wr(txt)
            wr('</textarea>')
            wr('<br>')
            wr('<input type="submit" value="Save Document Text">')
            wr('<input type="button" value="Cancel" onClick="javascript:history.go(-1)">')
            wr('</form>')

def sanitize (txt):
    txt = txt.replace('..', '')
    txt = txt.replace('/', '')
    txt = txt.replace('\\', '')
    return txt
