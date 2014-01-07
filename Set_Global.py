from Template_Main import Template_Main

from z_account import is_logged_in, is_site_admin
from z_constants import DIPLSTR, RESDSTR

class Set_Global (Template_Main):
    def title(self):
        return 'American College of Veterinary Anesthesia and Analgesia'

    def writeContent(self):
        wr = self.writeln
        req = self.request()
        ILI = is_logged_in(req)
        rolestr = self.request().cookies().get('role', '')
        IS_RES = rolestr == RESDSTR
        IS_DIP = rolestr == DIPLSTR
        qs = req.fields()
        g = qs.get('g')
        ISA = is_site_admin(self.request())

        ERROR = None

        if ISA:
            pass
        else:
            if g == 'd':
                if ILI:
                    if IS_DIP:
                        pass
                    else:
                        ERROR = 'You are not a Diplomate.'
                else:
                    ERROR = 'You are not logged in.'

            elif g == 'r':
                if ILI:
                    if (IS_DIP or IS_RES):
                        pass
                    else:
                        ERROR = 'You are neither a Candidate nor a Diplomate.' # this should never happen
                else:
                    ERROR = 'You are not logged in.'

        if ERROR:
            wr('<h1 class="error">Sorry.</h1>')
            wr('<P>You cannot access this section of the ACVAA website for the following reason:</P>')
            wr('<P>%s</P>' % ERROR)

        else:
            ex1 = self.getCookieExpiry('maxAge', y=10)
            ex2 = self.getCookieExpiry('Expires', y=10)
            self.setCookie('g', g, ex1, ex2)
            from_url = qs.get('from_url', '/')
            self.response().sendRedirect(from_url)

