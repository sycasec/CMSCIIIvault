### conversion problems
**kilobytes to bytes**

```c
int toBytes(int kB){
	return kB * 1024;
}
```

`kb * 1024*` $= 1 unit$ of time 
return also consumes 1 unit

$T(n) = 2$

```c
char toLower(char ch){
	if(ch >= 'A' && ch <= 'Z')
		return ch+32;
	else
		return ch;
}
```

`ch >= 'A'` = 1;  `ch <= 'Z'` = 1;  `return ch+32` = 2 : $T(n) = 4$
