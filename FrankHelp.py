Family_Members = {
	"My Generation": {
		"Brady": "Brother",
		"Mason": "Brother",
		"Haley": "Cousin",
		},
	"Parents' Generation": {
		"Mike": "Parent",
		"Christie": "Parent",
		"David": "Uncle",
		},
	"Grandparents' Generation": {
		"Frank": "Grandparent",
		"Clare": "Grandparent",
		"John": "Great-Uncle",
		},
}
for generation, person in Family_Members.items():
	print("\n" + generation + ":\n")
	print(variable + "s: ")
	for human, relation in person.items():
		if relation == "Brother" or "Cousin" or "Parent" or "Uncle" or "Grandparent" or "Great-Uncle":
			variable = relation
		 print(human + ", ")
	print("\n")
