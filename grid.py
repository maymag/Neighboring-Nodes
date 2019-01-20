class NeighboringNodes:
    
    def __init__(self, size, debug):
        self.size = size
        self.debug = debug
    
    def make_grid(self):
        
        '''Method for making and debugging a grid of NeighboringNodes.'''
        
        if type(self.size) is not int or self.size <= 0:
            raise ValueError("Size must be a positive integer.")
            
        else:
            j = []
            h = (self.size*[0])

            for k in range(0,self.size):
                (j.append(h))
            print (j)
            
            #debug
            if self.debug == True: 
                row = 0
                col = 0
                for c,g in enumerate(range(0, self.size**2),0):
                    if (c%self.size) == 0:
                        row+= 1
                        col = 0  
                    x = col
                    y = self.size-row
                    i = c
                    
                    print((x,y,i))
                    col+=1

            
    def get_coordinates (self,index):
        
        '''Method for getting node coordinates based on index in a grid of NeighboringNodes.'''
        
        if type(self.size) is not int or self.size <= 0:
            raise ValueError("Size must be a positive integer.")
            
        else:
            y = self.size -1 - index//self.size
            x = index%self.size
            return ([x,y])
    

    
    def find_neighbors (self, radius, ttype, index=None,center=None):
        
        '''Method for finding neighboring nodes based on radius, shape of neighborhood, and center node index or coordinates.'''
        
        Valid_Type = {'square','cross','diamond'}
        
        if center and index:
            raise ValueError("Use default value for index or center.")
            
        elif not center and not index:
            raise ValueError ("Assign non-zero value to index or center.")
        
        elif type(self.size) is not int or self.size <= 0:
            raise ValueError("Size must be a positive integer.")
        
        elif ttype not in Valid_Type:
            raise ValueError("ttype must be one of %r." % Valid_Type)          
                
        elif type(radius) is not int or radius < 0 or radius > self.size/2:
            raise ValueError('Radius must be a positive integer less than or equal to half of the NeighboringNode size.')
            
        
        #Find neighbors
        
        if index:
        
            center = nodi.get_coordinates(index)
        
        if ttype == 'square':

            row = center[1]
            col = center[0]
            ys =[]
            
                            
            #Each line of the square will have the same sequence of x values
            exes = (radius*2+1)*(list(range(col-radius,col+1+radius)))
                
            #Each line of the square will have the same y value
            for g in range(0, 2*radius+1):
                    
                ycoordinates = (2*radius+1)*[row]
                ys.extend(ycoordinates)
                row-=1
            
            #Quick check to make sure shape is not off-grid.
            if center[0]+radius < self.size and center[1]+radius < self.size and center[0]-radius > 0 and center[1]-radius > 0:

                #Pair up the x and y coordinates
                coordinates = [[i,j] for (i,j) in zip(exes,ys)]
                
            else:
                print ('Shape is partially or entirely off the grid.')
                
                #Pair up the x and y coordinates
                #If shape is off-grid, only return nodes that are not off-grid.
                coordinates = [[i,j] for (i,j) in zip(exes,ys) if i < self.size and j < self.size and i > 0 and j > 0 ]
                
            return coordinates

            
        if ttype == 'cross':
            
            row = center[1]
            col = center[0] 
            
            
            #The vertical line coordinates will have a range of y values and only one x value
            verty = list(range(row-radius, row+1+radius))
            n = len(verty)
            vertx = n*[col]
                
            #The horizontal line coordinates will have a range of x values and only one y value
            #Don't repeat center coordinates
            horix = list(range(col-radius, col+1+radius))
            horiy = n*[row]
            
            #Quick check to make sure shape is not off-grid.
            if center[0]+radius < self.size and center[1]+radius < self.size and center[0]-radius > 0 and center[1]-radius > 0:
                            
                #Pair up the x and y coordinates and add the vertical and horizontal lines
                coordinates = [[i,j]  for (i,j) in zip(vertx,verty)] + [[i,j]  for (i,j) in zip(horix, horiy)]

                coordinates.remove(center)
                
            else:
                
                print ('Shape is partially or entirely off the grid.')
            
                #Pair up the x and y coordinates and add the vertical and horizontal lines.
                #If shape is off-grid, only return nodes that are not off-grid.
                coordinates = [[i,j]  for (i,j) in zip(vertx,verty) if i < self.size and j < self.size and i > 0 and j > 0] + [[i,j]  for (i,j) in zip(horix, horiy) if i < self.size and j < self.size and i > 0 and j > 0]

                coordinates.remove(center)
            
            return coordinates
        
        if ttype == 'diamond':
                
                coordinates=[]
                row = center[1]+radius
                col = center[0]
                
                #Quick check to make sure shape is not off-the-grid
                if center[0]+radius < self.size and center[1]+radius < self.size and center[0]-radius > 0 and center[1]-radius > 0:
                    
                    #Coordinates for top triangle
                    for c,g in enumerate(range(0, (radius+1)),0):
                        exes = list(range(col-c,col+1+c))
                        ys = len(exes)*[row]
                        coordinates.extend([[i,j] for (i,j) in zip(exes,ys)])
                        row-=1
                    
                    #Coordinates for bottom triangle
                    for h in range(0,radius):
                        exes = list(range(col-(len(exes)//2-1) , col + len(exes)//2))
                        ys = len(exes)*[row]
                        coordinates.extend([[i,j] for (i,j) in zip(exes,ys)])
                        row-=1
                    
                else:
                    print('Shape is partially or entirely off the grid.')
                    
                    #Coordinates for top triangle
                    #Remove nodes that are off-the-grid
                    for c,g in enumerate(range(0, (radius+1)),0):
                        exes = list(range(col-c,col+1+c))
                        ys = len(exes)*[row]
                        coordinates.extend([[i,j] for (i,j) in zip(exes,ys) if i < self.size and j < self.size and i > 0 and j > 0])
                        row-=1
                    
                    #Coordinates for bottom triangle
                    #Remove nodes that are off-the-grid
                    for h in range(0,radius):
                        exes = list(range(col-(len(exes)//2-1) , col + len(exes)//2))
                        ys = len(exes)*[row]
                        coordinates.extend([[i,j] for (i,j) in zip(exes,ys) if i < self.size and j < self.size and i > 0 and j > 0])
                        row-=1
                    
                return coordinates
      
if __name__ == "__main__":
  nodi = NeighboringNodes(8,False)
  nodi.make_grid()
  nodi.get_coordinates(1)
  shape_xy = nodi.find_neighbors(2,'diamond', center = [4,4]
  print(shape_xy)
                                 
  
                
