# random-file-generator
### A handy python app for generating a number of randomly sized files with non-zero bytes.

Sometimes, it can be handy to have some content to test things like backups and restores, to have some files to manipulate or to test apps that manipulate files.

This tool generates a set number of files in a directory of choice, with a range of sizes between `MAZSIZE` and `MINSIZE`.

All flags are optional, except `DIR` which must be set. if the directory does not exist, it will be created.
## Flags:
|Flag|Alt|Description|
|--|--|--|
|-h|--help|Show help message and exit|
|-c|--count|Number of files to create|
|-m|--minsize|Minimum size of each file in MB|
|-x|--maxsize|Maximum size of each file in MB|
|-d|--dir|Directory where files will be created|
## Defaults:
|Flag|Default|Description|
|--|--|--|
|count|1|number of files generated
|minsize|1MB|The minimum size of a file
|mazsize|5MB|The maximum size of a file


