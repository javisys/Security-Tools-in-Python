#Javi_16018 - 22/12/2022
import iptc

# Create a new rule table
table = iptc.Table(iptc.Table.FILTER)

# Create a rule to block ping
rule = iptc.Rule()
rule.protocol = "icmp"
rule.target = iptc.Target(rule, "DROP")
table.append_rule(rule)

# Create a rule to block the RDP protocol
rule = iptc.Rule()
rule.protocol = "tcp"
rule.dport = 3389
rule.target = iptc.Target(rule, "DROP")
table.append_rule(rule)

# Add rule to allow TCP traffic from subnet 192.168.1.0/24 to subnet 192.168.2.0/24 on port 80, in this case. On these lines you can modify what is convenient for you.
rule = iptc.Rule()
rule.src = "192.168.1.0/24"
rule.dst = "192.168.2.0/24"
rule.protocol = "tcp"
rule.dport = 80
rule.target = iptc.Target(rule, "ACCEPT")
table.append_rule(rule)

table.commit()


