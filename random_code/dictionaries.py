#!/usr/bin/env python3

__author__ = "Stephen J. Burke"
__email__ = "steburke71@hotmail.com"
__date__ = "2/19/18"
__license__ = "GPL"

emailByState = {
    "AK": "Senator_Stevens@stevens.senate.gov",
    "AL": "senator@shelby.senate.gov",
    "AR": "senator.hutchinson@hutchinson.senate.gov",
    "AZ": "Senator_McCain@mccain.senate.gov",
    "CA": "senator@feinstein.senate.gov",
    "CO": "data@nighthorse.falcontech.com",
    "CT": "senator_lieberman@lieberman.senate.gov",
    "DE": "senator@biden.senate.gov",
    "FL": "bob_graham@graham.senate.gov",
    "GA": "senator_max_cleland@cleland.senate.gov",
    "HI": "senator@inouye.senate.gov",
    "IA": "tom_harkin@harkin.senate.gov",
    "ID": "larry_craig@craig.senate.gov",
    "IL": "senator@moseley-braun.senate.gov",
    "IN": "lugar@iquest.net",
    "KS": "sam_brownback@brownback.senate.gov",
    "KY": "senator@mcconnell.senate.gov",
    "LA": "senator@breaux.senate.gov",
    "MA": "senator@kennedy.senate.gov",
    "MD": "senator@mikulski.senate.gov",
    "ME": "senator@collins.senate.gov",
    "MI": "senator@levin.senate.gov",
    "MN": "senator@wellstone.senate.gov",
    "MO": "kit_bond@bond.senate.gov",
    "MS": "senatorlott@lott.senate.gov",
    "MT": "max@baucus.senate.gov",
    "NC": "senator@faircloth.senate.gov",
    "ND": "senator@conrad.senate.gov",
    "NE": "bob@kerrey.senate.gov",
    "NH": "opinion@smith.senate.gov",
    "NJ": "frank_lautenberg@lautenberg.senate.gov",
    "NM": "Senator_Bingaman@bingaman.senate.gov",
    "NV": "senator_reid@reid.senate.gov",
    "NY": "Senator@dpm.senate.gov",
    "OH": "Senator_Glenn@glenn.senate.gov",
    "OK": "nickles@rpc.senate.gov",
    "OR": "wyden@teleport.com",
    "PA": "senator@santorum.senate.gov",
    "RI": "senator_chafee@chafee.senate.gov",
    "SC": "senator@thurmond.senate.gov",
    "SD": "tom_daschle@daschle.senate.gov",
    "TN": "senator_frist@frist.senate.gov",
    "TX": "senator@hutchison.senate.gov",
    "UT": "senator_hatch@hatch.senate.gov",
    "VA": "senator@robb.senate.gov",
    "VT": "senator_leahy@leahy.senate.gov",
    "WA": "senator_murray@murray.senate.gov",
    "WI": "senator_kohl@kohl.senate.gov",
    "WY": "craig@thomas.senate.gov"
}
# print(emailByState["MA"])

while True:
    dicKey = input('\n' + "Enter a valid two letter State abbreviation: ").upper()
    if dicKey == "EXIT":
        print('\n' + 'now exiting, bye!')
        break
    if dicKey in emailByState:
        email = emailByState.get(dicKey)
        print('The email for {1} is: {0}'.format(email, dicKey))
