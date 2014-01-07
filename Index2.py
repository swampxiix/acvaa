from Template_Main import Template_Main
class Index2 (Template_Main):
    def writeContent(self):
        self.response().sendRedirect('Index')
