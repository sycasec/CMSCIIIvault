# Extreme Programming
- deliver software fast and safe

[[Week_IV_XPextreme_prog|Short version]]

##### stages:
- [[Week_IV_PlanningActs||Planning]]
- [[Week_IV_Design|Design]]
- [[Week_IV_coding_and_testing|coding and testing]]

### Pairing
- **pair programming**
	- all production code is developed by more than one person
	- *driver*
		- types the code on the keyboard
	- *navigator*
		- thinking on the code
	- switch between these roles, share the knowledge between the team
	- more people in the team understand how the code works
	- use everybody's skill to the fullest
	- your pair can sanity check your ideas
	- pair can spot bugs
- **Mobbing / mob programming**
	- many people sit around a screen and there is one *driver*
	- the team / mob are the *navigators*
	- team takes turn in becoming the *driver*
	- works best for 3-4 people
	- do a *spike*
		- one member goes solo and tests a functionality first
		- after testing, share it with the mob
		- improves quality of the code

### Test-first
- write tests first.
- gives confidence to refactor
- drive behavior to **oustide-in**
	- building acceptance tests first allows you to focus on what exactly needs to be built

### Continuous Delivery
- code is always ready for deployment
- no commit that isn't ready for production
- monitor the product live
- **toggles, not branches**
	- updates always deployed to main branch
	- updates are toggled off 
		- these updates are then tested by testers
		- when ready, toggled on
	- remove the feature toggle after a while

#### Top 3 tips
- **add monitoring**
	- see what is working in what platform
	- add healthchecks
- **test first bug fix**
- **pair code reviews**
	- makes code reviews fast