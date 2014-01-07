from Template_Authenticated import Template_Authenticated

from z_account import change_for_hire_status

class Acct_Change_Hire (Template_Authenticated):

    def writeContent(self):
        wr = self.writeln
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            C = self.request().cookies()
            un, hash = C.get('username'), C.get('hash')
            form = self.request().fields()
            ERROR = None
            if (un == form.get('form_username')) and (hash == form.get('form_hash')):
                if form.get('show_for_hire'):
                    change_for_hire_status (un, form)
                else:
                    ERROR = 'You must choose one of the options before clicking the form submission button.'
            else:
                ERROR = 'Credentials failure.'

            if ERROR:
                self.render_form_error('Form Error', ERROR)
            else:
                self.response().sendRedirect('Account?fh=1')


