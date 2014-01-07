from Template_Authenticated import Template_Authenticated

from z_account import get_user_acct
from z_constants import DIPLSTR
from z_forms import text, select, hidden, passwd, submit, radio, radio_jq

class Account (Template_Authenticated):
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

        wr('<div id="acct-container" class="acct-tabs"> ')
        wr('<ul class="idTabs">')
        wr('<li><a class="selected" href="#tab1">Contact Info</a></li> ')
        wr('<li><a href="#tab2">Change Password</a></li> ')
        wr('<li><a href="#tab3">Privacy Settings</a></li> ')
        if IS_DIP:
            wr('<li><a href="#tab4">For Hire?</a></li> ')
        wr('</ul> ')
        ######################################################
        wr('<div id="tab1">')
        wr('<h2>Your Contact Information</h2>')
        wr('<form method="POST" action="Acct_Edit_Info">')
        wr(hidden('form_username', un))
        wr(hidden('form_hash', self.request().cookies().get('hash')))
        wr('<div><table id="contact_info">')
        wr('<tr><td><label>First</label>')
        wr('<td>%s' % (text('fn', p.get('fn', ''), 'input')))
        wr('<td class="req">required')
        wr('<tr><td><label>MI</label>')
        wr('<td>%s' % (text('mi', p.get('mi', ''), 'input', 2)))
        wr('<tr><td><label>Last</label>')
        wr('<td>%s' % (text('sn', p.get('sn', ''), 'input')))
        wr('<td class="req">required')
        wr('<tr><td><label>Degrees Held</label>')
        wr('<td>%s' % (text('degrees', p.get('degrees', ''), 'input', 6)))
        wr('<td class="hint">(e.g., Ph.D., MBA, MS, etc.)')
        wr('<tr><td><label>Country</label>')
        wr('<td>%s' % (text('country', p.get('country', ''), 'input')))
        wr('<td class="req">required')
        wr('<tr><td><label>Addr 1</label>')
        wr('<td>%s' % (text('addr1', p.get('addr1', ''), 'input')))
        wr('<tr><td><label>Addr 2</label>')
        wr('<td>%s' % (text('addr2', p.get('addr2', ''), 'input')))
        wr('<tr><td><label>City</label>')
        wr('<td>%s' % (text('city', p.get('city', ''), 'input')))
        wr('<td class="req">required')
        wr('<tr><td><label>State/Prov.</label>')
        wr('<td>%s' % (text('state', p.get('state', ''), 'input')))
        wr('<td class="req">required')
        wr('<tr><td><label>ZIP/Postal Code</label>')
        wr('<td>%s' % (text('zip', p.get('zip', ''), 'input', 6)))
        wr('<tr><td><label>Email</label>')
        wr(hidden('original_email', p.get('email', '')))
        wr('<td>%s' % (text('email', p.get('email', ''), 'input')))
        wr('<td class="req">required')
        wr('<tr><td><label>Phone</label>')
        wr('<td>%s' % (text('phone', p.get('phone', ''), 'input')))
        wr('<tr><td><label>Fax</label>')
        wr('<td>%s' % (text('fax', p.get('fax', ''), 'input')))
        wr('<tr><td colspan="3">')
        wr(submit('Save Contact Info'))
        wr('</table></div>')
        wr('</form>')
        wr('</div><!-- tab1 -->')
        ######################################################
        wr('<div id="tab2">')
        wr('<h2>Change Your Password</h2>')
        wr('<div>If you wish to keep your current password, you shouldn\'t do anything here.</div>')
        wr('<form method="POST" action="Acct_Change_Pass">')
        wr(hidden('form_username', un))
        wr(hidden('form_hash', self.request().cookies().get('hash')))
        wr('<div>Enter your new password twice:</div>')
        wr('<div>%s</div>' % ( passwd('pw1', '', 'input', 24) ))
        wr('<div>%s</div>' % ( passwd('pw2', '', 'input', 24) ))
        wr('<div>%s</div>' % ( submit('Change Password') ))
        wr('</form>')
        wr('</div><!-- tab2 -->')
        ######################################################
        # radio_jq (name, value='', clss='', id='', checked=False)
        wr('<div id="tab3">')
        wr('<h2>Your Privacy Settings</h2>')
        wr('<div>Your current privacy settings are shown below. Change them as you see fit.</div>')
        wr('<form method="POST" action="Acct_Change_Privacy">')
        wr(hidden('form_username', un))
        wr(hidden('form_hash', self.request().cookies().get('hash')))
        wr('<div><table id="contact_info">')
        # ------------------------------------------------------
        wr('<fieldset>')
        wr('<legend>Please select your overall security posture:</legend>')
        wr('<tr><td>')
        wr('<label for="sec-paranoid">%s Hide all my information from everyone</label><br />' % \
            (radio_jq('sec_policy', 'paranoid', '', 'sec-paranoid', (p.get('sec_policy')=='paranoid') )))
        wr('<label for="sec-permissive">%s Display some of my information, specified below</label>' % \
            (radio_jq('sec_policy', 'permissive', '', 'sec-permissive', (p.get('sec_policy')=='permissive') )))
        wr('</fieldset>')
        # ------------------------------------------------------
        wr('<fieldset>')
        wr('<legend class="sec-legend">Who should be allowed to view your full postal address?</legend>')
        wr('<tr><td class="sec-td">')
        wr('<label for="hide1">%s Nobody; show only my city &amp; state</label><br />' % \
            (radio_jq('show_address', 'hide', 'sec-sub', 'hide1', (p.get('show_address')=='hide') )))
        wr('<label for="dips1">%s ACVAA Diplomates only</label><br />' % \
            (radio_jq('show_address', 'diplomates', 'sec-sub', 'dips1', (p.get('show_address')=='diplomates') )))
        wr('<label for="both1">%s ACVAA Diplomates &amp; Candidates</label><br />' % \
            (radio_jq('show_address', 'both', 'sec-sub', 'both1', (p.get('show_address')=='both') )))
        wr('<label for="all1">%s Everyone, even the general public</label>' % \
            (radio_jq('show_address', 'all', 'sec-sub', 'all1', (p.get('show_address')=='all') )))
        wr('</fieldset>')
        # ------------------------------------------------------
        wr('<fieldset>')
        wr('<legend class="sec-legend">Who should be allowed to view your email address?</legend>')
        wr('<tr><td class="sec-td">')
        wr('<label for="hide2">%s Nobody</label><br />' % \
            (radio_jq('show_email', 'hide', 'sec-sub', 'hide2', (p.get('show_email')=='hide') )))
        wr('<label for="dips2">%s ACVAA Diplomates only</label><br />' % \
            (radio_jq('show_email', 'diplomates', 'sec-sub', 'dips2', (p.get('show_email')=='diplomates') )))
        wr('<label for="both2">%s ACVAA Diplomates &amp; Candidates</label><br />' % \
            (radio_jq('show_email', 'both', 'sec-sub', 'both2', (p.get('show_email')=='both') )))
        wr('<label for="all2">%s Everyone, even the general public</label>' % \
            (radio_jq('show_email', 'all', 'sec-sub', 'all2', (p.get('show_email')=='all') )))
        wr('</fieldset>')
        # ------------------------------------------------------
        wr('<fieldset>')
        wr('<legend class="sec-legend">Who should be allowed to view your phone &amp; fax numbers?</legend>')
        wr('<tr><td class="sec-td">')
        wr('<label for="hide3">%s Nobody</label><br />' % \
            (radio_jq('show_numbers', 'hide', 'sec-sub', 'hide3', (p.get('show_numbers')=='hide') )))
        wr('<label for="dips3">%s ACVAA Diplomates only</label><br />' % \
            (radio_jq('show_numbers', 'diplomates', 'sec-sub', 'dips3', (p.get('show_numbers')=='diplomates') )))
        wr('<label for="both3">%s ACVAA Diplomates &amp; Candidates</label><br />' % \
            (radio_jq('show_numbers', 'both', 'sec-sub', 'both3', (p.get('show_numbers')=='both') )))
        wr('<label for="all3">%s Everyone, even the general public</label>' % \
            (radio_jq('show_numbers', 'all', 'sec-sub', 'all3', (p.get('show_numbers')=='all') )))
        wr('</fieldset>')
        # ------------------------------------------------------
        wr('<tr><td>%s' % (submit('Save Privacy Settings')))
        wr('</table></div>')
        wr('</form>')
        wr('</div><!-- tab3 -->')
        ######################################################
        if IS_DIP:
            wr('<div id="tab4">')
            wr('<h2>For Hire?</h2>')
            wr('<div>Control whether or not you wish to be listed in our "Consultants for Hire" section, which is intended to help other vets connect with ACVAA members.</div>')
            if p.get('sec_policy')=='paranoid':
                wr('<div>Unfortunately, you have selected to hide all your information. You must <em>adjust your privacy settings</em> to allow some information about you be available to the public before you can be included in the "Consultants for Hire" list.</div>')
            else:
                wr('<form method="POST" action="Acct_Change_Hire">')
                wr(hidden('form_username', un))
                wr(hidden('form_hash', self.request().cookies().get('hash')))
                wr('<div>')
                wr('<fieldset>')
                wr('<legend class="sec-legend">Do you wish to be listed as a Consultant for Hire?</legend>')
                wr('')
                wr('<label for="for-hire-yes">%s Yes, that would be fantastic.</label><br />' % \
                    (radio_jq('show_for_hire', 'yes', 'sec-sub', 'for-hire-yes', (p.get('show_for_hire')=='yes') )))
                wr('<label for="for-hire-no">%s No.</label><br />' % \
                    (radio_jq('show_for_hire', 'no', 'sec-sub', 'for-hire-no', (p.get('show_for_hire')!='yes') )))
                wr('</fieldset>')
                wr('<div id="for-hire-extra-info">')

                wr('<div>')
                wr('<b>What geographic area(s) do you serve?</b><br />')
                wr('<textarea name="for_hire_areas" class="input" cols="60" rows="3">%s</textarea>' % (p.get('for_hire_areas', '')))
                wr('</div>')

                wr('<div>')
                wr('<b>What services do you provide?</b><br />')
                wr('<textarea name="for_hire_services" class="input" cols="60" rows="3">%s</textarea>' % (p.get('for_hire_services', '')))
                wr('</div>')

                wr('<div>')
                wr('<b>If you have a website, provide it here:</b><br />')
                wr(text('for_hire_url', value=p.get('for_hire_url', ''), clss='input'))
                wr('</div>')

                wr('</div>')
                wr('%s' % (submit('Save Consultancy Status')))
                wr('</div>')
                wr('</form>')
    
            wr('</div><!-- tab4 -->')
        ######################################################
        wr('</div><!-- acct-container -->')

