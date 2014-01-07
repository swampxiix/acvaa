from acva.Template_Authenticated import Template_Authenticated
from acva.z_account import is_site_admin
from z_board import getBOD

class Index_New (Template_Authenticated):
    def title(self):
        return 'Board of Directors'

    def writeContent(self):
        wr = self.writeln

        IS_SITE_ADMIN = is_site_admin(self.request())
        if IS_SITE_ADMIN:
            wr('<div class="button">')
            wr('<a href="BOD_Form">Edit Board</a>')
            wr('</div>')

        wr('<h1>%s</h1>' % (self.title()))

        bod = getBOD()

        wr('''
<div class="sb">
<div class="st">
<div class="t12b">B.O.D. Links</div>
<P><a href="Regions">Regions &amp; Representatives</a></P>
<P><a href="Minutes">Meeting Teleconference Minutes</a></P>
</div>
</div>

<h2>ACVAA Executive Officers</h2>

<table style="margin: 10px 0px 20px 0px;">
        ''')

        for a in ['President', 'President-Elect', 'Past-President', 'Executive Secretary']:
            ad = bod.get(a, {})
            wr('<tr><td>%s:<td>' % (a))
            if ad.get('email'):
                wr('<a href="mailto:%s">%s</a>' % (ad.get('email'), ad.get('name')))
            else:
                wr(ad.get('name'))
            wr('<td>%s' % (ad.get('year', '')))

        wr('''
</table>

<h2>ACVAA Regional Officers</h2>

<table style="margin: 10px 0px 20px 0px;">
        ''')

        for a in ['Region 1', 'Region 2', 'Region 3', 'Region 4', 'Region 5']:
            ad = bod.get(a, {})
            wr('<tr><td>%s:<td>' % (a))
            if ad.get('email'):
                wr('<a href="mailto:%s">%s</a>' % (ad.get('email'), ad.get('name')))
            else:
                wr(ad.get('name'))
            wr('<td>%s' % (ad.get('year', '')))

        for a in ['At-Large_1', 'At-Large_2', 'At-Large_3']:
            ad = bod.get(a, {})
            wr('<tr><td>%s:<td>' % (a.split('_')[0]))
            if ad.get('email'):
                wr('<a href="mailto:%s">%s</a>' % (ad.get('email'), ad.get('name')))
            else:
                wr(ad.get('name'))
            wr('<td>%s' % (ad.get('year', '')))

        wr('''
</table>

<h3>ACVAA Representative to the American Board of Veterinary Specialties</h3>

<table style="margin: 10px 0px 20px 0px;">
        ''')
        for a in ['AVBS Representative', 'AVBS Alternate']:
            ad = bod.get(a, {})
            wr('<tr><td>%s:<td>' % (a))
            if ad.get('email'):
                wr('<a href="mailto:%s">%s</a>' % (ad.get('email'), ad.get('name')))
            else:
                wr(ad.get('name'))
            wr('<td>%s' % (ad.get('year', '')))



        wr('''
</table>

        ''')
















