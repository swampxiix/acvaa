from Template_Main import Template_Main

from z_account import authenticate, get_user_acct, hash_string

class Logout (Template_Main):

    def writeContent(self):
        wr = self.writeln
        self.killCookie('username')
        self.killCookie('hash')
        self.killCookie('role')
        self.killCookie('actingasuser')
        self.killCookie('g')
        if self.request().cookies().get('username'):
            self.response().sendRedirect('Logout')
        else:
            self.response().sendRedirect('Index')
