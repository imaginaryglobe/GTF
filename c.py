""" 

This script is used to check if all the countries in the reversed_countries.json file have a corresponding image in the images folder.

"""



import json

import os

with open("reversed_countries.json") as file:
    data = json.load(file)
    COUNTRY_LIST = [country.lower() for country in data]
    #print(COUNTRY_LIST[0])


directory = os.fsencode("images/")

IMG_NAME_LIST = []
 
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    IMG_NAME_LIST.append(filename[0:2])

COUNTRY_ABBS = ["BD", "AR", "AU", "AT", "BE", "MR", "BF", "BG", "BA", "BB", "BN", "BO", "BH", "BI", "BJ", "BT", "JM", "BW", "WS", "BR", "BS", "BY", "BZ", "RU", "RW", "RS", "TL", "TM", "TJ", "RO", "GW", "GT", "GR", "GQ", "JP", "GY", "GE", "GD", "GB", "GA", "SV", "GN", "GM", "GH", "OM", "TN", "JO", "HR", "HT", "HU", "HN", "VE", "PW", "PT", "PY", "IQ", "PA", "PG", "PE", "PK", "PH", "PL", "ZM", "EE", "EG", "ZA", "EC", "IT", "VN", "SB", "ET", "SO", "ZW", "SA", "ES", "ER", "ME", "MD", "MG", "MA", "MC", "UZ", "MM", "ML", "MN", "MH", "MK", "MU", "MT", "MW", "MV", "UG", "TZ", "MY", "MX", "IL", "FR", "FI", "FJ", "NI", "NL", "NO", "NA", "VU", "NE", "NG", "NZ", "NP", "NR", "CI", "CH", "CO", "CN", "CM", "CL", "CA", "CG", "CF", "CD", "CZ", "CY", "CR", "CV", "CU", "SZ", "SY", "KG", "KE", "SS", "SR", "KI", "KH", "KN", "KM", "ST", "SK", "KR", "SI", "KP", "KW", "SN", "SM", "SL", "SC", "KZ", "SG", "SE", "SD", "DO", "DM", "DJ", "DK", "DE", "YE", "DZ", "US", "UY", "LB", "LC", "LA", "TV", "TW", "TT", "TR", "LK", "LI", "LV", "TO", "LT", "LU", "LR", "LS", "TH", "TG", "TD", "LY", "VA", "VC", "AE", "AD", "AG", "AF", "IS", "IR", "AM", "AL", "AO", "IN", "AZ", "IE", "ID", "UA", "QA", "MZ"]

TERRITORY_ABBS = ["AI", "CC", "MF", "MQ", "GF", "GG", "AQ", "AS", "AW", "AX", "BL", "BM", "BQ", "BV", "CK", "CX", "CW", "EH", "FK", "FM", "FO", "GI", "GL", "GP", "GS", "GU", "HK", "IM", "IO", "JE", "KY", "MO", "MP", "MS", "NC", "NF", "NU", "PF", "PM", "PN", "PR", "PS", "RE", "SH", "SJ", "SX", "TC", "TF", "TK", "UM", "VG", "VI", "WF", "YT"]

# print(len(IMG_NAME_LIST))
# print(len(COUNTRY_LIST))

for i in COUNTRY_LIST:
    if i.upper() not in COUNTRY_ABBS and i.upper() not in TERRITORY_ABBS:
        print(i)