#IMPORTANT: currently this weighting is only applied to EC TERMS!! What that means:
#  If you have "arms sales" and "foreign arms dealers" all belonging to an "arms" concept,
#  and you weight "arms", then you could even FAIL to apply any weighting at all to the
#  overall concept, since there is no instance of "arms". Similarly, if you weight
#  "arms sales" as 2x, then you have effectively increased the weight of the "arms"
#  concept since one of it's contributing terms is weighted higher. However, if you
#  create an EC so that both "arms sales" and "foreign arms dealers" both roll into
#  an "arms" EC (not concept!) then your "arms" weighting WILL be applied to both
#  instances, in whatever DSI they appear in.

#Todo: Create another "weighted_concept_dict" to allow weighting CONCEPTS, indpendent of ECs

def get_weights():
    weight_dict = {
"donaldTrump":1,\
"surajPatel":10,\
"sanction":5,\
"trade":5,\
"gun":10,\
"ar15":10,\
"kellyanneConway":3,\
"georgeConway":3,\
"carterPage":3,\
"rushernBaker":5,\
"tonyBaker":5,\
"lisaPage":3,\
"stephonClark":5,\
"peteSessions":3,\
"brendanKelly":3,\
"anthonyKennedy":3,\
"jerryBrown":3,\
"robPorter":3,\


        }
    return weight_dict