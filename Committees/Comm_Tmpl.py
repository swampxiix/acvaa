from acva.Template_Authenticated import Template_Authenticated

class Comm_Tmpl (Template_Authenticated):

    def writeJavaScript(self):
        wr = self.writeln
        wr('<script src="https://use.fontawesome.com/034a9c2159.js"></script>')
