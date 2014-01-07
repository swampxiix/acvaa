from Index import Index
from acva.z_account import is_site_admin
from z_found import add_donor

class Donor_Add (Index):

    def writeContent(self):
        wr = self.writeln
        form = self.request().fields()
        IS_SITE_ADMIN = is_site_admin(self.request())
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            if IS_SITE_ADMIN:
                n, t = form.get('name'), form.get('type')
                if n and t:
                    add_donor(t, n)
                    self.response().sendRedirect('Donors')
            else:
                wr('You are not authorized to perform this action.')
        else:
            wr('You are not authorized to perform this action.')
