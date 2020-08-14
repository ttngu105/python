import graphviz
tree = open("process_tree.txt","r")
forktree = tree.read()
dot = graphviz.Graph(name = "process graph", filename = "process_graph", directory = ".", format = "png")
process = forktree.split()
i = 0
print(len(process))
while i < len(process)-12:
	child = process[i]
	parent = process[i +1]
	dot.node(str(child),str(child))
	dot.edge(str(child),str(parent))
	i = i+2

dot.render(filename = 'process_graph',directory = ".", view=True)