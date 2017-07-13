from Template_Authenticated import Template_Authenticated
from z_account import is_diplomate

class Scrubs (Template_Authenticated):

    def title(self):
        return "Order ACVAA Scrubs"

    def writeContent(self):
        wr = self.writeln
        req = self.request()
        IS_DIP = is_diplomate(req)
        if IS_DIP:
            wr('<h1>ACVAA Scrubs</h1>')
            wr('<div style="float: right;">')
            wr('<img src="/g/scrubs1.jpg"><br>')
            wr('<img src="/g/scrubs2.jpg">')
            wr('</div>')
            wr('''
<p>
To order scrubs with our custom logo (the two options are shown to the right), customers must register and log into the Veterinary Apparel Company website.
<ul>
<li> Here is their website: <a href="http://veterinaryapparel.com/">http://veterinaryapparel.com/</a>
<li> Register, and then log in.
<li> Click the "Scrubs" section in the menu bar at the top of the page to select the category of your desired apparel, then choose a product, size, and color (if necessary).
<li> Once on the product page, click the "Add Customization" button.
<li> On the next page, click the "Add" button in the "Custom Logo" section under "Customization Options". Note: This will add $6 to your order.
<li> Next, click in the square reading "Logo on file".
<li> In the special instructions, write "AC02AA" which is the account number for the logo. Or simply enter "ACVAA".
<li> To change the placement of the logo, click "Switch" under the photo of the model, or otherwise specify in the "Instructions" area.
<li> You can also specify the color of the embroidery (e.g., navy if on light-colored scrubs, or white on dark-colored scrubs) in the Instructions.
<li> Complete the order to provide shipping and payment information.
</ul>
<b>Note:</b> They do ship outside the U.S. At the upper-right-most corner of their website, click the "Ship to:" and American flag to select your desired shipping country.
</p> 
            ''')

        else:
            wr('<h1>Sorry.</h1><p>Scrubs are only available to ACVAA Diplomates.</p>')

