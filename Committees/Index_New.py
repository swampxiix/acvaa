from acva.Template_Authenticated import Template_Authenticated


class Index (Template_Authenticated):
    def title(self):
        return 'ACVAA Committees'

    def writeContent(self):
        wr = self.writeln
        wr('<a name="top"></a>')
        wr('<h1>%s</h1>' % (self.title()))
        wr('''

<div class="sb">
<div class="st">
<div class="t12b">Standing Committees</div>
<ul>
<li> <a href="#s1">Credentials Committee</a>
<li> <a href="#s2">Exam Committee</a>
<li> <a href="#s3">Committee on Education</a>
<li> <a href="#s4">Appeals Committee</a>
<li> <a href="#s5">Annual and 5-Year ABVS Report Committee</a>
<li> <a href="#s6">Committee on Residency Training</a>
<li> <a href="#s7">Multiple Choice Exam Committee</a>
<li> <a href="#s8">ACVAA-AVTA Liaison Committee</a>
<li> <a href="#s9">ACVAA Website Committee</a>
</ul>
<div class="t12b" style="margin-top: 10px;">Ad Hoc Committees</div>
<ul>
<li> <a href="#a1">Marketing the ACVAA</a>
<li> <a href="#a2">Bylaws Amendment Committee</a>
<li> <a href="#a3">Exam Review Committee</a>
</ul>
<div class="t12b" style="margin-top: 10px;"><a href="#other">Other Positions</a></div>

</div>
</div>

<h2>
Standing Committees
</h2>

<table class="comm">
<tr><th colspan="3">
<a name="s1"></a>
Credentials Committee                               <td class="top"><a href="#top">top</a>
<tr><td>Chair               <td>Becky Johnson       <td>(2010)
<tr><td>                    <td>Ben Brainard        <td>(2010)
<tr><td>                    <td>Lynne Kushner       <td>(2011)
<tr><td>                    <td>David Martin        <td>(2012)
<tr><td>                    <td>Tammy Grubb         <td>(2012)
<tr><td><i>Ex officio</i>   <td>Bob Meyer           <td>(2011)

<tr><th colspan="3">
<a name="s2"></a>
Exam Committee                                      <td class="top"><a href="#top">top</a>
<tr><td>Co-Chair            <td>Linda Barter        <td>(2010)
<tr><td>Co-Chair            <td>Phillip Lerche      <td>(2010)
<tr><td>                    <td>Eric Hofmeister     <td>(2010)
<tr><td>                    <td>Bonnie Wright       <td>(2011)
<tr><td>                    <td>Melissa Sinclair    <td>(2011)
<tr><td>                    <td>Dave Brunson        <td>(2011)
<tr><td>                    <td>Elizabeth Martinez  <td>(2012)
<tr><td>                    <td>Diane Wilson        <td>(2012)
<tr><td>                    <td>James Bailey        <td>(2012)
<tr><td>                    <td>Chris Egger         <td>(2013)
<tr><td>                    <td>Lynne Kushner       <td>(2013)
<tr><td>                    <td>Nigel Campbell      <td>(2013)
<tr><td><i>Ex officio</i>   <td>Bruno Pypendop      <td>(2011)

<tr><th colspan="3">
<a name="s3"></a>
Committee on Education                              <td class="top"><a href="#top">top</a>
<tr><td>Chair               <td>Heidi Shafford      <td>(2010)
<tr><td>                    <td>Khursheed Mama      <td>(2011)
<tr><td>                    <td>Ann Weil            <td>(2011)
<tr><td>                    <td>Lori Bidwell        <td>(2012)
<tr><td>Abstract Review     <td>Khursheed Mama      <td>
<tr><td>Abstract Coordinator<td>Craig Mosley        <td>
<tr><td>IVECCS Liaison      <td>Lydia Donaldson     <td>

<tr><th colspan="3">
<a name="s4"></a>
Appeals Committee                                   <td class="top"><a href="#top">top</a>
<tr><td>Chair               <td>Cliff Swanson       <td>(2010)
<tr><td>                    <td>Julie Smith         <td>(2011)
<tr><td>                    <td>Maria Glowaski      <td>(2011)

<tr><th colspan="3">
<a name="s5"></a>
Annual and 5-Year ABVS Report Committee             <td class="top"><a href="#top">top</a>
<tr><td>President           <td>Bob Meyer           <td>
<tr><td>Past-president      <td>David Martin        <td>
<tr><td>B.O.D. Chair        <td>Sophie Cuvelliez    <td>
<tr><td>Past B.O.D. Chair   <td>Tom Doherty         <td>
<tr><td>Executive Secretary <td>Lydia Donaldson     <td>
<tr><td>ABVS Representative <td>Jan Seahorn         <td>

<tr><th colspan="3">
<a name="s6"></a>
Committee on Residency Training                     <td class="top"><a href="#top">top</a>
<tr><td>Chair               <td>Debbie Wilson       <td>(2010)
<tr><td>                    <td>Andre Shih          <td>(2010)
<tr><td>                    <td>Stuart Clark-Price  <td>(2010)
<tr><td>                    <td>Bernd Driessen      <td>(2011)
<tr><td>                    <td>Daniel Pang         <td>(2011)

<tr><th colspan="3">
<a name="s7"></a>
Multiple Choice Exam Committee                      <td class="top"><a href="#top">top</a>
<tr><td>Chair               <td>Leigh Lamont        <td>(2010)
<tr><td>                    <td>Alonso Guedes       <td>(2010)
<tr><td>                    <td>Bruno Pypendop      <td>(2011)
<tr><td>                    <td>Kirsten Wegner      <td>(2011)
<tr><td>                    <td>Christina Braun     <td>(2011)
<tr><td><i>Ex officio</i>   <td>Frank Golder        <td>

<tr><th colspan="3">
<a name="s8"></a>
ACVAA-AVTA Liaison Committee                         <td class="top"><a href="#top">top</a>
<tr><td>Chair               <td>Diane Wilson        <td>(2011)
<tr><td>                    <td>Matt Read           <td>(2012)
<tr><td>                    <td>Emily McCobb        <td>(2012)

<tr><th colspan="3">
<a name="s9"></a>
ACVAA Website Committee                              <td class="top"><a href="#top">top</a>
<tr><td>Chair               <td>Stephanie Berry     <td>(2011)
<tr><td>                    <td>Kevin Concannon     <td>(2012)
<tr><td>                    <td>Ron Mandsager       <td>(2012)
<tr><td>                    <td>Pauline Wong        <td>(2012)

</table>

<h2>
Ad Hoc Committees
</h2>

<table class="comm">
<tr><th colspan="2">
<a name="a1"></a>
Marketing the ACVAA          <td class="top"><a href="#top">top</a>
<tr><td>                    <td>Victoria Lukasik

<tr><th colspan="2">
<a name="a2"></a>
Bylaws Amendment Committee  <td class="top"><a href="#top">top</a>
<tr><td>Chair               <td>Jan Seahorn
<tr><td>                    <td>Lori Bidwell
<tr><td>                    <td>Elizabeth Martinez
<tr><td>                    <td>Laurie Sorrell-Raschi

<tr><th colspan="2">
<a name="a3"></a>
Exam Review Committee       <td class="top"><a href="#top">top</a>
<tr><td>Chair               <td>Lois Wetmore
<tr><td>                    <td>Bruno Pypendop
<tr><td>                    <td>Dave Rankin
<tr><td>                    <td>Sophie Cuvelliez
<tr><td>                    <td>Juliana Figueiredo
<tr><td><i>Ex officio</i>   <td>Frank Golder
<tr><td><i>Ex officio</i>   <td>John Ludders

</table>

<a name="other"></a>
<h2>
Other Positions
</h2>

<table class="comm">
<tr><th>
ABVS Representative
<td class="top"><a href="#top">top</a>
<tr><td>Jan Seahorn
<tr><th>
ABVS Alternate
<td class="top"><a href="#top">top</a>
<tr><td>Lynelle Graham
<tr><th>
Banfield Anesthesia Procedures Consultants
<td class="top"><a href="#top">top</a>
<tr><td>Lynelle Graham
<tr><td>Stephanie Berry
<tr><td>Nora Matthews
<tr><td>Bob Meyer
<tr><th>
North American Veterinary Medical Education Consortium Representatives
<td class="top"><a href="#top">top</a>
<tr><td>Bonnie Wright
<tr><td>Rose McMurphy
<tr><th>
ACVIM Collaborative Listserve Representatives
<td class="top"><a href="#top">top</a>
<tr><td>Stuart Clark-Price
<tr><td>Manuel Martin-Flores
<tr><th>
ACVS Liaison
<td class="top"><a href="#top">top</a>
<tr><td>Sandie Perkowski
<tr><th>
NAVC Liaison
<td class="top"><a href="#top">top</a>
<tr><td>Khursheed Mama
<tr><th>
AVMA Liaison
<td class="top"><a href="#top">top</a>
<tr><td>Lydia Donaldson for AVMA 2010

</table>

        ''')

