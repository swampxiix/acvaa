from Template_Main import Template_Main
from z_locator import get_locations, get_flag

class Locator (Template_Main):

    def title(self):
        return 'ACVAA: Find a Doctor'

    def writeContent(self):
        wr = self.writeln
        wr('<h1>Find an ACVAA Doctor</h1>')
        locs = get_locations()
        countries = locs.keys()
        countries.sort()
        for country in countries:
            wr('<h2 style="margin-top: 20px; border-top: 2px solid #b4c3d3;">%s %s</h2>' % (country, get_flag(country)))
            cdict = locs[country]
            states = cdict.keys()
            states.sort()
            for state in states:
                wr('<h3 style="margin-top: 10px; margin-left: 10px; border-top: 1px dashed #b4c3d3;">%s</h3>' % (state))
                sdict = cdict[state]
                cities = sdict.keys()
                cities.sort()
                for city in cities:
                    wr('<div class="t14" style="margin-top: 10px; margin-left: 20px;">%s</div>' % (city))
                    dr_list = sdict[city]
                    for drid, drname in dr_list:
                        wr('<div class="t12" style="margin-left: 32px;">')
                        wr('<a href="Directory?view=%s">%s</a>' % (drid, drname))
                        wr('</div>')

