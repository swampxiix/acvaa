from acva.Template_Authenticated import Template_Authenticated

class Welcome (Template_Authenticated):
    def title(self):
        return "Welcome to the ACVAA"

    def writeContent(self):
        wr = self.writeln
        wr('''

<h1>
General Information for American College of Veterinary Anesthesia and Analgesia Residents
</h1>

<P>
Welcome to the American College of Veterinary Anesthesia and Analgesia (ACVAA). By applying and being accepted in the anesthesia residency program of an American Veterinary Medical Association (AVMA) accredited veterinary school, you have come under the wing of the ACVAA.
</P>

<P>
The ACVAA is the organization approved by the American Veterinary Medical Association's American Board of Veterinary Specialties to serve the public, veterinary profession, hospitals and veterinary schools and colleges by establishing and maintaining the highest standards in the practice of veterinary anesthesiology, advising the Council on Education of the A.V.M.A. on matters concerning approval of veterinary anesthesiology training programs, establishing criteria of fitness for the designation of a specialist in the practice of veterinary anesthesiology, administering examinations to determine the competence in veterinary anesthesiology of veterinarians who apply and to issue certificates to those who meet the required standards. The major criteria on which judgment of competence is based include technical facility, medical judgment and scholarship. 
</P>

<P>
The first step toward having the ACVAA be a resource for you during your residency training is to visit this website. 
</P>

<P>
Here you will find the:
<ol class="dec">
<li> <a href="/docs/candidates/ACVAA_2017_Residency_Training_Standards.docx">Residency Training Standards</a> &ndash; to give you perspective on the ACVAA's expectations of your training program
<li> <a href="/docs/candidates/ACVAA_Case_Activities_Log_template_2013.xls">Caselog & Activities Log Template</a> &ndash; to be maintained during your residency and submitted to the ACVAA Executive Secretary annually and on application to sit the certifying examination
<li> <a href="/docs/ACVA_Residency_Timeline_2010.xls">ACVAA Residency and Certification Timeline</a> &ndash; to be a guide throughout your residency and preparation for certification
<li> <a href="/docs/candidates/List_of_Recommended_Journals_for_Resident_Publication_Oct_2014.docx">A list of journals</a> considered suitable for your manuscript submission. This is not all inclusive. If you have any questions please contact the Executive Secretary.
</ol>
</P>

<P>
Additional information about the ACVAA, including the Constitution and Bylaws, can be found on the website under "<a href="/About.py">About the ACVAA</a>".
</P>

<P>
Keep in mind that, according to the ACVAA Bylaws and Residency Training Standards, to be eligible to take the ACVAA'S Certifying exam, you must:
</P>

<P>
<ol class="dec">
<li> be a graduate of a college or school of veterinary medicine and legally qualified to practice veterinary medicine in some country.
<li> have completed a year of general veterinary practice or a rotating internship (* 30% anesthesia)
<li> have satisfactorily participated in specialty training in a residency program that meets the requirements set by the ACVAA's <a href="/docs/candidates/ACVAA_2017_Residency_Training_Standards.docx">Residency Training Standards</a>
<li> be licensed to practice veterinary medicine in the US or Canada (exceptions are made for applicants coved by a veterinary school license)
<li> have a first-author manuscript describing original research in clinical or experimental anesthesia or pain management accepted by a peer-reviewed journal*
</ol>
</P>

<P>
* All research projects must be hypothesis driven. Although prospective experimental or clinical studies are preferred, retrospective projects will be accepted if there is a well formulated study design, hypothesis, appropriate study population selection criteria, data analysis and a well written manuscript. Publications of work done prior to entering residency training may be accepted under certain circumstances. The research must have been done after completion of your veterinary degree or during pursuit of a PhD or MS. Please contact the executive secretary if you would like such a publication to be considered by the Credentials Committee.
</P>

<P>
If you have concerns about any of these requirements, please contact the executive secretary (<a href="mailto:execdir@acvaa.org">execdir@acvaa.org</a>). It is far better to address possible deficits at the beginning of your training program than to deal with possible rejection of your credentials at the end.
</P>

<P>
Your residency training program is designed to develop your knowledge and skills in the anesthetic management of veterinary patients of all species. In addition, you should develop a degree of expertise in pain management, critical care and experimental method. To demonstrate that your training has prepared you for the ACVAA certifying exam you will be required to submit your "credentials", a collection of documents including an application, current curriculum vita, letter from a sponsor who must be an ACVAA diplomate, 3 letters of reference, a peer-reviewed manuscript and your caselog. Although traditionally credentials are submitted after completion of a residency training program, they may be submitted during the 3rd year as long as at least 104 weeks of the program have been completed.
</P>

<P>
Submission of your "credentials" begins the certification process. If your credentials are accepted by the ACVAA Credentials Committee, you will be invited to take the written portion of the certifying exam. The oral portion of the exam follows the written exam by 3-4 months and may only be taken by candidates who have completed all 3 years of their residency program and score 70 or higher on the written exam. 
</P>

<P>
If at any time during your residency you have any questions or issues, do not hesitate to contact the ACVAA executive secretary through the link Executive Director/Secretary on the website or at <a href="mailto:execdir@acvaa.org">execdir@acvaa.org</a>.
</P>

<P>
Have a fun and challenging residency.
</P>

            ''')