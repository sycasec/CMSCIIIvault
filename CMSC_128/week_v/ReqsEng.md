- [[week v]]
```toc
min_depth: number (default: 2) 
max_depth: number (default: 6) 
title: Requirements Engineering 
allow_inconsistent_headings: boolean (default: false) 
```

# Requirements Engineering
- systematic and scientific process is followed in creation of the work product
- the broad spectrum of tasks and techniques that lead to understanding requirements
- first stage where quality of the software can be introduced
- if not understood properly, quality of later stages of the products will eventually have poor quality.

## Challenges of requirements Engineering
- customers usually do not know what they want
	- do not tell you everything
		- ask the right probe questions
	- do not understand what features or functions provide benefit
	- requirements change overtime

## Tasks encompassing Requirements Engineering
- as product cycles shorten, there are pressures to streamline requirements engineering so that products come to market more quickly
- the problems remain the same: *getting timely, accurate, and stable stakeholder input.*
[[Week_IV_scrum]]
### Inception
- time when project is initiated
- you establish a **basic understanding** of the problem. 
- in this stage, the team produces:
	- definition of a business case
	- feasibility study
	- describe project's scope
- people involved are systems analysts:
	- program and understand / manage business
		- management info sys
	- know how to create a *business case*

#### Realities in requirements gathering
- customers may:
	- be located in a diff city or country
	- only have a vaguye idea of what si required in the software, or none at all
	- may have conflicting requirements
	- may have limited tech knowledge
	- have limited time to work with dev team
	- may resist the project

#### Establishing Groundwork
- **Identify Stakeholders**
	- stakeholders are anyone who may have a direct interest in or benefit from the system to be developed
	- create a list of peeople who will be able to contribute input as requirements are elicited. Grow the list as you go along
	- **sponsors**
	- **champions**
		- help promote or find stakeholders for your project
			- basically get brand ambassadors (preferrably for free)
- **recognize multiple viewpoints**
	- requirements of system will be explored from diff points of view
	- as information is collected, requirements may be inconsistent.
- **work towards collaboration**
	- there may be battles between customers
		- the work of the analyst is to bring the customers together 
	- stress to the clients that their collaboration is essential to completion of project.
- **ask the first questions right**
	- context free questions during inceptions
		- focus on the customers and other stakeholders
			- who is behind the request
			- who will use the solution
			- what will be the economic benefit for the solution
			- is there another source for the solution
		- gain a better understanding of the problem
		- focus on the effectiveness of the communication activity itself
			- am i asking too many questions
			- are there any other sh's involved
			- should i be asking you for anything else

### Elicitation 
- the key is to *describe the problem in a way that establishes a firm base for design*
	- beyond that point, you are already designing
	- we already hint on tech solutions
	- we want the suggestions to mainly come from SH
- engage SH's and encourage them to establish goals
	- **goal** is a long term aim that a solution must achieve
- upon establishment of goals, establish a prioritization mechanism 
	- sprint planning meeting (?) - scrum project backlog refinement meeting
	- *design rationale for a potential architecture that meets the SH goals*

#### Elicitation Work Products
- a bounded statement of scope for the system or product (release plan)
	- what will be released, and when?
- updated list of customers  users and other SH's who participated in reqs elicitation
- description of system technical environment
- list of reqs (organized by function) and domain constraints that apply to each
- set of usage scenarios that provide insight into the use of system or product under different operating conditions
- any prototypes develoepd to better define reqs

#### Types of User Reqs
##### Functional Reqs
- functions or features that user specifies should be present in the software
- usually related to users' function
	- examples:
		- add customers
		- create product catalogs
		- print reports
		- automatically calculate payables

##### Non-Functional Requirements
- requirements that address **usability**, **testability**, **security**, or maintainability.
- end users fail to articulate this.
- examples:
	- secure database
	- allow improvements to the software in the future
	- accessible from anywhere
	- acceptable response time


 
### Elaboration
- information obtained from the customer during inception & elicitation is *expanded* and *refined*
- focused on developing *refined requirements model* that identifies various aspects of software function, behavior, and information.
- basically **user stories**
### Negotiation
- addresses conflicting reqs, or customers are asking more than what is necessary
- using agile / scrum approach, team and product owner can:
	- prioritize reqs,
	- assess their cost and risk,
	- address internal conflicts,
- some reqs are eliminated, combined, or modified so that each party achieves some measure of satisfaction
### Specification
- requirements need to be presented in a **consistent** and therefore more understandable manner
- specification can be a written doc, set of graphs, formal math model, usage scenarios, prototypes, or any combination of these
- also known as **requirements modeling**
### Validation
- reqs validation tests the specs to ensure that:
	- all software reqs are unambiguous
	- inconsistencies, omissions, errors have been detected and corrected
	- work products conform to the standards established for the process, the project, and the product
### Management
- requirements for computer based systems change, and the desire to change reqs persists throughout hte life of the system
- the goal is to **identify**,**control**, and **track** requirements and changes to requirements at any time as the project proceeds

#### Change Requests
##### Raising a Change Request
- use a template
- identify a sched when changes can be accommodated
- where and to whom the change request is submitted
##### Assessing a Change Request
- assess impact of CR to the project sched and budget
- assess impact of change not accommodated
	- usually done by the PM
##### Making a decision
- review impact analysis
- management decides based on impact analysis
##### Accommodating Change
- accommodate change when approved
- communicate changes to the devs
- document the changes (changelog, release notes)

