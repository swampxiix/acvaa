from Template_Authenticated import Template_Authenticated

from z_account import get_user_acct
from z_constants import DIPLSTR
from z_forms import text, select, hidden, passwd, submit, radio, radio_jq

class Testing (Template_Authenticated):
    def title(self):
        un = self.request().cookies().get('username')
        global un
        return '%s Account Information' % (un)

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()

        rolestr = self.request().cookies().get('role', '')
        IS_DIP = rolestr == DIPLSTR

        wr('<h1><em>%s</em> Account Information</h1>' % (un))

        if qs.get('pc'):
            self.render_special_msg('Password changed successfully.')
        if qs.get('ic'):
            self.render_special_msg('Contact info saved.')
        if qs.get('pv'):
            self.render_special_msg('Privacy settings saved.')
        if qs.get('fh'):
            self.render_special_msg('Consultancy setting saved.')

        p = get_user_acct(un)

        wr('''

<div role="tabpanel">

<!-- Nav tabs -->
<ul class="nav nav-pills nav-justified" role="tablist">
<li role="presentation" class="active"><a href="#contact-page" aria-controls="Contact Info" role="tab" data-toggle="tab">Contact Info</a></li>
<li role="presentation"><a href="#password-page" aria-controls="Change Password" role="tab" data-toggle="tab">Change Password</a></li>
<li role="presentation"><a href="#privacy-page" aria-controls="Privacy Settings" role="tab" data-toggle="tab">Privacy Settings</a></li>
            ''')

        if IS_DIP:
            wr('<li role="presentation"><a href="#forhire-page" aria-controls="For Hire?" role="tab" data-toggle="tab">For Hire?</a></li>')

        wr('''
</ul><!-- .nav .nav-pills -->

<div id="acct-container" class="acct-tabs">

<!-- Tab panes -->
<div class="tab-content">
            ''')

        ######################################################

        wr('''
<div role="tabpanel" class="tab-pane active" id="contact-page">
<h2>Your Contact Information</h2>
<form method="POST" action="Acct_Edit_Info" class="form-inline" role="form">
<input type="hidden" name="form_username" value="%s">
<input type="hidden" name="form_hash" value="%s">
            ''' % (un, self.request().cookies().get('hash')))

        wr('''
<div class="form-group">
<label for="fn">First</label>
<input type="text" class="form-control" id="fn" name="fn" value="%s">
</div>
            ''' % ( p.get('fn', '') ))
        wr('''
<div class="form-group">
<label for="mi">MI</label>
<input type="text" class="form-control" id="mi" name="mi" value="%s" size="2">
</div>
            ''' % ( p.get('mi', '') ))
        wr('''
<div class="form-group">
<label for="sn">Last</label>
<input type="text" class="form-control" id="sn" name="sn" value="%s">
</div>
<br>
            ''' % ( p.get('sn', '') ))
        wr('''
<div class="form-group">
<label for="degrees">Degrees Held</label>
<input type="text" class="form-control" id="degrees" name="degrees" value="%s">
</div>
<br>
            ''' % ( p.get('degrees', '') ))
        wr('''
<div class="form-group">
<label for="country">Country</label>
<input type="text" class="form-control" id="country" name="country" value="%s">
</div>
<br>
            ''' % ( p.get('country', '') ))
        wr('''
<div class="form-group">
<label for="addr1">Addr 1</label>
<input type="text" class="form-control" id="addr1" name="addr1" value="%s">
</div>
            ''' % ( p.get('addr1', '') ))
        wr('''
<div class="form-group">
<label for="addr1">Addr 2</label>
<input type="text" class="form-control" id="addr2" name="addr2" value="%s">
</div>
<br>
            ''' % ( p.get('addr2', '') ))
        wr('''
<div class="form-group">
<label for="city">City</label>
<input type="text" class="form-control" id="city" name="city" value="%s">
</div>
            ''' % ( p.get('city', '') ))
        wr('''
<div class="form-group">
<label for="state">State/Prov.</label>
<input type="text" class="form-control" id="state" name="state" value="%s">
</div>
            ''' % ( p.get('state', '') ))
        wr('''
<div class="form-group">
<label for="zip">ZIP/Postal Code</label>
<input type="text" class="form-control" id="zip" name="zip" value="%s">
</div>
<br>
            ''' % ( p.get('zip', '') ))
        wr('''
<div class="form-group">
<label for="zip">Email</label>
<input type="email" class="form-control" id="email" name="email" value="%s">
</div>
<br>
<input type="hidden" name="original_email" value="%s">
            ''' % ( p.get('email', ''), p.get('email', '') ))
        wr('''
<div class="form-group">
<label for="zip">Phone</label>
<input type="text" class="form-control" id="phone" name="phone" value="%s">
</div>
<br>
            ''' % ( p.get('phone', '') ))
        wr('''
<div class="form-group">
<label for="zip">Fax</label>
<input type="text" class="form-control" id="fax" name="fax" value="%s">
</div>
<br>
            ''' % ( p.get('fax', '') ))
        wr('''
<div class="form-group">
<label for="institution">Institution(s)</label>
<input type="text" class="form-control" id="institution" name="institution" value="%s">
</div>
<br>
            ''' % ( p.get('institution', '') ))

        if 'honorary' in p.get('roles', []):
            wr('''
<div class="form-group">
<label for="conferred">Honorary Diplomate Year Conferred</label>
<input type="text" class="form-control" id="conferred" name="conferred" value="%s">
</div>
<br>
                ''' % ( p.get('conferred', '') ))

        if 'memoriam' in p.get('roles', []):
            wr('''
<div class="form-group">
<label for="birthyear">In Memoriam: Born</label>
<input type="text" class="form-control" id="birthyear" name="birthyear" value="%s" size="4">
</div>
<div class="form-group">
<label for="deathyear">Died</label>
<input type="text" class="form-control" id="deathyear" name="deathyear" value="%s" size="4">
</div>
<br>
                ''' % ( p.get('birthyear', ''), p.get('deathyear', '') ))

        wr('''
<input type="submit" value="Save Contact Info" class="btn btn-orange">
</form>
</div><!-- #contact-page -->
            ''')

        ######################################################
        wr('''
<div role="tabpanel" class="tab-pane" id="password-page">
<h2>Change Your Password</h2>
<p>If you wish to keep your current password, you shouldn\'t do anything here.</p>
<form method="POST" action="Acct_Change_Pass" class="form-inline" role="form">
<input type="hidden" name="form_username" value="%s">
<input type="hidden" name="form_hash" value="%s">
<p>Enter your new password twice:</p>
            ''' % (un, self.request().cookies().get('hash')))

        wr('''
<div class="form-group">
<label for="pw1">Password</label>
<input type="password" class="form-control" id="pw1" name="pw1" value="">
</div>
<br>
<div class="form-group">
<label for="pw2">Password</label>
<input type="password" class="form-control" id="pw2" name="pw2" value="">
</div>
<br>
<input type="submit" value="Change Password" class="btn btn-orange">
</form>
</div><!-- #password-page -->
            ''')

        ######################################################
        # radio_jq (name, value='', clss='', id='', checked=False)

        wr('''
<div role="tabpanel" class="tab-pane" id="privacy-page">
<h2>Your Privacy Settings</h2>
<p>Your current privacy settings are shown below. Change them as you see fit.</p>
<form method="POST" action="Acct_Change_Privacy" class="form-inline" role="form">
<input type="hidden" name="form_username" value="%s">
<input type="hidden" name="form_hash" value="%s">
            ''' % (un, self.request().cookies().get('hash')))
        wr('''
<fieldset>
<legend>Please select your overall security posture:</legend>
<div class="radio">
  <label for="sec-paranoid">
    %s Hide all my information from everyone
  </label>
</div>
            ''' % (radio_jq('sec_policy', 'paranoid', '', 'sec-paranoid', (p.get('sec_policy')=='paranoid'))))
        wr('''
<div class="radio">
  <label for="sec-permissive">
    %s Display some of my information, specified below
  </label>
</div>
</fieldset>
            ''' % (radio_jq('sec_policy', 'permissive', '', 'sec-permissive', (p.get('sec_policy')=='permissive'))))

        # ------------------------------------------------------

        wr('''
<fieldset>
<legend class="sec-legend">Who should be allowed to view your full postal address?</legend>
<div class="radio">
  <label for="hide1">
    %s Nobody; show only my city &amp; state
  </label>
</div>
<br>
            ''' % (radio_jq('show_address', 'hide', 'sec-sub', 'hide1', (p.get('show_address')=='hide'))))
        wr('''
<div class="radio">
  <label for="dips1">
    %s ACVAA Diplomates only
  </label>
</div>
<br>
            ''' % (radio_jq('show_address', 'diplomates', 'sec-sub', 'dips1', (p.get('show_address')=='diplomates'))))
        wr('''
<div class="radio">
  <label for="both1">
    %s ACVAA Diplomates &amp; Candidates
  </label>
</div>
<br>
            ''' % (radio_jq('show_address', 'both', 'sec-sub', 'both1', (p.get('show_address')=='both'))))
        wr('''
<div class="radio">
  <label for="all1">
    %s Everyone, even the general public
  </label>
</div>
</fieldset>
            ''' % (radio_jq('show_address', 'all', 'sec-sub', 'all1', (p.get('show_address')=='all'))))

        # ------------------------------------------------------
        wr('''
<fieldset>
<legend class="sec-legend">Who should be allowed to view your email address?</legend>

<div class="radio">
  <label for="hide2">
    %s Nobody
  </label>
</div>
<br>
            ''' % (radio_jq('show_email', 'hide', 'sec-sub', 'hide2', (p.get('show_email')=='hide'))))
        wr('''
<div class="radio">
  <label for="dips2">
    %s ACVAA Diplomates only
  </label>
</div>
<br>
            ''' % (radio_jq('show_email', 'diplomates', 'sec-sub', 'dips2', (p.get('show_email')=='diplomates'))))
        wr('''
<div class="radio">
  <label for="both2">
    %s ACVAA Diplomates &amp; Candidates
  </label>
</div>
<br>
            ''' % (radio_jq('show_email', 'both', 'sec-sub', 'both2', (p.get('show_email')=='both'))))
        wr('''
<div class="radio">
  <label for="all2">
    %s Everyone, even the general public
  </label>
</div>
</fieldset>
            ''' % (radio_jq('show_email', 'all', 'sec-sub', 'all2', (p.get('show_email')=='all'))))

        # ------------------------------------------------------

        wr('''
<fieldset>
<legend class="sec-legend">Who should be allowed to view your phone &amp; fax numbers?</legend>

<div class="radio">
  <label for="hide3">
    %s Nobody
  </label>
</div>
<br>
            ''' % (radio_jq('show_numbers', 'hide', 'sec-sub', 'hide3', (p.get('show_numbers')=='hide'))))
        wr('''
<div class="radio">
  <label for="dips3">
    %s ACVAA Diplomates only
  </label>
</div>
<br>
            ''' % (radio_jq('show_numbers', 'diplomates', 'sec-sub', 'dips3', (p.get('show_numbers')=='diplomates'))))
        wr('''
<div class="radio">
  <label for="both3">
    %s ACVAA Diplomates &amp; Candidates
  </label>
</div>
<br>
            ''' % (radio_jq('show_numbers', 'both', 'sec-sub', 'both3', (p.get('show_numbers')=='both'))))
        wr('''
<div class="radio">
  <label for="all3">
    %s Everyone, even the general public
  </label>
</div>
</fieldset>
<br>
<input type="submit" value="Save Privacy Settings" class="btn btn-orange">
</form>
</div><!-- #privacy-page -->
            ''' % (radio_jq('show_numbers', 'all', 'sec-sub', 'all3', (p.get('show_numbers')=='all'))))

        ######################################################

        if IS_DIP:
            wr('''
<div role="tabpanel" class="tab-pane" id="forhire-page">
<h2>For Hire?</h2>
<p>Control whether or not you wish to be listed in our "Consultants for Hire" section, which is intended to help other vets connect with ACVAA members.</p>
                ''')
            if p.get('sec_policy')=='paranoid':
                wr('''
<p>Unfortunately, you have selected to hide all your information. You must <em>adjust your privacy settings</em> to allow some information about you be available to the public before you can be included in the "Consultants for Hire" list.</p>
                    ''')
            else:
                wr('''
<form method="POST" action="Acct_Change_Hire" class="form-inline" role="form">
<input type="hidden" name="form_username" value="%s">
<input type="hidden" name="form_hash" value="%s">
                    ''' % (un, self.request().cookies().get('hash')))

                wr('''
<fieldset>
<legend class="sec-legend">Do you wish to be listed as a Consultant for Hire?</legend>

<div class="radio">
  <label for="for-hire-yes">
    %s Yes, that would be fantastic.
  </label>
</div>
<br>
                    ''' % (radio_jq('show_for_hire', 'yes', 'sec-sub', 'for-hire-yes', (p.get('show_for_hire')=='yes'))))
                wr('''
<div class="radio">
  <label for="for-hire-no">
    %s No.
  </label>
</div>
</fieldset>
                    ''' % (radio_jq('show_for_hire', 'no', 'sec-sub', 'for-hire-no', (p.get('show_for_hire')!='yes'))))
                wr('''
<div id="for-hire-extra-info">
  <div>
    <b>What geographic area(s) do you serve?</b><br />
    <textarea name="for_hire_areas" class="form-control" rows="3" cols="60">%s</textarea>
  </div>
                    ''' % (p.get('for_hire_areas', '')))
                wr('''
  <div>
    <b>What services do you provide?</b><br />
    <textarea name="for_hire_services" class="form-control" rows="3" cols="60">%s</textarea>
  </div>
                    ''' % (p.get('for_hire_services', '')))
                wr('''
  <div>
    <div class="form-group">
      <label for="for_hire_url">If you have a website, provide it here:</label><br>
      <input type="text" class="form-control" id="for_hire_url" name="for_hire_url" value="%s">
    </div>
  </div>
</div><!-- #for-hire-extra-info -->

<br>
<input type="submit" value="Save Consultancy Status" class="btn btn-orange">
</form>
</div><!-- #forhire-page -->

</div><!-- tab-content -->
</div><!-- acct-container -->
</div><!-- tabpanel -->
                    ''' % (p.get('for_hire_url', '')))
