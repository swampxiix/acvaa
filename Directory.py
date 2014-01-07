from Template_Main import Template_Main

from z_account import get_users, is_logged_in, get_user_acct
from z_constants import DIPLSTR, RESDSTR
from z_locator import get_flag

class Directory (Template_Main):
    def title(self):
        qs = self.request().fields()
        FOR_HIRE = qs.get('consult')
        if FOR_HIRE:
            return 'ACVAA Consultants for Hire'
        else:
            return 'ACVAA Directory'

    def get_full_addr(self, d):
        addr = ''
        if d.get('addr1'):
            addr = d.get('addr1')
            addr += '<br />'
        if d.get('addr2'):
            addr += d.get('addr2')
            addr += '<br />'
        addr += '%s, %s %s' % (d.get('city'), d.get('state'), d.get('zip'))
        if d.get('country'):
            addr += '<br />'
            addr += d.get('country')
        return addr

    def get_numbers(self, d):
        nums = ''
        if d.get('phone'):
            nums = '<b>Tel</b>: %s' % d.get('phone')
            if d.get('fax'):
                nums += '<br />'
        if d.get('fax'):
            nums += '<b>Fax</b>: %s' % d.get('fax')
        return nums

    def format_list (self, all):
        wr = self.writeln
        qs = self.request().fields()
        FOR_HIRE = qs.get('consult')
        ILI = is_logged_in(self.request())
        viewer = self.request().cookies().get('username', '')
        rolestr = self.request().cookies().get('role', '')
        IS_RES = rolestr == RESDSTR
        IS_DIP = rolestr == DIPLSTR
        aks = all.keys()
        aks = sorted(aks, key=lambda x: (x.isdigit() and float(x)) or x.lower())

        wr('<div id="directory">')
        for k in aks:
            d = all[k]
            if d.get('sec_policy') == 'paranoid':
                pass
            else:
                wr('<div>')
                dname = ''
                if d.get('salute'):
                    dname = '%s ' % (d['salute'])
                dname += '%s %s %s' % (d.get('fn', ''), d.get('mi', ''), d.get('sn', ''))
                if d.get('title'):
                    dname += ', %s' % (d['title'])
                if d.get('degrees'):
                    dname += ', %s' % (d['degrees'])
    
                if d.get('username') == viewer:
                    wr('<span class="button"><a href="Account">Your Account</a></span>')
                    wr('<h2>%s</h2>' % (dname))
                else:
                    # Country Flag Icon - Neato!
                    try:
                        wr(get_flag(d.get('country'), align="right"))
                    except AttributeError:
                        pass
                    wr('<h3>%s</h3>' % (dname))
    
                wr('<table><tr><td>') ####====####
                ##################
                # ADDRESS
                ##################
                addr = '%s, %s' % (d.get('city'), d.get('state'))
                if d.get('show_address') == 'hide':
                    pass
                elif d.get('show_address') == 'diplomates':
                    if ILI and IS_DIP:
                        addr = self.get_full_addr(d)
                elif d.get('show_address') == 'both':
                    if ILI and (IS_DIP or IS_RES):
                        addr = self.get_full_addr(d)
                elif d.get('show_address') == 'all':
                    addr = self.get_full_addr(d)
                wr('<P>%s</P>' % (addr))
                wr('<td style="padding-left: 30px;">') ####====####
                ##################
                # NUMBERS
                ##################
                nums = ''
                if d.get('show_numbers') == 'hide':
                    pass
                elif d.get('show_address') == 'diplomates':
                    if ILI and IS_DIP:
                        nums = self.get_numbers(d)
                elif d.get('show_address') == 'both':
                    if ILI and (IS_DIP or IS_RES):
                        nums = self.get_numbers(d)
                elif d.get('show_address') == 'all':
                    nums = self.get_numbers(d)
                wr('<P>%s</P>' % (nums))
                wr('<td style="padding-left: 30px;">') ####====####
                ##################
                # EMAIL
                ##################
                email = ''
                if d.get('show_email') == 'hide':
                    pass
                elif d.get('show_email') == 'diplomates':
                    if ILI and IS_DIP:
                        email = d.get('email', '')
                elif d.get('show_email') == 'both':
                    if ILI and (IS_DIP or IS_RES):
                        email = d.get('email', '')
                elif d.get('show_email') == 'all':
                    email = d.get('email', '')
                wr('<P>%s</P>' % (email))
                wr('</table>') ####====####
                wr('</div>')

            if FOR_HIRE:
                fh_area = d.get('for_hire_areas')
                if fh_area:
                    wr('<div>')
                    wr('<b>Area(s) Served:</b><br />')
                    fh_area = fh_area.replace('\r', '<br />')
                    wr(fh_area)
                    wr('</div>')

                fh_svcs = d.get('for_hire_services')
                if fh_svcs:
                    wr('<div>')
                    wr('<b>Services Offered:</b><br />')
                    fh_svcs = fh_svcs.replace('\r', '<br />')
                    wr(fh_svcs)
                    wr('</div>')

                fh_url = d.get('for_hire_url')
                if fh_url:
                    wr('<div>')
                    wr('<a href="%s">%s</a>' % (fh_url, fh_url))
                    wr('</div>')

        wr('</div>')

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()

        wr('<h1>%s</h1>' % (self.title()))

        if qs.get('view'):
            dr_id = qs.get('view')
#            wr(dr_id)
            upick = get_user_acct(dr_id)
            upick['username'] = dr_id
            uuid = '%s_%s_%s' % (upick.get('sn'), upick.get('fn'), dr_id)
            self.format_list( {uuid: upick} )

        else:
            Ds = get_users(utype='d')
            FOR_HIRE = qs.get('consult')
            if FOR_HIRE:
                Rs = {}
                hires = {}
                for k in Ds.keys():
                    vetdict = Ds.get(k)
                    if vetdict.get('show_for_hire') == 'yes':
                        hires[k] = Ds[k]
                Ds = hires
            else:
                Rs = get_users(utype='r')

            wr('<div id="acct-container" class="acct-tabs"> ')
            wr('<ul class="idTabs"> ')
            if Ds:
                wr('<li><a class="selected" href="#tab1">Diplomates</a></li> ')
            if Rs:
                wr('<li><a href="#tab2">Candidates</a></li> ')
            wr('</ul> ')

            if Ds:
                wr('<div id="tab1">')
                self.format_list(Ds)
                wr('</div><!-- tab1 -->')
            else:
                if FOR_HIRE:
                    wr('<P>There are no ACVAA members who have marked themselves as for hire at this time.</P>')

            if Rs:
                wr('<div id="tab2">')
                self.format_list(Rs)
                wr('</div><!-- tab2 -->')

            wr('</div><!-- acct-container -->')
