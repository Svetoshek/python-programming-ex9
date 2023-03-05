
access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10,
                 "FastEthernet0/14": 11,
                 "FastEthernet0/16": 17}

def generate_access_config(intf_vlan_mapping, access_template, psecurity=None):
    access_configure = []

    for intf, vlan in intf_vlan_mapping.items():
        access_configure.append(f"interface {intf}")
        for command in access_template:
            if command.endswith("access vlan"):
                access_configure.append(f"{command} {vlan}")
            else:
                access_configure.append(command)
        if psecurity:
            access_configure.extend(psecurity)
    return access_configure
config = generate_access_config(access_config,access_mode_template)
print(*config, sep="\n")