---
source_hash: 3046dd456bfe
---

# Telling Kirikiri 2 and Kirikiri Z Apart
## Static detection
In the TJS2 preprocessor, `kirikiriz` is 1, so you can use it for anything that needs to switch statically.  
However, scripts compiled to bytecode cannot switch this way, because the bytecode is generated according to the preprocessor at compile time.
Scripts stored as text have no such problem.

## Dynamic detection
The System.versionInformation property reads "吉里吉里[きりきり] 2 実行コア…" in Kirikiri 2 but "吉里吉里[きりきり] Z 実行コア…" in Kirikiri Z, so you can tell them apart.  
Also note the version string change: System.versionString returns 1.0.0.001.  
The version number was reset with Kirikiri Z, so be careful if your code expects something like 2.X.X.XXX.
