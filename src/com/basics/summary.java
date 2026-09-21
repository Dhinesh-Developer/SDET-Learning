package com.basics;

public class summary {
	
}

/**
TEsting function
- increasing team productivity
- limit need for debugging
- confidence during the refactoring
- clean code and good architecture
- Enabling test code coverage metric
- documentation

black box testing - test what software does EX. login - message verification [abstract]
white box testing - test how the software works internally - internal code testing


Testing level & testing pyramid
- Acceptance testing - does it actually meet the business requirement
- System testing - test the entire application
- Integration testing - multiple components -> ex. controller - service - repository - database
- Unit testing - individual testing - ex. class, method etc..

Defect Cost increase
- the later a software bug is found, the more expensive it becomes to fix.
| When you find the bug         | What happens                                  |     Cost |
| ----------------------------- | --------------------------------------------- | -------: |
| 👨‍💻 During coding           | Developer fixes the code                      |     ₹100 |
| 🧪 During testing             | Developer investigates + fixes + retests      |     ₹500 |
| 🚀 After release              | Customer finds it + hotfix + support          |   ₹5,000 |
| 💥 Production with many users | Data/business/customer impact + emergency fix | ₹50,000+ |


Functional and non-functional requirements
- Functional  - what the system should do
Ex. login, register, dashboard,transfer money etc..
- Non-Functional - how well the system should do 
Ex. login should perform within 2 seconds, system managesr 10,000 users, etc..

-- functional testing --
smoke, sanity, unit, integration, boundary , APi, user acceptance. regression. 

- smoke -> is the app is stabled enough to testing
- sanity -> focus on fixed area, or new changes done area for retesting
- unit -> small individual testing
- integration -> multiple components testing
- boundary -> edges/ limit case testing
- API -> wihtout using the UI., testing the Api
- user acceptance -> does the application solves the user need
- regression -> after testing the application, does it break another functionality

-- Non funtional -- 
availability, accessibility, performance, compatibility ,localization, volume, scalability. usability, reliablity.
 security, penetration, load, endurance, compilance, stress, maintainability, portability, disaster recovery 

-availability -> test whether the application is available for 24/7 when user need it
- accessibility -> test whether the application is used for different disabilities people
- performance -> check speed and responsiveness
- compatibility -> check working correctly in different environment
- localization -> checks whether the application works in specific region, country etc
- volume -> checks how the system works with large amount of data
- scalability -> checks whether application works when user increases, work load increases
- usability -> check whether the application is easy to understand and user
- Reliability -> check the application works longer wuthout failures
- security -> application protects the password, confidential information etc
- penetration -> actively protects from hackers
- load -> tests the system works under exxcepted,normal workload
- stress -> pushes the system beyond its normal capacity
-> endurance -> checks the system works long period of time
- maintainability ->Checks how easy the software is to modify, fix, test, and maintain.
- compilance -> is that system follows the required laws, regulations etc.
- portability -> checks the system move to another enviroments and work properly
- disaster recovery -> checks whether the system works after the major disaster
 */
