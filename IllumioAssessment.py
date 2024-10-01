import csv
from collections import defaultdict

def load_lookup_table(file_path):
  lookup_table = {}
  with open(file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
      dstport, protocol, tag = row
      lookup_table[(int(dstport), protocol.lower())] = tag
  return lookup_table

def parse_flow_logs(log_file, lookup_table):
  tag_counts = defaultdict(int)
  port_protocol_counts = defaultdict(int)

  with open(log_file, 'r') as file:
    for line in file:
      parts = line.split()
      if len(parts) < 14 or parts[0] != '2':
        continue

      dstport = int(parts[5])
      protocol = 'tcp' if parts[7] == '6' else 'udp'

      tag = lookup_table.get((dstport, protocol), 'Untagged')

      tag_counts[tag] += 1

      port_protocol_counts[(dstport, protocol)] += 1

  return tag_counts, port_protocol_counts

def write_output(tag_counts, port_protocol_counts, tag_output_file, port_protocol_output_file):
  with open(tag_output_file, 'w') as tag_file:
    tag_file.write('Tag,Count\n')
    for tag, count in sorted(tag_counts.items()):
      tag_file.write(f'{tag},{count}\n')

  with open(port_protocol_output_file, 'w') as port_protocol_file:
    port_protocol_file.write('Port,Protocol,Count\n')
    for (port, protocol), count in sorted(port_protocol_counts.items()):
      port_protocol_file.write(f'{port},{protocol},{count}\n')

def main():
  lookup_file = 'lookup_table.csv'
  flow_log_file = 'flow_logs.txt'
  tag_output_file = 'tag_counts.csv'
  port_protocol_output_file = 'port_protocol_counts.csv'


  lookup_table = load_lookup_table(lookup_file)

  tag_counts, port_protocol_counts = parse_flow_logs(flow_log_file, lookup_table)

  write_output(tag_counts, port_protocol_counts, tag_output_file, port_protocol_output_file)


if __name__ == '__main__':
  main()