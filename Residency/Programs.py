from acva.Template_Main import Template_Main
from acva.z_account import is_site_admin
from z_rez import get_residencies

class Programs (Template_Main):
    def title(self):
        return ("ACVAA Registered Residencies")

    def writeContent(self):
        wr = self.writeln
        ISA = is_site_admin(self.request())
        if ISA:
            wr('<div class="button">')
            wr('<a href="Program_Form">+ Add Program</a>')
            wr('</div>')


        wr('<h1>%s</h1>' % (self.title()))
        wr('''
<p>
The following residency programs were registered with the ACVAA. Veterinarians interested in a residency program are encouraged to contact the program leaders. Please note that these are registered programs and not available positions. Available positions can be found under <a href="/Jobs">Employment Opportunities</a>.
</p>
            ''')
        rezdict = get_residencies()
        rkeys = rezdict.keys()
        rkeys.sort()
        wr('<ol class="dec">')
        for rez in rkeys:
            progdict = rezdict[rez]
            wr('<li> %s' % (progdict.get('institution')))
            if ISA:
                wr('<a href="Program_Form?id=%s"><img src="/g/edit.png" alt="edit" width="17" height="17" border="0" /></a>' % (progdict.get('id')))
                wr('<a href="Delete_Program?id=%s"><img src="/g/delete.png" alt="delete" width="17" height="17" border="0" /></a>' % (progdict.get('id')))
            wr('<br>')

            listing = progdict.get('listing').strip()
            listing = listing.replace('\r\n', '\n')
            listing = listing.replace('\n', '<br>')
            wr(listing)
            wr('<br>')

            lead1 = progdict.get('leader1name')
            lead2 = progdict.get('leader2name')
            x = 'Program leader'
            if lead1 and lead2:
                x += 's'
            wr('%s: ' % (x))
            if lead1:
                lead1email = progdict.get('leader1email')
                if lead1email:
                    wr('<a href="mailto:%s">%s</a>' % (lead1email, lead1))
                else:
                    wr(lead1)
            if lead2:
                wr(' & ')
                lead2email = progdict.get('leader2email')
                if lead2email:
                    wr('<a href="mailto:%s">%s</a>' % (lead2email, lead2))
                else:
                    wr(lead2)
                wr('<br>')

        wr('</ol>')            
