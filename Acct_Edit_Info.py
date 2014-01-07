from Template_Authenticated import Template_Authenticated

from z_account import check_email_address, is_email_registered, save_user_info

class Acct_Edit_Info (Template_Authenticated):

    def writeContent(self):
        wr = self.writeln
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            C = self.request().cookies()
            un, hash = C.get('username'), C.get('hash')
            form = self.request().fields()
            ERROR = None

            if (un == form.get('form_username')) and (hash == form.get('form_hash')):

                required = {'fn': 'first name', 'sn': 'surname', 'city': 'city', 'state': 'state', 'email': 'email', }
                for r in required.keys():
                    if not form.get(r):
                        ERROR = 'The field "%s" is required.' % (required.get(r))

                if not ERROR:
                    ERROR = check_email_address(form.get('email'))

                if not ERROR:
                    if form.get('email') != form.get('original_email'): # user changing email address
                        if is_email_registered(form.get('email')):
                            ERROR = 'We already have an account that uses the email address: %s.' % (form.get('email'))

                if ERROR:
                    self.render_form_error('Account Error', ERROR)
                else:
                    save_user_info(form.get('form_username'), form)
                    self.response().sendRedirect('Account?ic=1')

            else:
                self.render_form_error('Account Error', 'Credentials failure.')
        else:
            self.render_form_error('Account Error', 'No post.')
