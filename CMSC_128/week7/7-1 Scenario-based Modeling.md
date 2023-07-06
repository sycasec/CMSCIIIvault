# Scenario-based Modeling

```toc
```

- analyse various ways user interact with the system
- scenarios can come from external systems

## Tools commonly used
**UML**
- **Use Cases**
- **Activity Diagrams**
- **Swimlane Diagrams**
- **User Stories**

### Use Case
- aid to defining what exists outside the system (*actors*) and
- what should be performed by the system (*use cases*)

#### Elements of a Use Case
- Actor
- Activities or actions performed by an actor (scenarios)
- Preconditions before a use case is initiated
- Trigger that invokes or gets the use case started
- Exceptions

visualized with a *use case diagram*

#### How to write a use case 
- identify who is going to be using the software (*actors*)
- pick one 
- define what actor wants to do using the software
	- each thing the user does is a use case
- for each use case, decide on the normal course of events (*scenarios*)
- describe the basic course in the description for the use case in terms of 
	- what user does
	- what system does in response
- consider alternate courses to each course, extend the use case with thse alt courses
- look for commonalities in use cases, extract these and note them as common course use cases 

**Enrollment System**
**FORMAL USE CASE EXAMPLE**
*Use Case 1* - Student enlists classes to enroll
*Actor* - Student
*Goal* - The student must be able to enlist in classes for courses prescribed by curriculum
*Precondition* - The student must be able to enlist in classes for courses preescribed by the curriculum
*Trigger* - It's the student's schedule for pre-enlistment and the student needs to enlist the classses that the student needs to enroll for
*Scenarios*
- A student checks what classes are offered in the semester
- The student selects from various classes based on the students' required courses to take
- The studetn checks the scedule for conflict.
- After the student selects classes, the student submits the selection for enlistment.
*Exceptions*
- The student ID and password does not match
- The student is not an active student for the semester
- There are no classes offered for the student based on the prescribed curriculum

### Activity Diagram
- just flowchart rules actually
- start is denoted with filled circle
- terminate is denoted with circle outline


### Swimlane Diagram
- flow of activities described by use 
- indicates which actor or analysis class has responsibility for action described
- **Activity Diagram**, but add a way to spearate the actor and the analysis class (system user interacts with)
![[Pasted image 20221109222010.png|550]]

## User Stories
- end users write user stories
- UML tools can complement this

- **user story** is a tool used in *Agile* software development to capture a description of a software feature from an end-user perspective
- describes:
	- **type of user**
	- **what they want**
	- **why**
- helps create a simplified description of a requirement
- as **<role/persona>**, I should be able to **<\requirement>** so that **<\benefit>**
