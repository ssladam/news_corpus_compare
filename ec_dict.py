# This will be swapped out after processing is complete, now you're safe to
#  swap out individual words for their EC equivalent.

def get_ecs():
    ec_dict = {
        # return {
        "us": "unitedStates", \
        "usa": "unitedStates", \
        "united states": "unitedStates", \
        "united state": "unitedStates", \
        "president-elect donald trump": "presidentElectDonaldTrump", \
        "presidentelect donald trumps": "presidentElectDonaldTrump", \
        "presidentelect donald trump": "presidentElectDonaldTrump", \
        "presidentelect donald j trump": "presidentElectDonaldTrump", \
        "presidentelects": "presidentElectDonaldTrump", \
        "presidentelect": "presidentElectDonaldTrump", \
        "Melania Trump": "melaniaTrump", \
        "fbi director james comey": "jamesComey", \
        "comey": "jamesComey", \
        "mr rosss": "wilburRoss", \
        "mr ross": "wilburRoss", \
        "commerce secretary wilbur ross": "wilburRoss", \
        "ross": "wilburRoss", \
        "sen dianne feinstein": "dianneFienstein", \
        "feinstein": "dianneFienstein", \
        "mueller": "robertMueller", \
        "robert mueller": "robertMueller", \
        "counsel robert mueller": "robertMueller", \
        "special counsel": "robertMueller", \
        "eu": "europeanUnion", \
        "european union": "europeanUnion", \
        "white house press secretary sarah huckabee sanders": "sarahHuckabeeSanders", \
        "trump administration": "trumpAdministration", \
        "united nations": "unitedNations", \
        "un": "unitedNations", \
        "ina": "immigrationAndNationalityAct", \
        "ocare": "obamacare", \
        "russias": "russia", \
        "tariffs": "tariff", \
        "us tariff": "tariff", \
        "percent tariff": "tariff", \
        "tariff hike": "tariff", \
        # ====================Begin pasted from excel generator=====================
"abrams":"staceyAbrams",\
"account posing":"cybersecurity",\
"accountability crisis":"accountability",\
"aclu":"americanCivilLibertiesUnion",\
"act kareem lanier":"kareemLanier",\
"acting attorney general rosenstein":"rodRosenstein",\
"acting fbi director andrew mccabe":"andrewMccabe",\
"action committee":"pac",\
"ad hominem attack":"controversy",\
"adam meyers":"adamMeyers",\
"adm mike rogers":"mikeRogers",\
"adm ronny jackson":"ronnyJackson",\
"admiral ronny jackson":"ronnyJackson",\
"advertisement wallenstrom":"joelWallenstrom",\
"aide john kelly":"johnKelly",\
"alex jones":"alexJones",\
"alex stamos":"alexStamos",\
"Alex van der Zwaan":"alexVanDerZwaan",\
"alexander hamilton":"alexanderHamilton",\
"amanda renteria":"amandaRenteria",\
"amazon share":"amazon",\
"ambassador jon huntsman":"jonHuntsman",\
"america first policy":"americaFirst",\
"american civil liberty union":"americanCivilLibertiesUnion",\
"amy klobuchar":"amyKlobuchar",\
"anderson cooper":"andersonCooper",\
"andrew cuomo":"andrewCuomo",\
"andrew mccabe":"andrewMccabe",\
"andrew mccabe fired":"andrewMccabe",\
"andrew mccabe legal defense fund":"andrewMccabe",\
"anita hill":"anitaHill",\
"anna kain":"annaKain",\
"anthony":"anthonyScaramucci",\
"anthony gonzalez":"anthonyGonzalez",\
"anthony kennedy":"anthonyKennedy",\
"anthony scaramucci":"anthonyScaramucci",\
"antiabortion":"womensRights",\
"antiabortion credential":"antiabortion",\
"antitrump fervor":"trumpOpposition",\
"antonio villaraigosa":"antonioVillaraigosa",\
"antonio villaraigosa":"antonioVillaraigosa",\
"antonov":"anatolyAntonov",\
"apol":"davidJApol",\
"arbitration clause":"arbitration",\
"arbitration provision":"arbitration",\
"assad":"basharAlAssad",\
"assange":"julianAssange",\
"assassination":"espionage",\
"assistant attorney general stephen boyd":"stephenBoyd",\
"assistant attorney general stephen boyd":"stephenBoyd",\
"atlanta mayor keisha lance bottom":"keishaLanceBottoms",\
"attorney alex van der zwaan":"alexVanDerZwaan",\
"attorney general jeff session":"jeffSessions",\
"attorney general jeff session decision":"jeffSessions",\
"attorney general jeff session hour":"jeffSessions",\
"audra grassia":"audraGrassia",\
"avenatti":"michaelAvenatti",\
"avenatti point":"michaelAvenatti",\
"avenattis word":"michaelAvenatti",\
"background check":"backgroundChecks",\
"background check system":"backgroundChecks",\
"baker":"tonyBaker",\
"baltimore county executive kevin kamenetz":"kevinKamenetz",\
"bank fraud charge":"bankFraud",\
"bannon":"steveBannon",\
"barack obama":"barackObama",\
"barack obamas":"barackObama",\
"barbara lee":"barbaraLee",\
"barr":"roseanneBarr",\
"barrack":"tomBarrack",\
"barzee flores":"maryBarzeeFlores",\
"basta michael avenatti":"michaelAvenatti",\
"bella thorne":"roseanneBarr",\
"ben jealous":"benJealous",\
"bernie":"bernieSanders",\
"bernie sander":"bernieSanders",\
"betsy dirksen londrigan":"betsyDirksenLondrigan",\
"bezos":"jeffBezos",\
"bharara":"preetBharara",\
"biden":"joeBiden",\
"bill clinton":"billClinton",\
"bill gate":"billGates",\
"billionaire tom steyers campaign":"tomSteyer",\
"billionaire tom steyers impeachment crusade":"tomSteyer",\
"billionaire tom steyers trumpimpeachmentment crusade":"tomSteyer",\
"black life matter":"blackLivesMatter",\
"blakely":"brentBlakely",\
"bob lord":"bobLord",\
"bob woodward rule":"bobWoodward",\
"bold pac":"pac",\
"bolton":"johnBolton",\
"bolton fan":"johnBolton",\
"bolton spokesperson garrett marquis":"johnBolton",\
"boltons":"johnBolton",\
"booker":"coryBooker",\
"boyd":"stephenBoyd",\
"bredesen aide":"philBredesen",\
"bredesens letter":"philBredesen",\
"brendan kelly":"brendanKelly",\
"brennan":"johnBrennan",\
"brent blakely":"brentBlakely",\
"brexiteer nigel farage":"nigelFarage",\
"brian frosh":"brianFrosh",\
"britain":"unitedKingdom",\
"brittanie mountz":"brittanieMountz",\
"brostrom":"martinaBrostrom",\
"brother anthony scaramucci":"anthonyScaramucci",\
"bruce rauner":"bruceRauner",\
"buffy wick":"buffyWicks",\
"bush":"georgeWBush",\
"bush administration":"bushAdministration",\
"bush white house":"bushAdministration",\
"bush year":"georgeWBush",\
"bustani":"joseBustani",\
"california air resource board chairperson mary nichols":"maryNichols",\
"california democrat adam schiff":"adamSchiff",\
"california republican":"republican",\
"california republican party":"republican",\
"california sen kamala harris":"kamalaHarris",\
"cambridge analytica":"cambridgeAnalytica",\
"cambridge analytica employee":"cambridgeAnalytica",\
"campaign loss":"campaign",\
"campaign manager matt rhoades":"mattRhoades",\
"campaign politics":"campaign",\
"campaign spokesperson kevin harris":"benJealous",\
"campaign trump campaign chair paul manafort":"paulManafort",\
"canvassing":"campaign",\
"carlson":"tuckerCarlson",\
"carney":"jayCarney",\
"caroline":"carolineSunshine",\
"caroline sunshine":"carolineSunshine",\
"carolyns record":"carolynMaloney",\
"carter page":"carterPage",\
"casey":"conorCasey",\
"cbp":"customsAndBorderProtection",\
"ceo jeff bezos":"jeffBezos",\
"challenger suraj patels":"surajPatel",\
"challenger suraj patels":"surajPatel",\
"charles harder":"charlesHarder",\
"cheneyrumsfeld era":"bushAdministration",\
"chiefofstaff":"johnKelly",\
"chiefofstaff john kelly":"johnKelly",\
"chinese":"china",\
"chinese president xi jinping":"xiJinPing",\
"chris lacivita":"chrisLacivita",\
"chris smith":"chrisSmith",\
"christina hagan":"christinaHagan",\
"ci counterintelligence agent":"intelligence",\
"cia director mike pompeo":"mikePompeo",\
"cia directordesignate gina haspel":"ginaHaspel",\
"cindy hydesmith":"cindyHydeSmith",\
"citizenship question":"citizenship",\
"claire mccaskill":"claireMccaskill",\
"clarence thomas":"clarenceThomas",\
"clark case":"stephonClark",\
"clifford":"stormyDaniels",\
"clinton":"hillaryClinton",\
"clinton campaign":"hillaryClinton",\
"coalition builder":"coalition",\
"cobb":"tyCobb",\
"cohen":"michaelCohen",\
"cohn":"garyCohn",\
"comey":"jamesComey",\
"comey friend":"jamesComey",\
"comeys":"jamesComey",\
"commanderinchief":"donaldTrump",\
"confidentiality provision":"settlement",\
"connecticut democrat":"democrat",\
"conner household":"roseanneBarr",\
"conners":"roseanneBarr",\
"conor lamb":"conorLamb",\
"conor lamb defeated":"conorLamb",\
"conor lamb win":"conorLamb",\
"conservative":"extremeRight",\
"conspiracy theory":"controversy",\
"conversation fbi official":"fbi",\
"coon":"chrisCoons",\
"cooper":"cooperCaffrey",\
"cooper caffrey":"cooperCaffrey",\
"cooper didnt":"cooperCaffrey",\
"cooper didnt clap":"cooperCaffrey",\
"corey lewandowski":"coreyLewandowski",\
"corfman":"leighCorfman",\
"corporate average fuel economy":"mpg",\
"corsi":"jeromeCorsi",\
"counsel":"specialCounsel",\
"counsel investigation":"robertMueller",\
"counsel work":"specialCounsel",\
"county seat":"election",\
"crystal mason":"crystalMason",\
"culberson":"johnCulberson",\
"cut pruitt":"scottPruitt",\
"cyber command side":"cybersecurity",\
"cyber meddling":"cybersecurity",\
"cyberattack":"cybersecurity",\
"cyberattacks":"cybersecurity",\
"cybersecurity briefing":"cybersecurity",\
"cybersecurity correspondent":"cybersecurity",\
"cybersecurity firm":"cybersecurity",\
"cybersecurity guidance":"cybersecurity",\
"cybersecurity procedure":"cybersecurity",\
"daly":"shaunaDaly",\
"dan coat":"danCoats",\
"dan halpern":"danHalpern",\
"dan webb":"danWebb",\
"dana nessel":"danaNessel",\
"daniel":"stormyDaniels",\
"daniel settlement agreement":"stormyDaniels",\
"data analysis firm":"bigData",\
"data raise concern":"privacy",\
"david apol":"davidJApol",\
"david hogg":"davidHogg",\
"david hogg conflict":"davidHogg",\
"david j apol":"davidJApol",\
"david maxwell":"davidMaxwell",\
"david schwartz":"davidSchwartz",\
"david scott":"davidScott",\
"david shulkin":"davidShulkin",\
"davidhogg111":"davidHogg",\
"dcalif":"democrat",\
"dccc chair ben ray lujan":"benRayLujan",\
"dccc highlight":"dccc",\
"dccc official":"dccc",\
"dccc spokesman tyler law":"dccc",\
"dccc treat":"dccc",\
"dcccs":"dccc",\
"dcccs email strategy":"dccc",\
"dcccs frontline candidate":"dccc",\
"death joseph mann":"josephMann",\
"deb pryce":"deborahPryce",\
"deep state conspiracy":"deep state",\
"defending digital democracy cofounder":"defendingDigitalDemocracy",\
"defense secretary donald rumsfeld":"donaldRumsfeld",\
"defense secretary james mattis":"jamesMattis",\
"dem":"democrat",\
"democrat andrew janz":"andrewJanz",\
"democrat candidate":"democrat",\
"democrat linda coleman":"lindaColeman",\
"dems":"democrat",\
"deputy attorney general rod rosenstein":"rodRosenstein",\
"deputy director job":"office",\
"der zwaan":"alexVanDerZwaan",\
"deripaska":"olegDeripaska",\
"devin nunes":"devinNunes",\
"dewine":"mikeDewine",\
"dewine ally":"mikeDewine",\
"dewines campaign":"mikeDewine",\
"dewines spokesperson":"mikeDewine",\
"dianne feinstein":"dianneFienstein",\
"district attorney":"attorney",\
"dittmar":"kellyDittmar",\
"dncs":"dnc",\
"doe":"departmentOfEnergy",\
"doj inspector general":"michaelHorowitz",\
"doj spokesperson sarah isgur flores":"sarahIsgurFlores",\
"don mcgahn":"donMcgahn",\
"donald j trump":"donaldTrump",\
"donald jr":"donaldTrumpJr",\
"donald trump":"donaldTrump",\
"donald trump jr":"donaldTrumpJr",\
"donaldjtrumpjr":"donaldTrumpJr",\
"dowd":"johnDowd",\
"dprk":"northKorea",\
"dr david shulkins service":"davidShulkin",\
"dr luiz loures":"luizLoures",\
"dr ronny":"ronnyJackson",\
"dr ronny jackson":"ronnyJackson",\
"dubose porter":"dubosePorter",\
"ec":"essentialConsultants",\
"ec andor defendant trump":"donaldTrump",\
"economics":"economy",\
"economy standard":"economy",\
"election ballot":"election",\
"election bid":"eleciton",\
"election cycle":"election",\
"emma gonzalez":"emmaGonzalez",\
"emmanuel macron":"emmanuelMacron",\
"encryption software company":"cybersecurity",\
"epa administrator":"environmentalProtectionAgency",\
"epa administrator scott pruitt":"scottPruitt",\
"epa chief":"environmentalProtectionAgency",\
"epa chief pruitt":"scottPruitt",\
"epa decides":"environmentalProtectionAgency",\
"epa secretary":"environmentalProtectionAgency",\
"epa source":"environmentalProtectionAgency",\
"eric trump":"ericTrump",\
"escobar":"veronicaEscobar",\
"esper":"markEsper",\
"essential consultants":"essentialConsultants",\
"esty":"elizabethEsty",\
"estys":"elizabethEsty",\
"ethan":"ethanSonneborn",\
"ethan sonneborn":"ethanSonneborn",\
"eu twice":"europeanUnion",\
"europe":"europeanUnion",\
"european union":"europeanUnion",\
"exchange student tinka hessenheffer":"carolineSunshine",\
"facebook controversy":"facebook",\
"facebook data":"facebook",\
"facebook image":"facebook",\
"facebook post":"facebook",\
"facebooks":"facebook",\
"facebooks chiefsecurityofficer":"facebook",\
"fake news":"media",\
"farage":"nigelFarage",\
"fbi agent peter strzok":"peterStrzok",\
"fbi compliance":"fbi",\
"fbi confidential source":"fbi",\
"fbi deputy director":"fbi",\
"fbi deputy director andrew mccabe":"andrewMccabe",\
"fbi director":"fbiDirector",\
"fbi director chris wray":"chrisWray",\
"fbi director christopher wray":"christopherWray",\
"fbi director james":"jamesComey",\
"fbi informant":"fbi",\
"fbi lawyer lisa page":"lisaPage",\
"fbi leader":"fbi",\
"fbi mole robert hanssen":"espionage",\
"fbi office":"fbi",\
"fbi official":"fbi",\
"fbi policy":"fbi",\
"fec":"federalElectionCommission",\
"fec investigation":"federalElectionCommission",\
"federal election commission":"federalElectionCommission",\
"feinsteins":"dianneFienstein",\
"feinsteins campaign":"dianneFienstein",\
"feinsteins reelection":"election",\
"felony conviction":"felony",\
"fidel castro uprising":"fidelCastro",\
"fire robert mueller":"robertMueller",\
"firearm":"guns",\
"fisa abuse":"fisa",\
"fisa abuse allegation":"fisa",\
"fisa court":"fisa",\
"fisa warrant":"fisa",\
"fisc":"foreignIntelligenceSurveillanceCourt",\
"flores":"sarahIsgurFlores",\
"florida sen marco rubio":"marcoRubio",\
"flynn":"michaelFlynn",\
"food stamp":"foodStamps",\
"food stamp recipient":"foodStamps",\
"foreign intelligence surveillance act":"fisa",\
"foreign intelligence surveillance court":"fisa",\
"former president barack obama":"barackObama",\
"former veteran affair secretary david shulkin":"davidShulkin",\
"fox news host laura ingraham":"lauraIngraham",\
"fray democrat":"democrat",\
"french president emmanuel macron campaign":"emmanuelMacron",\
"fugh":"justinaFugh",\
"fundraising term":"fundraising",\
"gabby trejo":"gabbyTrejo",\
"garaufis":"nicholasGaraufis",\
"gate":"rickGates",\
"gavin newsom":"gavinNewsom",\
"gawker":"media",\
"gender inequality":"genderInequality",\
"george conway":"georgeConway",\
"george w bush":"georgeWBush",\
"georgiaborn stacey evans":"staceyEvans",\
"georgian":"georgia",\
"giant amazon":"amazon",\
"gillibrand":"kirstenGillibrand",\
"gina haspel":"ginaHaspel",\
"giuffra":"robertGiuffra",\
"gonzalez":"emmaGonzalez",\
"gonzalez event":"emmaGonzalez",\
"gonzalez supporter":"emmaGonzalez",\
"gonzalezs":"emmaGonzalez",\
"gonzalezs family tie":"emmaGonzalez",\
"gonzalezs hispanic":"emmaGonzalez",\
"gop hand":"republican",\
"gop senate candidate jim renacci":"jimRenacci",\
"gorka":"sebastianGorka",\
"governor kasich":"johnKasich",\
"gru":"russianIntelligence",\
"gru hacker":"russianIntelligence",\
"gsr":"globalScienceResearch",\
"guterres":"antonioGuterres",\
"hack":"cybersecurity",\
"hagan":"christinaHagan",\
"hagans":"christinaHagan",\
"hagans bid":"christinaHagan",\
"hagans campaign":"christinaHagan",\
"hagans father":"christinaHagan",\
"hank johnson":"hankJohnson",\
"hank johnson":"hankJohnson",\
"harassment claim":"harassment",\
"harper":"malayahHarper",\
"harris":"kamalaHarris",\
"harris candidacy":"kamalaHarris",\
"hart":"stephenVickiHart",\
"haspel":"ginaHaspel",\
"haspels critic":"ginaHaspel",\
"hawaii state rep beth fukumoto":"bethFukumoto",\
"health":"healthCare",\
"health care":"healthCare",\
"health care system":"healthCare",\
"heidi heitkamp":"heidiHeitkamp",\
"henley":"nathanielOaks",\
"hensarling":"jebHensarling",\
"heritage foundation":"heritageFoundation",\
"heritage foundation president":"heritageFoundation",\
"hhs":"departmentOfHealthAndHumanServices",\
"hick":"hopeHicks",\
"hillary":"hillaryClinton",\
"hillary clinton":"hillaryClinton",\
"hogg":"davidHogg",\
"hope hick":"hopeHicks",\
"horowitz":"michaelHorowitz",\
"house candidate":"election",\
"house democrat":"democrat",\
"house freedomcaucus":"extremeRight",\
"house intelligence committee":"houseIntelligenceCommittee",\
"house judiciary committee chairman bob goodlatte":"bobGoodlatte",\
"house majority leader kevin mccarthy":"kevinMccarthy",\
"house minority leader nancy pelosi":"nancyPelosi",\
"house oversight committee chairman trey gowdy":"treyGowdy",\
"house speaker nancy pelosi":"nancyPelosi",\
"house speaker paul ryan":"paulRyan",\
"huber":"johnHuber",\
"hydesmith":"cindyHydeSmith",\
"hyten":"johnHyten",\
"ice":"immigrationAndCustomsEnforcement",\
"illinois house seat":"election",\
"improvisedExplosiveDevice attack":"improvisedExplosiveDevice",\
"infrastructure plan":"infrastructure",\
"infrastructure reform":"infrastructure",\
"infrastructure remark":"infrastructure",\
"ingraham":"lauraIngraham",\
"ingraham angle":"lauraIngraham",\
"ingrahamangle":"lauraIngraham",\
"ingrahams":"lauraIngraham",\
"inspector general michael horowitz":"michaelHorowitz",\
"intelligence division":"intelligence",\
"intelligence officer":"intelligence",\
"intelligence service":"intelligence",\
"investigation compliance":"investigation",\
"iraq legacy":"iraqWar",\
"iraq war":"iraqWar",\
"isi":"islamicState",\
"isi fighter":"islamicState",\
"isi operation":"islamicState",\
"ivanka":"ivankaTrump",\
"ivanka trump":"ivankaTrump",\
"jackson":"ronnyJackson",\
"jacobson":"robertaJacobson",\
"james":"kayKoleJames",\
"james comey":"jamesComey",\
"james comeys":"jamesComey",\
"janz":"andrewJanz",\
"jared kushner":"jaredKushner",\
"jay sekulow":"jaySekulow",\
"jean schmidt":"jeanSchmidt",\
"jeb":"jebBush",\
"jeb bush":"jebBush",\
"jeb hensarling":"jebHensarling",\
"jeff bezos":"jeffBezos",\
"jeffbezos":"jeffBezos",\
"jefferson":"thomasJefferson",\
"jennie willoughby":"jennieWilloughby",\
"jennie willoughby willoughby":"jennieWilloughby",\
"jennings":"jScottJennings",\
"jerome corsi":"jeromeCorsi",\
"jim renacci":"jimRenacci",\
"jinping":"xiJinPing",\
"joel wallenstrom":"joelWallenstrom",\
"john bolton":"johnBolton",\
"john culberson":"johnCulberson",\
"john dowd":"johnDowd",\
"john goodman":"roseanneBarr",\
"john kasich":"johnKasich",\
"john kasich short":"johnKasich",\
"john kasichs bid":"johnKasich",\
"john podesta":"johnPodesta",\
"john robert":"johnRoberts",\
"john weaver":"johnWeaver",\
"jon ossoff":"jonOssoff",\
"jon huntsman":"jonHuntsman",\
"jon ossoff":"jonOssoff",\
"jon tester":"jonTester",\
"jordan":"jimJordan",\
"jose bustani":"joseBustani",\
"judge reinhardt":"stephenReinhardt",\
"judge stephen reinhardt":"stephenReinhardt",\
"julian assange":"julianAssange",\
"justice attorney":"justiceDepartment",\
"justice department":"justiceDepartment",\
"justice department inspector general":"justiceDepartment",\
"justice department inspector general michael horowitz":"michaelHorowitz",\
"justice department inspector general office":"justiceDepartment",\
"justice department official":"justiceDepartment",\
"justice department report":"justiceDepartment",\
"justice department spokesperson":"justiceDepartment",\
"justice department spokesperson sarah isgur flores":"sarahIsgurFlores",\
"justice inspector general investigation":"investigation",\
"justice overhaul":"justiceDepartment",\
"justice reform":"justiceDepartment",\
"justin fairfax":"justinFairfax",\
"kain":"annaKain",\
"kamala harris":"kamalaHarris",\
"karl racine":"karlRacine",\
"kasich":"johnKasich",\
"kasichs":"johnKasich",\
"kasichs endorsement":"johnKasich",\
"kasichs team arent":"johnKasich",\
"kay cole james":"kayKoleJames",\
"keisha lance bottom":"keishaLanceBottoms",\
"kelly":"johnKelly",\
"kelly mazeski":"kellyMazeski",\
"kellyanne":"kellyanneConway",\
"kellyanne conway":"kellyanneConway",\
"kentucky sen rand paul":"randPaul",\
"kevin collier":"kevinCollier",\
"kevin cramer":"kevinCramer",\
"kihuen":"rubenKihuen",\
"kihuens district":"rubenKihuen",\
"kilimnik":"konstantinKilimnik",\
"kim":"kimJongUn",\
"kim jong il":"kimJongUn",\
"kim jong un":"kimJongUn",\
"kim jongun":"kimJongUn",\
"kim talk":"kimJongUn",\
"kims":"kimJongUn",\
"kirsten gillibrand":"kirstenGillibrand",\
"konstantin kilimnik":"konstantinKilimnik",\
"korea":"northKorea",\
"krikorian":"markKrikorian",\
"kudlow":"larryKudlow",\
"kushner":"jaredKushner",\
"kushner cos":"jaredKushner",\
"ladavia drane":"ladaviaDrane",\
"lamb":"conorLamb",\
"larry hogan":"larryHogan",\
"larry kudlow":"larryKudlow",\
"latinas veronica escobar":"veronicaEscobar",\
"laura ingraham":"lauraIngraham",\
"laura moser":"lauraMoser",\
"laura olin":"lauraOlin",\
"lauren underwood":"laurenUnderwood",\
"laurie metcalf":"roseanneBarr",\
"lavrov":"sergeiLavrov",\
"law enforcement":"lawEnforcement",\
"law firm morganLewisAndBockius":"morganLewisAndBockius",\
"leader kim jong un":"kimJongUn",\
"leader kim jongun":"kimJongUn",\
"leader xi jinping":"xiJinPing",\
"leigh corfman":"leighCorfman",\
"lewandowski":"coreyLewandowski",\
"lewis":"stephenLewis",\
"line spy":"espionage",\
"lisa page":"lisaPage",\
"litman":"amandaLitman",\
"los angeles mayor":"ericGarcetti",\
"los angeles mayor eric garcetti":"ericGarcetti",\
"loss conor":"conorLamb",\
"loures":"luizLoures",\
"lowenergy jeb":"jebBush",\
"luis miranda":"cybersecurity",\
"luiz loures":"luizLoures",\
"luiz loures":"luizLoures",\
"lyndsey stuart":"lyndseyStuart",\
"mailer":"politicalMailer",\
"majority leader":"kevinMccarthy",\
"malayah harper":"malayahHarper",\
"malloch":"tedMalloch",\
"maloney":"carolynMaloney",\
"maloney meant":"carolynMaloney",\
"maloney spokesperson":"carolynMaloney",\
"maloney spokesperson george arzt":"carolynMaloney",\
"maloneys campaign":"carolynMaloney",\
"maloneys comment":"carolynMaloney",\
"manafort":"paulManafort",\
"manafort associate":"paulManafort",\
"manafort didnt":"paulManafort",\
"manafort isnt":"paulManafort",\
"manaforts business dealing":"paulManafort",\
"manaforts lawyer":"paulManafort",\
"manigault newman":"omarosaManigault",\
"manigaultnewman":"omarosaManigault",\
"mann case":"josephMann",\
"marco rubio":"marcoRubio",\
"margo oge":"environmentalProtectionAgency",\
"marine corp veteran grant goodrich":"grantGoodrich",\
"marjory stoneman douglas high school":"parkland",\
"mark penn":"markPenn",\
"mark zuckerberg":"markZuckerberg",\
"markos moulitsas":"markosMoulitsas",\
"martina brostrom":"martinaBrostrom",\
"mary barzee flores":"maryBarzeeFlores",\
"mary taylor":"maryTaylor",\
"mary taylor short":"maryTaylor",\
"marytayloroh":"maryTaylor",\
"mason":"crystalMason",\
"matt borges":"mattBorges",\
"matthew mcgregor":"matthewMcgregor",\
"mattis":"jamesMattis",\
"may runoff":"election",\
"mayor keisha lance bottom":"keishaLanceBottoms",\
"mazeski":"kellyMazeski",\
"mcauliffe":"terryMcauliffe",\
"mccabe":"andrewMccabe",\
"mccabe look":"andrewMccabe",\
"mccabes bos james comey":"jamesComey",\
"mccain":"johnMccain",\
"mccain twitter message":"tweet",\
"mccaskill":"claireMccaskill",\
"mcconnell":"mitchMcconnell",\
"mcgregor":"matthewMcgregor",\
"mcmaster":"HRMcmaster",\
"medicareforall bill":"medicareforall",\
"meet dr ronny":"ronnyJackson",\
"melissa schwartz":"andrewMccabe",\
"messitte":"peterMessitte",\
"metoo phenomenon":"metoo",\
"metoo story":"metoo",\
"michael avenatti":"michaelAvenatti",\
"michael avenattis":"michaelAvenatti",\
"michael cohen":"michaelCohen",\
"michael duchesne":"maryTaylor",\
"michael fishman":"roseanneBarr",\
"michael flynn":"michaelFlynn",\
"michael sulmeyer":"cybersecurity",\
"michael t flynn":"michaelFlynn",\
"michaelavenatti":"michaelAvenatti",\
"michel sidibe":"michelSidibe",\
"microsoft ceo steve ballmer":"steveBalmer",\
"middle east":"middleEast",\
"midterm forecaster":"election",\
"mike dewine":"mikeDewine",\
"mike dewines view":"mikeDewine",\
"mike lee":"mikeLee",\
"mileage commitment":"mpg",\
"mileage compromise":"mpg",\
"mileage rule":"mpg",\
"mileage target":"mpg",\
"minnesota republican":"republican",\
"minority leader stacey abrams":"staceyAbrams",\
"mitt romneys":"mittRomney",\
"model united nation team":"unitedNations",\
"mooch":"anthonyScaramucci",\
"mooch fundraiser":"anthonyScaramucci",\
"mook":"robbyMook",\
"moore":"royMoore",\
"morrison":"samuelMorrison",\
"moser":"lauraMoser",\
"mountz":"brittanieMountz",\
"mr cohen":"michaelCohen",\
"mr cohens":"michaelCohen",\
"mr flynn":"michaelFlynn",\
"mr huber":"johnHuber",\
"mr manafort":"paulManafort",\
"mr trump":"donaldTrump",\
"mrs trump":"melaniaTrump",\
"ms mason":"crystalMason",\
"ms stephanie clifford":"stormyDaniels",\
"multiple california democrat":"democrat",\
"nancy pelosi":"nancyPelosi",\
"nathan click":"gavinNewsom",\
"national security":"nationalSecurity",\
"national security adviser john bolton":"johnBolton",\
"national security type":"nationalSecurity",\
"nationalsecurityadvisor john bolton":"johnBolton",\
"neocon":"extremeRight",\
"neoconservative":"extremeRight",\
"nessel":"danaNessel",\
"nevada democratic operative":"democrat",\
"nevada independent":"independent",\
"nevada rep ruben kihuen":"rubenKihuen",\
"never trump republican":"never trump",\
"new jersey democrat":"democrat",\
"new jersey sen cory booker":"coryBooker",\
"new york city democrat":"democrat",\
"new york rep yvette clarke":"yvetteClarke",\
"new york republican":"republican",\
"newsom":"gavinNewsom",\
"newsom applies":"gavinNewsom",\
"newsom detail":"gavinNewsom",\
"newsom push":"gavinNewsom",\
"newsom supporter":"gavinNewsom",\
"newsoms camp":"gavinNewsom",\
"newsoms communication director":"gavinNewsom",\
"newsoms friend":"gavinNewsom",\
"newsoms resignation":"gavinNewsom",\
"nigel farage":"nigelFarage",\
"nikema williams":"nikemaWilliams",\
"nikulin":"yevgeniyNikulin",\
"nominee donald trump":"candidateDonaldTrump",\
"north korea":"northKorea",\
"north korean":"northKorea",\
"north koreas":"northKorea",\
"november midterm":"election",\
"nra":"nationalRifleAssociation",\
"nrcc spokesperson jesse hunt":"nrcc",\
"nunberg":"samNunberg",\
"nuzzi":"oliviaNuzz",\
"oak":"nathanielOaks",\
"obama":"barackObama",\
"obama administration":"obamaAdministration",\
"obama administration shut":"obamaAdministration",\
"obama campaign":"barackObama",\
"obama enters":"barackObama",\
"obama white house":"obamaAdministration",\
"obama year":"barackObama",\
"ohio conservative":"conservative",\
"ohio republican party chair jane timken":"janeTimken",\
"ohio right":"extremeRight",\
"ohioan jim jordan":"jimJordan",\
"oig":"officeOfInspectorGeneral",\
"oleg deripaska":"olegDeripaska",\
"olson":"tedOlson",\
"omalley":"martinOmalley",\
"omarosa manigaultnewman":"omarosaManigault",\
"ortega":"rosaMariaOrtega",\
"orville fleming":"orvilleFleming",\
"orville fleming sits":"orvilleFleming",\
"osama bin laden":"osamaBinLaden",\
"parkland school shooting":"parkland",\
"parkland shooting":"parkland",\
"parkland student":"parkland",\
"parkland survivor":"parkland",\
"paul manafort":"paulManafort",\
"pelosi":"nancyPelosi",\
"pelosi wouldnt answer":"nancyPelosi",\
"peninsula":"northKorea",\
"penn":"markPenn",\
"pennsylvania republican":"republican",\
"pete session":"peteSessions",\
"phil bredesen":"philBredesen",\
"police investigator hand":"investigation",\
"pollack":"barryPollack",\
"pollster bill mcinturff":"opinionPolls",\
"pompeo":"mikePompeo",\
"porter":"dubosePorter",\
"president":"donaldTrump",\
"president barack obama":"barackObama",\
"president bashar":"basharAlAssad",\
"president carter":"jimmyCarter",\
"president clinton":"billClinton",\
"president donald trump":"donaldTrump",\
"president donald trump shakeup":"donaldTrump",\
"president donald trump thursday":"donaldTrump",\
"president george hw":"georgeHWBush",\
"president george w bush":"georgeWBush",\
"president gerald ford":"geraldFord",\
"president meant":"donaldTrump",\
"president putin":"vladimirPutin",\
"president ronald reagan":"ronaldReagan",\
"president trump":"donaldTrump",\
"president victor yanukovych":"victorYanukovych",\
"president vladimir putin":"vladimirPutin",\
"president xi":"xiJinPing",\
"president xi jinping":"xiJinPing",\
"press secretary sarah huckabee sander":"sarahHuckabeeSanders",\
"priebus":"reincePriebus",\
"prime minister yulia tymoshenko":"yuliaTymoshenko",\
"priyanka mantha":"staceyAbrams",\
"pruitt":"scottPruitt",\
"public affair research poll":"opinionPolls",\
"pulikovsky":"konstantinPulikovsky",\
"putin":"vladimirPutin",\
"pyongyang":"northKorea",\
"qanon conspiracy":"qanon",\
"qanon hashtag":"qanon",\
"qanon refers":"qanon",\
"qanon theory":"qanon",\
"qanon tweet":"tweet",\
"qanons message":"qanon",\
"qu":"huaQu",\
"question renterias intention":"amandaRenteria",\
"quinnipiac poll":"opinionPolls",\
"race isnt":"race",\
"racine":"karlRacine",\
"racketeering case":"racketeering",\
"raffel":"joshRaffel",\
"raffi krikorian":"raffiKrikorian",\
"rakhine state":"myanmar",\
"rand paul":"randPaul",\
"rauner":"bruceRauner",\
"ravel":"federalElectionCommission",\
"ravel point":"federalElectionCommission",\
"rcalif":"republican",\
"redfield":"robertRedfieldJr",\
"redfields":"robertRedfieldJr",\
"reform act":"congressionalReformAct",\
"reid":"harryReid",\
"reid letter":"harryReid",\
"reince":"reincePriebus",\
"reince priebus":"reincePriebus",\
"reinhardt":"stephenReinhardt",\
"remember harriet miers":"harrietMiers",\
"renacci":"jimRenacci",\
"renteria":"amandaRenteria",\
"renteria incident":"amandaRenteria",\
"renterias case":"amandaRenteria",\
"renterias resignation effort":"amandaRenteria",\
"rep carolyn maloney":"carolynMaloney",\
"rep elise stefanik":"eliseStefanik",\
"rep eric swalwell":"ericSwalwell",\
"rep gene green":"geneGreen",\
"rep jeb hensarling":"jebHensarling",\
"rep jim jordan":"jimJordan",\
"rep john lewis":"johnLewis",\
"rep maloney":"carolynMaloney",\
"rep marcia fudge":"marciaFudge",\
"reps marcia fudge":"marciaFudge",\
"reps robert goodlatte":"bobGoodlatte",\
"republican john culberson":"johnCulberson",\
"republican larry hogan":"larryHogan",\
"republican party future":"republican party",\
"republican politics":"republican",\
"republican pollster bill mcinturff":"opinionPolls",\
"republican will hurd":"willHurd",\
"republicancontrolled":"republican",\
"republicanled house intelligence committee":"houseIntelligenceCommittee",\
"ricci":"andrewRicci",\
"rice":"susanRice",\
"richard ojeda":"richardOjeda",\
"rick gate":"rickGates",\
"rick scott":"rickScott",\
"rippey gibney":"rubyRippeyGibney",\
"rnc":"republicanNationalConvention",\
"rob frost":"robFrost",\
"robby mook":"robbyMook",\
"robert redfield jr":"robertRedfieldJr",\
"robert wilkie":"robertWilkie",\
"rodman":"dennisRodman",\
"roger stone":"rogerStone",\
"ronny jackson":"ronnyJackson",\
"rosa maria ortega":"rosaMariaOrtega",\
"roseanne":"roseanneBarr",\
"roseanne barr":"roseanneBarr",\
"roseanne reply":"roseanneBarr",\
"ruben":"rubenKihuen",\
"ruby rippey gibney":"rubyRippeyGibney",\
"ruby rippey gibney":"rubyRippeyGibney",\
"rumsfelds":"donaldRumsfeld",\
"rushern l baker iii":"rushernBaker",\
"russian":"russia",\
"russian president vladimir putin":"vladimirPutin",\
"ryan":"paulRyan",\
"sacramento county prosecutor noah phillips":"noahPhillips",\
"sacramento district attorney race":"election",\
"sale tax collection":"tax",\
"salud carbajal":"saludCarbajal",\
"sam nunberg":"samNunberg",\
"sander":"bernieSanders",\
"sara gilbert":"roseanneBarr",\
"scalise":"steveScalise",\
"scaramucci":"anthonyScaramucci",\
"scaramucci event":"anthonyScaramucci",\
"school student":"student",\
"schubert":"anneMarieSchubert",\
"schumer":"chuckSchumer",\
"schwartz":"andrewMccabe",\
"SCL":"SCLGroup",\
"scoreboard trump job performance average approval":"opinionPolls",\
"scott jennings":"jScottJennings",\
"secondamendment right":"secondAmendment",\
"secondamendment will never be repealed":"secondAmendment",\
"secretarygeneral":"unitedNations",\
"secure technology":"cybersecurity",\
"security world":"cybersecurity",\
"sekulow":"jaySekulow",\
"sekulows team":"jaySekulow",\
"sen ben sasse":"benSasse",\
"sen chris coon":"chrisCoons",\
"sen chuck grassley":"chuckGrassley",\
"sen claire mccaskill":"claireMccaskill",\
"sen dianne feinsteins bid":"dianneFienstein",\
"sen heidi heitkamp":"heidiHeitkamp",\
"sen john mccain":"johnMccain",\
"sen jon tester":"jonTester",\
"sen lindsey graham":"lindseyGraham",\
"sen marco rubio":"marcoRubio",\
"sen orrin hatch":"orrinHatch",\
"sen sheldon whitehouse":"sheldonWhitehouse",\
"sen thad cochran seat":"thadCochran",\
"sen thom tillis":"thomTillis",\
"senate democratic leader chuck schumer":"chuckSchumer",\
"senate judiciary chairman chuck grassley":"chuckGrassley",\
"senate majority leader mitch mcconnell":"mitchMcconnell",\
"senate minority leader chuck schumer":"chuckSchumer",\
"senator kirsten gillibrand":"kirstenGillibrand",\
"sergei lavrov":"sergeiLavrov",\
"sergei skripal":"sergeiSkripal",\
"sergei skripal":"sergeiSkripal",\
"settlement agreement":"settlement",\
"shaub":"walterShaub",\
"shauna daly":"shaunaDaly",\
"sheryl sandberg":"sherylSandberg",\
"sheryl sandberg":"sherylSandberg",\
"shulkin":"davidShulkin",\
"shulkins":"davidShulkin",\
"shulkins wife":"davidShulkin",\
"sidibe":"michelSidibe",\
"sinclair":"sinclairBroadcastGroup",\
"skadden arp law firm":"lawFirm",\
"skripal":"sergeiSkripal",\
"snap":"supplmentalNutritionAssistanceProgram",\
"snap benefit":"supplmentalNutritionAssistanceProgram",\
"soninlaw":"jaredKushner",\
"soninlaw jared kushner":"jaredKushner",\
"sorensen":"davidSorensen",\
"south korea":"southKorea",\
"south koreas":"southKorea",\
"soviet union":"russia",\
"special counsel robert mueller":"robertMueller",\
"spy sergei skripal":"sergeiSkripal",\
"stacey abrams":"staceyAbrams",\
"stacey abrams porter":"staceyAbrams",\
"stacey evans":"staceyEvans",\
"stamos":"alexStamos",\
"star stormy daniel":"stormyDaniels",\
"state department spokesperson heather nauert":"stateDepartment",\
"state rex tillerson":"rexTillerson",\
"state sen toni atkins":"toniAtkins",\
"state tax internet sale":"tax",\
"statedesignate mike pompeo":"mikePompeo",\
"stephanie clifford":"stormyDaniels",\
"stephen lewis":"stephenLewis",\
"steve bannon":"steveBannon",\
"steven hart":"stephenVickiHart",\
"steyer":"tomSteyer",\
"stormy daniel":"stormyDaniels",\
"stormy daniel lawyer":"stormyDaniels",\
"stormy daniel story":"stormyDaniels",\
"strategic communication laboratory":"cambridgeAnalytica",\
"strzok":"peterStrzok",\
"stuart":"lyndseyStuart",\
"stubenrauch":"mikeDewine",\
"subscribe president donald trump":"donaldTrump",\
"summer new york primary":"election",\
"summer zervos":"summerZervos",\
"sunshine":"carolineSunshine",\
"superpacs":"pac",\
"support newsom":"gavinNewsom",\
"supreme court brief":"USSupremeCourt",\
"supreme court justice john paul stevens":"johnPaulStevens",\
"supreme court justice stevens":"johnPaulStevens",\
"survivor david hogg":"davidHogg",\
"swalwell":"ericSwalwell",\
"tarrant county jail":"lawEnforcement",\
"tax collection software":"tax",\
"tax dollar":"tax",\
"tax jurisdiction":"tax",\
"tax preparer":"tax",\
"tax requirement":"tax",\
"tax return":"tax",\
"taylor":"maryTaylor",\
"taylor campaign":"maryTaylor",\
"taylor face":"maryTaylor",\
"tco4fcna1agaa donald trump jr":"donaldTrumpJr",\
"tea party":"teaParty",\
"tell qanon":"qanon",\
"terry mcauliffe":"terryMcauliffe",\
"tester":"jonTester",\
"texas republican will hurd":"willHurd",\
"texas sen ted cruz":"tedCruz",\
"threat intelligence researcher":"intelligence",\
"thursday kihuen":"rubenKihuen",\
"tillerson":"rexTillerson",\
"tillis":"thomTillis",\
"time maloney":"carolynMaloney",\
"timken":"janeTimken",\
"tokyo":"japan",\
"tom steyer":"tomSteyer",\
"toni gidwani":"toniGidwani",\
"tony baker":"tonyBaker",\
"trade deal":"trade",\
"treasury secretary":"USTreasury",\
"trend poll":"poll",\
"trey gowdy":"treyGowdy",\
"trump":"donaldTrump",\
"trump administration official":"trumpAdministration",\
"trump attempt":"donaldTrump",\
"trump attorney ty cobb":"tyCobb",\
"trump campaign adviser carter page":"carterPage",\
"trump campaign adviser roger stone":"rogerStone",\
"trump campaign chairman paul manafort":"paulManafort",\
"trump daughter ivanka":"ivankaTrump",\
"trump directorofnationalintelligence":"directorOfNationalIntelligence",\
"trump era":"donaldTrump",\
"trump joining":"donaldTrump",\
"trump lawyer john dowd":"johnDowd",\
"trump lawyer michael cohen":"michaelCohen",\
"trump orbit":"donaldTrump",\
"trump order epa":"environmentalProtectionAgency",\
"trump push":"donaldTrump",\
"trump universe":"donaldTrump",\
"trump white house":"white house",\
"trumpputin revelation":"russia",\
"tucker carlson":"tuckerCarlson",\
"turkey justiceAndDevelopmentParty":"extremeRight",\
"tweet":"twitter",\
"tweet read":"tweet",\
"tweet saturday evening":"tweet",\
"tweet sunday morning":"tweet",\
"twitter account":"tweet",\
"twitter aim":"tweet",\
"twitter attack":"tweet",\
"twitter post":"tweet",\
"twitter profile":"tweet",\
"twitter thursday":"tweet",\
"ty cobb":"tyCobb",\
"tymoshenko":"yuliaTymoshenko",\
"u attorney":"USAttorney",\
"u attorney john huber":"johnHuber",\
"u constitution":"constitution",\
"u court":"USCourt",\
"u immigration system":"USImmigration",\
"u official":"USOfficial",\
"u supreme court":"USSupremeCourt",\
"u troop":"USTroops",\
"un ambassador":"unitedNations",\
"un official":"unitedNations",\
"un secretarygeneral":"UNSecretaryGeneral",\
"un system":"unitedNations",\
"underwood":"laurenUnderwood",\
"united nation":"unitedNations",\
"united state anatoly antonov":"anatolyAntonov",\
"united state postal service":"USPostalService",\
"us attorney john huber":"johnHuber",\
"us attorney john w huber speaks":"johnHuber",\
"us foreign intelligence surveillance court":"fisa",\
"us job":"jobs",\
"us rep elizabeth esty":"elizabethEsty",\
"va":"veteransAffairs",\
"va chief david shulkin":"davidShulkin",\
"va employee":"veteransAffairs",\
"va health care":"veteransAffairs",\
"va president donald trump":"donaldTrump",\
"va secretary":"veteransAffairs",\
"va secretary david shulkin":"davidShulkin",\
"va system":"veteransAffairs",\
"van der zwaan":"alexVanDerZwaan",\
"veronica escobar":"veronicaEscobar",\
"veteran affair":"veteransAffairs",\
"veteran affair david shulkin":"davidShulkin",\
"veteran affair david shulkin wednesday":"davidShulkin",\
"veteran affair nominee dr ronny jackson":"ronnyJackson",\
"veteran affair secretary":"veteransAffairs",\
"veteran affair secretary david shulkin":"davidShulkin",\
"vice president dick cheney":"dickCheney",\
"vice president mike penny":"mikePence",\
"victoria toensing":"victoriaToensing",\
"villaraigosa":"antonioVillaraigosa",\
"virginia sen mark warner":"markWarner",\
"vitiello":"ronaldVitiello",\
"vladimir putin":"vladimirPutin",\
"walker":"scottWalker",\
"wall street journal profile devin nunes":"devinNunes",\
"wallenstrom":"joelWallenstrom",\
"wang":"xiYueWang",\
"warner":"markWarner",\
"warren":"elizabethWarren",\
"weaver":"johnWeaver",\
"webb":"danWebb",\
"white house chiefofstaff":"johnKelly",\
"white house chiefofstaff john kelly":"johnKelly",\
"white house communication director":"sarahHuckabeeSanders",\
"white house hopeful":"election",\
"white house press secretary sarah huckabee sander":"sarahHuckabeeSanders",\
"white house press secretary sarah sander":"sarahHuckabeeSanders",\
"white house spokesperson lindsay walter":"lindsayWalter",\
"wickrs ceo":"wickr",\
"wikileaks founder julian assange":"julianAssange",\
"willoughby":"jennieWilloughby",\
"woman equality":"womensRights",\
"work requirement":"supplmentalNutritionAssistanceProgram",\
"wray":"christopherWray",\
"wylie":"christopherWylie",\
"wyoming rep liz cheney":"lizCheney",\
"xi":"xiJinPing",\
"xi jinping":"xiJinPing",\
"xiyue wang":"xiYueWang",\
"yekaterinburg":"russia",\
"zwaan":"alexVanDerZwaan",\
"ingrahams program":"lauraIngraham",\
"armstrong":"fultonArmstrong",\
"fulton armstrong":"fultonArmstrong",\
"intelligence community":"intelligence",\
"muellers team":"robertMueller",\
"hutchings":"robertHutchings",\
"robert hutchings":"robertHutchings",\
"kushners statement":"jaredKushner",\
"mr dowd":"johnDowd",\
"kislyak":"sergeyKislyak",\
"sergey i kislyak":"sergeyKislyak",\
"united state sergei kislyak":"sergeyKislyak",\
"russian ambassador sergey kislyak":"sergeyKislyak",\
"twitter follower":"tweet",\
"judge josann reynolds":"josannReynolds",\
"reynolds":"josannReynolds",\
"ingrahams tweet":"tweet",\
"laura ingraham show":"lauraIngraham",\
"trump jr":"donaldTrumpJr",\
"aca":"obamacare",\
"vicki hart":"stephenVickiHart",\
"parkland student david hogg":"davidHogg",\
"tcowfla4hwhxy laura ingraham":"lauraIngraham",\
"haass":"richardHaass",\
"richard haass":"richardHaass",\
"affordable care act":"obamacare",\
"manaforts":"paulManafort",\
"scott walker":"scottWalker",\
"laura ingrahams show":"lauraIngraham",\
"gibson":"leslieGibson",\
"leslie gibson":"leslieGibson",\
"dhs official":"dhs",\
"gowdy":"treyGowdy",\
"cheung":"stevenCheung",\
"steven cheung":"stevenCheung",\
"president steven cheung":"stevenCheung",\
"nunes":"devinNunes",\
"opcw chief":"opcw",\
"counsel robert mueller robert swan muellersasse":"robertMueller",\
"ingrahams advertiser":"lauraIngraham",\
"j steven hart":"stephenVickiHart",\
"oval office":"donaldTrump",\
"marjory stoneman douglas high school student david hogg":"davidHogg",\
"manaforts offer":"paulManafort",\
"sen richard blumenthal":"richardBlumenthal",\
"richard blumenthal":"richardBlumenthal",\
"blumenthal":"richardBlumenthal",\
"gorsuch":"neilGorsuch",\
"justice neil gorsuch":"neilGorsuch",\
"neil gorsuch":"neilGorsuch",\
"john bolton superpac":"pac",\
"lauren hogg":"davidHogg",\
"muellers":"robertMueller",\
"oligarch oleg deripaska":"olegDeripaska",\
"parkland survivor david hogg":"davidHogg",\
"president obama":"barackObama",\
"tweet wednesday":"tweet",\
"laura ingrahams program":"lauraIngraham",\
"tax increase":"tax",\
"istandwithlaura":"lauraIngraham",\
"strang":"stephenStrang",\
"stephen strang":"stephenStrang",\
"beautiful wall":"borderwall",\





        
        # ================end pasted section====================

    }
    # the parser converts all entries to lower case, so we should do the same
    ec_dict = {key.lower(): value for key, value in ec_dict.items()}
    return ec_dict