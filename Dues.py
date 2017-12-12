from acva.Template_Authenticated import Template_Authenticated
from z_execsec import NAME, ADDRESS
from z_times import get_year

class Dues (Template_Authenticated):
    def title(self):
        return "ACVAA Diplomate Dues"

    def writeContent(self):
        wr = self.writeln
        nowyear = get_year()
        wr('''
<div class="sb"><div class="st">
<div class="t12b">Pay Dues Here</div>

<p>
You can pay dues with your credit card using PayPal.
</p>

<P>
<b>PayPal</b>
<br>
<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=37LAHDVSLLY78" title="Pay ACVAA Dues Now"><img src="/g/btn_payduesCC_LG.png" alt="Pay ACVAA Dues Now" width="171" height="47" border="0"></a>
</P>

</div></div>
            ''')




        wr('<h1>%s</h1>' % (self.title()))
        wr('''

<P><b>Amount</b>: <b>$450</b></P>
<P><b>Due</b>: January&ndash;March (see the bylaws below)</P>
<P><b>Methods of Payment</b>:
<ol><li> Check made out the ACVAA and mailed to the ACVAA Executive Secretary
<li> PayPal by clicking on the "make a payment" button on this page to pay with credit card or an existing PayPal account you may have.
<li> If any questions about payment, please contact the ACVAA Secretary at <a href="mailto:execdir@acvaa.org">execdir@acvaa.org</a>
</ol>
</P>
<P><b>Executive Secretary</b>: %s: %s</P>
<blockquote>
<h2>ACVAA Bylaws, Article VI
<br>
Dues</h2>
<P>
<u>Section 1</u> &mdash; Annual dues for members of the College become payable on or before January 1 of each calendar year. Any proposed change in the amount shall be recommended by the Board of Directors and approved by a majority vote of the attending Diplomates at the annual business meeting. A written notice of the proposed change must be sent to all Diplomates thirty days prior to the annual business meeting.
</P>
<P>
<u>Section 2</u> &mdash; Email reminders of the date for annual dues payment will be sent by the Executive Secretary/Administrator in January, February, and March of that year. An email notice of pending delinquency will be sent to individual members who have not paid the current year's annual dues by April 1. Dues are considered delinquent July 1, and membership in the College will become inactive, but only after notification of the diplomate in question by registered mail, return receipt requested. If the diplomate cannot be reached or response received by registered mail has failed alternate methods of contact including attempts by phone at the last known contact number should be made before the diplomate is placed in inactive status. It is a diplomate's responsibility to maintain current contact information with the Executive Secretary/Administrator.  A fine of $50 will be added to annual dues paid after April 1 of the same year.
</P>

<h2>Constitution Article V
<br>
Membership and Qualifications</h2>
<P>
Section 2,e<br>
Inactive Diplomate<br>
e.<br>
</P>
<P>
A Diplomate will be deemed inactive upon non-payment of annual dues to the ACVAA. Dues are considered delinquent if not paid by July 1 of that calendar year. 
</P>
</blockquote>

<P>
See the ACVAA Constitution and Bylaws for more description of "inactive status". 
</P>

<P>
Please also consider a donation to the <a href="http://acvaa.org/Foundation/">ACVAA Foundation</a>. Contributions of any amount are welcome and can be made by check, Visa or MasterCard as above or by Authorize.net and PayPal through the "Donate" buttons on the <a href="http://acvaa.org/Foundation/">ACVAA Foundation page</a> of this website.
</P>

<P class="hint">
The ACVAA is a tax-exempt, 501(c)(3), charitable (509(a)(2) organization, EIN 58-156357, qualified to receive tax deductible contributions under sections 170, 2055 & 2522 of the Internal Revenue Code. 
</P>







        ''' % (NAME, ADDRESS))