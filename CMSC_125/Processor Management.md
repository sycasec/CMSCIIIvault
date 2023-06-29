[[CMSC_125_Root]]

```toc
```
# Processor Management
## CPU Scheduler
- allocates CPU to processes while ensuring optimal **system performance**
- decides through some criteria how *next* process is selected
- tries to not sacrifice user convenience

### system performance measures:
- **CPU utilization** - % of how busy is the CPU
- **System throughput** - number of jobs completed / time
- **Turnaround time** - average time from job execute to job end
- **Wait** - average wait before job gets execute
- **Response** - response to user input
	- not really explained, may be just another word for wait time.
- **Overhead** - time spent *NOT* executing jobs

#### to achieve *good* CPU SCHEDULING:
- follow aforementioned sys performance measures
- meet user specified deadlines
- provide good util for ALL sys resource (not just cpu)
- these are interrelated since an overall improvement is necessary to avoid bottlenecks

## Process Creation
- OS creates a Process Control Block (*PCB*) for process
	- adds this to list of PCBs with an initial state of **ready**
	- code is located
		- if any of the two is failed, process is not created (no space || code not located)

### State transition
- **READY** 
	- CPU busy / no control of CPU
- **RUN**
	- take control of CPU
- **BLOCKED**
	- waiting for I/O, code loading into memory, time of day (scheduled job), message from other process
### Information in the PCB
- **Process state**: 

### Process Termination
- **Normal termination**
	- `exit(0)` , expected termination of the program
- **Abnormal termination**
	- interrupt, all Exceptions, bound violation, arithmetic error, etc.

### Dispatchers
- allocates the CPU among various ready processes
	- (???) supposed job of the CPU scheduler. maybe this is the part of the cpu scheduler that does the specified job?
- **Long Term Scheduler (job scheduler)**
	- picks out processes from the job pool by through a scoring algorithm 
- **Short Term Scheduler (CPU scheduler)**
	- picks out processes to load into the CPU from the ready queue.
- if no process is in the ready state, do some deadend job.
	- loop within the dispatcher and wait for ready process
	- introduce null process (like calculating pi idk old computer shit)

### LTS
- admits processes into ready queue based on PCB information
- possible criteria:
	- expected run time
	- max memory size
	- I/O devices required
	- special resources required
	- priority / job schedule (CRON)
- jobs are aged (the later they are put into ready queue, the higher their score)
	- to prevent job starving, an event where a job never gets the chance to control CPU

### STS
-  preemptive - CPU suspended when higher priority job in RQ
	- used in time-sharing and real-time systems
- non-preemptive - exactly what it says
- possible criteria:
	- CPU Utilization
	- Throughput - jobs / time
	- Turnaround - job completion - job start
		- time waiting in memory + time in RQ + CPU usage time + I/O time
	- Waiting - job start - job ready
	- Response - job submission - job CPU allocation
	- Fairness - all jobs get executed at mrl



### Deterministic Sorting Algorithms
- known DDL
- **Minimizing Mean Response Time (MMRT)**
	- sort by non decreasing execution time
- **Minimizing mean weighted response time (Weighted MMRT)**
	- sort by non decreasing $t_{i}/p_{i}$.
- **Minimizing maximum lateness (MML)**
	- sort by non decreasing di
 

### NDSA
- properties
	- arrival distribution - rate at which jobs come into the system
	- service distribution - service time of jobs entering the system 
	- queue-length - number of jobs waiting in q
	- waiting time - time spent waiting in q
	- little’s result - AVG nCustomer = AVG arrival x AVG stay
	- utilization factor
 
###  Run to completion systems
- used in batch systems
- **FCFS**
	- wait time = execute time - prev job finish time
	- turnaround time = finish time
- **SJF**
	- same lang sa FCFS but sorted by non decreasing burst
- **SRPT**
	- you already know what it is
	 - wait time = finish time - burst time - arrival time
- **PRIO**
	- same lang sa FCFS but sorted by non decreasing PRIO
- **RR**
	- wait = finish time - burst
	- turnaround = curr-time


### Time-Sharing Scheduling
-  more CPU time = preempted every few MS
- achieved through:
	- interrupt clock
	- dynamic adjustment of job prio
	- deliberate switching between jobs by allocating definite time quantum (RR)
- improves response time at cost of overhead (math overhead for swapping between jobs, space overhead to store all suspended jobs)
- **RR**
	- u already know
- **MODIFIED RR**
	- job with run time completed within quantum is placed at start
- **Choice of Time Slice**
	- upperbound = response time / n jobs
	- lower bound:
		- small timeslice = math overhead
		- have some requests that can be completed in one time slice
- **Estimating Response Time**
	- given :
		- n - nUsr
		- t = time to enter command
		- c = time to process command
		- r = response time in seconds
	- n $\cdot$ c ≤ t + r
