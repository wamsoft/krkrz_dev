---
source_hash: 03e15351198b
---

# for Statement

## for Statement

The `for` statement is similar to the `while` statement, but more elaborate.

The syntax is as follows.

`
for(clause1;clause2;clause3)
statement or block
`


Clause 1 specifies an expression to execute before entering the loop. You can also declare variables here; variables declared here remain valid for the duration of the loop (they are removed when the loop exits). It can be omitted.



Clause 2 specifies the condition. The statement or block is executed repeatedly while this condition is `true`. If omitted, it is treated as always true.



Clause 3 specifies an expression to execute at the end of the statement or block. It can be omitted.



The behavior is as follows:

(1) First, execute clause 1

(2) Evaluate clause 2; if it is false, finish without executing the statement or block

(3) Execute the statement or block

(4) Execute clause 3

(5) Evaluate clause 2; if it is false, exit the loop

(6) Repeat from (3)



If a `**break**` statement is encountered in the block, the loop exits at that point. If a `**continue**` statement is encountered, execution jumps to (4).

```
	var i,a=1;
	for(i=1;i<5;i++)
	{
		a*=i;
	}

	var i;
	for(i=0;i<10;i++)
	{
		if(obj[i]==0) continue; // i++ is still executed after continue
		if(obj[i]==1) break; // break exits immediately
		func(obj[i]);
	}
```
