from acva.z_constants import BASEDIR, rP, wP, compnum
import os

COMDIR = os.path.join(BASEDIR, 'Committees')
COMFILE = os.path.join(COMDIR, 'committees.pick')

STANDING_KEYS = ['Credentials Committee','Exam Committee','Committee on Education','Appeals Committee','Annual and 5-Year ABVS Report Committee','Committee on Residency Training','Multiple Choice Exam Committee','ACVAA-AVTA Liaison Committee','ACVAA Website Committee','Annual Meeting Planning Committee','ACVAA Foundation Committee']
ANNUAL_KEYS =['Nominating Committee', 'Resident Abstract Awards Committee',]
ADHOC_KEYS = ['Essay Questions Bank Committee', 'Exam Review Committee', 'Practitioner Certificate Committee', 'Public Outreach Committee', 'Re-Certification Committee', 'Society Committee',]
OTHER_KEYS = ['ABVS Representative','ABVS Alternate','ACVIM Collaborative Listserve Representatives','ACVS Liaison','NAVC Liaison','AVMA Liaison',]

def getCommittees():
    return rP(COMFILE)

def updateCommittees(form):
    FINAL = {}
    for k in form.keys():
        FINAL[k] = {}
        FINAL[k]['title'], FINAL[k]['name'], FINAL[k]['year'] = form.get(k)
    wP(FINAL, COMFILE)

def getCommDict():
    C = getCommittees()
    FINAL = {'Standing Committees': {}, 'Annual Committees': {}, 'Ad Hoc Committees': {}, 'Other Positions': {}}
    for CTITLE, KEYSET in (('Standing Committees', STANDING_KEYS), ('Annual Committees', ANNUAL_KEYS), ('Ad Hoc Committees', ADHOC_KEYS), ('Other Positions', OTHER_KEYS)):
        for category in KEYSET:
            FINAL[CTITLE][category] = {}
            for posn in C.keys():
                newposn = posn.replace('ACVA', 'ACVAA') # name change
                if posn.startswith(category) or newposn.startswith(category):
                    FINAL[CTITLE][category][posn] = C.get(posn)
            CATKEYS = FINAL[CTITLE][category].keys()
            CATKEYS.sort(compnum)
            FINAL[CTITLE][category]['sorted'] = CATKEYS
    return FINAL
