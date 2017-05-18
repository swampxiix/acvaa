from Template_Authenticated import Template_Authenticated
from z_wiley import get_journal_access

class Testing (Template_Authenticated):

    def title(self):
        return 'Access to the Journal'

    def writeContent(self):
        wr = self.writeln
        clickusername = self.request().cookies().get('username')
        accesslist = get_journal_access()
        if clickusername in accesslist:



            wr('''
<h1>Journal of Veterinary Anaesthesia &amp; Analgesia</h1>

<p>
Welcome! Access to <a href="http://www.vaajournal.org/">Veterinary Anaesthesia and Analgesia</a> is a benefit for Diplomates of the ACVAA. To personalize your experience on the journal site (save searches, view recent searches, and receive email alerts), you will need to log in to access your account or <a href="http://www.vaajournal.org/action/registration"> register</a> if you have not previously done so.
</p>

<p>
<!-- http://www.elsevierhost.com/journal_home.html?TPSTOKEN=encryptedtoken -->
</p>

            ''')
        else:
            wr('<h2>Sorry, but you do not have access to the Veterinary Anaesthesia and Analgesia journal.</h2>')
