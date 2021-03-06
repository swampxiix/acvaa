from Template_Authenticated import Template_Authenticated
from z_wiley import get_journal_access
from z_elsevier import get_query_string

class Journal (Template_Authenticated):

    def title(self):
        return 'Access to the Journal'

    def writeContent(self):
        wr = self.writeln
        clickusername = self.request().cookies().get('username')
        accesslist = get_journal_access()
        if clickusername in accesslist:

            qs = get_query_string()

            wr('''
<h1>Journal of Veterinary Anaesthesia &amp; Analgesia</h1>

<div style="float: right; padding-left: 10px;">
<a href="http://www.vaajournal.org/?%s"><img src="/g/journal_big.jpg"></a>
</div>

<p>
Welcome! Access to <a href="http://www.vaajournal.org/?%s">Veterinary Anaesthesia and Analgesia</a> is a benefit for Diplomates of the ACVAA. You do not have to create an account on the Elsevier site to enjoy access. Click the image of the journal.
</p>

<p>
To personalize your experience on the journal site (save searches, view recent searches, and receive email alerts), you will need to log into your existing Elsevier account or <a href="http://www.vaajournal.org/action/registration">create a new account on the Elsevier website*</a>. This is not required for journal access.
</p>

<p>
* Any Elsevier account you create is separate from your account on the ACVAA website; no information is shared between the two.
</p>
            ''' % ( qs, qs ))
        else:
            wr('<h2>Sorry, but you do not have access to the Veterinary Anaesthesia and Analgesia journal.</h2>')
