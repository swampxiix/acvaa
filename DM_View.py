from Template_Authenticated import Template_Authenticated
from z_account import is_logged_in, is_site_admin, get_user_acct

class DM_View (Template_Authenticated):
    def title(self):
        pass

    def writeContent(self):
        wr = self.writeln
        ILI = is_logged_in(self.request())
        ISA = is_site_admin(self.request())
        username = self.request().cookies().get('username')
        useracct = get_user_acct(username)
        wr(useracct)
        userroles = useracct.get('roles')
