from Template_Main import Template_Main

class Mission_Statement (Template_Main):
    def title(self):
        return 'ACVAA Mission Statement'

    def writeContent(self):
        wr = self.writeln
        wr('<h1>%s</h1>' % (self.title()))

        wr('''
<p>
The American College of Veterinary Anesthesia and Analgesia (ACVAA) is an American Veterinary Medical Association recognized, not-for-profit veterinary medical organization founded in 1975 to serve society by: defining and promoting the highest standards of clinical practice of veterinary anesthesia and analgesia, defining criteria for designating veterinarians with advanced training as specialists in the clinical practice of veterinary anesthesiology, issuing certificates to those meeting these criteria, maintaining a list of such veterinarians, and advancing scientific research and education in veterinary anesthesiology and analgesia.
</p>

            ''')

