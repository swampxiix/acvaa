import os.path, cPickle, re

WWRTDIR = '/usr/local/wwrun'
BASEDIR = os.path.join(WWRTDIR, 'acva')
ACCTDIR = os.path.join(BASEDIR, 'accounts')
REGDIR = os.path.join(BASEDIR, 'reg')
EVENTDIR = os.path.join(BASEDIR, 'events')

EMAIL_REGISTER = os.path.join(REGDIR, 'email.dict')

DIPLSTR = 'T6yawy77cI11'
RESDSTR = 'c6z4d6G34AYx'

STATES = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']
STATES_LOOKUP = {'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AZ': 'Arizona', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia', 'HI': 'Hawaii', 'IA': 'Iowa', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'MA': 'Massachusetts', 'MD': 'Maryland', 'ME': 'Maine', 'MI': 'Michigan', 'MN': 'Minnesota', 'MO': 'Missouri', 'MS': 'Mississippi', 'MT': 'Montana', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NV': 'Nevada', 'NY': 'New York', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VA': 'Virginia', 'VT': 'Vermont', 'WA': 'Washington', 'WI': 'Wisconsin', 'WV': 'West Virginia', 'WY': 'Wyoming', }
PROVS = ['AB', 'BC', 'MB', 'NB', 'NL', 'NS', 'NT', 'NU', 'ON', 'PE', 'QC', 'SK', 'YT',]
PROVS_LOOKUP = {'AB': 'Alberta', 'BC': 'British Columbia', 'MB': 'Manitoba', 'NB': 'New Brunswick', 'NL': 'Newfoundland and Labrador', 'NS': 'Nova Scotia', 'NT': 'Northwest Territories', 'NU': 'Nunavut', 'ON': 'Ontario', 'PE': 'Prince Edward Island', 'QC': 'Quebec', 'SK': 'Saskatchewan', 'YT': 'Yukon',}

HARV_DIPL = 'B9cL4zb9526l'
HARV_RESD = 'W1PBy65Q567i'

ALL_ROLES = ['admin', 'diplomate', 'resident']

DIPL_REGISTER = os.path.join(REGDIR, 'diplomates.list')
RESD_REGISTER = os.path.join(REGDIR, 'residents.list')

EVENT_REGISTER = os.path.join(REGDIR, 'event_owners.dict')

JOB_CATS = ['Institution, Industry or Private Practice', 'Residency', 'Internship', 'Technician']
JOBDIR = os.path.join(BASEDIR, 'Jobs', 'job_files')
JOBCOUNT = os.path.join(JOBDIR, '.count')

######################################################
# MENU-RELATED CONSTANTS

MENUDIR = os.path.join(BASEDIR, 'menu_pieces')
menu_alltop = os.path.join(MENUDIR, 'all_top.html')
menu_admin = os.path.join(MENUDIR, 'admin_only.html')
menu_dips = os.path.join(MENUDIR, 'diplomates.html')
menu_cands = os.path.join(MENUDIR, 'candidates.html')
menu_allbottom = os.path.join(MENUDIR, 'all_bottom.html')
######################################################
# READ/WRITE FUNCTIONS

def rP(fullpath):
    try:
        file = open(fullpath, 'rb')
        p = cPickle.load(file)
        file.close()
    except IOError:
        p = {}
    return p

def wP(info, fullpath):
    file = open(fullpath, 'wb')
    cPickle.dump(info, file)
    file.close

def rText (fullpath):
    try:
        file = open(fullpath, 'r')
        txt = file.read()
        file.close()
    except IOError:
        txt = ''
    return txt

def wText (txt, fullpath):
    file = open(fullpath, 'w')
    file.write(txt)
    file.close()

######################################################
# SORT-RELATED FUNCTIONS

DIGITS = re.compile(r'[0-9]+')

def compnum(x, y):
    nx = ny = 0
    while True:
        a = DIGITS.search(x, nx)
        b = DIGITS.search(y, ny)
        if None in (a,b):
            return cmp(x[nx:], y[ny:])
        r = (cmp(x[nx:a.start()], y[ny:b.start()]) or
             cmp(int(x[a.start():a.end()]), int(y[b.start():b.end()])))
        if r:
            return r
        nx, ny = a.end(), b.end()


######################################################
MONTHS = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
FMONTHS = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

######################################################

COUNTRY_SELECT = '''
<select id="countryselect" name="country" class="input">

<optgroup label="N. America">
    <option>Canada</option>
    <option>Mexico</option>
    <option value="USA" SELECTED >United States of America</option>
</optgroup>

<optgroup label="Europe">
    <option>Albania</option>
    <option>Andorra</option>
    <option>Austria</option>
    <option>Belarus</option>
    <option>Belgium</option>
    <option>Bosnia and Herzegovina</option>
    <option>Bulgaria</option>
    <option>Croatia</option>
    <option>Czech Republic</option>
    <option>Denmark</option>
    <option>Estonia</option>
    <option>Finland</option>
    <option>France</option>
    <option>Germany</option>
    <option>Gibraltar</option>
    <option>Greece</option>
    <option>Hungary</option>
    <option>Iceland</option>
    <option>Ireland</option>
    <option>Italy</option>
    <option>Latvia</option>
    <option>Liechtenstein</option>
    <option>Lithuania</option>
    <option>Luxembourg</option>
    <option>Macedonia</option>
    <option>Malta</option>
    <option>Moldova</option>
    <option>Monaco</option>
    <option>Montenegro</option>
    <option>Netherlands</option>
    <option>Norway</option>
    <option>Poland</option>
    <option>Portugal</option>
    <option>Romania</option>
    <option>Russia</option>
    <option>San Marino</option>
    <option>Serbia</option>
    <option>Slovakia</option>
    <option>Slovenia</option>
    <option>Spain</option>
    <option>Sweden</option>
    <option>Switzerland</option>
    <option>Ukraine</option>
    <option>United Kingdom</option>
</optgroup>

<optgroup label="C. America/Carib.">
    <option>Anguilla</option>
    <option>Antigua and Barbuda</option>
    <option>Aruba</option>
    <option>Bahamas</option>
    <option>Barbados</option>
    <option>Belize</option>
    <option>Bermuda</option>
    <option>Cayman Is.</option>
    <option>Costa Rica</option>
    <option>Cuba</option>
    <option>Dominica</option>
    <option>Dominican Republic</option>
    <option>El Salvador</option>
    <option>Greenland</option>
    <option>Grenada</option>
    <option>Guadeloupe</option>
    <option>Guatemala</option>
    <option>Haiti</option>
    <option>Honduras</option>
    <option>Jamaica</option>
    <option>Martinique</option>
    <option>Montserrat</option>
    <option>Netherlands Antilles</option>
    <option>Nicaragua</option>
    <option>Panama</option>
    <option>Puerto Rico</option>
    <option>St. Barthelemy</option>
    <option>St. Kitts and Nevis</option>
    <option>St. Lucia</option>
    <option>St. Martin</option>
    <option>St. Pierre and Miquelon</option>
    <option>St. Vincent and the Grenadines</option>
    <option>Trinidad and Tobago</option>
    <option>Turks and Caicos Is.</option>
    <option>Virgin Is. (U.K.)</option>
    <option>Virgin Is. (U.S.)</option>
</optgroup>

<optgroup label="S. America">
    <option>Argentina</option>
    <option>Bolivia</option>
    <option>Brazil</option>
    <option>Chile</option>
    <option>Colombia</option>
    <option>Ecuador</option>
    <option>Falkland Is.</option>
    <option>French Guiana</option>
    <option>Guyana</option>
    <option>Paraguay</option>
    <option>Peru</option>
    <option>Suriname</option>
    <option>Uruguay</option>
    <option>Venezuela</option>
</optgroup>

<optgroup label="Asia">
    <option>Afghanistan</option>
    <option>Armenia</option>
    <option>Azerbaijan</option>
    <option>Bahrain</option>
    <option>Bangladesh</option>
    <option>Bhutan</option>
    <option>Brunei Darussalam</option>
    <option>Cambodia</option>
    <option>China</option>
    <option>Cyprus</option>
    <option>Georgia</option>
    <option>Hong Kong</option>
    <option>India</option>
    <option>Indonesia</option>
    <option>Iran</option>
    <option>Iraq</option>
    <option>Israel</option>
    <option>Japan</option>
    <option>Jordan</option>
    <option>Kazakhstan</option>
    <option>Korea, North</option>
    <option>Korea, South</option>
    <option>Kuwait</option>
    <option>Kyrgyz Republic</option>
    <option>Laos</option>
    <option>Lebanon</option>
    <option>Macao</option>
    <option>Malaysia</option>
    <option>Maldives</option>
    <option>Mongolia</option>
    <option>Myanmar</option>
    <option>Nepal</option>
    <option>Oman</option>
    <option>Pakistan</option>
    <option>Palestine</option>
    <option>Philippines</option>
    <option>Qatar</option>
    <option>Saudi Arabia</option>
    <option>Singapore</option>
    <option>Sri Lanka</option>
    <option>Syria</option>
    <option>Taiwan</option>
    <option>Tajikistan</option>
    <option>Thailand</option>
    <option>Timor-Leste</option>
    <option>Turkey</option>
    <option>Turkmenistan</option>
    <option>United Arab Emirates</option>
    <option>Uzbekistan</option>
    <option>Vietnam</option>
    <option>Yemen</option>
</optgroup>

<optgroup label="Africa">
    <option>Algeria</option>
    <option>Angola</option>
    <option>Benin</option>
    <option>Botswana</option>
    <option>Burkina Faso</option>
    <option>Burundi</option>
    <option>Cameroon</option>
    <option>Cape Verde</option>
    <option>Central African Republic</option>
    <option>Chad</option>
    <option>Comoros</option>
    <option>Congo</option>
    <option>Congo</option>
    <option>Cote d'Ivoire</option>
    <option>Djibouti</option>
    <option>Egypt</option>
    <option>Equatorial Guinea</option>
    <option>Eritrea</option>
    <option>Ethiopia</option>
    <option>Gabon</option>
    <option>Gambia</option>
    <option>Ghana</option>
    <option>Guinea-Bissau</option>
    <option>Guinea</option>
    <option>Kenya</option>
    <option>Lesotho</option>
    <option>Liberia</option>
    <option>Libya</option>
    <option>Madagascar</option>
    <option>Malawi</option>
    <option>Mali</option>
    <option>Mauritania</option>
    <option>Mauritius</option>
    <option>Mayotte</option>
    <option>Morocco</option>
    <option>Mozambique</option>
    <option>Namibia</option>
    <option>Niger</option>
    <option>Nigeria</option>
    <option>Reunion</option>
    <option>Rwanda</option>
    <option>Sao Tome and Principe</option>
    <option>Senegal</option>
    <option>Seychelles</option>
    <option>Sierra Leone</option>
    <option>Somalia</option>
    <option>South Africa</option>
    <option>St. Helena</option>
    <option>Sudan</option>
    <option>Swaziland</option>
    <option>Tanzania</option>
    <option>Togo</option>
    <option>Tunisia</option>
    <option>Uganda</option>
    <option>Western Sahara</option>
    <option>Zambia</option>
    <option>Zimbabwe</option>

<optgroup label="Oceania">
    <option>Australia</option>
    <option>Cook Is.</option>
    <option>Fiji</option>
    <option>French Polynesia</option>
    <option>Guam</option>
    <option>Kiribati</option>
    <option>Marshall Is.</option>
    <option>Micronesia</option>
    <option>Nauru</option>
    <option>New Caledonia</option>
    <option>New Zealand</option>
    <option>Niue</option>
    <option>Norfolk Island</option>
    <option>Northern Mariana Is.</option>
    <option>Palau</option>
    <option>Papua New Guinea</option>
    <option>Pitcairn Is.</option>
    <option>Samoa, American</option>
    <option>Samoa, Independent</option>
    <option>Solomon Is.</option>
    <option>Tokelau</option>
    <option>Tonga</option>
    <option>Tuvalu</option>
    <option>U.S. Minor Outlying Is.</option>
    <option>Vanuatu</option>
    <option>Wallis and Futuna</option>
</optgroup>
</select>
'''