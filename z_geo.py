DEFAULT = 'USA'
CONTINENT_ORDER = ["N. America", "C. America/Carib.", "S. America", "Europe", "Africa", "Asia", "Oceania", ]

COUNTRIES = {
    "N. America": [
        DEFAULT, 
        'Canada', 
        'Mexico', 
        ],
    "Europe": [
        'Albania',
        'Andorra',
        'Austria',
        'Belarus',
        'Belgium',
        'Bosnia and Herzegovina',
        'Bulgaria',
        'Croatia',
        'Czech Republic',
        'Denmark',
        'Estonia',
        'Finland',
        'France',
        'Germany',
        'Gibraltar',
        'Greece',
        'Hungary',
        'Iceland',
        'Ireland',
        'Italy',
        'Latvia',
        'Liechtenstein',
        'Lithuania',
        'Luxembourg',
        'Macedonia',
        'Malta',
        'Moldova',
        'Monaco',
        'Montenegro',
        'Netherlands',
        'Northern Ireland',
        'Norway',
        'Poland',
        'Portugal',
        'Romania',
        'Russia',
        'San Marino',
        'Serbia',
        'Slovakia',
        'Slovenia',
        'Spain',
        'Sweden',
        'Switzerland',
        'Ukraine',
        'United Kingdom',
        ],
    "C. America/Carib.": [
        'Anguilla',
        'Antigua and Barbuda',
        'Aruba',
        'Bahamas',
        'Barbados',
        'Belize',
        'Bermuda',
        'Cayman Is.',
        'Costa Rica',
        'Cuba',
        'Dominica',
        'Dominican Republic',
        'El Salvador',
        'Greenland',
        'Grenada',
        'Guadeloupe',
        'Guatemala',
        'Haiti',
        'Honduras',
        'Jamaica',
        'Martinique',
        'Montserrat',
        'Netherlands Antilles',
        'Nicaragua',
        'Panama',
        'Puerto Rico',
        'St. Barthelemy',
        'St. Kitts and Nevis',
        'St. Lucia',
        'St. Martin',
        'St. Pierre and Miquelon',
        'St. Vincent and the Grenadines',
        'Trinidad and Tobago',
        'Turks and Caicos Is.',
        'Virgin Is. (U.K.)',
        'Virgin Is. (U.S.)',
        ],
    "S. America": [
        'Argentina',
        'Bolivia',
        'Brazil',
        'Chile',
        'Colombia',
        'Ecuador',
        'Falkland Is.',
        'French Guiana',
        'Guyana',
        'Paraguay',
        'Peru',
        'Suriname',
        'Uruguay',
        'Venezuela',
        ],
    "Asia": [
        'Afghanistan',
        'Armenia',
        'Azerbaijan',
        'Bahrain',
        'Bangladesh',
        'Bhutan',
        'Brunei Darussalam',
        'Cambodia',
        'China',
        'Cyprus',
        'Georgia',
        'Hong Kong',
        'India',
        'Indonesia',
        'Iran',
        'Iraq',
        'Israel',
        'Japan',
        'Jordan',
        'Kazakhstan',
        'Korea, North',
        'Korea, South',
        'Kuwait',
        'Kyrgyz Republic',
        'Laos',
        'Lebanon',
        'Macao',
        'Malaysia',
        'Maldives',
        'Mongolia',
        'Myanmar',
        'Nepal',
        'Oman',
        'Pakistan',
        'Palestine',
        'Philippines',
        'Qatar',
        'Saudi Arabia',
        'Singapore',
        'Sri Lanka',
        'Syria',
        'Taiwan',
        'Tajikistan',
        'Thailand',
        'Timor-Leste',
        'Turkey',
        'Turkmenistan',
        'United Arab Emirates',
        'Uzbekistan',
        'Vietnam',
        'Yemen',
        ],
    "Africa": [
        'Algeria',
        'Angola',
        'Benin',
        'Botswana',
        'Burkina Faso',
        'Burundi',
        'Cameroon',
        'Cape Verde',
        'Central African Republic',
        'Chad',
        'Comoros',
        'Congo',
        'Congo',
        'Cote d\'Ivoire',
        'Djibouti',
        'Egypt',
        'Equatorial Guinea',
        'Eritrea',
        'Ethiopia',
        'Gabon',
        'Gambia',
        'Ghana',
        'Guinea-Bissau',
        'Guinea',
        'Kenya',
        'Lesotho',
        'Liberia',
        'Libya',
        'Madagascar',
        'Malawi',
        'Mali',
        'Mauritania',
        'Mauritius',
        'Mayotte',
        'Morocco',
        'Mozambique',
        'Namibia',
        'Niger',
        'Nigeria',
        'Reunion',
        'Rwanda',
        'Sao Tome and Principe',
        'Senegal',
        'Seychelles',
        'Sierra Leone',
        'Somalia',
        'South Africa',
        'St. Helena',
        'Sudan',
        'Swaziland',
        'Tanzania',
        'Togo',
        'Tunisia',
        'Uganda',
        'Western Sahara',
        'Zambia',
        'Zimbabwe',
        ],
    "Oceania": [
        'Australia',
        'Cook Is.',
        'Fiji',
        'French Polynesia',
        'Guam',
        'Kiribati',
        'Marshall Is.',
        'Micronesia',
        'Nauru',
        'New Caledonia',
        'New Zealand',
        'Niue',
        'Norfolk Island',
        'Northern Mariana Is.',
        'Palau',
        'Papua New Guinea',
        'Pitcairn Is.',
        'Samoa, American',
        'Samoa, Independent',
        'Solomon Is.',
        'Tokelau',
        'Tonga',
        'Tuvalu',
        'U.S. Minor Outlying Is.',
        'Vanuatu',
        'Wallis and Futuna',
        ],
}
################################################################################

def reverse_dict (dict):
    new = {}
    ks = dict.keys()
    for k in ks:
        v = dict[k]
        new[v] = k
    return new

def atoz (dict):
    ks = dict.keys()
    ks.sort()
    return ks

USA_STATES = {
    'Alabama': 'AL', 
    'Alaska': 'AK', 
    'Arizona': 'AZ', 
    'Arkansas': 'AR', 
    'California': 'CA', 
    'Colorado': 'CO', 
    'Connecticut': 'CT', 
    'Delaware': 'DE', 
    'Florida': 'FL', 
    'Georgia': 'GA', 
    'Hawaii': 'HI', 
    'Idaho': 'ID', 
    'Illinois': 'IL',
    'Indiana': 'IN', 
    'Iowa': 'IA', 
    'Kansas': 'KS', 
    'Kentucky': 'KY', 
    'Louisiana': 'LA', 
    'Maine': 'ME', 
    'Maryland': 'MD', 
    'Massachusetts': 'MA', 
    'Michigan': 'MI', 
    'Minnesota': 'MN', 
    'Mississippi': 'MS', 
    'Missouri': 'MO', 
    'Montana': 'MT',
    'Nebraska': 'NE', 
    'Nevada': 'NV', 
    'New Hampshire': 'NH', 
    'New Jersey': 'NJ', 
    'New Mexico': 'NM', 
    'New York': 'NY', 
    'North Carolina': 'NC', 
    'North Dakota': 'ND', 
    'Ohio': 'OH', 
    'Oklahoma': 'OK', 
    'Oregon': 'OR', 
    'Pennsylvania': 'PA', 
    'Rhode Island': 'RI', 
    'South Carolina': 'SC', 
    'South Dakota': 'SD', 
    'Tennessee': 'TN', 
    'Texas': 'TX', 
    'Utah': 'UT', 
    'Vermont': 'VT', 
    'Virginia': 'VA', 
    'Washington': 'WA', 
    'Washington, D.C.': 'DC', 
    'West Virginia': 'WV', 
    'Wisconsin': 'WI', 
    'Wyoming': 'WY', 
}
USA_STATES_LOOKUP = reverse_dict(USA_STATES)
USA_STATES_ORDER = atoz(USA_STATES)


CAN_STATES = {
    'Alberta': 'AB', 
    'British Columbia': 'BC', 
    'Manitoba': 'MB', 
    'New Brunswick': 'NB', 
    'Newfoundland and Labrador': 'NL', 
    'Northwest Territories': 'NT', 
    'Nova Scotia': 'NS', 
    'Nunavut': 'NU', 
    'Ontario': 'ON', 
    'Prince Edward Island': 'PE', 
    'Quebec': 'QC', 
    'Saskatchewan': 'SK', 
    'Yukon': 'YT', 
}
CAN_STATES_LOOKUP = reverse_dict(CAN_STATES)
CAN_STATES_ORDER = atoz(CAN_STATES)

MEX_STATES = {
    'Aguascalientes': 'AGS',
    'Baja California Norte': 'BCN',
    'Baja California Sur': 'BCS',
    'Campeche': 'CAM',
    'Chiapas': 'CHIS',
    'Chihuahua': 'CHIH',
    'Coahuila': 'COAH',
    'Colima': 'COL',
    'Distrito Federal': 'DF',
    'Durango': 'DGO',
    'Guanajuato': 'GTO',
    'Guerrero': 'GRO',
    'Hidalgo': 'HGO',
    'Jalisco': 'HAL',
    'Mexico (Estado de)': 'MEX',
    'Michoacan ': 'MICH',
    'Morelos': 'MOR',
    'Nayarit': 'NAY',
    'Nuevo Leon': 'NL',
    'Oaxaca': 'OAX',
    'Puebla': 'PUE',
    'Queretaro': 'QRO',
    'Quintana Roo': 'QROO',
    'San Luis Potosi': 'SLP',
    'Sinaloa': 'SIN',
    'Sonora': 'SON',
    'Tabasco': 'TAB',
    'Tamaulipas': 'TAMPS',
    'Tlaxcala': 'TLAX',
    'Veracruz': 'VER',
    'Yucatan': 'YUC',
    'Zacatecas': 'ZAC',
}
MEX_STATES_LOOKUP = reverse_dict(MEX_STATES)
MEX_STATES_ORDER = atoz(MEX_STATES)

