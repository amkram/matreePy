import mat
import tqdm

print("loading tree")
tree = mat.MATree("public-latest.all.masked.pb.gz")

print("depth first expansion")
dfs = tree.depth_first_expansion()

print("getting closest pairs")
all_closest = []
for node in tqdm.tqdm(dfs):
    if node.is_leaf():
        try:
            print(node.get_id())
            closest = tree.get_closest_samples(node.get_id())
            all_closest.append(closest)
        except:
	        print(node.get_id())
        


print(all_closest[:100])
print('len', len(all_closest))

