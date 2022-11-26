### 1. `int reverse(int n)` - returns the reverse of n, e.g. `n = 103, return 301; n = 1496, return 6941`

``` C
int reverse(int n){
	int rev = 0;
	while(n > 0){
		rev = rev * 10 + n % 10;
		n = n / 10;
	}

	return rev;
}
```

outside of loop:

`int rev = 0;` = 1, `return rev;` = 1  `n > 0` = 1; total = 3

inside loop:

- `rev = rev * 10 + n % 10;` = 4
- `n = n / 10;` = 2
- `n > 0` = 1
	- total: 7

$$
3 + \sum_{i=0}^{log_{10}(n)} 7 = 3 + 7 (log_{10}(n) - 0 + 1) = 7log_{10}(n) + 10
$$
<br />

### 2. `void reverse(char st[])` - reverses the string st, e.g. st = "dragrace", reverse(st) = "ecargard";
```C
void reverse(char *st){
	char temp;
	int n = strlen(st); // we count 2, because we assume function calls to be O(1)
	
	for (int i=0; i < n/2; i++){
		temp = st[i];
		st[i] = st[n - i - 1];
		st[n - i - 1] = temp;
	}
}
```
outside loop:

- `char temp` = 1;
- `int n = strlen(st)` = 2
- `int i=0;` = 1
- `i < n/2;` = 2
	- total = 6

inside loop:

- `i < n/2; i++` = 3
- `temp = st[i];` = 1
- `st[i] = st[n - i - 1];` = 3
- `st[n - i - 1] = temp;` = 3
	- total = 10

<br />
$$
6 + \sum_{i=0}^{\frac{n}{2} - 1} 10 = 6 + 10(\frac{n}{2}-1-0+1)
$$<br />
$$
= 5n + 6
$$
<br />

### 3. `bool sorted(int A[], int n)` - returns true if array A with size n is sorted in increasing fashion or in decreasing fashion
```python
def sorted(A:list[int], n:int) -> bool:
	if n==0 or n==1:
		return True
	if A.count(A[0]) == n: # we count 2, because we assume function calls to be O(1)
		return False
	state:int = -1
	p_state:int = -1

	for i in range(n - 1):  #for(int i=0; i < n-1; i++)
		if A[i] <= A[i+1]:
			state = 0
		elif A[i] >= A[i+1]:
			state = 1
		if i > 0 and p_state != state:
			return False
		p_state = state

	return True
```
out of loop:

- `n==0 || n==1` = 2
- `A.count(A[0]) == n` = 2
- `state:int = -1`, `p_state:int = -1` = 2
- `int i=0, i < n-1` = 3
	- total =  9

inside loop:

- `i < n-1; i++` = 3
- `A[i] <= A[i+1]` = 2
- `A[i] >= A[i+1]` = 2
- `if i > 0 and p_state != state:` = 2
- `p_state = state` = 1
	- total 10, upper bound n-2, lower bound 0

<br />

$$
9 + \sum_{i=0}^{n - 2} 10 = 9 + 10(n-2-0+1)
$$

<br />


$$
= 10n - 1
$$

<br />

# int remainder(int a, int b) - returns the remainder when a is divided by b, recursive subtraction

```c
int remainder(int a, int b){
	if(a < b)
		return a;
	return (remainder(a-b, b));
}
```

- `a < b` = 1
- `return (remainder(a-b, b))` = 3

base case:

- `a < b; return a;` = 2


<br />
$$T(n) = 4 + T(a-b)$$ <br />
$$= 4 + 4 + T(a-2b)$$ <br />
$$= 4 + 4 + 4 + T(a-3b)$$ <br />
$$= 4 + 4 + ... + 4 + T(a < b)$$ <br />
$$= 4(n-1) + 2$$ <br />
$$= 4n - 2$$