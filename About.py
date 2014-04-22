from Template_Main import Template_Main

class About (Template_Main):
    def title(self):
        return 'About the ACVAA'

    def writeContent(self):
        wr = self.writeln
        wr('<h1>%s</h1>' % (self.title()))

        wr('''
<div style="margin-top: 30px;">
<h2>
ACVAA Constitution &amp; Bylaws
</h2>
<div style="padding-left: 20px;">
<p>
<img src="/g/word_icon.png" width="16" height="16" alt="MSWord" />
<a href="/docs/ACVA_Constitution_Bylaws_2009.doc">Download the Microsoft Word document</a> (131 kB).
</p>
</div>
</div>

<div style="margin-top: 30px;">
<h2>
<a href="/docs/History">History of the ACVAA</a>
</h2>
</div>

<div style="margin-top: 30px;">
<h2>
ACVAA Standards
</h2>
<div style="padding-left: 20px;">

<h3>
Position Statements
</h3>
<P><a href="/docs/Pain_Treatment">Position Statement: The Treatment of Pain in Animals</a></P>
<P><a href="/docs/Waste_Gas">Position Statement: Control of Waste Anesthetic Gases in the Workplace</a></P>

<h3 style="color: #647382;">
Residency Training Standards
</h3>
<p>
<img src="/g/word_icon.png" width="16" height="16" alt="MSWord" />
<a href="/docs/diplomates/ACVAA_Residency_Training_Standards_2014_final.doc">Download the Microsoft Word document</a> (193 kB).
</p>
</div>
</div>

            ''')

