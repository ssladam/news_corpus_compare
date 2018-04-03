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
"abortion clinic":"abortion",\
"abortion provider":"abortion",\
"abrams":"staceyAbrams",\
"aca":"obamacare",\
"account posing":"cybersecurity",\
"accountability crisis":"accountability",\
"act kareem lanier":"kareemLanier",\
"acting attorney general rosenstein":"rodRosenstein",\
"acting fbi director andrew mccabe":"andrewMccabe",\
"action committee":"pac",\
"ad hominem attack":"controversy",\
"adam meyers":"adamMeyers",\
"adm mike rogers":"mikeRogers",\
"adm ronny jackson":"ronnyJackson",\
"administrator pruitt":"scottPruitt",\
"admiral ronny jackson":"ronnyJackson",\
"advertisement wallenstrom":"joelWallenstrom",\
"affordable care act":"obamacare",\
"african":"africa",\
"aide john kelly":"johnKelly",\
"alex jones":"alexJones",\
"alex stamos":"alexStamos",\
"Alex van der Zwaan":"alexVanDerZwaan",\
"alexander hamilton":"alexanderHamilton",\
"alexander nix":"cambridgeAnalytica",\
"alito":"samuelAlito",\
"amanda renteria":"amandaRenteria",\
"amazon share":"amazon",\
"ambassador jon huntsman":"jonHuntsman",\
"america first policy":"americaFirst",\
"american civil liberty union":"aclu",\
"americancivillibertiesunion":"aclu",\
"amy klobuchar":"amyKlobuchar",\
"amzn":"amazon",\
"anderson cooper":"andersonCooper",\
"andrew cuomo":"andrewCuomo",\
"andrew mccabe":"andrewMccabe",\
"andrew mccabe fired":"andrewMccabe",\
"andrew mccabe legal defense fund":"andrewMccabe",\
"andrew mccabes fbi career":"andrewMccabe",\
"anita hill":"anitaHill",\
"anna kain":"annaKain",\
"anthony":"anthonyScaramucci",\
"anthony gonzalez":"anthonyGonzalez",\
"anthony kennedy":"anthonyKennedy",\
"anthony kennedy":"anthonyKennedy",\
"anthony scaramucci":"anthonyScaramucci",\
"antiabortion":"womensRights",\
"antiabortion credential":"antiabortion",\
"antitrump fervor":"trumpOpposition",\
"antonin scalia":"antoninScalia",\
"antonio villaraigosa":"antonioVillaraigosa",\
"antonio villaraigosa":"antonioVillaraigosa",\
"antonov":"anatolyAntonov",\
"apol":"davidJApol",\
"arbitration clause":"arbitration",\
"arbitration provision":"arbitration",\
"arm control":"guns",\
"armstrong":"fultonArmstrong",\
"arpaio":"joeArpaio",\
"assad":"basharAlAssad",\
"assange":"julianAssange",\
"assassination":"espionage",\
"assistant attorney general stephen boyd":"stephenBoyd",\
"assistant attorney general stephen boyd":"stephenBoyd",\
"assistant john mcentee":"johnMcentee",\
"asylum":"immigration",\
"atlanta mayor keisha lance bottom":"keishaLanceBottoms",\
"attorney alex van der zwaan":"alexVanDerZwaan",\
"attorney general jeff session":"jeffSessions",\
"attorney general jeff session decision":"jeffSessions",\
"attorney general jeff session hour":"jeffSessions",\
"attorney general jeff session jefferson":"jeffSessions",\
"audra grassia":"audraGrassia",\
"avenatti":"michaelAvenatti",\
"avenatti point":"michaelAvenatti",\
"avenattis word":"michaelAvenatti",\
"background check":"backgroundChecks",\
"background check system":"backgroundChecks",\
"baker":"tonyBaker",\
"baker":"georgeBaker",\
"baltimore county executive kevin kamenetz":"kevinKamenetz",\
"bangladesh":"asia",\
"bank fraud charge":"bankFraud",\
"banker kirill dmitriev":"kirillDmitriev",\
"bannon":"steveBannon",\
"barack obama":"barackObama",\
"barack obamas":"barackObama",\
"barbara lee":"barbaraLee",\
"barr":"roseanneBarr",\
"barrack":"tomBarrack",\
"barrs politics":"roseanneBarr",\
"barzee flores":"maryBarzeeFlores",\
"basta michael avenatti":"michaelAvenatti",\
"beautiful wall":"borderwall",\
"bedroom apartment":"controversy",\
"bella thorne":"roseanneBarr",\
"ben jealous":"benJealous",\
"bentsenrio grande valley state park":"wildlife",\
"bernie":"bernieSanders",\
"bernie sander":"bernieSanders",\
"betsy dirksen londrigan":"betsyDirksenLondrigan",\
"bezos":"jeffBezos",\
"bharara":"preetBharara",\
"biden":"joeBiden",\
"bill clinton":"billClinton",\
"bill gate":"billGates",\
"bill nelson":"billNelson",\
"billionaire tom steyers campaign":"tomSteyer",\
"billionaire tom steyers impeachment crusade":"tomSteyer",\
"billionaire tom steyers trumpimpeachmentment crusade":"tomSteyer",\
"black life matter":"blackLivesMatter",\
"blackwater":"erikPrince",\
"blakely":"brentBlakely",\
"blumenthal":"richardBlumenthal",\
"bob lord":"bobLord",\
"bob woodward rule":"bobWoodward",\
"bold pac":"pac",\
"bolton":"johnBolton",\
"bolton fan":"johnBolton",\
"bolton spokesperson garrett marquis":"johnBolton",\
"boltons":"johnBolton",\
"booker":"coryBooker",\
"border fence":"borderwall",\
"border patrol agent":"borderPatrol",\
"border patrol agent":"borderwall",\
"bordersecurity funding":"borderwall",\
"borderwalls":"borderwall",\
"borderwalls":"borderwall",\
"bowman":"tomBowman",\
"boyd":"stephenBoyd",\
"brad sherman":"bradSherman",\
"braga":"jonathanBraga",\
"bredesen aide":"philBredesen",\
"bredesens letter":"philBredesen",\
"brendan kelly":"brendanKelly",\
"brennan":"johnBrennan",\
"brent blakely":"brentBlakely",\
"brexiteer nigel farage":"nigelFarage",\
"breyer":"stephenBreyer",\
"brian frosh":"brianFrosh",\
"britain":"unitedKingdom",\
"british":"unitedKingdom",\
"brittanie mountz":"brittanieMountz",\
"brostrom":"martinaBrostrom",\
"brother anthony scaramucci":"anthonyScaramucci",\
"bruce rauner":"bruceRauner",\
"buffy wick":"buffyWicks",\
"bullock":"steveBullock",\
"bump stock":"guns",\
"bush":"georgeWBush",\
"bush administration":"bushAdministration",\
"bush white house":"bushAdministration",\
"bush year":"georgeWBush",\
"bustani":"joseBustani",\
"Buttigieg":"peteButtigieg",\
"california air resource board chairperson mary nichols":"maryNichols",\
"california democrat adam schiff":"adamSchiff",\
"california republican":"republican",\
"california republican party":"republican",\
"california sen kamala harris":"kamalaHarris",\
"cambridge analytica":"cambridgeAnalytica",\
"cambridge analytica employee":"cambridgeAnalytica",\
"campaign aide":"campaign",\
"campaign loss":"campaign",\
"campaign manager matt rhoades":"mattRhoades",\
"campaign politics":"campaign",\
"campaign spokesperson kevin harris":"benJealous",\
"campaign team":"campaign",\
"campaign trump campaign chair paul manafort":"paulManafort",\
"canadian prime minister justin trudeau":"justinTrudeau",\
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
"ceo sean trauschke":"robertTrauschke",\
"challenger suraj patels":"surajPatel",\
"challenger suraj patels":"surajPatel",\
"charles harder":"charlesHarder",\
"cheneyrumsfeld era":"bushAdministration",\
"cheung":"stevenCheung",\
"chief justice john robert":"johnRoberts",\
"chief justice william rehnquist":"wiliamRehnquist",\
"chiefofstaff":"johnKelly",\
"chiefofstaff john kelly":"johnKelly",\
"childhood arrival program":"immigration",\
"chinese":"china",\
"chinese president xi jinping":"xiJinPing",\
"chris christie":"chrisChristie",\
"chris lacivita":"chrisLacivita",\
"chris smith":"chrisSmith",\
"christian westermann":"christianWestermann",\
"christie":"chrisChristie",\
"christina hagan":"christinaHagan",\
"christopher liddell":"christopherLiddell",\
"christopher liddell":"christopherLiddell",\
"christopher steele":"christopherSteele",\
"ci counterintelligence agent":"intelligence",\
"cia director mike pompeo":"mikePompeo",\
"cia directordesignate gina haspel":"ginaHaspel",\
"cindy hydesmith":"cindyHydeSmith",\
"circuit court":"USCourt",\
"citizenship question":"citizenship",\
"claire mccaskill":"claireMccaskill",\
"clarence thomas":"clarenceThomas",\
"clark case":"stephonClark",\
"cleanpower plan":"cleanpower",\
"clifford":"stormyDaniels",\
"clinton":"hillaryClinton",\
"clinton campaign":"hillaryClinton",\
"cnn president jeff zucker":"jeffZucker",\
"coalition builder":"coalition",\
"cobb":"tyCobb",\
"cohen":"michaelCohen",\
"cohn":"garyCohn",\
"columbine":"guns",\
"comey":"jamesComey",\
"comey friend":"jamesComey",\
"comeys":"jamesComey",\
"commanderinchief":"donaldTrump",\
"company vice president paul renfrow":"paulRenfrow",\
"confidentiality provision":"settlement",\
"congresswoman esty":"elizabethEsty",\
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
"cornyn":"johnCornyn",\
"corporate average fuel economy":"mpg",\
"corsi":"jeromeCorsi",\
"coulter":"annCoulter",\
"counsel":"specialCounsel",\
"counsel investigation":"robertMueller",\
"counsel robert mueller robert swan muellersasse":"robertMueller",\
"counsel robert mueller tuesday":"robertMueller",\
"counsel robert s mueller iii":"robertMueller",\
"counsel team":"robertMueller",\
"counsel work":"specialCounsel",\
"county seat":"election",\
"cruz":"tedCruz",\
"crystal mason":"crystalMason",\
"cuban threat":"cuba",\
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
"daca deal":"daca",\
"daca program":"daca",\
"daca recipient":"daca",\
"daca status":"daca",\
"daly":"shaunaDaly",\
"dan coat":"danCoats",\
"dan halpern":"danHalpern",\
"dan scavino":"danScavino",\
"dan webb":"danWebb",\
"dana nessel":"danaNessel",\
"daniel":"stormyDaniels",\
"daniel settlement agreement":"stormyDaniels",\
"danielle thomsen":"danielleThomsen",\
"data analysis firm":"bigData",\
"data firm":"cybersecurity",\
"data policy":"cybersecurity",\
"data raise concern":"privacy",\
"david apol":"davidJApol",\
"david hogg":"davidHogg",\
"david hogg conflict":"davidHogg",\
"david j apol":"davidJApol",\
"david koch":"kochBrothers",\
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
"defense budget":"USMilitary",\
"defense secretary donald rumsfeld":"donaldRumsfeld",\
"defense secretary james mattis":"jamesMattis",\
"dem":"democrat",\
"democrat andrew janz":"andrewJanz",\
"democrat candidate":"democrat",\
"democrat linda coleman":"lindaColeman",\
"dems":"democrat",\
"deputy attorney general rod rosenstein":"rodRosenstein",\
"deputy director andrew mccabe":"andrewMccabe",\
"deputy director job":"office",\
"der zwaan":"alexVanDerZwaan",\
"deripaska":"olegDeripaska",\
"deripaskas":"olegDeripaska",\
"deripaskas representative":"olegDeripaska",\
"dershowitz":"alanDershowitz",\
"detention facility":"USMilitary",\
"devin nunes":"devinNunes",\
"dewine":"mikeDewine",\
"dewine ally":"mikeDewine",\
"dewines campaign":"mikeDewine",\
"dewines spokesperson":"mikeDewine",\
"dhs official":"dhs",\
"dianne feinstein":"dianneFienstein",\
"disease control":"healthcare",\
"distribution center":"USPostalService",\
"district attorney":"attorney",\
"dittmar":"kellyDittmar",\
"dmitriev":"kirillDmitriev",\
"dmitrievs":"kirillDmitriev",\
"dnc chair race":"campaign",\
"dncs":"dnc",\
"dobbs":"louDobbs",\
"doe":"departmentOfEnergy",\
"doj inspector general":"michaelHorowitz",\
"doj spokesperson sarah isgur flores":"sarahIsgurFlores",\
"don mcgahn":"donMcgahn",\
"donald":"donaldTrump",\
"donald j trump":"donaldTrump",\
"donald jr":"donaldTrumpJr",\
"donald trump":"donaldTrump",\
"donald trump deputy campaign chairman rick gate":"rickGates",\
"donald trump jr":"donaldTrumpJr",\
"donaldjtrumpjr":"donaldTrumpJr",\
"doug jones":"dougJones",\
"dowd":"johnDowd",\
"dprk":"northKorea",\
"dr david shulkins service":"davidShulkin",\
"dr luiz loures":"luizLoures",\
"dr ronny":"ronnyJackson",\
"dr ronny jackson":"ronnyJackson",\
"dubose porter":"dubosePorter",\
"dylann roof":"dylannRoof",\
"eastern ghouta region":"syria",\
"ec":"essentialConsultants",\
"ec andor defendant trump":"donaldTrump",\
"economics":"economy",\
"economy standard":"economy",\
"education budget":"education",\
"election ballot":"election",\
"election bid":"eleciton",\
"election cycle":"election",\
"election day":"election",\
"election year":"election",\
"electricity":"energy",\
"emma gonzalez":"emmaGonzalez",\
"emmanuel macron":"emmanuelMacron",\
"encryption software company":"cybersecurity",\
"energy company":"energy",\
"england":"unitedKingdom",\
"environmental protection agency":"environmentalProtectionAgency",\
"epa administrator":"environmentalProtectionAgency",\
"epa administrator scott pruitt":"scottPruitt",\
"epa chief":"environmentalProtectionAgency",\
"epa chief pruitt":"scottPruitt",\
"epa decides":"environmentalProtectionAgency",\
"epa office":"environmentalProtectionAgency",\
"epa regulation":"environmentalProtectionAgency",\
"epa secretary":"environmentalProtectionAgency",\
"epa source":"environmentalProtectionAgency",\
"epa travel":"environmentalProtectionAgency",\
"eric trump":"ericTrump",\
"erik prince":"erikPrince",\
"escobar":"veronicaEscobar",\
"esper":"markEsper",\
"essential consultants":"essentialConsultants",\
"esty":"elizabethEsty",\
"estys":"elizabethEsty",\
"ethan":"ethanSonneborn",\
"ethan sonneborn":"ethanSonneborn",\
"ethic practice":"ethic",\
"eu twice":"europeanUnion",\
"europe":"europeanUnion",\
"european union":"europeanUnion",\
"exchange student tinka hessenheffer":"carolineSunshine",\
"exporter":"eExport",\
"facebook controversy":"facebook",\
"facebook data":"facebook",\
"facebook image":"facebook",\
"facebook post":"facebook",\
"facebook user":"facebook",\
"facebooks":"facebook",\
"facebooks chiefsecurityofficer":"facebook",\
"fake news":"media",\
"fake news narrative":"fakenews",\
"fake story":"fakenews",\
"fake washington post":"fakenews",\
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
"fbi director james comeys conversation":"jamesComey",\
"fbi informant":"fbi",\
"fbi lawyer lisa page":"lisaPage",\
"fbi leader":"fbi",\
"fbi mole robert hanssen":"espionage",\
"fbi office":"fbi",\
"fbi official":"fbi",\
"fbi policy":"fbi",\
"fbi report":"fbi",\
"fbi veteran":"fbi",\
"fec":"USElectionCommission",\
"fec investigation":"USElectionCommission",\
"fecs dismissal":"USElectionCommission",\
"federal election commission":"USElectionCommission",\
"federalElectionCommission":"USElectionCommission",\
"feinsteins":"dianneFienstein",\
"feinsteins campaign":"dianneFienstein",\
"feinsteins reelection":"election",\
"felony conviction":"felony",\
"fidel castro uprising":"fidelCastro",\
"fire robert mueller":"robertMueller",\
"firearm":"guns",\
"fisa abuse":"fisa",\
"fisa abuse allegation":"fisa",\
"fisa abuse more":"fisa",\
"fisa court":"fisa",\
"fisa warrant":"fisa",\
"fisc":"foreignIntelligenceSurveillanceCourt",\
"flores":"sarahIsgurFlores",\
"florida school shooting":"parkland",\
"florida sen marco rubio":"marcoRubio",\
"flynn":"michaelFlynn",\
"food stamp":"foodStamps",\
"food stamp recipient":"foodStamps",\
"foreign affair sergey ryabkov":"sergeiRyabkov",\
"foreign intelligence surveillance act":"fisa",\
"foreign intelligence surveillance court":"fisa",\
"former president barack obama":"barackObama",\
"former veteran affair secretary david shulkin":"davidShulkin",\
"fossil fuel lobbyist":"oil",\
"fox business network":"foxnews",\
"fox news host laura ingraham":"lauraIngraham",\
"fray democrat":"democrat",\
"french president emmanuel macron campaign":"emmanuelMacron",\
"fugh":"justinaFugh",\
"fulton armstrong":"fultonArmstrong",\
"fundraising term":"fundraising",\
"gabby trejo":"gabbyTrejo",\
"gang":"eGangs",\
"gang law":"eGangs",\
"gang member":"eGangs",\
"gangneung":"southKorea",\
"garaufis":"nicholasGaraufis",\
"gary cohn":"garyCohn",\
"gate":"rickGates",\
"gavin newsom":"gavinNewsom",\
"gawker":"media",\
"gen jonathan braga":"jonathanBraga",\
"gender inequality":"genderInequality",\
"george baker":"georgeBaker",\
"george conway":"georgeConway",\
"george w bush":"georgeWBush",\
"george w bush administration":"georgeWBush",\
"georgiaborn stacey evans":"staceyEvans",\
"georgian":"georgia",\
"giant amazon":"amazon",\
"gibson":"leslieGibson",\
"gillibrand":"kirstenGillibrand",\
"gina haspel":"ginaHaspel",\
"ginsburg":"ruthBaderGinsburg",\
"giuffra":"robertGiuffra",\
"gonzalez":"emmaGonzalez",\
"gonzalez event":"emmaGonzalez",\
"gonzalez supporter":"emmaGonzalez",\
"gonzalezs":"emmaGonzalez",\
"gonzalezs family tie":"emmaGonzalez",\
"gonzalezs hispanic":"emmaGonzalez",\
"gop hand":"republican",\
"gop lawmaker":"republican",\
"gop member":"republican",\
"gop nomination":"election",\
"gop presidency":"republican",\
"gop senate candidate jim renacci":"jimRenacci",\
"gop senator":"republican",\
"gorka":"sebastianGorka",\
"gorsuch":"neilGorsuch",\
"governor kasich":"johnKasich",\
"gowdy":"treyGowdy",\
"graham":"lindseyGraham",\
"gru":"russianIntelligence",\
"gru hacker":"russianIntelligence",\
"gsr":"globalScienceResearch",\
"gun debate":"guns",\
"gun law":"guns",\
"gun violence":"guns",\
"gunman":"guns",\
"guterres":"antonioGuterres",\
"haass":"richardHaass",\
"hack":"cybersecurity",\
"hagan":"christinaHagan",\
"hagans":"christinaHagan",\
"hagans bid":"christinaHagan",\
"hagans campaign":"christinaHagan",\
"hagans father":"christinaHagan",\
"hank johnson":"hankJohnson",\
"hank johnson":"hankJohnson",\
"hannity":"seanHannity",\
"harassment claim":"harassment",\
"harper":"malayahHarper",\
"harris":"kamalaHarris",\
"harris candidacy":"kamalaHarris",\
"hart":"stephenVickiHart",\
"haspel":"ginaHaspel",\
"haspels critic":"ginaHaspel",\
"hawaii state rep beth fukumoto":"bethFukumoto",\
"health":"healthcare",\
"health care":"healthcare",\
"health care issue":"healthcare",\
"health care system":"healthcare",\
"health issue":"healthcare",\
"health service":"healthcare",\
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
"hospital executive":"healthcare",\
"hostage":"terrorism",\
"house candidate":"election",\
"house democrat":"democrat",\
"house freedomcaucus":"extremeRight",\
"house intelligence committee":"houseIntelligenceCommittee",\
"house judiciary committee chairman bob goodlatte":"bobGoodlatte",\
"house majority leader kevin mccarthy":"kevinMccarthy",\
"house minority leader nancy pelosi":"nancyPelosi",\
"house oversight":"houseOversightCommittee",\
"house oversight committee":"houseOversightCommittee",\
"house oversight committee chairman trey gowdy":"treyGowdy",\
"house speaker nancy pelosi":"nancyPelosi",\
"house speaker paul ryan":"paulRyan",\
"huber":"johnHuber",\
"hutchings":"robertHutchings",\
"hydesmith":"cindyHydeSmith",\
"hyten":"johnHyten",\
"ice":"immigrationAndCustomsEnforcement",\
"ice office":"immigrationAndCustomsEnforcement",\
"ice office":"immigrationAndCustomsEnforcement",\
"illinois house seat":"election",\
"immigration authority":"immigration",\
"immigration law":"immigration",\
"immigration policy":"immigration",\
"immigration service":"immigration",\
"immigrationandcustomsenforcementofficers":"immigration",\
"improvisedExplosiveDevice attack":"improvisedExplosiveDevice",\
"infrastructure plan":"infrastructure",\
"infrastructure policy":"infrastructure",\
"infrastructure reform":"infrastructure",\
"infrastructure remark":"infrastructure",\
"infrastructure week":"infrastructure",\
"ingraham":"lauraIngraham",\
"ingraham angle":"lauraIngraham",\
"ingraham angle host":"lauraIngraham",\
"ingrahamangle":"lauraIngraham",\
"ingrahams":"lauraIngraham",\
"ingrahams advertiser":"lauraIngraham",\
"ingrahams apology":"controversy",\
"ingrahams comment":"controversy",\
"ingrahams program":"lauraIngraham",\
"ingrahams tweet":"tweet",\
"ingram":"lauraIngraham",\
"inhofe":"jamesInhofe",\
"inspector general michael horowitz":"michaelHorowitz",\
"instance trump":"donaldTrump",\
"intelligence bureau":"intelligence",\
"intelligence community":"intelligence",\
"intelligence division":"intelligence",\
"intelligence information":"intelligence",\
"intelligence officer":"intelligence",\
"intelligence service":"intelligence",\
"investigation compliance":"investigation",\
"investment income":"investment",\
"iraq legacy":"iraqWar",\
"iraq war":"iraqWar",\
"isi":"islamicState",\
"isi fighter":"islamicState",\
"isi operation":"islamicState",\
"istandwithlaura":"lauraIngraham",\
"ivanka":"ivankaTrump",\
"ivanka trump":"ivankaTrump",\
"j steven hart":"stephenVickiHart",\
"jackson":"ronnyJackson",\
"jacobson":"robertaJacobson",\
"james":"kayKoleJames",\
"james comey":"jamesComey",\
"james comeys":"jamesComey",\
"james inhofe":"jamesInhofe",\
"janz":"andrewJanz",\
"jared kushner":"jaredKushner",\
"jason kander":"jasonKander",\
"jason kander":"jasonKander",\
"jay sekulow":"jaySekulow",\
"jean schmidt":"jeanSchmidt",\
"jeb":"jebBush",\
"jeb bush":"jebBush",\
"jeb hensarling":"jebHensarling",\
"jeff bezos":"jeffBezos",\
"jeff session":"jeffSessions",\
"jeff zucker":"jeffZucker",\
"jeffbezos":"jeffBezos",\
"jefferson":"thomasJefferson",\
"jennie willoughby":"jennieWilloughby",\
"jennie willoughby willoughby":"jennieWilloughby",\
"jennings":"jScottJennings",\
"jerome corsi":"jeromeCorsi",\
"jerry brown":"jerryBrown",\
"jim inhofe":"jamesInhofe",\
"jim renacci":"jimRenacci",\
"jinping":"xiJinPing",\
"job plan":"jobs",\
"joe arpaio":"joeArpaio",\
"joe biden":"joeBiden",\
"joe morelle":"joeMorelle",\
"joel wallenstrom":"joelWallenstrom",\
"john bolton":"johnBolton",\
"john bolton superpac":"pac",\
"john culberson":"johnCulberson",\
"john dowd":"johnDowd",\
"john f kelly":"johnKelly",\
"john goodman":"roseanneBarr",\
"john kasich":"johnKasich",\
"john kasich short":"johnKasich",\
"john kasichs bid":"johnKasich",\
"john paul stevens":"johnPaulStevens",\
"john podesta":"johnPodesta",\
"john robert":"johnRoberts",\
"john weaver":"johnWeaver",\
"jon ossoff":"jonOssoff",\
"jon huntsman":"jonHuntsman",\
"jon ossoff":"jonOssoff",\
"jon tester":"jonTester",\
"jordan":"jimJordan",\
"jose bustani":"joseBustani",\
"judd":"brandonJudd",\
"judge josann reynolds":"josannReynolds",\
"judge reinhardt":"stephenReinhardt",\
"judge s james otero":"jamesOtero",\
"judge stephen reinhardt":"stephenReinhardt",\
"julian assange":"julianAssange",\
"justice anthony kennedy":"anthonyKennedy",\
"justice attorney":"justiceDepartment",\
"justice department":"justiceDepartment",\
"justice department criminal division":"justiceDepartment",\
"justice department inspector general":"justiceDepartment",\
"justice department inspector general michael horowitz":"michaelHorowitz",\
"justice department inspector general office":"justiceDepartment",\
"justice department official":"justiceDepartment",\
"justice department report":"justiceDepartment",\
"justice department spokesperson":"justiceDepartment",\
"justice department spokesperson sarah isgur flores":"sarahIsgurFlores",\
"justice inspector general investigation":"investigation",\
"justice kennedy":"anthonyKennedy",\
"justice neil gorsuch":"neilGorsuch",\
"justice overhaul":"justiceDepartment",\
"justice reform":"justiceDepartment",\
"justin fairfax":"justinFairfax",\
"justin trudeau":"justinTrudeau",\
"kain":"annaKain",\
"kaine":"timKaine",\
"kamala harris":"kamalaHarris",\
"kander":"jasonKander",\
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
"kemerovo":"russia",\
"kentucky sen rand paul":"randPaul",\
"kessler":"ronaldKessler",\
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
"kirill dmitriev":"kirillDmitriev",\
"kirsten gillibrand":"kirstenGillibrand",\
"kislyak":"sergeyKislyak",\
"koch":"kochBrothers",\
"koch brother":"kochBrothers",\
"konstantin kilimnik":"konstantinKilimnik",\
"korea":"northKorea",\
"kremlin thursday":"russia",\
"krikorian":"markKrikorian",\
"kudlow":"larryKudlow",\
"kushner":"jaredKushner",\
"kushner cos":"jaredKushner",\
"kushners":"jaredKushner",\
"kushners statement":"jaredKushner",\
"ladavia drane":"ladaviaDrane",\
"lady melania trump":"melaniaTrump",\
"laguna atascosa national wildlife refuge":"wildlife",\
"lamb":"conorLamb",\
"larry hogan":"larryHogan",\
"larry kudlow":"larryKudlow",\
"latinas veronica escobar":"veronicaEscobar",\
"laura ingraham":"lauraIngraham",\
"laura ingraham show":"lauraIngraham",\
"laura ingrahams":"lauraIngraham",\
"laura ingrahams advertiser":"controversy",\
"laura ingrahams program":"lauraIngraham",\
"laura ingrahams show":"lauraIngraham",\
"laura moser":"lauraMoser",\
"laura olin":"lauraOlin",\
"lauren hogg":"davidHogg",\
"lauren underwood":"laurenUnderwood",\
"laurie metcalf":"roseanneBarr",\
"lavrov":"sergeiLavrov",\
"law enforcement":"lawEnforcement",\
"law firm morganLewisAndBockius":"morganLewisAndBockius",\
"law now":"law",\
"leader kim jong un":"kimJongUn",\
"leader kim jongun":"kimJongUn",\
"leader xi jinping":"xiJinPing",\
"leigh corfman":"leighCorfman",\
"leslie gibson":"leslieGibson",\
"lewandowski":"coreyLewandowski",\
"lewis":"stephenLewis",\
"lgbt right group minneapolis fbi agent":"lgbt",\
"liddell":"christopherLiddell",\
"line spy":"espionage",\
"lisa page":"lisaPage",\
"litman":"amandaLitman",\
"los angeles mayor":"ericGarcetti",\
"los angeles mayor eric garcetti":"ericGarcetti",\
"loss conor":"conorLamb",\
"lou dobbs":"louDobbs",\
"loudobbs":"louDobbs",\
"loures":"luizLoures",\
"lowenergy jeb":"jebBush",\
"luis miranda":"cybersecurity",\
"luiz loures":"luizLoures",\
"luiz loures":"luizLoures",\
"lyndsey stuart":"lyndseyStuart",\
"m popovas":"nataliaPopova",\
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
"manaforts":"paulManafort",\
"manaforts business dealing":"paulManafort",\
"manaforts lawyer":"paulManafort",\
"manaforts offer":"paulManafort",\
"manaforts spokesman":"paulManafort",\
"manaforts translator":"konstantinKilimnik",\
"manigault newman":"omarosaManigault",\
"manigaultnewman":"omarosaManigault",\
"mann case":"josephMann",\
"marco rubio":"marcoRubio",\
"margo oge":"environmentalProtectionAgency",\
"maria zakharova":"russia",\
"marine corp veteran grant goodrich":"grantGoodrich",\
"marjory stoneman douglas high school":"parkland",\
"marjory stoneman douglas high school student david hogg":"davidHogg",\
"mark penn":"markPenn",\
"mark zuckerberg":"markZuckerberg",\
"market rate":"economy",\
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
"mccabes dismissal":"andrewMccabe",\
"mccabes termination":"andrewMccabe",\
"mccain":"johnMccain",\
"mccain twitter message":"tweet",\
"mccaskill":"claireMccaskill",\
"mcconnell":"mitchMcconnell",\
"mcdougal":"susanMcdougal",\
"mcdougals case":"susanMcdougal",\
"mcentee":"johnMcentee",\
"mcgregor":"matthewMcgregor",\
"mcmaster":"HRMcmaster",\
"medicareforall bill":"medicareforall",\
"meet dr ronny":"ronnyJackson",\
"melissa schwartz":"andrewMccabe",\
"messitte":"peterMessitte",\
"metoo phenomenon":"metoo",\
"metoo story":"metoo",\
"mexican president enrique pena nieto":"enriquePenaNieto",\
"michael avenatti":"michaelAvenatti",\
"michael avenattis":"michaelAvenatti",\
"michael brune":"michaelBrune",\
"michael cohen":"michaelCohen",\
"michael duchesne":"maryTaylor",\
"michael fishman":"roseanneBarr",\
"michael flynn":"michaelFlynn",\
"michael sulmeyer":"cybersecurity",\
"michael t flynn":"michaelFlynn",\
"michaelavenatti":"michaelAvenatti",\
"michel sidibe":"michelSidibe",\
"michigan democratic party dinner":"campaign",\
"microsoft ceo steve ballmer":"steveBalmer",\
"middle east":"middleEast",\
"midterm election":"election",\
"midterm forecaster":"election",\
"mike dewine":"mikeDewine",\
"mike dewines view":"mikeDewine",\
"mike lee":"mikeLee",\
"mike pompeo":"mikePompeo",\
"mileage commitment":"mpg",\
"mileage compromise":"mpg",\
"mileage rule":"mpg",\
"mileage target":"mpg",\
"minnesota republican":"republican",\
"minority leader stacey abrams":"staceyAbrams",\
"mitt romneys":"mittRomney",\
"mlk assassination more":"mlk",\
"model united nation team":"unitedNations",\
"mooch":"anthonyScaramucci",\
"mooch fundraiser":"anthonyScaramucci",\
"mook":"robbyMook",\
"moore":"royMoore",\
"more daca deal":"daca",\
"more daca deal":"daca",\
"morelle":"joeMorelle",\
"morning tweet":"tweet",\
"morrison":"samuelMorrison",\
"moser":"lauraMoser",\
"mountz":"brittanieMountz",\
"mr cohen":"michaelCohen",\
"mr cohens":"michaelCohen",\
"mr deripaska":"olegDeripaska",\
"mr dmitriev":"kirillDmitriev",\
"mr dmitrievs job":"kirillDmitriev",\
"mr dmitrievs wife natalia popova":"nataliaPopova",\
"mr dowd":"johnDowd",\
"mr flynn":"michaelFlynn",\
"mr flynns":"michaelFlynn",\
"mr huber":"johnHuber",\
"mr manafort":"paulManafort",\
"mr mueller":"robertMueller",\
"mr muellers investigator":"robertMueller",\
"mr putin":"vladimirPutin",\
"mr trump":"donaldTrump",\
"mrs trump":"melaniaTrump",\
"ms mason":"crystalMason",\
"ms stephanie clifford":"stormyDaniels",\
"muellers":"robertMueller",\
"muellers interest":"robertMueller",\
"muellers investigation":"robertMueller",\
"muellers probe":"robertMueller",\
"muellers team":"robertMueller",\
"multiple california democrat":"democrat",\
"mumbai":"india",\
"nancy pelosi":"nancyPelosi",\
"natalia popova":"nataliaPopova",\
"nathan click":"gavinNewsom",\
"national defense":"USMilitary",\
"national intelligence council":"intelligence",\
"national security":"nationalSecurity",\
"national security adviser john bolton":"johnBolton",\
"national security type":"nationalSecurity",\
"nationalsecurityadvisor john bolton":"johnBolton",\
"nationalsecurityadvisor michael flynn":"michaelFlynn",\
"navarro":"peterNavarro",\
"navy":"USMilitary",\
"need wall":"borderwall",\
"neil gorsuch":"neilGorsuch",\
"nelson":"billNelson",\
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
"new york sen kirsten gillibrand":"kirstenGillibrand",\
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
"night rate pruitt paid":"controversy",\
"nikema williams":"nikemaWilliams",\
"nikulin":"yevgeniyNikulin",\
"nix":"cambridgeAnalytica",\
"nominee donald trump":"candidateDonaldTrump",\
"noncitizen":"immigration",\
"north korea":"northKorea",\
"north korean":"northKorea",\
"north koreas":"northKorea",\
"november midterm":"election",\
"nra":"nationalRifleAssociation",\
"nrcc spokesperson jesse hunt":"nrcc",\
"nugent":"tedNugent",\
"nunberg":"samNunberg",\
"nunes":"devinNunes",\
"nutrish":"controversy",\
"nuzzi":"oliviaNuzz",\
"oak":"nathanielOaks",\
"obama":"barackObama",\
"obama administration":"obamaAdministration",\
"obama administration shut":"obamaAdministration",\
"obama campaign":"barackObama",\
"obama enters":"barackObama",\
"obama white house":"obamaAdministration",\
"obama year":"barackObama",\
"obergefell":"obergefellVHodges",\
"obergefell v hodges":"obergefellVHodges",\
"obstruction case":"obstruction",\
"oge chairman":"environmentalProtectionAgency",\
"oge chairman peter delaney":"environmentalProtectionAgency",\
"oge energy corp":"ogeenergy",\
"ohio conservative":"conservative",\
"ohio republican party chair jane timken":"janeTimken",\
"ohio right":"extremeRight",\
"ohioan jim jordan":"jimJordan",\
"oig":"officeOfInspectorGeneral",\
"oil field":"oil",\
"oleg deripaska":"olegDeripaska",\
"oligarch oleg deripaska":"olegDeripaska",\
"olson":"tedOlson",\
"omalley":"martinOmalley",\
"omarosa manigaultnewman":"omarosaManigault",\
"omnibus spending bill":"economy",\
"opcw chief":"opcw",\
"ortega":"rosaMariaOrtega",\
"orville fleming":"orvilleFleming",\
"orville fleming sits":"orvilleFleming",\
"osama bin laden":"osamaBinLaden",\
"otero":"jamesOtero",\
"oval office":"donaldTrump",\
"pardon offer":"pardon",\
"pardon power":"pardon",\
"parkland school":"parkland",\
"parkland school shooting":"parkland",\
"parkland shooting":"parkland",\
"parkland student":"parkland",\
"parkland student david hogg":"davidHogg",\
"parkland survivor":"parkland",\
"parkland survivor david hogg":"davidHogg",\
"parkland survivor david hogg call":"davidHogg",\
"paul manafort":"paulManafort",\
"paul renfrow":"paulRenfrow",\
"pelosi":"nancyPelosi",\
"pelosi wouldnt answer":"nancyPelosi",\
"pena nietos position":"enriquePenaNieto",\
"peninsula":"northKorea",\
"penn":"markPenn",\
"pennsylvania republican":"republican",\
"pet food company nutrish":"controversy",\
"pet food maker nutrish":"controversy",\
"Pete Buttigieg":"peteButtigieg",\
"pete session":"peteSessions",\
"peter navarro":"peterNavarro",\
"phil bredesen":"philBredesen",\
"pm justin trudeau":"justinTrudeau",\
"po":"USPostalService",\
"police investigator hand":"investigation",\
"policy adviser stephen miller":"stephenMiller",\
"polk county democrat":"democrat",\
"pollack":"barryPollack",\
"pollster bill mcinturff":"opinionPolls",\
"pompeo":"mikePompeo",\
"popova deputydirects tikhonovas innopraktika foundation":"nataliaPopova",\
"post office":"USPostalService",\
"post office scam":"USPostalService",\
"postal service":"USPostalService",\
"postintelligencer":"intelligence",\
"power plant emission":"pollution",\
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
"president obama":"barackObama",\
"president putin":"vladimirPutin",\
"president reagan":"ronaldReagan",\
"president ronald reagan":"ronaldReagan",\
"president steven cheung":"stevenCheung",\
"president trump":"donaldTrump",\
"president trump donald john trumpkushner":"jaredKushner",\
"president trump donald john trumpnew york magazine cover":"donaldTrump",\
"president victor yanukovych":"victorYanukovych",\
"president vladimir putin":"vladimirPutin",\
"president xi":"xiJinPing",\
"president xi jinping":"xiJinPing",\
"press secretary sarah huckabee sander":"sarahHuckabeeSanders",\
"priebus":"reincePriebus",\
"prime minister yulia tymoshenko":"yuliaTymoshenko",\
"prince":"erikPrince",\
"priyanka mantha":"staceyAbrams",\
"protection agency administrator scott pruitt":"scottPruitt",\
"pruitt":"scottPruitt",\
"public affair research poll":"opinionPolls",\
"pulikovsky":"konstantinPulikovsky",\
"putin":"vladimirPutin",\
"putin comment":"vladimirPutin",\
"putin daughter":"vladimirPutin",\
"pyeongchang winter olympics":"southKorea",\
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
"ravel":"USElectionCommission",\
"ravel point":"USElectionCommission",\
"rcalif":"republican",\
"rdif ceo kirill dmitriev":"kirillDmitriev",\
"redfield":"robertRedfieldJr",\
"redfields":"robertRedfieldJr",\
"reelection campaign":"campaign",\
"reform act":"congressionalReformAct",\
"rehnquist":"wiliamRehnquist",\
"reid":"harryReid",\
"reid letter":"harryReid",\
"reince":"reincePriebus",\
"reince priebus":"reincePriebus",\
"reinhardt":"stephenReinhardt",\
"relationship kilimnik":"konstantinKilimnik",\
"remember harriet miers":"harrietMiers",\
"remember kirill dmitriev":"kirillDmitriev",\
"renacci":"jimRenacci",\
"renfrow":"paulRenfrow",\
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
"report jeb bush":"jebBush",\
"reps marcia fudge":"marciaFudge",\
"reps robert goodlatte":"bobGoodlatte",\
"republican candidate":"republican",\
"republican john culberson":"johnCulberson",\
"republican larry hogan":"larryHogan",\
"republican party future":"republican party",\
"republican party platform":"republican",\
"republican politics":"republican",\
"republican pollster bill mcinturff":"opinionPolls",\
"republican will hurd":"willHurd",\
"republicancontrolled":"republican",\
"republicanled house intelligence committee":"houseIntelligenceCommittee",\
"rex tillerson":"rexTillerson",\
"reynolds":"josannReynolds",\
"ricci":"andrewRicci",\
"rice":"susanRice",\
"richard blumenthal":"richardBlumenthal",\
"richard haass":"richardHaass",\
"richard ojeda":"richardOjeda",\
"rick gate":"rickGates",\
"rick scott":"rickScott",\
"rippey gibney":"rubyRippeyGibney",\
"rnc":"republicanNationalConvention",\
"rob frost":"robFrost",\
"robby mook":"robbyMook",\
"robert hutchings":"robertHutchings",\
"robert redfield jr":"robertRedfieldJr",\
"robert wilkie":"robertWilkie",\
"rodman":"dennisRodman",\
"roger stone":"rogerStone",\
"ronaldKessler":"ronaldKessler",\
"ronny jackson":"ronnyJackson",\
"roof":"dylannRoof",\
"rosa maria ortega":"rosaMariaOrtega",\
"roseanne":"roseanneBarr",\
"roseanne barr":"roseanneBarr",\
"roseanne reply":"roseanneBarr",\
"rosenstein":"rodRosenstein",\
"ruben":"rubenKihuen",\
"rubio":"marcoRubio",\
"ruby rippey gibney":"rubyRippeyGibney",\
"ruby rippey gibney":"rubyRippeyGibney",\
"rumsfelds":"donaldRumsfeld",\
"rushern l baker iii":"rushernBaker",\
"russia direct investment fund":"rdif",\
"russia policy":"russia",\
"russia response":"russia",\
"russian":"russia",\
"russian ambassador sergey kislyak":"sergeyKislyak",\
"russian double agent living":"espionage",\
"russian foreign ministry":"russia",\
"russian president vladimir putin":"vladimirPutin",\
"russiandirectinvestmentfund":"rdif",\
"ruth bader ginsburg":"ruthBaderGinsburg",\
"ryabkov":"sergeiRyabkov",\
"ryan":"paulRyan",\
"sacramento county prosecutor noah phillips":"noahPhillips",\
"sacramento district attorney race":"election",\
"saddam hussein iraq":"saddamHussein",\
"sale tax collection":"tax",\
"salud carbajal":"saludCarbajal",\
"sam nunberg":"samNunberg",\
"samuel alito":"samuelAlito",\
"sanction proposal":"sanction",\
"sander":"bernieSanders",\
"sandra day oconnor":"sandraDayOconnor",\
"santa ana national wildlife refuge":"wildlife",\
"santa ana refuge":"wildlife",\
"sara gilbert":"roseanneBarr",\
"scalia":"antoninScalia",\
"scalise":"steveScalise",\
"scaramucci":"anthonyScaramucci",\
"scaramucci event":"anthonyScaramucci",\
"scavino":"danScavino",\
"school administration":"education",\
"school official":"education",\
"school resource officer":"education",\
"school safety":"guns",\
"school student":"student",\
"school teacher":"education",\
"schubert":"anneMarieSchubert",\
"schumer":"chuckSchumer",\
"schwartz":"andrewMccabe",\
"SCL":"SCLGroup",\
"scoreboard trump job performance average approval":"opinionPolls",\
"scott jennings":"jScottJennings",\
"scott pruitt":"scottPruitt",\
"scott walker":"scottWalker",\
"sean hannity":"seanHannity",\
"secondAmendment":"secondamendment",\
"secondamendment right":"secondamendment",\
"secondamendment will never be repealed":"secondamendment",\
"secretarygeneral":"unitedNations",\
"secure technology":"cybersecurity",\
"security official":"intelligence",\
"security world":"cybersecurity",\
"sekulow":"jaySekulow",\
"sekulows team":"jaySekulow",\
"sen ben sasse":"benSasse",\
"sen bill nelson":"billNelson",\
"sen chris coon":"chrisCoons",\
"sen chuck grassley":"chuckGrassley",\
"sen claire mccaskill":"claireMccaskill",\
"sen dianne feinsteins bid":"dianneFienstein",\
"sen doug jones":"dougJones",\
"sen heidi heitkamp":"heidiHeitkamp",\
"sen james inhofe":"jamesInhofe",\
"sen john mccain":"johnMccain",\
"sen jon tester":"jonTester",\
"sen lindsey graham":"lindseyGraham",\
"sen marco rubio":"marcoRubio",\
"sen orrin hatch":"orrinHatch",\
"sen richard blumenthal":"richardBlumenthal",\
"sen sheldon whitehouse":"sheldonWhitehouse",\
"sen thad cochran seat":"thadCochran",\
"sen thom tillis":"thomTillis",\
"sen tim kaine":"timKaine",\
"senate armed service committee":"USMilitary",\
"senate democratic leader chuck schumer":"chuckSchumer",\
"senate judiciary chairman chuck grassley":"chuckGrassley",\
"senate majority leader mitch mcconnell":"mitchMcconnell",\
"senate minority leader charles e schumer":"chuckSchumer",\
"senate minority leader chuck schumer":"chuckSchumer",\
"senator kirsten gillibrand":"kirstenGillibrand",\
"sergei lavrov":"sergeiLavrov",\
"sergei ryabkov":"sergeiRyabkov",\
"sergei skripal":"sergeiSkripal",\
"sergei skripal":"sergeiSkripal",\
"sergey i kislyak":"sergeyKislyak",\
"settlement agreement":"settlement",\
"seychelles island":"seychelles",\
"shaub":"walterShaub",\
"shauna daly":"shaunaDaly",\
"sherman":"bradSherman",\
"sheryl sandberg":"sherylSandberg",\
"sheryl sandberg":"sherylSandberg",\
"shipping cost":"USPostalService",\
"shulkin":"davidShulkin",\
"shulkins":"davidShulkin",\
"shulkins wife":"davidShulkin",\
"sidibe":"michelSidibe",\
"sinclair":"sinclairBroadcastGroup",\
"sinclair broadcast group":"sinclairBroadcastGroup",\
"sinclair vice president":"sinclairBroadcastGroup",\
"skadden arp law firm":"lawFirm",\
"skripal":"sergeiSkripal",\
"snap":"supplmentalNutritionAssistanceProgram",\
"snap benefit":"supplmentalNutritionAssistanceProgram",\
"somali men":"somalia",\
"somali migrant":"somalia",\
"somali official":"somalia",\
"sonia sotomayor":"soniaSotomayor",\
"soninlaw":"jaredKushner",\
"soninlaw jared kushner":"jaredKushner",\
"sorensen":"davidSorensen",\
"sotomayor":"soniaSotomayor",\
"south korea":"southKorea",\
"south koreas":"southKorea",\
"south sudan":"africa",\
"southern borderwall":"borderwall",\
"soviet union":"russia",\
"special counsel robert mueller":"robertMueller",\
"spy sergei skripal":"sergeiSkripal",\
"sri lanka":"asia",\
"stacey abrams":"staceyAbrams",\
"stacey abrams porter":"staceyAbrams",\
"stacey evans":"staceyEvans",\
"staff secretary rob porter":"robPorter",\
"stamos":"alexStamos",\
"star stormy daniel":"stormyDaniels",\
"state colin powell":"colinPowell",\
"state department spokesperson heather nauert":"stateDepartment",\
"state department spokeswoman heather nauert":"stateDepartment",\
"state department spokeswoman heather nauert":"stateDepartment",\
"state election law":"election",\
"state hillary clinton use":"hillaryClinton",\
"state republican":"republican",\
"state rex tillerson":"rexTillerson",\
"state sen toni atkins":"toniAtkins",\
"state tax internet sale":"tax",\
"state teacher union":"education",\
"statedesignate mike pompeo":"mikePompeo",\
"steele":"christopherSteele",\
"stephanie clifford":"stormyDaniels",\
"stephen bannon":"steveBannon",\
"stephen breyer":"stephenBreyer",\
"stephen lewis":"stephenLewis",\
"stephen strang":"stephenStrang",\
"steve bannon":"steveBannon",\
"steve bullock":"steveBullock",\
"steve miller":"stephenMiller",\
"steve scalise":"steveScalise",\
"steven cheung":"stevenCheung",\
"steven hart":"stephenVickiHart",\
"steyer":"tomSteyer",\
"stormy daniel":"stormyDaniels",\
"stormy daniel lawyer":"stormyDaniels",\
"stormy daniel story":"stormyDaniels",\
"strang":"stephenStrang",\
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
"supreme court justice":"USSupremeCourt",\
"supreme court justice anthony kennedy":"anthonyKennedy",\
"supreme court justice anthony kennedy anthony kennedy":"anthonyKennedy",\
"supreme court justice anthony kennedy gorsuch":"anthonyKennedy",\
"supreme court justice anthony kennedy kennedy":"anthonyKennedy",\
"supreme court justice anthony kennedy kennedy meet":"anthonyKennedy",\
"supreme court justice anthony kennedy kennedy testifies":"anthonyKennedy",\
"supreme court justice anthony kennedy photo":"anthonyKennedy",\
"supreme court justice anthony kennedy president obama":"anthonyKennedy",\
"supreme court justice anthony kennedy trump":"anthonyKennedy",\
"supreme court justice john paul stevens":"johnPaulStevens",\
"supreme court justice stevens":"johnPaulStevens",\
"survivor david hogg":"davidHogg",\
"susan mcdougal":"susanMcdougal",\
"swalwell":"ericSwalwell",\
"swamp scott pruitt":"scottPruitt",\
"swing district":"campaign",\
"syngentas fine":"syngenta",\
"syria yesterday":"syria",\
"tariff decision":"tariff",\
"tarrant county jail":"lawEnforcement",\
"tax bill":"tax",\
"tax collection software":"tax",\
"tax credit":"tax",\
"tax cut cut cut plan":"tax",\
"tax dollar":"tax",\
"tax increase":"tax",\
"tax jurisdiction":"tax",\
"tax preparer":"tax",\
"tax requirement":"tax",\
"tax return":"tax",\
"taxpayer dollar":"tax",\
"taxpayer fund":"tax",\
"taxpayer resource":"tax",\
"taylor":"maryTaylor",\
"taylor campaign":"maryTaylor",\
"taylor face":"maryTaylor",\
"tco4fcna1agaa donald trump jr":"donaldTrumpJr",\
"tcowfla4hwhxy laura ingraham":"lauraIngraham",\
"tea party":"teaParty",\
"teabagger":"teaparty",\
"teacher salary":"education",\
"ted nugent":"tedNugent",\
"tell qanon":"qanon",\
"terror group":"terrorism",\
"terry mcauliffe":"terryMcauliffe",\
"tester":"jonTester",\
"texas civilrights organization":"civilRights",\
"texas republican will hurd":"willHurd",\
"texas sen ted cruz":"tedCruz",\
"threat intelligence researcher":"intelligence",\
"thursday kihuen":"rubenKihuen",\
"tillerson":"rexTillerson",\
"tillis":"thomTillis",\
"time maloney":"carolynMaloney",\
"timken":"janeTimken",\
"tokyo":"japan",\
"tom bowman":"tomBowman",\
"tom steyer":"tomSteyer",\
"toni gidwani":"toniGidwani",\
"tony baker":"tonyBaker",\
"trade announcement":"trade",\
"trade deal":"trade",\
"trade surplus":"trade",\
"trade war":"tradeWar",\
"transgender policy public":"transgender",\
"trauschke":"robertTrauschke",\
"travel spending":"controversy",\
"treasury secretary":"USTreasury",\
"trend poll":"poll",\
"trey gowdy":"treyGowdy",\
"troop":"USMilitary",\
"troop":"USMilitary",\
"trudeau":"justinTrudeau",\
"trump":"donaldTrump",\
"trump administration official":"trumpAdministration",\
"trump adviser":"trumpAdviser",\
"trump aide":"trumpAide",\
"trump attempt":"donaldTrump",\
"trump attorney ty cobb":"tyCobb",\
"trump campaign adviser carter page":"carterPage",\
"trump campaign adviser roger stone":"rogerStone",\
"trump campaign chairman paul manafort":"paulManafort",\
"trump daughter ivanka":"ivankaTrump",\
"trump decision":"donaldTrump",\
"trump directorofnationalintelligence":"directorOfNationalIntelligence",\
"trump era":"donaldTrump",\
"trump joining":"donaldTrump",\
"trump jr":"donaldTrumpJr",\
"trump lawyer john dowd":"johnDowd",\
"trump lawyer michael cohen":"michaelCohen",\
"trump orbit":"donaldTrump",\
"trump order epa":"environmentalProtectionAgency",\
"trump push":"donaldTrump",\
"trump rally":"campaign",\
"trump speech":"donaldTrump",\
"trump tower meeting":"collusion",\
"trump tweet":"tweet",\
"trump universe":"donaldTrump",\
"trump white house":"white house",\
"trump win":"donaldTrump",\
"trumpimpeachment trump":"impeach",\
"trumpputin revelation":"russia",\
"tucker carlson":"tuckerCarlson",\
"turkey justiceAndDevelopmentParty":"extremeRight",\
"tweet":"twitter",\
"tweet friday morning":"tweet",\
"tweet read":"tweet",\
"tweet saturday evening":"tweet",\
"tweet sunday morning":"tweet",\
"tweet wednesday":"tweet",\
"twitter account":"tweet",\
"twitter aim":"tweet",\
"twitter attack":"tweet",\
"twitter follower":"tweet",\
"twitter post":"tweet",\
"twitter profile":"tweet",\
"twitter thursday":"tweet",\
"ty cobb":"tyCobb",\
"tymoshenko":"yuliaTymoshenko",\
"u air strike":"USMilitary",\
"u attorney":"USAttorney",\
"u attorney john huber":"johnHuber",\
"u border":"borderwall",\
"u constitution":"constitution",\
"u court":"USCourt",\
"u defense official":"USMilitary",\
"u embassy":"USEmbassy",\
"u force":"USMilitary",\
"u immigration system":"USImmigration",\
"u official":"USOfficial",\
"u politics":"USPolitics",\
"u postal service":"USPostalService",\
"u president donald trump":"donaldTrump",\
"u supreme court":"USSupremeCourt",\
"u troop":"USTroops",\
"un ambassador":"unitedNations",\
"un official":"unitedNations",\
"un secretarygeneral":"UNSecretaryGeneral",\
"un system":"unitedNations",\
"underwood":"laurenUnderwood",\
"union chief brandon judd":"brandonJudd",\
"united nation":"unitedNations",\
"united state anatoly antonov":"anatolyAntonov",\
"united state election":"election",\
"united state postal service":"USPostalService",\
"united state sergei kislyak":"sergeyKislyak",\
"us ally":"USAlly",\
"us assistance":"foreignAid",\
"us attorney john huber":"johnHuber",\
"us attorney john w huber speaks":"johnHuber",\
"us border":"borderwall",\
"us campaign":"campaign",\
"us consulate general":"USConsulate",\
"us consumer":"consumer",\
"us court":"USCourt",\
"us district court":"USCourt",\
"us embassy":"USEmbassy",\
"us foreign intelligence surveillance court":"fisa",\
"us intelligence agency":"intelligence",\
"us job":"jobs",\
"us post office":"USPostalService",\
"us rep elizabeth esty":"elizabethEsty",\
"us sen elizabeth warren":"elizabethWarren",\
"us troop":"USMilitary",\
"usmexico borderwall":"borderwall",\
"va":"veteransAffairs",\
"va chief david shulkin":"davidShulkin",\
"va employee":"veteransAffairs",\
"va health care":"veteransAffairs",\
"va president donald trump":"donaldTrump",\
"va secretary":"veteransAffairs",\
"va secretary david shulkin":"davidShulkin",\
"va system":"veteransAffairs",\
"va transition":"veteransAffairs",\
"van der zwaan":"alexVanDerZwaan",\
"veronica escobar":"veronicaEscobar",\
"veteran affair":"veteransAffairs",\
"veteran affair david shulkin":"davidShulkin",\
"veteran affair david shulkin wednesday":"davidShulkin",\
"veteran affair nominee dr ronny jackson":"ronnyJackson",\
"veteran affair secretary":"veteransAffairs",\
"veteran affair secretary david shulkin":"davidShulkin",\
"veteran health system":"healthcare",\
"vice president dick cheney":"dickCheney",\
"vice president joe biden":"joeBiden",\
"vice president mike penny":"mikePence",\
"vicki hart":"stephenVickiHart",\
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
"washington living arrangement":"controversy",\
"weaver":"johnWeaver",\
"webb":"danWebb",\
"week ingraham":"controversy",\
"west wing structure":"trumpAdministration",\
"westermann":"christianWestermann",\
"white house chiefofstaff":"johnKelly",\
"white house chiefofstaff john f kelly":"johnKelly",\
"white house chiefofstaff john kelly":"johnKelly",\
"white house communication director":"sarahHuckabeeSanders",\
"white house hopeful":"election",\
"white house press secretary sarah huckabee sander":"sarahHuckabeeSanders",\
"white house press secretary sarah sander":"sarahHuckabeeSanders",\
"white house spokesperson lindsay walter":"lindsayWalter",\
"white house trade adviser peter navarro":"peterNavarro",\
"wickrs ceo":"wickr",\
"wikileaks founder julian assange":"julianAssange",\
"wildlife refuge":"wildlife",\
"william rehnquist":"wiliamRehnquist",\
"willoughby":"jennieWilloughby",\
"woman equality":"womensRights",\
"work requirement":"supplmentalNutritionAssistanceProgram",\
"workforce":"jobs",\
"worldwide cyberattack":"cybersecurity",\
"wray":"christopherWray",\
"wylie":"christopherWylie",\
"wyoming rep liz cheney":"lizCheney",\
"xi":"xiJinPing",\
"xi jinping":"xiJinPing",\
"xiyue wang":"xiYueWang",\
"yekaterina tikhonova":"vladimirPutin",\
"yekaterinburg":"russia",\
"zero republican":"republican",\
"zucker":"jeffZucker",\
"zwaan":"alexVanDerZwaan",\



        
        # ================end pasted section====================

    }
    # the parser converts all entries to lower case, so we should do the same
    ec_dict = {key.lower(): value for key, value in ec_dict.items()}
    return ec_dict