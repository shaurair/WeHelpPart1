print("====Task1====")

def find_and_print(messages):
	for KeyName in messages:
		# Check age
		if "I'm 18 years old" in messages[KeyName]:
			print(KeyName)
			continue

		# Check education
		if "I'm a college student" in messages[KeyName]:
			print(KeyName)
			continue

		# Check rights for Taiwan case
		if "I am of legal age in Taiwan" in messages[KeyName]:
			print(KeyName)
			continue

		# Check rights for USA case
		if "I will vote" in messages[KeyName]:
			print(KeyName)
			continue

find_and_print({
	"Bob":"My name is Bob. I'm 18 years old.",
	"Mary":"Hello, glad to meet you.",
	"Copper":"I'm a college student. Nice to meet you.",
	"Leslie":"I am of legal age in Taiwan.",
	"Vivian":"I will vote for Donald Trump next week",
	"Jenny":"Good morning."
})

print("====Task2====")

def calculate_sum_of_bonus(data):
	EmployeeList = data["employees"]
	SumofBonus = 0
	EffSalary = 0.01
	USD2TWD = 30
	AvgBonus = 1000

	for Employee in EmployeeList:
		EmployeeBonus = 0
		# Check salary
		# integer type, add to sum directory
		if type(Employee["salary"]) == int:
			EmployeeBonus += EffSalary * Employee["salary"]

		# string type,
		else:
			# remove ',' mark
			Employee["salary"] = Employee["salary"].replace(",","")

			# USD case
			if "USD" in Employee["salary"]:
				Employee["salary"] = Employee["salary"].replace("USD","")
				Employee["salary"] = int(Employee["salary"]) * USD2TWD
			# TWD case
			else:
				Employee["salary"] = int(Employee["salary"])
				
			EmployeeBonus += EffSalary * Employee["salary"]

		# Check performance
		if Employee["performance"] == "above average":
			EmployeeBonus += AvgBonus * 1.5
		elif Employee["performance"] == "average":
			EmployeeBonus += AvgBonus
		else:
			EmployeeBonus += AvgBonus * 0.5

		# Check role
		if Employee["role"] == "CEO":
			EmployeeBonus += 1000
		elif Employee["role"] == "Engineer":
			EmployeeBonus += 2000
		elif Employee["role"] == "Sales":
			EmployeeBonus += 1500

		SumofBonus += EmployeeBonus

	# Check sum of bonus of all employees
	if(SumofBonus > 10000):
		print("larger than 10000")
	else:
		print(SumofBonus)

calculate_sum_of_bonus({ "employees":[
{
	"name":"John","salary":"1000USD", "performance":"above average", "role":"Engineer"
},
{
	"name":"Bob", "salary":60000, "performance":"average", "role":"CEO"
},
{
	"name":"Jenny", "salary":"50,000", "performance":"below average", "role":"Sales"
} ]
}) # call calculate_sum_of_bonus function

print("====Task3====")

def func(*data):
	MidNameAppearSet = set()
	IsNoRepeatMidName = True

	for NameIndex in range(len(data)):
		# Check if repeated with previous name
		if NameIndex in MidNameAppearSet:
			if NameIndex < (len(data) - 1):
				continue
			# Check if no repeat while reach end
			else:
				if IsNoRepeatMidName:
					print("沒有")
				break

		# Check if repeated with Next name
		for OtherNameIndex in range(NameIndex + 1,len(data)):
			if( data[NameIndex][1] == data[OtherNameIndex][1]):
				MidNameAppearSet.add(NameIndex)
				MidNameAppearSet.add(OtherNameIndex)
		
		if(NameIndex not in MidNameAppearSet):
			print(data[NameIndex])
			IsNoRepeatMidName = False

func("彭大牆", "王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有

print("====Task4====")

def get_number(index):
	if index % 2 == 0:
		print(int(index / 2 * 3))
	else:
		print(int((index + 1) / 2 * 3 + 1))

get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15