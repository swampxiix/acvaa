from acva.Template_Main import Template_Main

class Position_Statements (Template_Main):
    def title(self):
        return "ACVA Position Statements"

    def writeContent(self):
        wr = self.writeln
        wr('<h1>%s</h1>'% (self.title()))
        wr('''

<p>
<a href="/docs/Anesthesia_Free_Dentistry.pdf">Anesthesia-Free Dentistry</a>
<img src="/g/pdf_icon.png" alt="PDF">
</p>

<p>
<a href="/docs/2013_ACVAA_Waste_Anesthetic_Gas_Recommendations.pdf">Control of Waste Anesthetic Gases in the Workplace</a>
<img src="/g/pdf_icon.png" alt="PDF">
</p>

<p>
<a href="/docs/Non_Discrimination_Statement.pdf">Non-Discrimination Statement</a>
<img src="/g/pdf_icon.png" alt="PDF">
</p>

<p>
<a href="/docs/ACVAA_Statement_of_Inclusiveness.pdf">Statement of Inclusiveness</a>
<img src="/g/pdf_icon.png" alt="PDF">
</p>

<p>
<a href="/docs/Training_Process_and_Role_of_an_ACVAA_Diplomate.pdf">Training Process and Role of an ACVAA Diplomate</a>
<img src="/g/pdf_icon.png" alt="PDF">
</p>

<p>
<a href="/docs/Pain_Treatment">The Treatment of Pain in Animals</a>
</p>

            ''')