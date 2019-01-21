
import argparse 

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
            print ("Grid:{}".format(j))
            
            #debug
            if self.debug == True: 
                print('Debug!')
                row = 0
                col = 0
                for c,g in enumerate(range(0, self.size**2),0):
                    if (c%self.size) == 0:
                        row+= 1
                        col = 0  
                    x = col
                    y = self.size-row
                    i = c
                    
                    print(x,y,i)
                    col+=1

            
    def get_coordinates (self,index):
        
        '''Method for getting node coordinates based on index in a grid of NeighboringNodes.'''
        
        if type(self.size) is not int or self.size <= 0:
            raise ValueError("Size must be a positive integer.")
            
        else:
            y = self.size -1 - index//self.size
            x = index%self.size
            return ([x,y])
    

    
    def find_neighbors (self, radius, ttype, center_idx=None,center=None):
        
        '''Method for finding neighboring nodes based on radius, shape of neighborhood, and center node index or coordinates.'''
        
        Valid_Type = {'square','cross','diamond'}
        
        if center and center_idx:
            raise ValueError("Use default value for either center_idx or center.")
            
        elif not center and not center_idx:
            raise ValueError ("Assign non-zero value to either center_idx or center.")
        
        elif type(self.size) is not int or self.size <= 0:
            raise ValueError("Size must be a positive integer.")
        
        elif ttype not in Valid_Type:
            raise ValueError("ttype must be one of %r." % Valid_Type)          
                
        elif type(radius) is not int or radius < 0 or radius > self.size/2:
            raise ValueError('Radius must be a positive integer less than or equal to half of the grid size.')
            
        
        #Find neighbors
        
        if center_idx:
        
            center = nodi.get_coordinates(center_idx)
        
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
            row = center[1] + radius
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



    parser = argparse.ArgumentParser(description='MyGridStuff')



    requiredNamed = parser.add_argument_group('arguments')
    requiredNamed.add_argument('size', help='grid size is required', type =int)
    requiredNamed.add_argument('shape', help='shape is required')
    requiredNamed.add_argument('radius', help='shape radius is required', type = int)
    requiredNamed.add_argument('index', help='index is required', type = int)
    requiredNamed.add_argument('debug', help='debug is required', type = int)
    requiredNamed.add_argument('-center_idx', help='either shape center index or center coordinates are required but do not assign both', type = int, default = None)
    #requiredNamed.add_argument('-center', help='either shape center index or center coordinates are required but do not assign both', action = 'append',nargs =2, default = None)
    requiredNamed.add_argument('-center', type=int, nargs=2, help='either shape center index or center coordinates are required but do not assign both', default = None)



    args = parser.parse_args()
    #print("size: " + args.size)
    #print("shape: " + args.shape)
    #print("radius: " + args.radius)



    nodi = NeighboringNodes(args.size,args.debug)
    nodi.make_grid()
    idx_xy =nodi.get_coordinates(args.index)
    print ("Coordinates of this node index are {}".format(idx_xy))
    shape_xy = nodi.find_neighbors(args.radius,args.shape, args.center_idx, args.center)
    print("Coordinates of this shape are {}".format(shape_xy))  


                                 
  
                
