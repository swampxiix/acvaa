from acva.Template_Main import Template_Main

class Index (Template_Main):
    def title(self):
        return 'The ACVAA Foundation'

    def sidebar(self):
        wr = self.writeln
        wr('''
<div class="sb"><div class="st">
<div class="t12b">Foundation</div>
<P><a href="/Foundation/">Introduction</a></P>
<P><a href="/Foundation/Donors">List of Donors</a></P>
</div></div>
            ''')


    def writeContent(self):
        wr = self.writeln
        wr('<h1>%s</h1>' % (self.title()))
        self.sidebar()

        wr('''
<h2>
The ACVAA Foundation at Work
</h2>

<p>
The ACVAA Foundation is pleased to accept applications for two travel scholarships for residents (up to $500 each). To apply please send <a href="/docs/candidates/ACVAA_Foundation_Scholarship_Application.doc">completed application</a>* and required attachments to <a href="mailto:execdir@acvaa.org">execdir@acvaa.org</a>.
<br />
<small>* 20kB Word document</small>
</p>

<h2>
Mission Statement
</h2>

<p>
The ACVAA Foundation supports research and training in the specialty of Veterinary Anesthesiology and Pain management. These critical areas of specialization benefit all Veterinary patients.
</p>
<p>
Specific goals of the foundation include:
<ol class="la">
<li> To support development of innovative approaches for anesthetic management or analgesic management of all animal species, by funding related research.
<li> Support Veterinarians in specialty training through grants for education-related travel.
</ol>
</p>
<p>
A standing committee will direct the activities of the Foundation, solicit and award research grants, and raise financial support both inside and outside ACVAA.
</p>

<h2>
Organization
</h2>
<p>
The Foundation is a committee of the ACVAA, which is an Internal Revenue Code Section 501(c)(3) charitable organization. 
</p>

<h2>
Funding
</h2>
<p>
NOW accepting donations. As a committee of a 501(c)(3) organization, the Foundation is eligible for tax-deductible contributions. If you would like more information about the ACVAA Foundation, or would like to make a donation, please contact <a href="mailto:ldonldsn@earthlink.net">Lydia Donaldson</a> or <a href="mailto:wilsondv@cvm.msu.edu">Debbie Wilson</a>. Directed donations to specific areas (research/resident travel) will be accepted. Contributions will be acknowledged to the donor and recognized annually in the Foundation’s annual report.
</p>

            ''')

