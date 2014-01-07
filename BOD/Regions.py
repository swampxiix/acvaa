from acva.Template_Authenticated import Template_Authenticated
from acva.z_constants import STATES, STATES_LOOKUP, PROVS, PROVS_LOOKUP
from z_board import get_region_dict, reg_hex, getBOD

class Regions (Template_Authenticated):
    def title(self):
        return 'Regions and Representatives'

    def writeContent(self):
        wr = self.writeln
        wr('<h1>%s</h1>' % (self.title()))
        wr('''
<div class="sb">
<div class="st">
<div class="t12b">B.O.D. Links</div>
<P><a href="Index">Board of Directors</a></P>
<P><a href="Minutes">Meeting Teleconference Minutes</a></P>
</div>
</div>
        ''')


        wr('<div>')
        wr('<h2>Board of Directors Representatives</h2>')
        wr('<table class="reg">')

        bod = getBOD()
        for r in range(1,6):
            wr('<tr style="border: 1px solid #666; background-color: #%s;">' % (reg_hex.get(r)))
            wr('<td class="reg">Region %s' % (r))
            wr('<td class="reg">')
            bk = "Region %s" % (r)
            bd = bod.get(bk, {})
            if bd.get('email'):
                wr('<a href="mailto:%s">%s</a>' % (bd.get('email'), bd.get('name')))
            else:
                wr(bd.get('name'))

        wr('</table>')
        wr('</div>')




        wr('<div style="text-align: center;">')
        wr('<img src="/g/north_america.png" width="600" height="530" alt="Map of Regions" border="0" />')
        wr('</div>')

        wr('<div style="float: left; margin-right: 20px;">')

        wr('<h2>USA</h2>')

        RDICT = get_region_dict()

        count = 0
        wr('<table><tr valign="top">')

        for s in STATES:
            if count == 0 or count == 25:
                wr('<td>')
                wr('<table class="reg">')
                wr('<tr><td><td>State<td>Reg')
            count += 1
            region = RDICT.get(s)
            wr('<tr style="border: 1px solid #666; background-color: #%s;">' % (reg_hex.get(region)))
            wr('<td class="reg">%s ' % (s))
            wr('<td class="reg">')
            wr(STATES_LOOKUP.get(s))
            wr('<td class="reg">')
            wr(region)

            if count == 25 or count == 50:
                wr('</table>')

        wr('</table>')

        wr('</div>')

        wr('<div>')
        wr('<h2>Canada</h2>')

        RDICT = get_region_dict('CA')
        wr('<table class="reg">')
        wr('<tr><td><td>Province<td>Reg')

        for s in PROVS:
            region = RDICT.get(s)
            wr('<tr style="background-color: #%s;">' % (reg_hex.get(region)))
            wr('<td class="reg">%s ' % (s))
            wr('<td class="reg">')
            wr(PROVS_LOOKUP.get(s))
            wr('<td class="reg">')
            wr(region)

        wr('</table>')
        wr('</div>')



