"""
Args will be passed in the query string for pages that don't require people
to be logged in, e.g., for Pet Owners or Vets. If no role is passed in QS,
then we check user creds and get their role(s) to determine what to display.
The QS will be used for active vs. archived documents.
"""

from Template_Main import Template_Main
from z_account import is_logged_in, is_site_admin, get_user_acct
from z_docmgmt import get_docs_by_access, modify_user_roles, RESTRICTED_ROLES, \
    listify_a_thing, do_archived_docs_exist, get_descriptions, \
    group_docs_by_category, get_all_possible_categories

class DM_View (Template_Main):
    def title(self):
        return 'ACVAA Documents'

    def addJavaScript(self):
        wr = self.writeln
        wr('<script type="text/javascript" src="/js/acvaa_dm_view.js"></script>')

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

        # Show archives sidebar?
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

        # Display the documents' info
        if display_results:
            desc_dict = get_descriptions()
            if docslist:
                wr('<h1>')
                if archived:
                    wr('Archived')
                wr('Documents for %s</h1>' % (titlerole))
                wr('<div style="font-size: 10pt;">Click the <i class="fa fa-caret-down"></i> or <i class="fa fa-caret-right"></i> to show/hide sections.</div>')

                all_cats_sorted = get_all_possible_categories()
                docs_by_cat = group_docs_by_category(docslist)

                for MCAT in all_cats_sorted:
                    if MCAT in docs_by_cat:
                        wr('<h2 style="color: #324150; border-top: 1px dotted #324150;">%s' % (MCAT))
                        wr('<i class="fa fa-caret-down doc_hider" id="%s"></i>' % (MCAT))
                        wr('</h2>')
                        wr('<div id="%s_content">' % (MCAT))
                        local_doc_list = docs_by_cat.get(MCAT, [])
                        for doctitle, docfile in local_doc_list:
                            wr('<h3><a href="/DocRepo/%s">%s</a></h3>' % (docfile, doctitle))
                            wr('<p style="margin-top: 0px;">')
                            if desc_dict.get(docfile):
                                wr('<span style="font-style: italic; color: #999999;">%s</span><br>' % (desc_dict.get(docfile)))
                            wr('Filename: %s</p>' % (docfile))
                        wr('</div>')

            else:
                wr('<h3>Sorry, there are no documents to display.</h3>')
        else:
            wr('<h3>Sorry, there are no documents to display.</h3>')
