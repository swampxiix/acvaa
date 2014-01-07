from Template_Authenticated import Template_Authenticated

from z_account import save_user_info

class Acct_Change_Privacy (Template_Authenticated):

    def writeContent(self):
        wr = self.writeln
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            C = self.request().cookies()
            un, hash = C.get('username'), C.get('hash')
            form = self.request().fields()
            if (un == form.get('form_username')) and (hash == form.get('form_hash')):
                save_user_info(form.get('form_username'), form)
                self.response().sendRedirect('Account?pv=1')

            else:
                self.render_form_error('Account Error', 'Credentials failure.')
        else:
            self.render_form_error('Account Error', 'No post.')
