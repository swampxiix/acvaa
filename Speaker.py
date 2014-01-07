from Template_Main import Template_Main

class Speaker (Template_Main):

    def title(self):
        return 'ACVAA: Care for your Pet'

    def writeContent(self):
        wr = self.writeln

        wr('''

<h1>
Need an ACVAA Speaker?
</h1>

<P>
If you would like an ACVAA diplomate to speak at your conference or seminar, please send an <a href="mailto:execdir@acva.org">email to the ACVAA's executive secretary</a> for more information.
</P>

<div style="margin-bottom: 400px;">
&nbsp;
</div>

            ''')



