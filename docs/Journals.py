from acva.Template_Main import Template_Main

class Journals (Template_Main):
    def title(self):
        return "ACVA Recommended Peer Reviewed Journals"

    def writeContent(self):
        wr = self.writeln
        wr('<h1>%s</h1>'% (self.title()))
        wr('''

<p>
A manuscript reporting new knowledge in the area of anesthesiology, pain management or critical care must be accepted for publication in a refereed biomedical journal acceptable to the ACVA prior to examination for admittance into the College.
</p>

<p>
All research projects must be hypothesis driven. Although prospective experimental or clinical studies are preferred, retrospective projects will be accepted if there is a well formulated study design, hypothesis, appropriate study population selection criteria, data analysis and a well written manuscript. The manuscript must report research done after the candidate has completed his/her Doctorate in Veterinary Medicine. In some cases, research done in pursuit of a Masters or Doctor of Philosophy degree may be suitable. If there are any questions as to whether a proposed research or manuscript will be acceptable, please contact the Executive Secretary or the Chair of the Credentials Committee.
</p>

<h2>
VETERINARY JOURNALS
</h2>

<p>
American Journal of Veterinary Research
<br />
Applied Behaviour
<br />
Australian Veterinary Journal
<br />
Behaviour
<br />
Canadian Journal of Veterinary Research
<br />
Canadian Veterinary Journal
<br />
Comparative Medicine
<br />
Equine Veterinary Journal
<br />
International Journal Applied Research Veterinary Medicine
<br />
Journal of the American Association of Laboratory Animal Science
<br />
Journal of Feline Medicine and Surgery
<br />
Journal of Small Animal Practice
<br />
Journal of the American Animal Hospital Association
<br />
Journal of the American Veterinary Medical Association
<br />
Journal of Veterinary Emergency and Critical Care
<br />
Journal of Veterinary Internal Medicine
<br />
Journal of Veterinary Pharmacology and Therapeutics
<br />
Journal of Zoo and Wildlife Medicine
<br />
New Zealand Veterinary Journal
<br />
The Veterinary Journal
<br />
Veterinary Anesthesia and Analgesia
<br />
Veterinary Radiology and Ultrasound
<br />
Veterinary Record
<br />
Veterinary Surgery
<br />
Veterinary Therapeutics: Research in Applied
<br />
Veterinary Medicine
</p>

<h2>
NON-VETERINARY JOURNALS
</h2>

<p>
American Heart Journal
<br />
American Journal of Pathology
<br />
American Journal of Physiology
<br />
American Journal of Surgery
<br />
American Journal of Sports Medicine, The
<br />
Anatomical Record
<br />
Anesthesiology
<br />
Arthritis and Rheumatism
<br />
Bone
<br />
Cancer
<br />
Journal of Applied Physiology
<br />
Journal of Bone and Joint Surgery
<br />
Journal of Clinical Investigation
<br />
Journal of Investigative Surgery
<br />
Journal of Orthopaedic Research
<br />
Journal of Rheumatology
<br />
Journal of Surgical Research
<br />
Osteoarthritis and Cartilage
<br />
Nature
<br />
Pain
<br />
Science
</p>

<p>
If a candidate wants to publish in a journal not on the current Approved Journals List, a petition must be made to the Credentials Committee through the Executive Secretary.
</p>

<p>
Case reports, short communications, book chapters, meeting proceedings or lay publications are not appropriate.
</p>

            ''')