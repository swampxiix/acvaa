from acva.Template_Main import Template_Main

from z_jobs import get_jobs_by_cat
from acva.z_constants import JOB_CATS

synonyms = {'Institution, Industry or Private Practice': ['Institution, Industry or Public Practice']}

class Testing (Template_Main):
    def writeContent(self):
        wr = self.writeln
#        wr(JOB_CATS)
#        wr('<hr>')
        x = get_jobs_by_cat()
        wr(x.keys())
        wr('<hr>')
        for c in JOB_CATS:
            wr('')
            wr('<p>'+c)
            deezjobs = x.get(c)

            synlist = synonyms.get(c, [])
            for syn in synlist:
#                deezjobs = deezjobs + 
                deezjobs = dict(deezjobs, **x.get(syn))
            wr(len(deezjobs.keys()))

