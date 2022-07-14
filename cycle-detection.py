def has_cycle(head):
    
    ## Check to see if list exists in head
    ## If it is NULL, cycle doesn't exist
    if (head == None):
        return 0
    
    ## If cycle might exist
    else:
        node1 = head ## Initial node
        node2 = head.next ## Forward node
        
        ## Continuously loop through list as long as the intial and forward nodes are    not the same
        while (node1 != node2):
            
            ## If forward node is NULL or the subsequent node after forward node is Null, a cycle doesn't exist
            if (node2 == None or node2.next == None):
                return 0
            ## Else, continue traversing both nodes until a cycle is found
            else:
                node1 = node1.next
                node2 = node2.next.next
                
        return 1