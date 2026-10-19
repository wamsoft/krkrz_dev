---
source_hash: e55949e6798a
---

# Array Class

## Array class

The Array class handles **arrays**.



Create an object of this class and you can use it like an array, with indexes specified through the indirect member selection operator. Indexes are integers: 0 is the first element, 1 is the next, and so on. A negative integer counts from the end of the array (-1 is the last element).

```
	var a = new Array();
	var i;
	for(i=0;i<100;i++) a[i]=i;
```

You do not need to declare the size of an array. It grows automatically to fit the specified index, and elements that have not been assigned are initialized to void.



The count property holds the size of the array. You can also change the size by assigning a value to count.

## Inline arrays

With `**[ ]**`, you can write an `Array` object in place within an expression. List the initial elements inside `[ ]`, separated by commas. For example,

`
var ar = ["a", "b", "c"];
`
assigns to `ar` a reference to an `Array` object containing the elements `"a" "b" "c"`.

## count

The count property holds the size of the array.

## load

The load method reads an array from a file.

```
構文 : load(<ファイル名>, <モード=''>)
```

Reads an array from a text file (first argument: the file name). Each line of the file goes into one element, so count ends up equal to the number of lines in the file.

The mode (second argument) is the mode string used when reading the file; its meaning depends on the environment TJS runs in. "o" followed by a decimal offset starts reading at that byte position in the file.

Depending on the environment TJS runs in, this method, the save method, and the saveStruct method may not be available.

The load method returns this Array object itself.

## save

The save method writes an array to a file.

```
構文 : save(<ファイル名>, <モード=''>)
```

Writes the array to a file (first argument: the file name). Each member is written on its own line; references to objects, classes, functions, and the like become empty lines.

The mode (second argument) is the mode string used when writing the file. Its meaning depends on the environment TJS runs in; in Kirikiri, "c" applies simple encryption to the file (it can still be read with the load method as is). "z" saves the file compressed (cannot be combined with "c"; it can also be read with the load method as is). "o" followed by a decimal offset starts writing at that byte position in the file.

The save method returns this Array object itself.

## split

The split method splits a string.

```
構文 : split(<パターン/デリミタ集合>, <文字列>, <(予約)>, <空の要素を無視するか=false>)
```

Initializes the array and fills it with the pieces of the string (second argument) separated by the pattern or delimiter set.

The first argument is a pattern or a delimiter set.

A pattern must be a regular expression object.

A delimiter set specifies the characters used as separators. Passing a string specifies multiple separator characters.

The third argument is reserved for future versions.

For the fourth argument (whether to ignore empty elements), specify true to leave out empty elements (for example, those produced by ,,,,, when a comma is the delimiter).

Note the order of the arguments.

## join

The join method joins the array into a single string.

```
構文 : join(<デリミタ>, <(予約)>, <空の要素を無視するか=false>)
```

Joins the elements of the array with the delimiter (first argument) and returns the joined string. The second argument is reserved.

If the third argument (whether to ignore empty elements) is true, void elements are skipped.

```
	var ar = [ "a", "b", void, "d" ];
	var s1 = ar.join(","); // s1 には "a,b,,d" が代入される
	var s2 = ar.join(",",,true); // s2 には "a,b,d" が代入される
```

## reverse

The reverse method reverses the order of the array's elements.

```
構文 : reverse()
```

## sort

The sort method sorts the array.

```
構文 : sort(<ソート順='+'>, <安定ソートを行うか=false>)
```

The sort order (first argument) is one of the following strings. Ascending order sorts from smallest to largest, and descending order is the reverse. If omitted, '+' is assumed.

```
"+"  : 昇順 (通常の < 演算子での比較)
"-"  : 降順
"0"  : 数値による昇順 ( 10,2,1 は 1,2,10 に並び替えられます )
"9"  : 数値による降順
"a"  : 文字列による昇順 ( "a","c","b" は "a","b","c" に並び替えられます )
"z"  : 文字列による降順
```

That is: "+" ascending (compared with the ordinary < operator), "-" descending, "0" numeric ascending (10,2,1 becomes 1,2,10), "9" numeric descending, "a" string ascending ("a","c","b" becomes "a","b","c"), and "z" string descending.

Instead of a sort-order string, you can pass a function. The function takes two arguments and should return true when the first argument should come before the second (note that the meaning of the return value differs from the function passed to JavaScript's sort method).



The second argument specifies whether to perform a stable sort. If omitted, false is assumed and an unstable sort is performed. With a stable sort, elements that rank equally keep their relative order after sorting. With an unstable sort, there is no guarantee that equally ranked elements keep their order.

```
	var array = [ 0, 1, 2, 10, 12, 14, 4, 6, 2 ];
	array.sort();
		// ↑ メソッド実行後、array は [0, 1, 2, 2, 4, 6, 10, 12, 14] に
	array.sort('-');
		// ↑ メソッド実行後、array は [14, 12, 10, 6, 4, 2, 2, 1, 0] に
	array.sort('a');
		// ↑ メソッド実行後、array は [0, 1, 10, 12, 14, 2, 2, 4, 6] に

	var array = [ "hoge", "foo" , "bar", "baz" ];
	array.sort();
		// ↑ メソッド実行後、array は ["bar", "baz", "foo", "hoge"] に

	var array = [ "abcd", "abc", "ab", "a" , "b", "c" ];
	array.sort(function(a,b) { return a< b; } );
		// ↑ '+' の指定と同じ意味

	var array = [ "abcd", "abc", "ab", "a" , "b", "c" ];
	array.sort(function(a,b) { return a.length < b.length; } );
		// ↑ 文字列の長さの短い順
		// (長さが同じ"a" "b" "c" がソート後も "a" "b" "c"
		// の順番である保証はない)

	var array = [ "abcd", "abc", "ab", "a" , "b", "c" ];
	array.sort(function(a,b) { return a.length < b.length; }, true );
		// ↑ 文字列の長さの短い順
		// (長さが同じ"a" "b" "c" はソート後もこの順番である)
```

## saveStruct

saveStruct writes structured data to a file.

```
構文 : saveStruct(<ファイル名>, <モード=''>)
```

The saveStruct method writes the elements to a file in a form from which their state can be restored.

Elements can be strings, real numbers, octet strings, or integers. An element that is an object has its contents written to the file only if it is an Array or Dictionary object; any other element is written as void.

For example,

```
	([ 1, 2, 3, [4, 5], %[ a : 1, b : 2 ], "文字列" ]).saveStruct("out.txt");
```

writes something like the following.

```
(const) [
	1,
	2,
	3,
	(const) [
		4,
		5
	],
	(const) %[
		"a" => 1,
		"b" => 2
	],
	"文字列"
]
```

Evaluating the whole file as a single expression restores the same structure as when it was saved.

Here, (const) indicates that the contents of [ ] or %[ ] consist only of constant terms. When the compiler finds (const), it assumes the inline dictionary array or inline array that follows contains only constant terms, and can load it efficiently.

The saveStruct method returns this Array object itself.

## assign

The assign method copies an array.

```
構文 : assign(<コピー元配列>)
```

Copies the entire contents of another array given as the argument (the source array).



If a dictionary array (a Dictionary object) is given as the source, the result is an array in which the dictionary's members appear alternately as name, value. The order of the members is undefined.

## assignStruct

The assignStruct method copies an array together with its structure.

```
構文 : assignStruct(<コピー元配列>)
```

Copies the entire contents of another array given as the argument (the source array).

Unlike the assign method, members that are arrays or dictionary arrays are also copied recursively (assign copies only the references).

## clear

The clear method removes all elements of the array.

## erase

The erase method removes the element at the specified index.

```
構文 : erase(<添え字>)
```

Removes the element at the specified index. The elements after it each shift forward by one to close the gap. An exception is thrown if the index is out of range.

## remove

The remove method removes elements that have the specified value.

```
構文 : remove(<値>, <すべて削除するか=true>)
```

Compares each element with the specified value by identity (the behavior of the **===** operator) and removes the matching elements.

If the second argument (whether to remove all) is false, only the first matching element is removed. Otherwise, all matching elements are removed.

## insert

The insert method inserts the specified value at the specified position.

```
構文 : insert(<位置>, <値>)
```

Inserts the value (second argument) at the index given by the position (first argument). The elements from that position onward each shift back by one.

## add

The add method appends the specified value to the end of the array.

```
構文 : add(<値>)
```

Appends the value to the end of the array.

This method returns the position at which the value was added.

## find

The find method returns the index at which the specified value first appears.

```
構文 : find(<値>, <検索開始位置=0>)
```

Examines the elements in order, starting from the start index (second argument, default 0), and returns the index at which the value (first argument) first appears. Returns -1 if the value is not found.

Identity comparison (the behavior of the === operator) is used.

## push

The push method appends the specified elements to the end of the array.

Unlike the add method, this method returns the size of the array after appending. If multiple arguments are given, all of them are appended in order.

```
構文 : push(<値>, ...)
```

## pop

The pop method takes one element from the end of the array and returns it. The element is removed from the array (the array's size decreases by one).

This method returns the removed element, or void if there were no elements.

```
構文 : pop()
```

## unshift

The unshift method adds elements to the beginning of the array. If multiple elements are given, all of them are added to the beginning; for example, if a, b, c are passed in that order, the array begins with a, b, c in that order.

This method returns the size of the array after adding.

```
構文 : unshift(<値>, ...)
```

## shift

The shift method takes one element from the beginning of the array and returns it. The element is removed from the array (the array's size decreases by one).

This method returns the removed element, or void if there were no elements.

```
構文 : shift()
```
