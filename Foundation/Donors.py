from Index import Index
from z_found import get_donors
from acva.z_account import is_site_admin

class Donors (Index):
    def title(self):
        return 'ACVAA Foundation Donors'

    def writeContent(self):
        wr = self.writeln
        wr('<h1>%s</h1>' % (self.title()))
        self.sidebar()
        IS_SITE_ADMIN = is_site_admin(self.request())
        if IS_SITE_ADMIN:
            wr('''
<p>
<form action="Donor_Add" method="POST">
Name: <input type="text" name="name" value="">
<select name="type">
<option value="r">Regular</option>
<option value="c">Charter</option>
<option value="f">Founder</option>
</select>
<input type="submit" value="Add Donor">
</form>
</p>
                ''')

        wr('<p>The ACVAA Foundation would like to thank the following:</p>')
        for ttl, cat in [ 
                ('ACVAA Founders', 'f'),
                ('ACVAA Charter Donors', 'c'),
                ('ACVAA Supporters', 'r'),
                ]:
            lst = get_donors(cat)
            if lst:
                wr('<h2>%s</h2>' % (ttl))
                wr('<p><ul class="list">')
                for n in lst:
                    wr('<li> %s' % (n))
                    if IS_SITE_ADMIN:
                        wr('<a href="Donor_Del?n=%s&t=%s"><img src="/g/delete.png" alt="delete" border="0"></a>' % (n, cat))
                wr('</ul></p>')
