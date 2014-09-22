import networkx as nx

if __name__=="__main__":
    hollywood_graph=nx.Graph()
    hollywood_graph.add_edge("Kevin Bacon", "Michael Fassbender", data={"film":"X-Men: First Class"} )
    hollywood_graph.add_edge("Kevin Bacon", "Lasco Atkins", data={"film":"X-Men: First Class"})
    hollywood_graph.add_edge("Kevin Bacon","Scott Cann",data={"film":"Novacaine"})
    hollywood_graph.add_edge("Kevin Bacon", "James McAvoy",data={"film":"X-Men: First Class"})
    hollywood_graph.add_edge("Kevin Bacon","Richard Frice",data={"film":"Planes, Trains and Automobiles"})
    hollywood_graph.add_edge("Kevin Bacon","David Crow",data={"film":"X-Men: First Class"})


    hollywood_graph.add_edge("Scott Cann", "Vicent Cassel",data={"film":"Ocean's Thirteen"})
    
    hollywood_graph.add_edge("Vicent Cassel", "James McAvoy",data={"film":"Trance"})
    
    hollywood_graph.add_edge("James McAvoy", "Rasario Dawson",data={"film":"Trance"})
    
    hollywood_graph.add_edge("Rasario Dawson", "Richard Frice", data={"film":"Unstoppable"})
    
    hollywood_graph.add_edge("David Crow", "Idris Elba",data={"film":"Buffalo Soldiers"})
    
    hollywood_graph.add_edge("Michael Fassbender", "Idris Elba",data={"film":"Prometheus"})
    hollywood_graph.add_edge("Michael Fassbender", "Noomi Rapace",data={"film":"Prometheus"})

    hollywood_graph.add_edge("Noomi Rapace", "Lasco Atkins",data={"film":"Sherlock Holmes: A Game of Shadows"})

    print(nx.neighbors(hollywood_graph,"Kevin Bacon"))
    print(nx.degree(hollywood_graph,"Kevin Bacon"))
                             
                             
