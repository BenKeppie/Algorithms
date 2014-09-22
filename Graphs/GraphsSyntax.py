import networkx as nx

if __name__=="__main__":
    test=nx.Graph()
    test.add_node("Matt")
    test.add_node("Ben")
    test.add_edge("Matt","Ben")
    test.neighbors("Matt")
    test.degree("Ben")

    test.add_edge("Matt","Ben", data={"film":"x-men"})
