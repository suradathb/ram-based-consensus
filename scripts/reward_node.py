def reward_node(node):
    node['reward'] += 1
    return node

node = {'id': 'node1', 'reward': 0}
rewarded_node = reward_node(node)
print(f"Node {rewarded_node['id']} has {rewarded_node['reward']} rewards")