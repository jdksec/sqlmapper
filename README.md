# sqlmapper

Script to automate authenticated Sqlmap testing.

## Install notes

- Modify the location in the script for sqlmap.py
- Modify the script to add your sqlmap arguments.

## Usage

Run the following:

```
python3 sqlmapper.py
```

Then save your burp requests to the newly created folder called watcher. Use copy to file then it will parse the file and run sqlmap then move the file to completed.

Review log.txt for any injection points.

Saves the request at the top of the log file so you can provide easy evidence.
