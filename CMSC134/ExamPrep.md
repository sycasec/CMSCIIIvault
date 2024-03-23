# Exam Prep CS161

## 2 - Memory Safety Vulnerabilities
### I
``` c
#include <stdlib.h>
#include <string.h>

struct log_entry {
	char title[8];
	char *msg;
}

void log_event(char *title, char *msg) {
	size_t len = strnlen(msg, 256);
	if (len == 256) return; /* message too long */

	struct log_entry *entry = malloc(sizeof(struct_log_entry));
	entry->msg = malloc(256);
	strcpy(entry->title, title);
	strncpy(entry->msg, msg, len+1);
	add_to_log(entry);
}
```
1. Line 14, `strcpy` 
2. 1 = title, 2 = `entry->title`, 3 = `entry->message`
3. 