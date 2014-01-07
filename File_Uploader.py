from Template_Authenticated import Template_Authenticated
from z_account import is_site_admin
from z_docs import save_document

class File_Uploader (Template_Authenticated):
    def writeContent(self):
        if is_site_admin(self.request()):
            if self.request()._environ.get('REQUEST_METHOD') == 'POST':
                ERROR = None
                form = self.request().fields()
                fobj = form.get('datafile')
                try:
                    filename = fobj.filename
                except:
                    ERROR = 'You must select a file to upload.'
            if ERROR:
                self.render_form_error('Upload Error', ERROR)
            else:
                save_document(form)
                self.response().sendRedirect(form.get('redir'))

        else:
            wr('<p>You are not authorized to do that.</p>')
