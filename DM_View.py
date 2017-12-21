"""
Args will be passed in the query string for pages that don't require people
to be logged in, e.g., for Pet Owners or Vets. If no role is passed in QS,
then we check user creds and get their role(s) to determine what to display.
The QS will be used for active vs. archived documents.
"""

from Template_Main import Template_Main
from z_account import is_logged_in, is_site_admin, get_user_acct
from z_docmgmt import get_docs_by_access, modify_user_roles, RESTRICTED_ROLES, \
    listify_a_thing, do_archived_docs_exist

class DM_View (Template_Main):
    def title(self):
        pass

    def writeContent(self):
        wr = self.writeln
        ISA = is_site_admin(self.request())
        ILI = is_logged_in(self.request())
        qs = self.request().fields()
        role = qs.get('role')
        archived = qs.get('archived', None)
        display_results = False
        docslist = []
        titlerole = 'Everyone'
        role_to_check = []

        if role: # Explicit
            if role not in RESTRICTED_ROLES:
                titlerole = role
                docslist = get_docs_by_access(role, archived)
                display_results = True
                role_to_check = role

        else: # Role-based
            if ILI:
                username = self.request().cookies().get('username')
                useracct = get_user_acct(username)
                userroles = useracct.get('roles')
                modroles = modify_user_roles(userroles)
                role_to_check = modroles
                titlerole = ' & '.join(listify_a_thing(modroles))
                docslist = get_docs_by_access(modroles, archived)
                display_results = True

        if ISA:
            wr('<p><a href="DM_Index" class="btn btn-default">Document Management</a></p>')

        archives_exist = do_archived_docs_exist(role_to_check)
        if archives_exist:
            if archived:
                arch_url = 'DM_View?'
                arch_text = 'Active Documents'
            else:
                arch_url = 'DM_View?archived=True'
                arch_text = 'Archived Documents'
            if role:
                arch_url += '&role=%s' % (role)
            wr('<div class="sb"><div class="st"><a href="%s">%s</a></div></div>' % (arch_url, arch_text))

        if display_results:
            if docslist:
                wr('<h1>')
                if archived:
                    wr('Archived')
                wr('Documents for %s</h1>' % (titlerole))
                for doctitle, docfile in docslist:
                    wr('<h3><a href="/DocRepo/%s">%s</a></h3>' % (docfile, doctitle))
                    wr('Filename: %s' % (docfile))
            else:
                wr('<h3>Sorry, there are no documents to display.</h3>')
        else:
            wr('<h3>Sorry, there are no documents to display.</h3>')
