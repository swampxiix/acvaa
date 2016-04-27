from acva.Template_Authenticated import Template_Authenticated

class Dues (Template_Authenticated):
    def title(self):
        return "ACVAA Diplomate Dues"

    def writeContent(self):
        wr = self.writeln

        wr('''
<div class="sb"><div class="st">
<div class="t12b">Pay Dues Here</div>

<p>
You can pay dues with your credit card using either authorize.net or PayPal.
</p>

<!-- (c) 2005, 2016. Authorize.Net is a registered trademark of CyberSource Corporation --> <div class="AuthorizeNetSeal" style="float: right;"> <script type="text/javascript" language="javascript">var ANS_customer_id="b88e90b2-8a42-4860-8c46-ee32d10f8f87";</script> <script type="text/javascript" language="javascript" src="//verify.authorize.net/anetseal/seal.js" ></script></div>	

<p>
<b>Authorize.net</b> (preferred)
<br>
<form name="PrePage" method="post" action="https://Simplecheckout.authorize.net/payment/CatalogPayment.aspx"><input type="hidden" name="LinkId" value ="3dd447cc-5f1b-4d05-8643-c1acfb842d85" /><input type="submit" value="Pay Dues Now" /></form>
<br><br>
</p>

<P>
<b>PayPal</b>
<br>
<a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=37LAHDVSLLY78" title="Pay ACVAA Dues Now"><img src="/g/btn_payduesCC_LG.png" alt="Pay ACVAA Dues Now" width="171" height="47" border="0"></a>
</P>

<P style="text-align: center;">
<br><br>
<script type='text/javascript' src='https://www.rapidscansecure.com/siteseal/siteseal.js?code=65,47C2D86FE467831D0F4862EEE1AA7EC87A3BB6F5'></script>
</P>

</div></div>
            ''')




        wr('<h1>%s</h1>' % (self.title()))
        wr('''

<P><b>Amount</b>: for 2016 = <b>$450</b></P>
<P><b>Due</b>: April 1, 2016</P>
<P><b>Methods of Payment</b>:
<ol><li> Check made out to ACVAA and mailed to the ACVAA Executive Secretary.
<li> Credit Card by communicating the Visa or MasterCard numbers and expiration date to the Executive Secretary.
<li> PayPal by clicking on the "Pay Dues" button on this page. This will take you to a payment authorization site which will allow you to pay your dues either with a credit card (Visa, MasterCard, American Express or Discover) or through a PayPal Account.
</P>
<P><b>Executive Secretary</b>: Dr. Lydia Donaldson, P.O. Box 1100, Middleburg, VA 20118</P>
<blockquote>
<h2>ACVAA Bylaws, Article VI - Dues</h2>
<P>
<u>Section 1</u> &mdash; Annual dues for members of the College become <u>payable January 1 of each calendar year</u>. Any proposed change in the amount shall be recommended by the Board of Directors and approved by a majority vote of the attending Diplomates at the annual business meeting. A written notice of the proposed change must be sent to all Diplomates thirty days prior to the annual business meeting. 
</P>
<P>
<u>Section 2</u> &mdash; A notice of pending delinquency will be sent to members in arrears on <u>April 1</u>. Dues are delinquent <u>July 1</u> and, <u>if not paid by December 31 of the same year, membership in the College will become inactive</u>, but only after notification of the diplomate in question by registered mail, return receipt requested. A <u>fine of $50</u> will be added to annual dues paid <u>after October</u> of the same year.
</P>
<P>
<u>Section 3</u> &mdash; Reactivation of membership will require petition to the Executive Secretary including payment of all delinquent dues and fines and approval by a majority of the Board of Directors.
</P>
</blockquote>

<P>
Please also consider a donation to the <a href="http://acvaa.org/Foundation/">ACVAA Foundation</a>. Contributions of any amount are welcome and can be made by check, Visa or MasterCard as above or by PayPal through the "Donate" link on the ACVAA Foundation page of this website.
</P>

<P class="hint">
The ACVAA is a tax-exempt, 501(c)(3), charitable (509(a)(2) organization, EIN 58-156357, qualified to receive tax deductible contributions under sections 170, 2055 & 2522 of the Internal Revenue Code. 
</P>







        ''')