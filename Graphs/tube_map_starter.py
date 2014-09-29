import networkx as nx
import matplotlib.pyplot as plt
import numpy
import csv

class TubeMap:
    def __init__(self,file_name):
        self.map=nx.Graph()
        self.file_name=file_name
        print(self.map)

    def get_stations(self):
        
        with open(self.file_name, mode = "r", encoding="utf-8") as stations:
            reader=csv.reader(stations)
            for line in reader:
                data={"Line":line[0], "Edge Colour":line[1]}
                self.map.add_path(line[2:])
                print(self.map.edges())
                print(self.map.get_edge_data())
                
                
                
            
                  

    def generate_edge_colours(self,current_map):
        return edge_colours

    def create_graph_plot(self,current_map):
        pass

    def display_full_map(self):
        pass

    def display_travel_map(self,start,end):
        pass

    def get_directions(self,start,end):
        return directions

if __name__ == "__main__":
    Map=TubeMap("tube.csv")
    Map.get_stations()
