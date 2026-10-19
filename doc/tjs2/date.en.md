---
source_hash: 1ad99c349d6a
---

# Date Class

## Date class

Creating a Date object from a string and creating a string from a Date object are not implemented; otherwise, it is almost compatible with JavaScript's Date.



The constructor syntax is as follows.

```
new Date();
new Date(<日付文字列>);
new Date(<年>, <月(0～)=0>, <日=1>, <時=0>, <分=0>, <秒=0>);
```

The first form takes no arguments. The object holds the current date and time at the moment the constructor runs.

The second form takes a date string. The string must be in the ANSI C asctime() format, the format defined in RFC 1123, the format defined in RFC 1036, or the form "year/month/day hour:minute:second". The format is detected automatically and some variations are accepted, but strings that differ too much from the expected formats may not be recognized.

The third form takes the year, month (counted from 0, default 0), day (default 1), hour, minute, and second (each default 0).



Implemented methods (JavaScript compatible):

setYear/getYear (sets/gets the 4-digit year in local time)

setMonth/getMonth (sets/gets the month in local time)

setDate/getDate (sets/gets the day of the month in local time)

setHours/getHours (sets/gets the hour in local time)

setMinutes/getMinutes (sets/gets the minutes in local time)

setSeconds/getSeconds (sets/gets the seconds in local time)

setTime/getTime (sets/gets the number of milliseconds elapsed since January 1, 1970, 0:00)

getDay (gets the day of the week)

parse (parses a date string)
