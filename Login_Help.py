from Template_Main import Template_Main

from z_forms import text, submit

class Login_Help (Template_Main):
    def title(self):
        return 'Need Help Logging In?'

    def writeContent(self):
        wr = self.writeln
        wr('<h1>%s</h1>' % (self.title()))
        wr('<P>It happens to the best of us.</P>')

        wr('<P>')
        wr('We can reset your password and email the new one to you.')
        wr('</P>')

        wr('<div style="margin-bottom: 30px;">')
        wr('<P>If you know your <em>ACVAA website username</em>, please enter it here:</P>')
        wr('<form method="POST" action="Login_Lookup">')
        wr(text('username', clss='input'))
        wr(submit('Reset Password'))
        wr('</form>')
        wr('</div>')

        wr('<div style="margin-bottom: 30px;">')
        wr('<P><em>If you do not remember your site username</em>, then you will have to contact an ACVAA site administrator to get things fixed.</P>')
        wr('</div>')
