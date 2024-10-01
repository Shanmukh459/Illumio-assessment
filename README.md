# Illumio Technical Assessment

## Assumptions

- We only support the default log format, and the log version supported is "2" (as per the example logs).
- The lookup table only contains three columns: dstport, protocol, and tag, and the protocol names are case-insensitive.
- If a flow log record does not match any tag, it is categorized as "Untagged".
- We assume all protocols are specified in the lookup table as either TCP or UDP.
