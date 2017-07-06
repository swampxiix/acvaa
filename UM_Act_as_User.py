from Template_Admin import Template_Admin
from z_account import get_user_acct, hash_string, get_user_role

class UM_Act_as_User (Template_Admin):

    def writeContent(self):
        wr = self.writeln
        req = self.request()
        form = req.fields()
        username = form.get('u')
        userinfo = get_user_acct(username)
        possible_role = get_user_role(username)
        hvc = hash_string(userinfo.get('vcode', ''))
        ex1 = self.getCookieExpiry('maxAge', y=10)
        ex2 = self.getCookieExpiry('Expires', y=10)
        self.setCookie('username', username, ex1, ex2)
        self.setCookie('hash', hvc, ex1, ex2)
        self.setCookie('role', possible_role, ex1, ex2)
        self.setCookie('actingasuser', 'true', ex1, ex2)
        self.response().sendRedirect("Index")

