NO_ERRORS

:Entity_0001	type	GPE
:Entity_0001	canonical_mention	"Boston"	NYT_ENG_20131113.0264:402-407	1.0
:Entity_0001	mention	"Boston"	NYT_ENG_20131113.0264:402-407	1.0
:Entity_0001	gpe:residents_of_city	:Entity_0007	NYT_ENG_20131113.0264:402-450	0.5493061443340549
:Entity_0001	gpe:conflict.attack_place.actual	:Event_0001	NYT_ENG_20131113.0264:261-431;NYT_ENG_20131113.0264:402-407;NIL	1.0

:Entity_0007	type	PER
:Entity_0007	canonical_mention	"Dzhokhar Tsarnaev"	NYT_ENG_20131113.0264:434-450	1.0
:Entity_0007	mention	"Dzhokhar Tsarnaev"	NYT_ENG_20131113.0264:434-450	1.0
:Entity_0007	pronominal_mention	"he"	NYT_ENG_20131113.0264:546-547	1.0
:Entity_0007	per:cities_of_residence	:Entity_0001	NYT_ENG_20131113.0264:402-450	0.5493061443340549
:Entity_0007	per:siblings	:Entity_0010	NYT_ENG_20131113.0264:561-577	0.73588133800021

:Entity_0010	type	PER
:Entity_0010	canonical_mention	"Tamerlan Tsarnaev"	NYT_ENG_20131113.0264:684-700	1.0
:Entity_0010	mention	"Tamerlan Tsarnaev"	NYT_ENG_20131113.0264:684-700	1.0
:Entity_0010	nominal_mention	"brother"	NYT_ENG_20131113.0264:571-577	1.0
:Entity_0010	per:siblings	:Entity_0007	NYT_ENG_20131113.0264:561-577	0.73588133800021

# The document does not support or deny the following, however, we are including this
# only to demonstrate how a sentiment would be represented in the KB
#
# The inverse would be inferred by the validator with a warning
:Entity_0001	gpe:is_disliked_by	:Entity_0010	NYT_ENG_20131113.0264:402-407	1.0

# Example showing normalized date string
:String_0001	type	STRING
:String_0001	mention	"April 15"	NYT_ENG_20131113.0264:624-631	1.0
# the provenance of normalized_mention has to be a mention of the subject
:String_0001	normalized_mention	"2014-04-15"	NYT_ENG_20131113.0264:624-631	1.0

# Example showing string for victims
:String_0002	type	STRING
:String_0002	mention	"three people"	NYT_ENG_20131113.0264:642-653	1.0

:Event_0001	type	CONFLICT.ATTACK
:Event_0001	mention.actual	"bombing"	NYT_ENG_20131113.0264:418-424	1.0
:Event_0001	canonical_mention.actual	"bombing"	NYT_ENG_20131113.0264:418-424	1.0

:Event_0001	conflict.attack:attacker.actual	:Entity_0007	NYT_ENG_20131113.0264:492-681;NYT_ENG_20131113.0264:546-547;NIL	1.0

# Feel free to change the above actual attacker to generic, for e.g.:
#:Event_0001	conflict.attack:attacker.generic	:Entity_0007	NYT_ENG_20131113.0264:492-681;NYT_ENG_20131113.0264:546-547;NIL	1.0
# If you use the commented assertion instead, you would notice that resolve-queries would not return this assertion

:Event_0001	conflict.attack:place.actual	:Entity_0001	NYT_ENG_20131113.0264:261-431;NYT_ENG_20131113.0264:402-407;NIL	1.0
:Event_0001	conflict.attack:time.actual	:String_0001	NYT_ENG_20131113.0264:624-631;NYT_ENG_20131113.0264:492-681;NYT_ENG_20131113.0264:624-631;NIL	1.0
:Event_0001	conflict.attack:target.actual	:String_0002	NYT_ENG_20131113.0264:642-653;NYT_ENG_20131113.0264:492-681;NYT_ENG_20131113.0264:642-653;NIL	1.0
