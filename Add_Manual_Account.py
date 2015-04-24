from Template_Admin import Template_Admin
from z_account import save_manual_account
from z_constants import ALL_ROLES
from z_forms import text, select, hidden, passwd, submit, radio, radio_jq

class Add_Manual_Account (Template_Admin):
    def title(self):
        return 'Add Manual Account'

    def writeContent(self):
        un = self.request().cookies().get('username')
        global un
        wr = self.writeln
        qs = self.request().fields()
        if self.request()._environ.get('REQUEST_METHOD') == 'POST':
            wr(qs)
            save_manual_account(qs)
        else:
            wr('<h1>%s</h1>' % (self.title()))
            wr('''
<P><em>This form should only be used if the user will not need to log into the ACVAA website.</em></P>
<div id="acct-container" class="acct-tabs"> 

<h2>Contact Information</h2>
<form method="POST" action="Add_Manual_Account" class="form-inline" role="form">

<div class="form-group">
<label for="fn">First</label>
<input type="text" class="form-control" id="fn" name="fn" placeholder="Jane">
</div>

<div class="form-group">
<label for="mi">MI</label>
<input type="text" class="form-control" id="mi" name="mi" placeholder="Q." size="2">
</div>

<div class="form-group">
<label for="sn">Last</label>
<input type="text" class="form-control" id="sn" name="sn" placeholder="Doe">
</div>
<br>

<div class="form-group">
<label for="degrees">Degrees</label>
<input type="text" class="form-control" id="degrees" name="degrees" placeholder="Ph.D., MBA, MS, etc.">
</div>
<br>

<div class="form-group">
<label for="country">Country</label>
<input type="text" class="form-control" id="country" name="country" placeholder="">
</div>
<br>

<div class="form-group">
<label for="addr1">Addr 1</label>
<input type="text" class="form-control" id="addr1" name="addr1" placeholder="">
</div>

<div class="form-group">
<label for="addr2">Addr 2</label>
<input type="text" class="form-control" id="addr2" name="addr2" placeholder="">
</div>
<br>

<div class="form-group">
<label for="city">City</label>
<input type="text" class="form-control" id="city" name="city" placeholder="">
</div>

<div class="form-group">
<label for="state">State/Prov.</label>
<input type="text" class="form-control" id="state" name="state" placeholder="">
</div>

<div class="form-group">
<label for="zip">ZIP/Postal Code</label>
<input type="text" class="form-control" id="zip" name="zip" placeholder="">
</div>
<br>

<div class="form-group">
<label for="institution">Institution(s)</label>
<input type="text" class="form-control" id="institution" name="institution">
</div>
<br>

<div class="form-group">
<label for="birthyear">Born</label>
<input type="text" class="form-control" id="birthyear" name="birthyear" size="4">
</div>
<div class="form-group">
<label for="deathyear">Died</label>
<input type="text" class="form-control" id="deathyear" name="deathyear" size="4">
</div>
<br>
<div class="form-group">

                ''')

            for r in ALL_ROLES:
                wr('''
<label class="checkbox-inline">
  <input type="checkbox" id="%s" name="roles" value="%s"> %s
</label>
                    ''' % (r, r, r.capitalize()))
            wr('''
</div>
<br>
<input type="submit" value="Save Account" class="btn btn-orange">

</div><!-- acct-container -->
                ''')
