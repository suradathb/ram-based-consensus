def select_validator(nodes, last_transacted_node):
    max_ram = 0
    selected_node = None
    for node in nodes:
        if node['id'] != last_transacted_node:
            ram = int(node['ram'])
            if ram > max_ram:
                max_ram = ram
                selected_node = node
    return selected_node

nodes = [{'id': 'node1', 'ram': '4096'}, {'id': 'node2', 'ram': '8192'}, {'id': 'node3', 'ram': '2048'}]
last_transacted_node = 'node1'
validator = select_validator(nodes, last_transacted_node)
print(f"Selected validator: {validator['id']}")