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
