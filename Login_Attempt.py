from Template_Main import Template_Main

from z_account import authenticate, get_user_acct, hash_string, get_user_role
from z_constants import DIPLSTR, RESDSTR

class Login_Attempt (Template_Main):

    def writeContent(self):
        wr = self.writeln
        req = self.request()
        form = req.fields()
        ERROR = authenticate(form)
        if ERROR:
            wr('<h1 class="error">Login Failed</h1>')
            wr('<P>Here\'s why: %s</P>' % (ERROR))
            wr('<P>You can try again at the top of this page, or <a href="Login_Help">get some help</a>. </P>')

        else:
            username = form.get('username')
            userinfo = get_user_acct(username)
            # Set 10-year cookie.
            hvc = hash_string(userinfo.get('vcode'))
            ex1 = self.getCookieExpiry('maxAge', y=10)
            ex2 = self.getCookieExpiry('Expires', y=10)
            self.setCookie('username', username, ex1, ex2)
            self.setCookie('hash', hvc, ex1, ex2)
            possible_role = get_user_role(username)
            if possible_role:
                self.setCookie('role', possible_role, ex1, ex2)
#                if possible_role == RESDSTR:
#                    self.setCookie('g', 'r', ex1, ex2)
#                if possible_role == DIPLSTR:
#                    self.setCookie('g', 'd', ex1, ex2)

            # Redirect.
            from_url = form.get('from_url', '')
            if 'Login_Lookup' in from_url:
                from_url = 'Index'
            if not from_url:
                from_url = 'Index'

            self.response().sendRedirect(from_url)

