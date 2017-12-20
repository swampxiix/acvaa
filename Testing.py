from Template_Authenticated import Template_Authenticated
from z_account import is_site_admin
from z_docmgmt import get_all_possible_categories, MASTER_ROLES_LIST, \
    save_doc_file

class Testing (Template_Authenticated):

    def title(self):
        return 'Documents'

    def writeContent(self):
        wr = self.writeln
        ISA = is_site_admin(self.request())
        if ISA:
            form = self.request().fields()
            if self.request()._environ.get('REQUEST_METHOD') == 'POST':
                ERRORS = []
                if not form.get('title'):
                    ERRORS.append('You must provide a title for this document.')
                if not form.get('role'):
                    ERRORS.append('You must allow access to one or more roles.')
                if not form.get('category'):
                    ERRORS.append('You must select one or more categories for this document.')

                fobj = form.get('datafile')
                try:
                    filename = fobj.filename
                except:
                    ERRORS.append('You must select a file on your computer to upload.')

                if ERRORS:
                    self.render_form_error('Upload Error', '<br>'.join(ERRORS))

                else:
#                    wr(form)
                    save_doc_file(form)
                    self.response().sendRedirect('DM_Index')


            else:
                wr('<h2>Add a Document</h2>')
                wr('<p>All form fields are required.</p>')
                wr('<form method="POST" action="Testing" enctype="multipart/form-data">')
                wr('<table>')
                wr('<tr><td>Title:<td><input type="text" name="title" value=""><br />')
                wr('<tr><td>Categories:<br><small>(pick at least one)</small><td>')
                for cat in get_all_possible_categories():
                    wr('<label for="%s"><input type="checkbox" name="category" value="%s" id="%s"> %s</label><br>' % (cat, cat, cat, cat))
                wr('<hr>')
                wr('<td><a href="DM_Edit_Categories" class="btn btn-default btn-sm"><i class="fa fa-pencil">&nbsp;</i>Edit Categories</a>')
                wr('<tr><td>Allowed access:<br><small>(pick at least one)</small><td>')
                for role in MASTER_ROLES_LIST:
                    wr('<label for="%s"><input type="checkbox" name="role" value="%s" id="%s"> %s</label><br>' % (role, role, role, role))
                wr('<tr><td>File:<td><input type="file" name="datafile"><br />')
                wr('<tr><td><td><input type="submit" value="Upload">')
                wr('</table>')
                wr('</form>')
