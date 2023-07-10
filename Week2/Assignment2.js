console.log("====Task1====");

function findAndPrint(messages){
	for(let KeyName in messages) {
		// Check age
		if(messages[KeyName].includes("I'm 18 years old")) {
			console.log(KeyName);
			continue;
		}

		// Check education
		if(messages[KeyName].includes("I'm a college student")) {
			console.log(KeyName);
			continue;
		}
		
		// Check rights for Taiwan case
		if(messages[KeyName].includes("I am of legal age in Taiwan")) {
			console.log(KeyName);
			continue;
		}

		//  Check rights for USA case
		if(messages[KeyName].includes("I will vote")) {
			console.log(KeyName);
			continue;
		}
	}
}
	
findAndPrint({
	"Bob":"My name is Bob. I'm 18 years old.",
	"Mary":"Hello, glad to meet you.",
	"Copper":"I'm a college student. Nice to meet you.",
	"Leslie":"I am of legal age in Taiwan.",
	"Vivian":"I will vote for Donald Trump next week",
	"Jenny":"Good morning."
});

console.log("====Task2====")

function calculateSumOfBonus(data){
	let EmployeeList = data.employees;
	let SumofBonus = 0;
	let EffSalary = 0.01;
	let USD2TWD = 30;
	let AvgBonus = 1000;

	for(let i in EmployeeList) {
		let EmployeeBonus = 0;

		// Check salary
		// integer type, add to sum directory
		if(typeof(EmployeeList[i].salary) == "number" ) {
			EmployeeBonus += EffSalary * EmployeeList[i].salary;
		}
		// string type,
		else {
			// remove ',' mark
			EmployeeList[i].salary = EmployeeList[i].salary.replace(/,/g,"");

			// USD case
			if(EmployeeList[i].salary.includes("USD")) {
				EmployeeList[i].salary = EmployeeList[i].salary.replace(/USD/g,"");
				EmployeeList[i].salary = EmployeeList[i].salary * USD2TWD;
			} 
				
			EmployeeBonus += EffSalary * EmployeeList[i].salary;
		}

		// Check performance
		if(EmployeeList[i].performance == "above average") {
			EmployeeBonus += AvgBonus * 1.5;
		}
		else if(EmployeeList[i].performance == "average") {
			EmployeeBonus += AvgBonus;
		}
		else {
			EmployeeBonus += AvgBonus * 0.5;
		}

		// 	Check role
		if(EmployeeList[i].role == "CEO") {
			EmployeeBonus += 1000;
		}
		else if(EmployeeList[i].role == "Engineer") {
			EmployeeBonus += 2000;
		}
		else if(EmployeeList[i].role == "Sales") {
			EmployeeBonus += 1500;
		}

		SumofBonus += EmployeeBonus;
	}
	// Check sum of bonus of all employees
	if(SumofBonus > 10000) {
		console.log("larger than 10000");
	}
	else {
		console.log(SumofBonus);
	}
}
calculateSumOfBonus({
	"employees":[
		{
			"name":"John", "salary":"1000USD", "performance":"above average", "role":"Engineer"
		},
		{
			"name":"Bob", "salary":60000, "performance":"average", "role":"CEO"
		},
		{
			"name":"Jenny", "salary":"50,000", "performance":"below average", "role":"Sales"
		} ]
}); // call calculateSumOfBonus function
	
console.log("====Task3====")

function func(...data){
	let MidNameAppearSet = {}; 
	let IsNoRepeatMidName = true;

	for(let NameIndex = 0; NameIndex < data.length; NameIndex++) {
		// Check if repeated with previous name
		if(MidNameAppearSet[NameIndex]) {
			if(NameIndex < data.length - 1) {
				continue;
			}
			// Check if no repeat while reach end
			else {
				if(IsNoRepeatMidName) {
					console.log("沒有");
				}
				break;
			}
		}

		// Check if repeated with Next name
		for(let OtherNameIndex = NameIndex + 1; OtherNameIndex < data.length; OtherNameIndex++) {
			if(data[NameIndex][1] == data[OtherNameIndex][1]) {
				MidNameAppearSet[NameIndex] = true;
				MidNameAppearSet[OtherNameIndex] = true;
			}
		}

		if(MidNameAppearSet[NameIndex] != true) {
			console.log(data[NameIndex]);
			IsNoRepeatMidName = false;
		}
	}
}

func("彭大牆", "王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有

console.log("====Task4====")

function getNumber(index){
	if(index % 2 == 0) {
		console.log(index / 2 * 3);
	}
	else {
		console.log((index + 1)/ 2 * 3 + 1);
	}
}

getNumber(1); // print 4
getNumber(5); // print 10
getNumber(10); // print 15