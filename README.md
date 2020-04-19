# ZSC 

This is an experimental python to zscript transpiler. 

At this point in its evolution the goal is to speed the rough in of a conplex zscript, not to allow the complete 
replacement of ZScripting with python.  The ZScript language is a very narrow subset of python, and implementing 
a lot of core python concepts in ZScrtipt would be a major undertaking. This project is aimed at the more modest 
goal of quickly building up a Zscript with cleaner syntax and more predictable behaviors.


# IMPORTANT NOTE
## Active development in this repo is now happening here: https://github.com/techartorg/zsc


## Usage

```
py zsc.py <path_to_python file>
```

The first argument is always the path to a python file.  The output will be written to a file in the same location with the extension changed from `.py` to `.txt`

If the optional `--output`  argument is supplied, the file will be written to that path instead.

If the optional `--show` flag is supplied, the transpiled file will be printed to stdout


