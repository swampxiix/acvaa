from acva.Template_Main import Template_Main

class Index_2 (Template_Main):
    def title(self):
        return 'Jobs & Available Positions'

    def writeContent(self):
        wr = self.writeln
        wr('<h1>%s</h1>' % (self.title()))

        wr('''
<div class="sb">
<div class="st">
<div class="t12b">Job Categories</div>
<p><a href="#institution">Institution, Industry, or Public Practice</a></p>
<p><a href="#residency">Residency</a></p>
<p><a href="#internship">Internship</a></p>
<p><a href="#technician">Technician</a></p>
<p><a href="#consultant">Professional Consultant</a></p>
</div>
</div>
            ''')

        wr('''
<a name="institution"></a>
<h2>
Institution, Industry, or Public Practice
</h2>

<ol class="dec">

<li> <a href="Display?id=0001">Senior Clinician in Anaesthesia and Analgesia</a>
    <br />
    The Animal Health Trust (AHT)

<li> <a href="Display?id=0002">Veterinary Anesthesiologist</a>
    <br />
    The Ross University School of Veterinary Medicine (RUSVM)

<li> <a href="Display?id=0003">Assistant or Associate Clinical Professor in Comparative Anesthesia</a>
    <br />
    Department of Veterinary Clinical Sciences 
    <br />
    College of Veterinary Medicine
    <br />
    University of Minnesota

<li> <a href="Display?id=0004">Clinical Instructor of Anesthesia</a>
    <br />
    Department of Clinical Sciences
    <br />
    College of Veterinary Medicine
    <br />
    Auburn University 

<li> <a href="Display?id=0009">Cornell Clinical Fellows</a>
    <br />
    College of Veterinary Medicine
    <br />
    Cornell University 

<li> <a href="Display?id=0010">Locum in Anaesthesiology</a>
    <br />
    Centre Hospitalier Universitaire V&eacute;t&eacute;rinaire (Chuv) 
    <br />
    Facult&eacute; De M&eacute;decine V&eacute;t&eacute;rinair 

<li> <a href="Display?id=0011">Assistant Professor (Oberassistent) Emergency &amp; Critical Care Veterinary Medicine</a>
    <br />
    Vetsuisse Faculty
    <br />
    University of Zurich

<li> <a href="Display?id=0012">Chair</a>
    <br />
    Department of Clinical Sciences
    <br />
    Cummings School of Veterinary Medicine
    <br />
    Tufts University 

<li> <a href="Display?id=0013">Chair Position</a>
    <br />
    Department of Clinical Sciences
    <br />
    The College of Veterinary Medicine
    <br />
    Cornell University

<li> <a href="Display?id=0014">Assistant Head of R&amp;D</a>
    <br />
    Jurox

<li> <a href="Display?id=0020">Postdoctoral Fellowships</a>
    <br />
    Vice Rectorate of Research
    <br />
    Vetmeduni Vienna

</ol>

<a name="residency"></a>
<h2>
Residency
</h2>

<ol class="dec">

<li> <a href="Display?id=0015">Residency in Veterinary Anaesthesia and Analgesia</a>
    <br />
    Section of Anaesthesiology
    <br />
    Vetsuisse Faculty
    <br />
    University of Zurich

<li> <a href="Display?id=0016">Resident Position(s)</a>
    <br />
    William R. Pritchard Veterinary Medical Teaching Hospital
    <br />
    School of Veterinary Medicine
    <br />
    University of California

<li> <a href="Display?id=0017">Anesthesiology and Pain Management Resident Position</a>
    <br />
    School of Veterinary Medicine
    <br />
    The University of Wisconsin

<li> <a href="Display?id=0021">Anesthesia Residency</a>
    <br />
    Virginia-Maryland Regional College of Veterinary Medicine

</ol>

<a name="internship"></a>
<h2>
Internship
</h2>

<ol class="dec">

<li> <a href="Display?id=0018">Internships (3)</a>
    <br />
    Small Animal Anaesthesia
    <br />
    Liverpool University

</ol>

<a name="technician"></a>
<h2>
Technician
</h2>

<ol class="dec">

<li> <a href="Display?id=0019">Anesthesia Technician / Veterinary Technician I</a>
    <br />
    Veterinary Medicine Teaching Hospital
    <br />
    College of Veterinary Medicine
    <br />
    Virginia Tech.

</ol>

<a name="consultant"></a>
<h2>
Professional Consultant
</h2>

<p>
No positions available at this time.
</p>

            ''')
