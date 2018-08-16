def make_edge_list(adjacency):
    """ this function create an edge list representation of a graph using the supplied adjacency matrix
    """
    # Maybe start with an empty edge_list
    edge_list_1 = ['A', 'B', 'C', 'D']
    edge_list = []
    
    # Insert code here
   
    #edge_list_2 = [for sub_lst in ]
    sub_lst = 0

    i = 0 
    for sub_lst in adjacency:
        #print sub_lst
        
        while i < len(sub_lst):
            j = i
    
            if sub_lst[i] == 1:
    
                edge_list.append(edge_list_1[j])
                j +=1 
                #print(edge_list_2)
                i += 1
            else:
        
                i += 1
                j += 1     
        
    
    return edge_list

print(make_edge_list([[0,1], [1,0]]))
#print(make_edge_list([1, 0]))
