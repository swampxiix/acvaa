from Index import Index
from acva.z_account import is_site_admin
from z_found import del_donor

class Donor_Del (Index):

    def writeContent(self):
        wr = self.writeln
        form = self.request().fields()
        n, t = form.get('n'), form.get('t')
        IS_SITE_ADMIN = is_site_admin(self.request())

        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            if IS_SITE_ADMIN:
                if n and t:
                    del_donor(t, n)
                    self.response().sendRedirect('Donors')
            else:
                wr('You are not authorized to perform this action.')
        else:
            wr('''
<form method="POST" action="Donor_Del">
Are you sure you want to remove this donor from the list?
<input type="hidden" name="n" value="%s">
<input type="hidden" name="t" value="%s">
<br /><br />
<b>%s</b>
<br /><br />
<input type="submit" value="Yes">
<input type="button" value="No. Leave them kids alone." onClick="javascript:history.go(-1)">
</form>
                ''' % (n, t, n))
