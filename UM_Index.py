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

        wr('''
<table border="1"><tr><th>&nbsp;<th colspan="6">Roles        
<tr><th>Name<th>A<th>D<th>R<th>E<th>H<th>M<th><small>RTC</small><th>Actions
            ''')

        for ak in aks:
            ud = all[ak]
            wr('<tr class="c">')
            wr('<td class="t12">')
            firstletter = ak[0].lower()
            if firstletter not in DISPLAYLETTERS:
                wr('<a name="%s"></a>' % (firstletter))
                DISPLAYLETTERS.append(firstletter)
            wr('%s, %s' % ( ud.get('sn'), ud.get('fn') ))

            ROLEICONS = (
                          ('admin', 'fa-pencil'),
                          ('diplomate', 'fa-user-md'),
                          ('resident', 'fa-graduation-cap'),
                          ('emeritus', 'fa-trophy'),
                          ('honorary', 'fa-certificate'),
                          ('memoriam', 'fa-cloud-upload'),
                          ('rtc', 'fa-clipboard'),
                            )
            for role, icon in ROLEICONS:
                color = '#E0E0E0'
                if role in ud.get('roles', []):
                    color = '#006600'
                wr('<td><i class="fa %s" style="color: %s;"></i>' % (icon, color))

            if 'master' in ud.get('roles'):
                wr('<td class="t10 hint" colspan="4">You cannot manage the master account.</td>')
            elif self.request().cookies().get('username') == ud.get('username'):
                wr('<td class="t10 hint" colspan="4">You cannot manage your own account.</td>')
            else:
                un = ud.get('username')
                wr('''<td>
<select class="form-control" onChange="javascript:window.location = this.options[this.selectedIndex].value">
  <option value="#">Select...</option>
  <option value="UM_Act_as_User?u=%s">Act as User</option>
  <option value="UM_Roles_Form?u=%s">Edit Roles</option>
  <option value="UM_Reset_User_Pass?u=%s">Reset Password</option>
  <option value="UM_Delete_User?u=%s">Delete User</option>
</select>
                    ''' % (un, un, un, un))

        wr('</table>')


