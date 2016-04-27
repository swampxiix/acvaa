from acva.Template_Main import Template_Main
from acva.z_account import is_site_admin
from z_found import show_travel

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

<p>
You can make donations via authorize.net or PayPal.
</p>

<!-- (c) 2005, 2016. Authorize.Net is a registered trademark of CyberSource Corporation --> <div class="AuthorizeNetSeal" style="float: right;"> <script type="text/javascript" language="javascript">var ANS_customer_id="b88e90b2-8a42-4860-8c46-ee32d10f8f87";</script> <script type="text/javascript" language="javascript" src="//verify.authorize.net/anetseal/seal.js" ></script></div>	

<p>
<b>Authorize.net</b> (preferred)
<br>
<form name="PrePage" method="post" action="https://Simplecheckout.authorize.net/payment/CatalogPayment.aspx"><input type="hidden" name="LinkId" value ="c942dc85-fdf8-42e6-a86a-1001f994af4c" /><input type="image" src ="//content.authorize.net/images/donate-gold.gif" /></form>
<br><br>
</p>

<P>
<b>PayPal</b>
<br>
<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=UYE3G92TAWBYA" title="Donate to the ACVAA Foundation"><img src="/g/btn_donateCC_LG.gif" alt="Donate to the ACVAA Foundation" width="147" height="47" border="0"></a>
</P>

<P style="text-align: center;">
<br><br>
<script type='text/javascript' src='https://www.rapidscansecure.com/siteseal/siteseal.js?code=65,47C2D86FE467831D0F4862EEE1AA7EC87A3BB6F5'></script>
</P>

</div></div>''')


    def writeContent(self):
        wr = self.writeln

        ISA = is_site_admin(self.request())
        if ISA:
            wr('<div class="flt_r">')
            if show_travel():
                wr('<a class="btn btn-warning" href="Change_Travel" role="button">Hide Scholarship Info</a>')
            else:
                wr('<a class="btn btn-success" href="Change_Travel" role="button">Show Scholarship Info</a>')
            wr('</div>')


        wr('<h1>%s</h1>' % (self.title()))
        self.sidebar()

        if show_travel():
            wr('''
<h2>
The ACVAA Foundation at Work
</h2>

<p>
The ACVAA Foundation is pleased to accept applications for two travel scholarships for residents (up to $500 each). To apply please send <a href="/docs/candidates/ACVAA_Foundation_Scholarship_Application.doc">completed application</a>* and required attachments to <a href="mailto:execdir@acvaa.org">execdir@acvaa.org</a>.
<br />
<small>* 20kB Word document</small>
</p>
            ''')

        wr('''
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
NOW accepting donations. As a committee of a 501(c)(3) organization, the Foundation is eligible for tax-deductible contributions. If you would like more information about the ACVAA Foundation, or would like to make a donation, please contact <a href="mailto:ldonldsn@earthlink.net">Lydia Donaldson</a> or <a href="mailto:wilsondv@cvm.msu.edu">Debbie Wilson</a>. Directed donations to specific areas (research/resident travel) will be accepted. Contributions will be acknowledged to the donor and recognized annually in the Foundation's annual report.
</p>''')

