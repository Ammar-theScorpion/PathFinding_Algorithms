import pygame

WIDTH = 800
ROWS = 50
FILE= 0
WIN = pygame.display.set_mode( (900,WIDTH))
pygame.display.set_caption("AlGo!")
pygame.init()

#AlGo 
WhatAlGo = 1
#AlGo

 

# Colors Code
WIHIE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
START = (123, 100, 101)
END = (10, 50, 190)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


#PriorityQueue
class Priorityqueue:
     def __init__(self):
          self.q = []
     def put ( self,value,item):
          self.q.append(value)
          self.q.append(item)
     def pop(self):
          min = 0
          l =len(self.q )
          for i in range(l):
               if i%2==0: 

                    if self.q [i] < self.q [min]: 
                        min = i 
               i=i+2 
          send = self.q[min+1]
          del self.q[min]
          del self.q[min ]

          return send

     def p(self):
          for i in range(3):
               print(self.q[i])  

     def get(self):
         return self.q[0] 
            
     def empty(self):
         return len(self.q)==0  

# Class Spot
class spot(object):
    def __init__(self, current_row, current_col, width,  ROWS  ):
        self.color = WIHIE
        self.current_row=current_row
        self.current_col = current_col
        self.x = current_row*width
        self.y = current_col*width
        self.ROWS = ROWS
        self.width = width
        self.neighbors=[]
        self.pointer = None

    def get_row_col_pos(self):
        return self.current_row , self.current_col 

    def get_pos(self):
        return self.x,self.y

    def get_color(self):
        return self.color
    def is_checked(self):
        return self.color == RED
    def is_bairrer(self):
        return self.color == BLACK
    def is_ok(self):
        return self.color == WIHIE
    def reset(self):
        self.color = WIHIE
    def repointer(self):
        return self.pointer.current_row, self.pointer.current_col    
    #startnode
    def is_start(self):
        return self.color == START
    # endnode    
    def is_end(self):
        return self.color == END
    #set
    def make_bairrer(self):
        self.color = BLACK
    def make_checked(self):
        self.color = RED
    def make_end(self):
        self.color = END
    def make_start(self):
        self.color = START    
    def make_path(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.width))
    def get_path(self):
        self.color = (140,6,180)  
    def getr(self):
        return self.current_row 
    def getc(self):
        return self.current_col   
    def make_begin(self):
        self.color = GREEN      
    def make_pointer(self,point):
        self.pointer = point


    ####### Up-date 
    ##SCANING THE MAZE##
    def Update_neighbors(self, grid):
        #FB in search space
        self.neighbors = []

        if self.current_col>0 and not grid[self.current_row][self.current_col-1].is_bairrer() :   
            self.neighbors.append(grid[self.current_row][self.current_col-1])
            
        if self.current_row < self.ROWS - 1 and not grid[self.current_row  + 1][self.current_col ].is_bairrer()  :

            self.neighbors.append(grid[self.current_row+1][self.current_col]) 

        if self.current_col< self.ROWS-1 and not grid[self.current_row][self.current_col+1].is_bairrer():

            self.neighbors.append(grid[self.current_row ][self.current_col+1 ])    

        if self.current_row >0 and not grid [self.current_row -1][self.current_col].is_bairrer() :
             self.neighbors.append(grid[self.current_row -1][self.current_col])

#############
#GUI
def draw_path(came_from):
    for i in came_from:
        i.get_path()
        i.make_path()
        pygame.display.update()
#GETTING ALL VAILD NEIGHBORS
def Gerenal_F_A(grid):
    for row in grid:
        for spot in row:
            spot.Update_neighbors(grid)
    return grid   
#REVERSE A LIST
def reverse(came):
    size = len(came)-1 
    ra = 0
    if size == 1:
        ra = size
    else:
        ra = int(size/2)       
    for j in range(ra):
        b =came[j] 
        came[j] = came[size]
        came[size] = b
        size-=1
        j+=1
def short_path(clos,w, start, grid):
    reverse(clos)
    came1 = []
    d=0
    D=0
    i = clos[0]
    while D != w:
        D+=1
        if i.pointer !=None:
            d+=1
            came1.append(i)
            i = i.pointer
    reverse(came1)       
    for i in came1:
        i.get_path()
        i.make_path()
        draw (grid,int(  ROWS))
        draw_grids( int (ROWS), int (  WIDTH), int(WIDTH)//int(ROWS))
        pygame.display.update()  
        print("col,row",i.get_row_col_pos(),"y,x",i.get_pos())

    return d






def draw_f_path(start,end,came_from, grid):
    came=[]
    d=0
    e= end
     
    while end in came_from:
        
        came.append(  came_from[end])
        end = came_from[end]
        d+=1
        
    reverse(came)    
    for i  in came:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return True


         
        print("row,col",i.get_row_col_pos(),"y,x",i.get_pos())
        i.get_path()
        i.make_path()
        d+=1
        


        draw (grid,int(  ROWS))
        draw_grids( int (ROWS), int (  WIDTH), int(WIDTH)//int(ROWS))
        pygame.display.update()  

    return d
#REPEATED STATES    
def notIn(nei,open):
    for i in (range(len(open))) :
        if nei == open[i]:
            return False 
    return True      

def Pop(open,size):
    newOpen = []
    j =  len(open) 
    j -= 1
    size-=1 
     
    for i in range(j) :
        newOpen.append(  open[i+1])
    return newOpen, size    
 
def last_index(closed, size):
    return closed[size]
#BREADTH
def Breadth(start, end, grid):
    grid = Gerenal_F_A(grid)
    open =   []
    size = 1
    c_size=-1
    closed = []
    open.append(start)
    current = open[0]
    t= False
    w=0
    number_expand=0
    while  open:
 
        #closing the game while playing
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return True
                pygame.quit( )
                
        #it cannot be true (end = start)
        #
        if current == end:
            return True

        #from open to closed, pop open
        closed.append(open[0])

        c_size+=1
        open,size = Pop(open,size) 

        if not t:
            number_expand+=1 

        current = closed[-1]
        if t : 
            number_expand+=1

            last_index(closed,c_size-1).make_checked()
        t = True 
        closed[-1].make_path()

        for nei in current.neighbors:
            if notIn(nei, open) and  notIn(nei,closed):
                
                nei.make_pointer(current)
                open.append(nei)
                size+=1
                nei.make_begin( )
                
            # end point = current
            if nei.get_pos() == end.get_pos(): 

                print("col,row",start.get_row_col_pos(),"y,x",start.get_pos())
                d=short_path(closed, c_size+1 ,  start, grid)
                print("col,row",end.get_row_col_pos(),"y,x",end.get_pos())

                end.make_end()
                start.make_start()
                print("Breath-first Search guarantees the shortest path!")
                print("Number Of Expansion Nodes is",number_expand)
                print("Time and space complexiy are O(b^d); b: Branching factor, d: The Depth, so in this example b is",3 ," ,and d is:",d+1,"==",3**(d+1))
                return True
                
        draw (grid,int(  ROWS))
        draw_grids( int (ROWS), int (  WIDTH), int(WIDTH)//int(ROWS))
        pygame.display.update()       
          
#DEPTH
def Depth(start, end, grid):
    grid = Gerenal_F_A(grid)
    open =   []
    closed = []
    c_size=-1
    i = 0
    open.append(start)
    current = open[0]
    t= False
    number_expand =0
    size = 0
    while open:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return True

        #open to closed
        closed.append(open[0])
        open,size = Pop(open,size) 

        c_size+=1      

        last_index(closed,c_size) .make_begin()  
        if not t:
            number_expand+=1

        if t : 
            number_expand+=1

            last_index (closed,c_size-1) .make_checked()
        t = True       
        last_index(  closed,c_size).make_path()
        current = last_index(closed,c_size) 


        for nei in current.neighbors:
            if notIn(nei, closed ):
                nei.make_pointer(current)
               
                open.insert(i, nei)  
                i+= 1
        if current == end:
            cl =True
            d=0
            print("col,row",start.get_row_col_pos(),"y,x",start.get_pos())
            short_path(closed,c_size+1, start, grid)
            print("col,row",end.get_row_col_pos(),"y,x",end.get_pos())
            row, col = start.get_row_col_pos()
            row1, col1 = end.get_row_col_pos()
            x = abs(row - row1 )
            y = abs(col - col1 ) 
            end.make_end()
            start.make_start()
            d = x + y   
            print("Depth-first Search is unweighted and does not guarantee the shortest path!")

            print("Number Of Expansion Nodes is ",number_expand)

            print("Time and space complexiy are O(b^d); b: Branching factor, d: The Depth, so in this example b is ",3 ," ,and d is: ",d,"== ",3**d)


            return True
        i=0        

        draw (grid,int(  ROWS))
        draw_grids( int (ROWS), int (  WIDTH), int(WIDTH)//int(ROWS))
        pygame.display.update()      

def h_path(current, end):
    row, col = current.get_row_col_pos()
    row1, col1 = end.get_row_col_pos()
    x = abs(row - row1 )
    y = abs(col - col1 ) 
    h = x + y
    return h 
          

#       best
def Best(start, end, grid):
    grid =Gerenal_F_A(grid)
    q = Priorityqueue()
    h = h_path(start, end)
    c_size=-1
    q.put( h, start)
    s_open = []
    s_open.append(start)
    closed = []
    came_from = {}
    t = False
    number_expand =0

    
    while not q.empty():
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return True
        c_size+=1       
        closed.append ( q.pop())
        current = last_index(closed,c_size)
        if current == end:

            print("col,row",start.get_row_col_pos(),"y,x",start.get_pos())
            d=short_path(closed,c_size+1, start, grid)
            print("col,row",end.get_row_col_pos(),"y,x",end.get_pos())

            print("Greedy Best-first Search does not guarantee the shortest path!")
            print("manhattan distance depends only on the distance between the inital point and the end point")
            print("Number Of Expansion Nodes is",number_expand)
            print("Time and space complexiy are O(b^d); b: Branching factor, d: The Depth, so in this example b is",3 ," ,and d is:",  d, "==",3**d )

            end.make_end()
            start.make_start()
            return True
        last_index(closed,c_size).make_begin()  
        if not t:
            number_expand +=1

        if t : 
            number_expand +=1

            last_index(closed,c_size).make_checked()
        t = True       
        last_index(closed,c_size).make_path()
 
        for nei in current.neighbors:

            if  notIn(nei, s_open):
                nei.make_pointer(current)
                
                s_open.append(nei)

                h = h_path(nei, end)
                q.put( h, nei )
                s_open[-1].make_begin()
        draw (grid,int(  ROWS))
        draw_grids( int (ROWS), int (  WIDTH), int(WIDTH)//int(ROWS))
        pygame.display.update()  
#A*        
def Astart(start, end, grid):

    grid = Gerenal_F_A(grid)
    q = Priorityqueue()
    s_open = []
    s_open.append(start)
    closed = []
    t = False
    number_expand =0
    c_size=-1
    g_score = {spot:float("inf") for r in grid for spot in r}
    
    f_score = {spot:float("inf") for r in grid for c in r}
    g_score[start]=0
    f_score[start]=h_path(start,end)
    count = 0
    h=h_path(start, end)
    q.put( f_score[start] ,start) 

    while not q.empty():

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return True
        c_size+=1        
        closed.append ( q.pop())
        current=  last_index( closed, c_size )  
        if current == end:
            print("col,row",start.get_row_col_pos(),"y,x",start.get_pos())
            d=short_path(closed,c_size+1, start, grid)
            print("col,row",end.get_row_col_pos(),"y,x",end.get_pos())
 
            print("A* Search guarantees the shortest path!")
            print("manhattan distance depends on the distance between the inital and the end point; h(), and on the distance between the inital point and current point; g()" )
            print("Number Of Expansion Nodes is",number_expand)
            print("Time and space complexiy are O(b^d); b: Branching factor, d: The Depth, so in this example b is",3 ," ,and d is:", d ,"==",3**d )
            end.make_end()
            start.make_start()

            return True
        last_index(closed,c_size) .make_begin() 
        if not t:
            number_expand+=1

        if t : 
            number_expand+=1

            last_index(closed,c_size) .make_checked()
        t = True       
        last_index(  closed,c_size).make_path()
 
        for nei in current.neighbors:
            t_g =g_score[current]+1
            if t_g < g_score[nei]:

                g_score[nei] = t_g
                h = h_path(nei, end)
                f_score[nei] = g_score[nei] + h
                if notIn(nei, s_open):
                    nei.make_pointer(current)


                    count+=1
                    q.put (f_score[nei] , nei  )
                    s_open.append(nei)
                    s_open[-1].make_begin()
                    
        draw (grid,int(  ROWS))
        draw_grids( int (ROWS), int (  WIDTH), int(WIDTH)//int(ROWS))
        pygame.display.update()  

 # hill
def hill(start, end, grid):
    grid = Gerenal_F_A(grid)
    s_open = []
    s_open.append(start)
    closed = []
    c_size=-1
    q = Priorityqueue()
    number_expand=0
    Not = True
    t = False
    g_score = {spot:float("inf") for r in grid for spot in r}
    
    f_score = {spot:float("inf") for r in grid for c in r}
    g_score[start]=0
    f_score[start]=h_path(start,end)
    count = 0
    h=h_path(start, end)
    q.put (f_score[start] , start) 

    take_f = float("inf")
    while not q.empty():

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                return True
        c_size+=1        
        closed.append ( q.pop())
        current=  last_index( closed, c_size )  
        if current.get_pos() == end.get_pos():
            print("col,row",start.get_row_col_pos(),"y,x",start.get_pos())
            d=short_path(closed,c_size+1, start, grid)
            print("col,row",end.get_row_col_pos(),"y,x",end.get_pos())    
            end.make_end()
            start.make_start()
            print("Number Of Expansion Nodes is",number_expand)

            print("Time and space complexiy are O(b^d); b: Branching factor, d: The Depth, so in this example b is",3 ," ,and d is:", d ,"==",3**d )
 
            return True
        last_index(closed,c_size) .make_begin()  
        if not t:
            number_expand+=1

        if t : 
            number_expand+=1
            last_index(closed,c_size-1) .make_checked()
        t = True
        last_index(closed,c_size).make_path()
 
        for nei in current.neighbors:
            t_g =g_score[current]+1
            g_score[nei] = t_g
            h = h_path(nei, end)

            s_open[-1].make_begin()
            if take_f>h:
                take_f = h
                take_nei = nei
                Not = True

                nei.make_pointer(current)
        if not Not:
            print("Cannot find the shortest path ")  
            return False    
        Not = False
        if notIn(take_f, s_open) :

            count+=1

            q.put( take_f , take_nei  )
            s_open.append(take_nei)
                      
        draw (grid,int(  ROWS))
        draw_grids( int (ROWS), int (  WIDTH), int(WIDTH)//int(ROWS))
        pygame.display.update()
    return False

 
def store_data(ROWS, gap, width):
    grid = []
    for i in range(ROWS):
        grid.append([])
        for j in range(ROWS):
            s=spot(i, j,gap,ROWS    )
            grid[i].append(s)
    return grid        


#Making grids
def draw_grids(  ROWS , width,  gap) :
    
    for i in range  (ROWS) :
        pygame.draw.line(WIN, (135, 135, 135),(0, i*gap),(width,i*gap))
        for j in range(  ROWS) :
         
            pygame.draw.line(WIN, (135, 135, 135),(j*gap,0), (j*gap,width))

def draw(grid,  ROWS ):
    for i in grid :
        for j in i :
            j.make_path()
 # GAME
def game(WIN,first, Fi, grid):

    #start
    start = None 
    #end
    end = None
    #####
    isPressed = False
    s= False
    E = False
    gap = round(int(WIDTH)//int(ROWS))
    run = True
    while run:
        WIN.fill(WIHIE)
        draw(grid,int(ROWS))
        
        if FILE:
            if not start and  not s:

                y,x=first

                y=int(y)
                x=int(x)
                row = y//gap
                col = x//gap
                Sp = grid[row][col]
                start=Sp 
                start.make_start() 
            if not end and not E:
                y,x=Fi
                y=int(y)
                x=int(x)
                row = y//gap
                col = x//gap
                Sp = grid[row][col]
                end=Sp 
                end.make_end() 

        for e in pygame.event.get():
            if e.type == pygame.QUIT: 
                run=False
            if  pygame.mouse.get_pressed()[0]:

                pos =  pygame.mouse.get_pos()
                y, x = pos
                row = y//gap
                col = x//gap
	           
                Sp = grid[row][col]

                if not start and Sp!=end  :

                    start=Sp 
                    start.make_start() 


                elif not end and Sp!=start:
                    end=Sp
                    end.make_end()  
                elif Sp == start:
                    s = True
                    start.reset()
                    start = None    
                elif Sp == end:
                    E=True
                    end.reset()
                    end =None       
                elif Sp != end and Sp != start :

                    Sp.make_bairrer()

            if pygame.mouse.get_pressed()[2]:
                pos =  pygame.mouse.get_pos()
                y, x = pos
                row = y//gap
                col = x//gap
                Sp = grid[row][col]  
                if Sp.is_bairrer()  :

                    Sp.reset()


            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE and start and end:
                    if WhatAlGo == 1:
                        Breadth(start, end ,grid  ) 
                    if WhatAlGo == 2:
                        Depth(start, end ,grid  ) 
                    if WhatAlGo == 3:
                        Best(start, end ,grid  ) 
                    if WhatAlGo == 4:
                        Astart(start, end ,grid  )
                    if WhatAlGo == 5:
                        hill(start, end ,grid  )
                if e.key == pygame.K_c:
                    E =True
                    s=True
                    start=None
                    end=None
                    grid = store_data(int(ROWS), int(WIDTH ) // int(ROWS), int(WIDTH) )

                    WIN.fill(WIHIE)
                    draw_grids( int(ROWS) ,  int(WIDTH),  int(WIDTH) //int(  ROWS) )
        draw_grids( int(ROWS) ,  int(WIDTH),round(  int(WIDTH) //   int(ROWS))) 
        pygame.display.update()        

def render_instructions(WIN):
    rrun = True
    while rrun:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                rrun=0
        WIN.fill((WIHIE))
        font = pygame.font.Font("freesansbold.ttf", 20) 
        text=font.render('How To Play!', True, BLACK) 
        font = pygame.font.Font("freesansbold.ttf", 15) 

        text2=font.render("When You Press The 'Play!' Button You Will See A Map With A Number Of Rows As You Specified Before.", True, BLACK) 
        text3=font.render("Pick A Search Type By Selecting One in the 'Algorithm' Button.", True, BLACK) 

        text4=font.render("Use Your Mouse To Make Grids, And To Indicate The Start And The End Point.", True,  BLACK) 
        text5=font.render("When You Finish Press 'Space'. To Clear The Bored Press 'C'", True,  BLACK) 
        text6=font.render("About Colors:", True,  BLACK) 
        text7=font.render("red:Spots Already Visited.", True,  BLACK) 
        text8=font.render("green: Spots Were About To Be Visited (but they increase the distance).", True,  BLACK) 
        text9=font.render("Last color: In some Algorithms means the shortest distance.", True,  BLACK) 
        text10=font.render("Left Click Or Right Click To Remove The Bairres Or The Start And The End Point.", True,  BLACK) 

        textRect = text.get_rect() 
        textRect2 = text2.get_rect() 
        textRect3 = text3.get_rect() 
        textRect4 = text4.get_rect()
        textRect5 = text5.get_rect()
        textRect6 = text6.get_rect()
        textRect7 = text7.get_rect()
        textRect8 = text8.get_rect()
        textRect9 = text9.get_rect()
        textRect10 = text10.get_rect()

        textRect.center = (int(WIDTH)/2 + 70 , 20)
        textRect2.center = (380 , 80)
        textRect3.center = (240 , 110)
        textRect4.center = (285 , 130)
        textRect5.center = (220 , 160)
        textRect6.center = (100 , 190)
        textRect7.center = (100 , 220)
        textRect8.center = (260 , 240)
        textRect9.center = (215 , 260)
        textRect10.center = (295 , 290)

        WIN.blit(text, textRect) 
        WIN.blit(text2, textRect2) 
        WIN.blit(text3, textRect3) 
        WIN.blit(text4, textRect4) 
        WIN.blit(text5, textRect5) 
        WIN.blit(text6, textRect6) 
        WIN.blit(text7, textRect7) 
        WIN.blit(text8, textRect8) 
        WIN.blit(text9, textRect9) 
        WIN.blit(text10, textRect10) 

        pygame.display.update()
def pick_AlGo(WIN):
    menu_run = 1
    while menu_run:

        WIN.fill((10, 20, 40)) 
        x,y = pygame.mouse.get_pos()
        font = pygame.font.Font("freesansbold.ttf", 20) 
        text=font.render('Breadth First', True, GREEN, BLUE) 
        text2=font.render('Depth First', True, GREEN, BLUE) 
        text3=font.render('Best First', True, GREEN, BLUE) 
        text4=font.render('A*', True, GREEN, BLUE) 
        text5=font.render('Hill Climbing', True, GREEN, BLUE) 

        textRect = text.get_rect() 
        textRect2 = text2.get_rect() 
        textRect3 = text3.get_rect() 
        textRect4 = text4.get_rect() 
        textRect5 = text5.get_rect() 

        textRect.center = (int(WIDTH)/2 + 70 , 220)
        textRect2.center = (int(WIDTH)/2 + 70 , 320)
        textRect3.center = (int(WIDTH)/2 + 80 , 420)
        textRect4.center = (int(WIDTH)/2 + 80 , 520)
        textRect5.center = (int(WIDTH)/2 + 80 , 620)
      
        Breadth = pygame.Rect(int(WIDTH)/2, 200, 150, 50)
        Depth = pygame.Rect(int(WIDTH)/2, 300, 150, 50)
        Best = pygame.Rect(int(WIDTH)/2, 400, 150, 50)
        Astart = pygame.Rect(int(WIDTH)/2, 500, 150, 50)
        hill = pygame.Rect(int(WIDTH)/2, 600, 150, 50)

        pygame.draw.rect(WIN, (135, 135, 135),Breadth )
        pygame.draw.rect(WIN, (135, 135, 135),Depth )
        pygame.draw.rect(WIN, (135, 135, 135),Best )
        pygame.draw.rect(WIN, (135, 135, 135),Astart )
        pygame.draw.rect(WIN, (135, 135, 135),hill )
 
        WIN.blit(text, textRect) 
        WIN.blit(text2, textRect2) 
        WIN.blit(text3, textRect3) 
        WIN.blit(text4, textRect4) 
        WIN.blit(text5, textRect5) 
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                menu_run=0
            if pygame.mouse.get_pressed()[0]:

                global WhatAlGo
                if Breadth.collidepoint((x, y)):
                    WhatAlGo = 1
                    menu_run=0

                if Depth.collidepoint((x,y)):
                    WhatAlGo = 2   
                    menu_run=0

                if Best.collidepoint((x,y)):
                    WhatAlGo = 3  
                    menu_run=0

                if Astart.collidepoint((x,y)):
                    WhatAlGo = 4 
                    menu_run=0
                if hill.collidepoint((x,y)):
                    WhatAlGo = 5 
                    menu_run=0

        pygame.display.update ()


# MENU
 
def MENU(WIN, first,Fi, grid):
    menu_run=1
    while menu_run:

        WIN.fill((10, 20, 40)) 
        x,y = pygame.mouse.get_pos()
        font = pygame.font.Font(None, 30) 
        text0=font.render('READ THE INSTRUCTIONS FIRST!', True, RED, BLUE) 
        text00=font.render('(Press c to Clear!', True, RED, BLUE) 
        text=font.render('Play!', True, GREEN, BLUE) 
        text2=font.render('Instructions', True, GREEN, BLUE) 
        text3=font.render('Algorithms', True, GREEN, BLUE) 

        textRect00 = text.get_rect() 
        textRect0 = text.get_rect() 
        textRect = text.get_rect() 
        textRect2 = text2.get_rect() 
        textRect3 = text2.get_rect() 

        textRect00.center = (int(WIDTH)/2-50 , int(WIDTH)/2-250)
        textRect0.center = (int(WIDTH)/2-50 , int(WIDTH)/2-200)
        textRect.center = (int(WIDTH)/2 + 70 , int(WIDTH)/2 -130)
        textRect2.center = (int(WIDTH)/2 + 70 , int(WIDTH)/2 +20)
        textRect3.center = (int(WIDTH)/2 + 80 , int(WIDTH)/2 +170)
      
        buttonGame = pygame.Rect(int(WIDTH)/2,int(WIDTH)/2 -150, 150, 50)
        buttonInfo = pygame.Rect(int(WIDTH)/2, int(WIDTH)/2, 150, 50)
        buttonAlGo = pygame.Rect(int(WIDTH)/2, int(WIDTH)/2 +150, 150, 50)

        pygame.draw.rect(WIN, (135, 135, 135),buttonGame )
        pygame.draw.rect(WIN, (135, 135, 135),buttonInfo )
        pygame.draw.rect(WIN, (135, 135, 135),buttonAlGo )
 
        WIN.blit(text0, textRect0) 
        WIN.blit(text00, textRect00) 
        WIN.blit(text, textRect) 
        WIN.blit(text2, textRect2) 
        WIN.blit(text3, textRect3) 

     
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                menu_run=0

            if pygame.mouse.get_pressed()[0]:
                if buttonGame.collidepoint((x, y)):
                    game(WIN,first,Fi, grid)
                if buttonInfo.collidepoint((x,y)):
                    render_instructions(WIN)    
                if buttonAlGo.collidepoint((x,y)):
                    pick_AlGo(WIN)    
              

        pygame.display.update ()






def star(WIN):
    file_text=pygame.Rect(350,370,210,32)
    width_text=pygame.Rect(300,190,140,32)
    row_text=pygame.Rect(350,290,140,32)
    us_te = False
    us_te2 = False
    us_te3 = False

    ro_te = False
    ro_te2 = False
    fi_te2 = False

    add = False
    add2 = False

    user = ''
    row = ''
    File = ''
    run_in =True
    global WIDTH
    global FILE
    global ROWS
    f=0
    l=0
   
    while run_in:


        WIN.fill((250,230,255))
        x,y = pygame.mouse.get_pos()
        font = pygame.font.Font(None, 30) 

        buttonGo = pygame.Rect(300,600, 100, 50)
        buttonClear = pygame.Rect(550,600, 100, 50)
        for e in pygame.event.get():
            if e .type == pygame.QUIT:
                run_in =False
            if pygame.mouse.get_pressed()[0]:

                if buttonGo.collidepoint((x,y)):
                    if FILE:

                        ma = open(File,'r')
                        w=0
                        for i in ma.readlines():

                            if w ==0:
                                if row=='':
                                    row='50'

                                WIDTH = int(i)

                                while (int(WIDTH) % int(row  ))     !=0:
                                    WIDTH=int(WIDTH) + 1
                                ROWS=row    
                                gap = int(WIDTH)//int(ROWS)
                                grid = store_data((int)(ROWS),round(  (int) (WIDTH) // int(ROWS)), int(WIDTH) )

                            elif w==1:    
                                Ar= i.split() 
                            elif w==2:
                                Fi= i.split() 
                            

                            else:
                                g = i.split()
                                g[0]= int(g[0])*gap
                                g[1]= int(g[1])*gap

                                ro = int(g[0])//gap
                                co = int(g[1])//gap
                                if g[2] == '1':
                                    grid[ro][co].make_bairrer()


                            w+=1
               
                        f=Ar
                        l=Fi
                        File.close()
                    if not FILE:
                    
                        while (int(user) % int(row  ))!=0:
                            user=int(user) + 1
                        WIDTH=user
                        ROWS = row
                        grid = store_data((int)(ROWS),round(  (int) (WIDTH) // int(ROWS)), int(WIDTH) )

                    WIN = pygame.display.set_mode(( int(WIDTH),int(  WIDTH)))

                    MENU(WIN,f,l,grid) 

                    WIN = pygame.display.set_mode( [800 ,   800 ] )

                         
                if x>350 and x<490 and y>290 and y<330:
                    ro_te = True
                    us_te =False
                    ro_te2=True
                    fi_te2=True
                    us_te3=False


                if buttonClear.collidepoint((x,y)):
                    user=''
                    row=''
                    File=''
                if x>300 and x<440 and y>190 and y<240:
                    us_te3=False
                    us_te =True

                    fi_te2=True

                    ro_te=False
                    us_te2=True


                if x>350 and x<560 and y>370 and y<472:

                    us_te =False

                    ro_te =False
                    fi_te2=True
                    us_te3=True

            if e.type == pygame.KEYDOWN:

                if us_te:
                    user += e.unicode 
                if ro_te:
                    row += e.unicode   
                  
                if us_te3:

                    File += e.unicode  

                    FILE=1
 

        go_text = font.render("Go!", True, BLACK)
        clear_text = font.render("Clear!", True, BLACK)


        get_width_text = font.render("Screen Width:", True, BLACK)
        get_row_text = font.render("Rows Of The Maze:", True, BLACK)
        get_file_text = font.render("Or From A File:(Full Root)", True, BLACK)
        note_file_text = font.render("Note:For the File You Need To Specify The Total Rows Or It", True, BLACK)
        note2_file_text = font.render("Will Be 50 Rows(the width of each square will be 16px):", True, BLACK)


        pygame.draw.rect(WIN, (135, 135, 135),buttonGo )
        pygame.draw.rect(WIN, (135, 135, 135),buttonClear )

        go_text = font.render("Go!", True, BLACK)
        WIN.blit(go_text,(320,615))
        Clear_text = font.render("Go!", True, BLACK)
        WIN.blit(clear_text,(570,615))

        WIN.blit(get_width_text,(150,200))
        WIN.blit(get_row_text,(150,300))
        WIN.blit(get_file_text,(150,350))
        WIN.blit(note_file_text,(5,450))
        WIN.blit(note2_file_text,(5,490))

        pygame.draw.rect(WIN, (25,25,25),width_text ,2)
        pygame.draw.rect(WIN, (25,25,25),file_text ,2)
        pygame.draw.rect(WIN, (25,25,25),row_text ,2)


        if us_te2:
            text0= font.render(user, True, (0,0,0))
            WIN.blit(text0,(305,195))

        if ro_te2:    
            text2= font.render(row, True, (0,0,0))
            WIN.blit(text2,(355,295))

            
        if fi_te2:    
            text3= font.render(File, True, (0,0,0))
            WIN.blit(text3,(355,380))

        pygame.display.update()
    pygame.quit()


star(WIN) 