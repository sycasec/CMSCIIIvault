[[CMSC_128]]
# Week 2 Notes

##### Why does software failure graph look like that

-   Number of users have dramatically increased
-   user needs have grown more complex
-   because systems are mission critical, software must be of high quality
-   because user-base and needs increase, software must be maintainable
-   given that change is inevitable, the best that we can do is minimize the these failures.
-   Additional points
    -   concerted effort must be made before a software solution is developed
    -   large teams of people now maintain programs that were created by a single individual (see php history)
    -   sophisticated software that were implemented in a predictable, self-contained, computing environment are now embedded inside everything.
    -   individuals, businesses, and government entities increasingly rely on software for decision making as well as daily operations and control. software should be of high quality
    -   s

#### Software, in all of its forms and across all of is application domains should be engineered.

-   to engineer is to use scientific principles to design and build.
-   it enables us to build complex systems in a timely manner and with high quality.

#### Software engineering is a layered technology

-  We achieve this through the **three aspects of software engineering**: 
	- **process**,              structured
	- **methods**,           like 
	- and **tools**.           a 
	- **quality focus**    triangle
-   All of these aspects are established with a **quality focus** in mind.
-   **Quality Focus**
    -   bedrock
    - quality must be introduced at every step of the software development process
-   **Process**
    -   overarching framework
    -   basis for management control of software projects.
    -   establishes context in which technical methods are applied
    -   work products are produced
    -   milestones are established
    -   quality is ensured
    -   change is properly managed
-   **Methods**
    -   technical how to’s for building software
    -   communication, requirement analysis, design modeling,
    -   program construction, testing and support.
-   **Tools**
    -   provide automated or semi-auto support for process and methods
    -   CASE tools, Modelling tools like StarUML, ERD Plus to create ER diagrams (lucid chart?), IDE tools to speed up programming, testing and integration.
    

### Software Engineering Process

- Guide or template that the dev team must follow.
- collection of activities, actions, tasks that are performed
- **Process Framework**
    -   **Activity** - achieve a broader objective (e.g. construction)
        - *Action* - tasks that produce a major work product (e.g. create a component)
        - *Tasks* - small but well-defined objective that produces a tangible outcome.
- process is not a rigid prescription for how to build software,
- it is an adaptable approach that enables the dev team to choose appropriate work actions

### The Process Framework

> **Communication → Planning → Modelling → Construction → Deployment**

-   activities that are applicable to all software projects
- **Communication**
    - critical to communicate & collab with customer
    - understand stakeholder’s objectives for the project.
    - capture initial requirements that help define s/w features and functions.
- **Planning**
    - creates a map that helps guide the team
    - describes the technical tasks to be conducted
    - risks that are likely
    - resources required
    - products to be produced
    - work schedule
- **Modelling**
    - create models to understand software requirements
    - create a design model specifically for those requirements.
- **Construction**
    - generate code (build phase) and test errors in the code (test phase)

#### Different Process Flow Types
- **Deployment**
    - software is delivered to the customer
    - evaluated and given feedback
- **Linear Process Flow**
    - the above process is executed linearly
- **Iterative PF**
    - some activities/tasks are repeated before proceeding
- **Evolutionary PF**
    - executes activities in a “circular” manner
    - each completion leads to a more complete version of the software
- **Parallel PF**
    - executes one or more activities in parallel with other activities

### Software Dev Myths

- **Software reqs continually change, but change can be easily accommodated because software is flexible**
    -   software reqs change, but the impact of the change varies with the time (relative to the development stage) at which it is introduced.
-   **If software is outsourced, the firm will just build it**
    -   If the org does not understand how to manage and control sw projects internally, it will struggle when it outsource sw projects
    -   basically if a shitty company cant build your software, it will try to outsource and the result is even more shitty
-   **We already have an established procedure for building software**
    -   is the procedure used, are the software practitioners aware of it,
    -   does it reflect modern sw practice, is it complete, is it adaptable,
    -   is it streamlined to improve time-to-delivery while maintaing focus on qual,
    -   many question, little time.
-   **Once we write the program and get it to work, LGTM.**
    -   industry data indicates that 60-80% of work is done after initial delivery
    -   like damn, so the evolutionary + parallel process is the way to go?
-   **Until I get the program running we cannot assess its quality**
    -   a technical review is a very effective sw qa mechanism that can be applied anytime.
-   **The only deliverable work product for a successful project is the working program**
    -   models, documents, plans, provide a foundation for successful engineering
    -   planning and documentation are also instrumental
-   **SW Eng will make us create big and needless documentation which will slow team down**
    -   not about docs, but about quality product.
    -   better qual = less rework
    -   less rework = faster delivery times.
    -   like you could just remove the less rework part and it makes more sense.