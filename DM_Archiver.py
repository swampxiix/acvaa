from Template_Authenticated import Template_Authenticated
from z_account import is_site_admin
from z_docmgmt import archive_doc, activate_doc

class DM_Archiver (Template_Authenticated):

    def title(self):
        return 'Document Archiver'

    def writeContent(self):
        wr = self.writeln
        ISA = is_site_admin(self.request())
        if ISA:
            qs = self.request().fields()
            fn = qs.get('fn')
            action = qs.get('action')
            if fn and action:
                if action == 'archive':
                    archive_doc(fn)
                if action == 'activate':
                    activate_doc(fn)

        self.response().sendRedirect('DM_Index')
