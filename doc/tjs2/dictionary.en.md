---
source_hash: 8783ef22bb24
---

# Dictionary Class

## Dictionary class

The Dictionary class handles **dictionary arrays**.



A dictionary array, also called an **associative array**, is an object that holds multiple pairs of a name and its associated value.

Like an array, it is accessed with the **[ ]** (indirect member access) operator, but a string is used instead of an index, and that string is the name. If the name is a valid identifier, the **.** (direct member access) operator can also be used.

Referencing a name that does not exist yields void.

Use the delete operator to remove an element.

```
	var d=new Dictionary();
	d["sat"] = 1; // d.sat = 1 と同じ
	d["sun"] = 2; // d.sun = 2 と同じ
	d["mon"] = 3; // d.mon = 3 と同じ
	d["name"] ="value!"; // d.name = "value!" と同じ
	d["continue"] = 4; // continue は識別子ではないが OK
	d.continue = 4; // continue は識別子ではないのでエラー

	var sat = d["sat"]; // 1 が代入される
	var none = d["none"]; // void が代入される

	delete d.sat; // sat を削除
	delete d["continue"]; // continue を削除
```

## Inline dictionary arrays

With `**%[ ]**`, you can write a `Dictionary` object in place within an expression. List the initial elements as comma-separated "name => value" pairs. For example,

`
var dic = %["a" => 1, "b" => 2, "c" => 3];

`
assigns to `dic` a reference to a `Dictionary` object whose name/value pairs are `"a":1`, `"b":2`, and `"c":3`.

Internally, `=>` is exactly the same as a comma, but it is allowed for readability (as in Perl).

## Accessing Dictionary class methods

A newly created Dictionary object has no members at all.

For example, if you want to use the assign method and write `dict.assign(src)` for a Dictionary object dict, it fails because dict has no method called assign.

Instead, use the **incontextof** operator to run a method that belongs directly to the Dictionary class with the target Dictionary object as its context.

```
	var a = %[];
	var b = %[];
	(Dictionary.assign incontextof a)(b); // b を a にコピー
	(Dictionary.clear incontextof b)(); // b の内容をクリア
```

## saveStruct

saveStruct writes structured data to a file.

See the method of the same name in the [Array class](array.md#savestruct).

## assign

The assign method copies a dictionary array.

```
構文 : assign(<コピー元辞書配列>, <内容をクリアするか=true>)
```

Copies the entire contents of another dictionary array given as the argument (the source dictionary array).

If the second argument (whether to clear the contents) is false, the contents of the destination (the object the method runs on) are not cleared, and the contents of the source are written over them. When the destination has a member with the same name as one in the source, the destination's value is overwritten with the source's.



If an array (an Array object) is given as the source, its elements are treated as the members of this dictionary array, laid out as name, value, name, value, and so on, and they are copied into this dictionary array.

## assignStruct

The assignStruct method copies a dictionary array.

```
構文 : assignStruct(<コピー元辞書配列>)
```

Copies the entire contents of another dictionary array given as the argument (the source dictionary array).

Unlike the assign method, members that are arrays or dictionary arrays are also copied recursively (assign copies only the references).

## clear

The clear method removes all contents of the dictionary array.
