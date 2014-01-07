from Template_Admin import Template_Admin
from z_account import get_user_acct, hash_string

class UM_Act_as_User (Template_Admin):

    def writeContent(self):
        wr = self.writeln
        req = self.request()
        form = req.fields()
        username = form.get('u')
#        wr(username)
        userinfo = get_user_acct(username)
#        wr(userinfo)
        hvc = hash_string(userinfo.get('vcode'))
#        wr(hvc)
        ex1 = self.getCookieExpiry('maxAge', y=10)
        ex2 = self.getCookieExpiry('Expires', y=10)
        self.setCookie('username', username, ex1, ex2)
        self.setCookie('hash', hvc, ex1, ex2)
        self.setCookie('actingasuser', 'true', ex1, ex2)
        self.response().sendRedirect("Index")

