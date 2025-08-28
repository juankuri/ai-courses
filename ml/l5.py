#=====1=====
candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
# Write loop to find the ideal tree size from candidate_max_leaf_nodes
results = []
for n in candidate_max_leaf_nodes:
    results.append(get_mae(n, train_X, val_X, train_y, val_y))

# Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
best_tree_size = candidate_max_leaf_nodes[results.index(min(results))]

# Check your answer
step_1.check()
