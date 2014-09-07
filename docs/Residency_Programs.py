from acva.Template_Main import Template_Main

class Residency_Programs (Template_Main):
    def title(self):
        return "This page has moved..."

    def writeContent(self):
        self.response().sendRedirect('/Residency/Programs')
        wr = self.writeln
        wr('This page has moved...<br>')
        wr('<a href="http://www.acvaa.org/Residency/Programs">http://www.acvaa.org/Residency/Programs</a>')
