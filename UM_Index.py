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

        wr('<table>')
        wr('<tr>')
        wr('<th colspan="2">&nbsp;')
        wr('<th colspan="3">Roles')
        
        wr('<tr>')
        wr('<th>Name')
#        wr('<th>ID')
#        wr('<th>Email')
        wr('<th>A')
        wr('<th>D')
        wr('<th>R')
        wr('<th>E')
        wr('<th colspan="3">Actions')

        for ak in aks:
            ud = all[ak]
            wr('<tr class="c">')
            wr('<td class="t12">%s, %s' % ( ud.get('sn'), ud.get('fn') ))
#            wr('<td class="t10 hint">%s' % ( ud.get('username') ))
#            wr('<td class="t9"><a href="mailto:%s">%s</a>' % (ud.get('email'), ud.get('email')))
            for r in ALL_ROLES:
                wr('<td>')
                if r in ud.get('roles'):
                    wr('<img src="/g/on.png" width="14" height="14" alt="is %s" title="is %s" />' % (r, r))
                else:
                    wr('<img src="/g/off.png" width="14" height="14" alt="not %s" title="not %s" />' % (r, r))


            if 'master' in ud.get('roles'):
                wr('<td class="t10 hint" colspan="3">You cannot manage the master account.</td>')
            elif self.request().cookies().get('username') == ud.get('username'):
                wr('<td class="t10 hint" colspan="3">You cannot manage your own account.</td>')
            else:
                wr('<td class="t10"><a href="UM_Act_as_User?u=%s">Act as User</a>' % (ud.get('username')))
                wr('<td class="t10"><a href="UM_Roles_Form?u=%s">Edit Roles</a>' % (ud.get('username')))
                wr('<td class="t10"><a href="UM_Reset_User_Pass?u=%s">Reset Password</a>' % (ud.get('username')))
                wr('<td class="t10"><a href="UM_Delete_User?u=%s">Delete User</a>' % (ud.get('username')))

        wr('</table>')


