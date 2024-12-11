#!/usr/bin/env python3
import sys
import json
import traceback

PRINT_EXCEPTIONS=False

def parseLines (lines, lookup):
    deletedBytes = 0
    modifiedBytes = 0
    renamedBytes = 0

    changedBytes = 0

    for l in lines:
        record = l.split('\t')
        time = record[0]
        operation = record[1]
        inodeType = record[2]
        inode = record[3].replace('\n', '')

        try:
            if operation == '+':
                continue
            sizeOfFile = lookup[inode]
            changedBytes += sizeOfFile
            if operation == '-':
                deletedBytes += sizeOfFile

            if operation == 'M':
                modifiedBytes += sizeOfFile
            
            if operation == 'R':
                renamedBytes += sizeOfFile

        except KeyError:
            pass # Probably a new file - not part of the dataset
            if PRINT_EXCEPTIONS:
                traceback.print_exc()

    #print('changed [MB]:')
    #print(changedBytes / 1024 / 1024)
    #print('\n')
    #print('deleted [MB]')
    #print(deletedBytes / 1024 / 1024)
    #print('renamed [MB]')
    #print(renamedBytes / 1024 / 1024)
    #print('modifiedbytes [MB]')
    #print(modifiedBytes / 1024 / 1024)

    #print('\nCSV:')
    #print('name, changed, deleted, renamed, modified')
    print(sys.argv[1] + "," + str(changedBytes) + "," + str(deletedBytes) + "," + str(renamedBytes) + "," + str(modifiedBytes))



def main():
    with open('./fileLookup.json') as lookupfile:
        lookup = json.load(lookupfile)

        with open(sys.argv[1]) as diff:
            lines = diff.readlines()
            parseLines(lines, lookup)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('No diff supplied')
        exit(1)
    main()
