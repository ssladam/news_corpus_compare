#Preprocessing, opportunity to replace words or phrases with ECs
#  DO NOT add "president" --> "presidentTrump" here, otherwise all instances
#  of "president obama" would be converted to "presidentTrump obama"
#  this should be used for fixed phrases ONLY


def get_phrases():
    #phrase_dict = {
    return {
            "Trans-Pacific Partnership": "TPP",\
            "North American Free Trade Agreement":"NAFTA",\
            "World Trade Organization":"WTO",\
            "fire and fury":"fireAndFury",\
            "lost jobs":"jobLosses",\
            "job losses":"jobLosses",\
            "chief of staff":"chiefOfStaff",\
            "E&E News":"EandENews",\
            "S&P 500":"SandP500",\
            "Immigration and Nationality Act":"immigrationAndNationalityAct",\
            "Club For Growth and Heritage":"clubForGrowthAndHeritage",\
            "Freedom Caucus":"freedomCaucus",\
            "Office of Personnel Management ":"officeOfPersonnelManagement",\
            "Office of Management and Budget":"officeOfManagementAndBudget",\
            "Office of Special Counsel":"officeOfSpecialCounsel",\
            #Here is my first hack-y cheat. To avoid phrase clumping, insert a determiner to force phrase-split
            #   the below will force the code to split this into "memorandum" and "donald trump", instead of a single term
            "memorandum donald trump":"memorandum which donald trump",\
            #My 2nd hack-y cheat: pre-filtering some terms that would be tricky to remove otherwise
            #   these terms become "nested" with other terms, easier to just axe them here
            "[sic]":"",\
            "percent":"",\
            "percentage":"",\
            


"Trans-Pacific Partnership":"TPP",\
"Fire and Fury":"fireAndFury",\
"North American Free Trade Agreement":"NAFTA",\
"World Trade Organization":"WTO",\
"lost jobs":"jobLosses",\
"job losses":"jobLosses",\
"chief of staff":"chiefOfStaff",\
"E&E News":"EandENews",\
"S&P 500":"SandP500",\
"Immigration and Nationality Act":"immigrationAndNationalityAct",\
"Club for Growth and Heritage":"clubForGrowthAndHeritage",\
"Freedom Caucus":"freedomeCaucus",\
"Office of Personnel Management":"officeOfPersonelManagement",\
"Office of Special Counsel":"officeOfSpecialCounsel",\
"memorandum donald trump":"memorandum which donald trump",\
"[sic]":"",\
"percent":"",\
"percentage":"",\
"Ohio Conservatives for a Change":"ohioConservativesForAChange",\
"Director of National Intelligence":"directorOfNationalIntelligence",\
"9th Circuit":"ninthCircuit",\
"back channel":"backChannel",\
"super pac":"superPAC",\
"chief security officer":"chiefSecurityOfficer",\
"progressive security corp":"progressiveSecurityCorps",\
"private email server":"privateEmailServer",\
"right to life":"rightToLife",\
"states rights":"statesRights",\
"emily\'s list":"emilysList",\
"National Diversity Coalition for Trump":"nationalDiversityCoalitionForTrump",\
"public defender":"publicDefender",\
"German Free Party":"germanFreeParty",\
"Justice and Development Party":"justiceAndDevelopmentParty",\
"border security":"borderSecurity",\
"defending digital democracy":"defendingDigitalDemocracy",\
"new york times":"newYorkTimes",\
"advertisement":"",\
"civil rights":"civilRights",\
"Morgan, Lewis & Bockius":"morganLewisAndBockius",\
"national security adviser":"nationalSecurityAdvisor",\
"William & Mary":"williamAndMary",\
"world health organization":"worldHealthOrganization",\
"Miller & Chevalier ":"millerAndChevalier",\
"improvised explosive device":"improvisedExplosiveDevice",\
"Sullivan & Cromwell":"sullivanAndCromwell",\
"second amendment":"secondAmendment",\
"2nd amendment":"secondAmendment",\
"Supplemental Nutrition Assistance Program":"supplmentalNutritionAssistanceProgram",\
"federal bureau of investigation":"fbi",\
"domestic abuse":"domesticAbuse",\
"political action committee":"pac",\
"customs and border protection":"customsAndBorderProtection",\
"crooked hillary":"crookedHillary",\
"federal election commission":"federalElectionCommission",\
"Department of Health and Human Services":"departmentOfHealthAndHumanServices",\
"united kingdom":"unitedKingdom",\
"American Civil Liberties Union":"americanCivilLibertiesUnion",\
"travel ban":"travelBan",\
"islamic exteremist":"islamicExtremist",\
"black lives matter":"blackLivesMatter",\
"need to impeach":"needToImpeach",\
"impeach":"trumpImpeachment",\
"national rifle association":"nationalRifleAssociation",\
"congressional reform act":"congressionalReformAct",\
"Immigration and Customs Enforcement ":"immigrationAndCustomsEnforcement",\
"undocumented immigrant":"undocumentedImmigrants",\
"undocumented immigrants":"undocumentedImmigrants",\
"organization for the prohibition of chemical weapons":"opcw",\
"food stamps":"foodstamps",\
"border wall":"borderwall",\



            }