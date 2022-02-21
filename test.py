import mat
print("Loading tree...")
t = mat.MATree("public-latest.all.masked.pb.gz")
print("Tree successfully loaded.")
parsimony = t.get_parsimony_score()
print("Parsimony score:", parsimony)
print("Traversing tree...")
nodes = t.depth_first_expansion()
print("{} nodes traversed.".format(len(nodes)))
print("Checking the tenth node...")
testnode = nodes[9]
print("Name:",testnode.get_id())
children = testnode.get_children()
print("{} children.".format(len(children)))
parent = testnode.get_parent()
print("Parent:",parent.get_id())
mutations = testnode.get_mutations()
print("Mutations: ",mutations)
print("Done!")