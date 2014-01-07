from acva.Template_Authenticated import Template_Authenticated
from acva.z_account import is_site_admin
from acva.z_constants import compnum, FMONTHS
from acva.z_times import get_year
from z_board import get_all_minutes

class Minutes (Template_Authenticated):
    def title(self):
        return 'Meeting Teleconference Minutes'

    def writeContent(self):
        wr = self.writeln
        qs = self.request().fields()
        viewyear = qs.get('yr', str(get_year()))

        IS_SITE_ADMIN = is_site_admin(self.request())
        if IS_SITE_ADMIN:
            wr('<div class="button">')
            wr('<a href="Minutes_Form">+ Add Minutes</a>')
            wr('</div>')

        all = get_all_minutes()
        vyd = {} # viewyear_dict
        allyears = []
        for x in all.keys():
            mdate = all[x]['date']
            minyear = mdate[-1]
            if minyear not in allyears:
                allyears.append(minyear)
            if minyear == viewyear:
                vyd[x] = all[x]
#        wr(vyd)
        allyears = sorted(allyears, key=lambda x: (x.isdigit() and float(x)) or x.lower())
        allyears.reverse()

        wr('<h1>%s</h1>' % (self.title()))
        wr('''
<div class="sb">
<div class="st">
<div class="t12b">B.O.D. Links</div>
<P><a href="Index">Board of Directors</a></P>
<P><a href="Regions">Regions &amp; Representatives</a></P>
<div class="t12b">Minutes by Year</div>
        ''')
        for my in allyears:
            wr('<P class="t12"><a href="Minutes?yr=%s">%s</a></P>' % (my, my))
        wr('''
</div>
</div>
        ''')

        aks = vyd.keys()
        aks.sort(compnum)
        aks.reverse()
        for k in aks:
            meet_dict = vyd.get(k)
            M, D, Y = meet_dict.get('date')
            wr('<h2 style="margin-top: 30px;">%s %s, %s</h2>' % (FMONTHS.get(int(M)), D, Y))
            wr('<P>%s</P>' % (meet_dict.get('summary')))
            df = meet_dict.get('datafile')
            wr('<P>Click here to download: <a href="/BOD/minutes_docs/%s">%s</a></P>' % (df, df))
            if IS_SITE_ADMIN:
                wr('<div><a href="Min_Delete_Confirm?id=%s"><img src="/g/delete.png" width="17" height="17" alt="Delete" border="0" /></a><a href="Min_Delete_Confirm?id=%s">Delete</a></div>' % (k, k))

