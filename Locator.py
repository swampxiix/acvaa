import string
from Template_Main import Template_Main
from z_locator import get_locations, get_flag

class Locator (Template_Main):

    def title(self):
        return 'ACVAA: Find a Doctor'

    def addJavaScript(self):
        wr = self.writeln
        wr('<script type="text/javascript" src="/js/acvaa_locator.js"></script>')

    def writeContent(self):
        wr = self.writeln
        wr('<h1>Find an ACVAA Doctor</h1>')
        wr('<P>Click the name of any country to expand and view all of its doctors.</P>')
        locs = get_locations()
        countries = locs.keys()
        countries.sort()

        if 'USA' in countries:
            del countries[countries.index('USA')]
        countries = ['USA'] + countries

        for country in countries:
            ctyid = country.translate(None, string.punctuation)
            ctyid = ctyid.replace(' ', '-')
            wr('<h2 style="margin-top: 20px; border-top: 2px solid #b4c3d3;" id="%s">%s %s</h2>' % (ctyid, country, get_flag(country)))
            wr('<div id="%s" class="country">' % (ctyid))
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
            wr('</div><!-- country id -->')
