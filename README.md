# Rename files

Python script to rename all files within the same directory to the name of the folder.

## Getting Started

* Copy the files <br />`git clone 'https://github.com/jhonnyelhelou91/RenameFiles.git' 'C:\git\Python\RenameFiles\'`
* Compile script <br />`python -m py_compile C:\git\Python\RenameFiles\rename_files.py`
* Run script `python C:\git\Python\RenameFiles\rename_files.py`

### Prerequisites

* Python 3+ `https://www.python.org/downloads/`
* Add Python path to environment variable

- - - -

### Examples
<details>
   <summary>Rename files in current directory</summary>
   <p>python 'C:\git\Python\RenameFiles\rename_files.py'</p>
</details>
<details>
   <summary>Rename files in current directory and its subfolder only</summary>
   <p>python 'C:\git\Python\RenameFiles\rename_files.py' 1</p>
</details>
<details>
   <summary>Rename files in current directory with specific depth</summary>
   <p>python 'C:\git\Python\RenameFiles\rename_files.py' 12</p>
</details>
<details>
   <summary>Rename files in current directory recursively</summary>
   <p>python 'C:\git\Python\RenameFiles\rename_files.py' -1</p>
</details>
<details>
   <summary>Rename files in specific directory recursively</summary>
   <p>python 'C:\git\Python\RenameFiles\rename_files.py' -1 'C:\Test\'</p>
</details>
<details>
   <summary>Rename files in specific directories recursively</summary>
   <p>python 'C:\git\Python\RenameFiles\rename_files.py' -1 'C:\Test\' 'C:\Test1\' 'C:\Test2\'</p>
</details>
