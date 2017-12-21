from Template_Authenticated import Template_Authenticated
from z_account import is_site_admin
from z_docmgmt import get_all_possible_categories, MASTER_ROLES_LIST, \
    save_doc_file, get_document_properties, edit_doc_file
from z_forms import hidden, submit, text

class DM_Add_Edit_Doc (Template_Authenticated):

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

                if form.get('formaction') == 'add':
                    fobj = form.get('datafile')
                    try:
                        filename = fobj.filename
                    except:
                        ERRORS.append('You must select a file on your computer to upload.')

                if ERRORS:
                    self.render_form_error('Upload Error', '<br>'.join(ERRORS))

                else:
                    if form.get('formaction') == 'add':
                        save_doc_file(form)
                        self.response().sendRedirect('DM_Index')
                    if form.get('formaction') == 'edit':
                        edit_doc_file(form)
                        self.response().sendRedirect('DM_Index')

            else:
                qs = form
                if qs.get('fn'):
                    filename = qs.get('fn')
                    pick = get_document_properties(filename)
                    hideval = 'edit'
                    ttl = 'Edit Document Properties'
                    subval = 'Save Changes'
                else:
                    filename = ''
                    pick = {}
                    hideval = 'add'
                    ttl = 'Add a New Document'
                    subval = 'Save Changes'

                wr('<h2>%s</h2>' % (ttl))
                wr('<p>All form fields are required.</p>')
                wr('<form method="POST" action="DM_Add_Edit_Doc" enctype="multipart/form-data">')
                wr(hidden('formaction', hideval))
                wr(hidden('filename', filename))

                wr('<table>')
                wr('<tr><td>Title:<td>')
                wr(text('title', pick.get('title', '')))

                wr('<tr><td>Categories:<br><small>(pick at least one)</small><td>')
                for cat in get_all_possible_categories():
                    wr('<label for="%s"><input type="checkbox" name="category" value="%s" id="%s"' % (cat, cat, cat))
                    if cat in pick.get('categories', []):
                        self.write(' checked')
                    wr('> %s</label><br>' % (cat))
                wr('<hr>')
                wr('<td><a href="DM_Edit_Categories" class="btn btn-default btn-sm"><i class="fa fa-pencil">&nbsp;</i>Edit Categories</a>')
                wr('<tr><td>Allowed access:<br><small>(pick at least one)</small><td>')
                for role in MASTER_ROLES_LIST:
                    wr('<label for="%s"><input type="checkbox" name="role" value="%s" id="%s"' % (role, role, role))
                    if role in pick.get('roles', []):
                        self.write(' checked')
                    wr('> %s</label><br>' % (role))
                if not qs.get('fn'):
                    wr('<tr><td>File:<td><input type="file" name="datafile"><br />')
                wr('<tr><td><td>')
                wr(submit(subval))
                wr('</table>')
                wr('</form>')
