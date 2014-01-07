from acva.Template_Main import Template_Main

class Equine (Template_Main):
    def title(self):
        return "Guidelines for Anesthesia in Horses"

    def writeContent(self):
        wr = self.writeln
        wr('''
<h1>
Guidelines for Anesthesia in Horses
</h1>
 
<P>
Prepared by the ACVA Equine Standards Committee<br />
Elizabeth A. Martinez<br />
Ann E. Wagner<br />
Bernd Driessen<br />
Cynthia Trim
</P>



<P>
<ol class="ur">

  <li> Preoperative Evaluation
  <ol class="ua">
    <li> History
    <ol class="dec">
      <li> Response to prior sedation or anesthesia
      <li> History of any significant illness or injury
      <li> Current problem
    </ol>
    <li> Physical Examination
    <ol class="dec">
      <li> Temperature, pulse rate, respiratory rate
      <li> Evaluation of all organ systems, focusing on the presence or absence of cardiovascular and/or respiratory abnormalities
      <li> Capillary refill time, mucous membrane color
    </ol>
    <li> Laboratory Blood Work
    <ol class="dec">
      <li> Order and/or perform any necessary blood work.
      <li> Recommended tests, if any, will depend on physical status of the patient and the procedure to be performed.
    </ol>
  </ol>

  <li> Selection of Anesthetic Regimen
  <ol class="ua">
    <li> An appropriate regimen should be chosen based on:
    <ol class="dec">
      <li> Physical status of patient
      <li> Duration of anesthesia required
      <li> Number and skill of personnel available
      <li> Safety of facility/location where anesthesia (including induction and recovery) will be performed
      <li> Anesthetic equipment available
      <li> Monitoring equipment available
    </ol>
    <li> Total Intravenous Anesthesia (TIVA)
    <ol class="dec">
      <li> Recommended for procedures expected to be 1 hour or less in duration
      <li> Muscle relaxation may not be as profound compared to inhalant anesthesia
      <li> Anesthetic agents may be administered as intermittent boluses or as an intravenous infusion
    </ol>
    <li> Inhalant Anesthesia
    <ol class="dec">
      <li> Preferred for lengthy procedures (> 1 hour of anesthesia time)
      <li> Requires additional equipment compared to TIVA
      <li> Commonly used inhalants include halothane, isoflurane, sevoflurane
    </ol>
  </ol>

  <li> Monitoring and Supportive Care
  <ol class="ua">
    <li> Intravenous catheterization is recommended for administration of anesthetic drugs, fluids, and/or supportive medications
    <li> Proper position and padding is vital to aid in prevention of muscle or nerve injury
    <li> TIVA
    <ol class="dec">
      <li> Oxygen source + flowmeter for nasal insufflation, if indicated
      <li> Endotracheal tubes and demand valve readily available to ventilate, if necessary
      <li> Pad / cloth for face and eye
    </ol>
    <li> Inhalant Anesthesia
    <ol class="dec">
      <li> Appropriately sized, cuffed, endotracheal tube
      <li> Oxygen source + anesthesia machine
      <li> Means to scavenge anesthetic waste gases
      <li> Means to manually or mechanically ventilate, if necessary
    </ol>
    <li> Monitoring of the cardiovascular system
    <ol class="dec">
      <li> Digital pulse palpation
      <li> CRT, mucous membrane color
      <li> ECG, if indicated
      <li> Arterial blood pressure, if indicated (strongly recommended whenever inhalation anesthesia is used)
      <li> Hypotension should be treated with appropriate medication (fluids, inotropes, etc)
    </ol>

    <li> Monitoring of the respiratory system
    <ol class="dec">
      <li> Observation or respiratory rate and rhythm
      <li> Pulse oximetry, if indicated
      <li> Capnometry, if indicated (note: ETCO2 frequently underestimates PaCO2 in anesthetized horses)
      <li> Arterial blood gas analysis, if indicated
      <li> Hypoventilation is treated with either assisted or controlled ventilation
    </ol>
  </ol>

  <li> Injectable adjuncts during anesthesia
  <ol class="ua">
    <li> May be useful to provide additional anesthesia, analgesia, or muscle relaxation during anesthesia.
    <li> May be administered as a bolus or, with certain medications, be given as a constant rate infusion
    <li> Common adjuncts include:
    <ol class="dec">
      <li> Opioids (eg: butorphanol)
      <li> Ketamine
      <li> Local anesthetics (either intravenously or as a local/regional technique)
      <li> Muscle relaxants
      <ol class="la">
        <li> Diazepam or midazolam
        <li> Guaifenesin
        <li> Neuromuscular blocking agents (controlled ventilation and monitoring of neuromuscular function is required during paralysis)
      </ol>
    </ol>
  </ol>

  <li> Local and regional analgesia/anesthesia
  <ol class="ua">
    <li> May be chosen as the sole technique for certain procedures.
    <li> Depending on the temperament of the patient and type of procedure, chemical restraint may also be used in combination with a local or regional technique.
    <li> May also be used as an adjunct to general anesthesia
    <li> Choice of local anesthetics includes lidocaine, mepivacaine, and bupivacaine. The addition of epinephrine (5 micrograms/ml) may help to improve the quality and duration of anesthesia.
    <li> Local and regional techniques include    :
    <ol class="dec">
      <li> Local infiltration (eg: line block, ring block)
      <li> Peripheral nerve block
      <li> Intraarticular block
      <li> Paravertebral block
      <li> Epidural analgesia/anesthesia
      <ol class="la">
        <li> Local anesthetics
        <li> Alpha-2 agonists
      </ol>
    </ol>
  </ol>

  <li> Recovery
  <ol class="ua">
    <li> TIVA
    <ol class="dec">
      <li> If in padded, confined area (recovery stall), no assistance may be needed
      <li> If in open area (outside), area should be relatively soft (grass), free of obstacles (trees, fences), and assistance should be provided to prevent too much momentum
      <ol class="la">
        <li> Control head, protect eyes
        <li> Assist on tail (if possible)
      </ol>
    </ol>
    <li> Inhalant Anesthesia
    <ol class="dec">
      <li> Depending on temperament and physical status of horse, inhalant used, surgical procedure performed, and design of recovery stall, the horse may recover either unassisted or with assistance on the head and/or tail.
      <li> If recovery is unassisted, the patient should be observed as often as needed to be able to be able to identify if the horse unexpectedly requires assistance.
      <li> Sedatives and/or analgesics may be administered during the recovery period to aid in a smooth transition to standing.
    </ol>
  </ol>

</ol>
</P>



            ''')


