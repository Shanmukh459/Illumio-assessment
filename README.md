# Illumio Technical Assessment

## Assumptions

- We only support the default log format, and the log version supported is "2" (as per the example logs).
- The lookup table only contains three columns: dstport, protocol, and tag, and the protocol names are case-insensitive.
- If a flow log record does not match any tag, it is categorized as "Untagged".
- We assume all protocols are specified in the lookup table as either TCP or UDP.

## Steps followed to implement the solution

- Parse the flow log file: Each line in the flow log contains data which includes destination port (dstport) and protocol. These fields are extracted to determine the corresponding tag.
- Parse the lookup table file: This will map combinations of dstport and protocol to a tag.
- Match flow logs to tags: For each log entry, find a matching tag using the lookup table. If no match exists, classify the entry as "Untagged".
- Generate output: The program will generate two output reports:
  - A count of matches for each tag.
  - A count of matches for each unique port/protocol combination.

## Explanation for each function in the source code

- load_lookup_table: This function reads the lookup table CSV and stores it in a dictionary where the key is a tuple (dstport, protocol) and the value is the tag.
- parse_flow_logs: This function reads each flow log, extracts the destination port and protocol, and attempts to find a matching tag from the lookup table. It updates counts for both tags and port/protocol combinations.
- write_output: This function writes two output files:
  - tag_counts.csv: Contains the counts of each tag.
  - port_protocol_counts.csv: Contains the counts of each port/protocol combination.
- Main function: The program coordinates reading the lookup table, parsing the logs, and writing the output files.

## Steps to reproduce

- Clone the git repository or paste the python script in your code editor
- Remove the output files (tag_counts.csv, port_protocol_counts.csv) from the directory
- Place the flow log file (e.g., flow_logs.txt) and lookup table file (e.g., lookup_table.csv) in the same directory as the Python script.
- Run the script: ``` python flow_log_parser.py ````
- The output will be generated in two CSV files:
  - tag_counts.csv
  - port_protocol_counts.csv

## Sample output

#### tag_counts.csv

```
Tag,Count
Untagged,8
email ,3
sv_P1 ,2
sv_P2 ,1
```

#### port_protocol_count.csv

```
Port,Protocol,Count
23,tcp,1
25,tcp,1
80,tcp,1
110,tcp,1
143,tcp,1
443,tcp,1
993,tcp,1
1024,tcp,1
1030,tcp,1
49152,tcp,1
49153,tcp,1
49154,tcp,1
49321,tcp,1
56000,tcp,1
```

Thank you ;)
