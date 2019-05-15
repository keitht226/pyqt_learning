# Python Overview

## Variables and Objects
- Python is dynamically typed as opposed to C/C++.
- "Variables" in python are sometimes referred to as "object references" since they refer to objects rather than being objects in their own right.
```Python
# Creates a new object and assigned a reference to that object to x
# This is called "binding" in python or "rebinding"
x = 7
# y and x point to the same object. A copy is not performed.
y = x
```
- Objects that are no longer in use, such as when a variable is rebound/reassigned, will be cleaned up by automatic garbage collection.
- Naming is case sensative.

## Numbers
- numeric types and strings are all immutable. So what do operators really do (ex: +=, -=, etc.)?
  - Operators are really syntactic sugar. Actually create a new object an bind it to the variable name.
    ```Python
    # bind object initially
    y = 6
    # rebind with brand new object. The original object will be destroyed.
    y = y + 1
- 3 numeric types: int, long, bool.
  - long is only limited by maximum memory available on the system. 
  - long is slower and should be avoided when possible
  - Python uses the suffix L to signify a long `p = 7L`
- Python division performs truncating division for both kinds of int

## Floats and Decimals
- 3 types of floating-point values: float, Decimal, complex
  - Decimal requires the "decimal" module `import decimal`
    - Accurate to user specified level of precision (default is 28 places)
    - Slower than floats
    - Integer literals can be passed to the Decimal constructor, but because Decimals are high-precision and floats are not, we cannot pass floats. Strings are used instead.
      ```Python
      import decimal
      x = decimal.Decimal("5.1")
      ```
  - floats hold double precision numbers. They have limited precision and cannot be reliably compared for equality
    - Scientific notation is acceptable: `x = 8.9e-4`
  - Complex is built in and doesn't require an import.
    ```Python
    c = 5.4+0.8j
    ```
- Integers get promoted to floats when mixed with a float expression
    
## Namespaces
- Each module automatically has its own namespace.
- You can import a namesapce into the current module to save typing (prevents having to type the module name before every usage), but it is generally frowned upon. 
  ```Python
  from PyQt4.QtCore import *
  # no explicit namespace needed
  x = QString()
  
## Bytestrings, Unicode Strings, and QStrings
- Python has 2 builtin string types:
  - str: holds bytes
  - unicode: holds Unicode characters
- If we only deal with 7-bit ASCII characters, that is, characters in teh range 0-127, and if wwe want to save some memory, we can use `strs`
  - 8-bit characters set requires knowledge of proper encoding
  Modern GUI libraries, including Qt, use Unicode strings, so teh safest route is to use strs for 7-bit ASCII and for raw binary 8-bit bytes, and unicdoe or QString otherwise.
```Python
bird = "Sparrow"
# 'u' specified unicode
beast = u"Unicorn"
type(bird + beast) # unicode
```
- Characters are single length strings. To go to/from a byte value use chr(), unichr(), and ord()
  ```Python
  # beyond ASCII 127 so unicode is needed
  euro = unichr(8364)
  ord(euro) # 8364
  ```
- Since strings are immutable, individual characters cannot be reassigned.
```Python
p = "pad"
p[1] = "0" # WRONG
```
  
## Slicing
- negative numbers start at the end and work backwords
- The slice range is exclusive of the end point.
```Python
phrase = "The red ballooon"
phrase[:3] # The
phrase[-3:] # oon
phrase[4:7] # red
```
