from Template_Authenticated import Template_Authenticated
from z_account import is_site_admin
from z_docmgmt import get_document_properties, rm_doc_file
from z_forms import submit, hidden

class DM_Delete_Doc (Template_Authenticated):

    def title(self):
        return 'Confirm Document Deletion'

    def writeContent(self):
        wr = self.writeln
        ISA = is_site_admin(self.request())
        if ISA:
            if self.request()._environ.get('REQUEST_METHOD') == 'POST':
                form = self.request().fields()
                rm_doc_file(form.get('filename'))
                self.response().sendRedirect('DM_Index')
            else:
                qs = self.request().fields()
                filename = qs.get('fn')
                pick = get_document_properties(filename)
                wr('<h1>%s</h1>' % (self.title()))
                wr('<p>Are you sure you wish to delete this file?</p>')
                wr('<p><table>')
                wr('<tr><td>Filename:<td>%s' % (filename))
                wr('<tr><td>Title:<td>%s' % (pick.get('title', '')))
                wr('<tr><td>Categories:<td>%s' % (', '.join(pick.get('categories', []))))
                wr('<tr><td>Access:<td>%s' % (', '.join(pick.get('roles', []))))
                wr('</table></p>')
                wr('<p><form method="POST" action="DM_Delete_Doc">')
                wr(hidden('filename', filename))
                wr(submit('Yes.'))
                wr('<input type="button" value="No, better to leave well-enough alone." onclick="javascript:history.go(-1)">')
                wr('</form></p>')
