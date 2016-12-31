from Template_Authenticated import Template_Authenticated
from z_account import is_site_admin
from z_forms import hidden, submit
from z_docs import archive_document

class File_Archiver (Template_Authenticated):
    def title(self):
        qs = self.request().fields()
        is_restore = qs.get('restore')
        if is_restore:
            return 'Restore File?'
        else:
            return 'Archive File?'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        doctype, category, filename = qs.get('doctype'), qs.get('category'), qs.get('filename')
        is_restore = qs.get('restore')
        IS_SITE_ADMIN = is_site_admin(self.request())
        if doctype and filename:
            if IS_SITE_ADMIN:
                if self.request()._environ.get('REQUEST_METHOD') == 'POST':
                    archive_document(doctype, category, filename)
                    redir = ''
                    if doctype == 'document':
                        redir += 'Documents?cat=%s' % (category)
                    if doctype == 'report':
                        redir += 'Reports'
                    self.response().sendRedirect(redir)
                else:
                    wr('<h1>%s</h1>' % (self.title()))
                    if is_restore:
                        wr('<P>Are you sure you want to restore this %s?</P>' % (doctype))
                    else:
                        wr('<P>Are you sure you want to archive this %s?</P>' % (doctype))
                    wr('<P>%s</P>' % (filename))
                    wr('<form method="POST" action="File_Archiver">')
                    wr(hidden('doctype', doctype))
                    wr(hidden('category', category))
                    wr(hidden('filename', filename))
                    if is_restore:
                        wr(submit('Yes, restore the %s.' % (doctype)))
                    else:
                        wr(submit('Yes, archive the %s.' % (doctype)))
                    wr('<input type="button" value="Do nothing." onClick="javascript:history.go(-1)">')
                    wr('</form>')
            else:
                wr('<p>You are not a site administrator.</p>')
        else:
            wr('<p>No document type and/or filename.</p>')


