
trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}

trunk_config_2 = {
    "FastEthernet0/11": [120, 131],
    "FastEthernet0/15": [111, 130],
    "FastEthernet0/14": [117],
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    trunk_configurate = []
    for port, vlans in intf_vlan_mapping.items():
        trunk_configurate.append(f"interface {port}")
        for command in trunk_template:
            if command.endswith("allowed vlan"):
                vlans_str = ",".join([str(vl) for vl in vlans])
                trunk_configurate.append(f"{command} {vlans_str}")
            else:
                trunk_configurate.append(command)
    return trunk_configurate

config = generate_trunk_config(trunk_config,trunk_mode_template)
print(*config, sep="\n")