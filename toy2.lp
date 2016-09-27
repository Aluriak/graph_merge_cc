graph("net1").
graph("net2").

node("A","net1").
node("B","net1").
node("C","net1").
node("D","net1").
node("E","net1").
node("G","net1").

node("a","net2").
node("b","net2").
node("c","net2").
node("e","net2").
node("f","net2").
node("g","net2").

edge("A","B","net1").
edge("B","C","net1").
edge("C","D","net1").
edge("C","E","net1").
edge("D","G","net1").
edge("G","E","net1").

edge("a","b","net2").
edge("b","c","net2").
edge("c","e","net2").
edge("c","f","net2").
edge("f","g","net2").

align("A","net1","a","net2").
align("B","net1","b","net2").
align("C","net1","c","net2").
align("E","net1","e","net2").
align("G","net1","g","net2").
