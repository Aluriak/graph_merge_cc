graph("net1").
graph("net2").

node("A","net1").
node("B","net1").
node("C","net1").
node("D","net1").
node("E","net1").
node("G","net1").

node("A","net2").
node("B","net2").
node("C","net2").
node("E","net2").
node("F","net2").
node("G","net2").

edge("A","B","net1").
edge("B","C","net1").
edge("C","D","net1").
edge("C","E","net1").
edge("D","G","net1").
edge("G","E","net1").

edge("A","B","net2").
edge("B","C","net2").
edge("C","E","net2").
edge("C","F","net2").
edge("F","G","net2").

align("A","net1","A","net2").
align("B","net1","B","net2").
align("C","net1","C","net2").
align("E","net1","E","net2").
align("G","net1","G","net2").
