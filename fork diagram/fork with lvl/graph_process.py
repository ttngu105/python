import graphviz
tree = open("process_tree.txt","r")
forktree = tree.read()

dot = graphviz.Graph(name = "process graph", filename = "process_graph", directory = ".", format = "png")
process = forktree.split()
i = 0
while i < len(process):
	child = process[i]
	child_lvl = process[i] + "\nlevel "
	parent = process[i +1]
	parent_lvl = process[i +1] + "\nlevel "

	dot.node(str(child),str(child_lvl))
	dot.node(str(parent),str(parent_lvl))
	dot.edge(str(child),str(parent))
	i = i+2

dot.render(filename = 'process_graph',directory = ".", view=True)