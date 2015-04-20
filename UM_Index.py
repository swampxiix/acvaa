from Template_Admin import Template_Admin

from z_account import get_all_users
from z_constants import ALL_ROLES

class UM_Index (Template_Admin):

    def title(self):
        return 'ACVAA: User Management'

    def writeContent(self):
        wr = self.writeln
        wr('<div class="button">')
        wr('<a href="UM_Journal">ACVAA Journal Access</a>')
        wr('</div>')


        wr('<h1>%s</h1>' % (self.title()))

        qs = self.request().fields()
        if qs.get('delok'):
            self.render_special_msg('User account %s deleted.' % (qs.get('delok')))
        if qs.get('rolok'):
            self.render_special_msg('User roles for %s saved.' % (qs.get('rolok')))

        all = get_all_users()
        aks = all.keys()
        aks = sorted(aks, key=lambda x: (x.isdigit() and float(x)) or x.lower())

        # Create bookmarks & jump links.
        NAVLETTERS, DISPLAYLETTERS = [], []
        for namestring in aks:
            firstletter = namestring[0].lower()
            if firstletter not in NAVLETTERS:
                NAVLETTERS.append(firstletter)
        wr('<P>')
        for letter in NAVLETTERS:
            wr('<a href="#%s">%s</a>' % (letter, letter.capitalize()))
        wr('</P>')

        wr('<table border="1">')
        wr('<tr>')
        wr('<th>&nbsp;')
        wr('<th colspan="6">Roles')
        
        wr('<tr>')
        wr('<th>Name')
        wr('<th>A')
        wr('<th>D')
        wr('<th>R')
        wr('<th>E')
        wr('<th>H')
        wr('<th>M')
        wr('<th colspan="4">Actions')

        for ak in aks:
            ud = all[ak]
            wr('<tr class="c">')
            wr('<td class="t12">')
            firstletter = ak[0].lower()
            if firstletter not in DISPLAYLETTERS:
                wr('<a name="%s"></a>' % (firstletter))
                DISPLAYLETTERS.append(firstletter)
            wr('%s, %s' % ( ud.get('sn'), ud.get('fn') ))
            for r in ALL_ROLES:
                wr('<td>')
                if r in ud.get('roles'):
                    wr('<img src="/g/on.png" width="14" height="14" alt="is %s" title="is %s" />' % (r, r))
                else:
                    wr('<img src="/g/off.png" width="14" height="14" alt="not %s" title="not %s" />' % (r, r))


            if 'master' in ud.get('roles'):
                wr('<td class="t10 hint" colspan="4">You cannot manage the master account.</td>')
            elif self.request().cookies().get('username') == ud.get('username'):
                wr('<td class="t10 hint" colspan="4">You cannot manage your own account.</td>')
            else:
                wr('<td class="t10"><a href="UM_Act_as_User?u=%s">Act as User</a>' % (ud.get('username')))
                wr('<td class="t10"><a href="UM_Roles_Form?u=%s">Edit Roles</a>' % (ud.get('username')))
                wr('<td class="t10"><a href="UM_Reset_User_Pass?u=%s">Reset Password</a>' % (ud.get('username')))
                wr('<td class="t10"><a href="UM_Delete_User?u=%s">Delete User</a>' % (ud.get('username')))

        wr('</table>')


