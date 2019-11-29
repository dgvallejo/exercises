import numpy as np

class spring:
    length = 20.0
    factor = 1.
    local_x = np.zeros([])
    local_y = np.zeros([])
    global_x = np.zeros(11)
    global_y = np.zeros(11)
    r0x = 0.0
    r0y = 0.0
    th = 0.0
    def __init__(self, L):
        self.length = L
        
        th0 = 60.*np.pi/180.
        x0 = 0.0
        y0 = 0.0
        x1 = x0 + 1.*np.cos(0.)
        y1 = y0 + 1.*np.sin(0.)
        x2 = x1 + 1.*np.cos(th0)
        y2 = y1 + 1.*np.sin(th0)
        x3 = x2 + 2.*np.cos(-th0)
        y3 = y2 + 2.*np.sin(-th0)
        x4 = x3 + 2.*np.cos(th0)
        y4 = y3 + 2.*np.sin(th0)
        x5 = x4 + 2.*np.cos(-th0)
        y5 = y4 + 2.*np.sin(-th0)
        x6 = x5 + 2.*np.cos(th0)
        y6 = y5 + 2.*np.sin(th0)
        x7 = x6 + 2.*np.cos(-th0)
        y7 = y6 + 2.*np.sin(-th0)
        x8 = x7 + 2.*np.cos(th0)
        y8 = y7 + 2.*np.sin(th0)
        x9 = x8 + 1.*np.cos(-th0)
        y9 = y8 + 1.*np.sin(-th0)
        x10 = x9 + 1.*np.cos(0.)
        y10 = y9 + 1.*np.sin(0.)
        
        self.factor = self.length/x10
        
        self.local_x = np.array([x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10])*self.factor
        self.local_y = np.array([y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10])
        
    def locate_spring(self, r0x,r0y,th):
        self.r0x = r0x
        self.r0y = r0y
        self.th = th
        #first rotate
        A = np.array([[np.cos(self.th),-np.sin(self.th)],
         [np.sin(self.th),np.cos(self.th)]])
        for k in range(0,11):
            x = A.dot(np.array([[self.local_x[k]],[self.local_y[k]]]))
            self.global_x[k] = x[0]
            self.global_y[k] = x[1]
        #now move
        self.global_x = self.r0x + self.global_x 
        self.global_y = self.r0y + self.global_y
        
    def change_length(self, new_length):
        self.length = new_length
        
    def change_thickness(self, new_thickness):
        self.thickness = new_thickness
    def deform(self, delta):
        inc = (self.length + delta)/self.length
        #first rotate
        A = np.array([[np.cos(self.th),-np.sin(self.th)],
         [np.sin(self.th),np.cos(self.th)]])
        for k in range(0,11):
            x = A.dot(np.array([[self.local_x[k]*inc],[self.local_y[k]]]))
            self.global_x[k] = x[0]
            self.global_y[k] = x[1]
        #now move
        self.global_x = self.r0x + self.global_x 
        self.global_y = self.r0y + self.global_y 

class damper:
    length = 20.0
    factor = 1.
    
    local_rod_x = np.zeros(7)
    local_rod_y = np.zeros(7)
    local_cyl_x = np.zeros(7)
    local_cyl_y = np.zeros(7)
    
    global_rod_x = np.zeros(7)
    global_rod_y = np.zeros(7)
    global_cyl_x = np.zeros(7)
    global_cyl_y = np.zeros(7)
    
    r0x = 0.0
    r0y = 0.0
    th = 0.0
    
    def __init__(self, L):
        self.length = L
        
        th0 = np.pi/2.
        
        x0 = 0.0
        y0 = 0.0
        x1 = x0 + 1.*np.cos(0.)
        y1 = y0 + 1.*np.sin(0.)
        x2 = x1 + 1.*np.cos(th0)
        y2 = y1 + 1.*np.sin(th0)
        x3 = x2 + 9.*np.cos(0.)
        y3 = y2 + 9.*np.sin(0.)
        x4 = x3 + 2.*np.cos(-th0)
        y4 = y3 + 2.*np.sin(-th0)
        x5 = x4 + 9.*np.cos(np.pi)
        y5 = y4 + 9.*np.sin(np.pi)
        x6 = x5 + 1.*np.cos(th0)
        y6 = y5 + 1.*np.sin(th0)
        
        self.local_cyl_x = np.array([x0,x1,x2,x3,x4,x5,x6])
        self.local_cyl_y = np.array([y0,y1,y2,y3,y4,y5,y6])
        
        x0 = 13.0
        y0 = 0.0
        x1 = x0 + 7.*np.cos(np.pi)
        y1 = y0 + 7.*np.sin(np.pi)
        x2 = x1 + 1.*np.cos(th0)
        y2 = y1 + 1.*np.sin(th0)
        x3 = x2 + 0.5*np.cos(np.pi)
        y3 = y2 + 0.5*np.sin(np.pi)
        x4 = x3 + 2.*np.cos(-th0)
        y4 = y3 + 2.*np.sin(-th0)
        x5 = x4 + 0.5*np.cos(0.)
        y5 = y4 + 0.5*np.sin(0.)
        x6 = x5 + 1.*np.cos(th0)
        y6 = y5 + 1.*np.sin(th0)
        
        self.local_rod_x = np.array([x0,x1,x2,x3,x4,x5,x6])
        self.local_rod_y = np.array([y0,y1,y2,y3,y4,y5,y6])
        
        self.factor = self.length/x0
        self.local_cyl_x = self.local_cyl_x*self.factor
        self.local_rod_x = self.local_rod_x*self.factor
        
    def locate_damper(self, r0x,r0y,th):
        self.r0x = r0x
        self.r0y = r0y
        self.th = th
        #first rotate
        A = np.array([[np.cos(self.th),-np.sin(self.th)],
         [np.sin(self.th),np.cos(self.th)]])
        for k in range(0,7):
            x = A.dot(np.array([[self.local_cyl_x[k]],[self.local_cyl_y[k]]]))
            self.global_cyl_x[k] = x[0]
            self.global_cyl_y[k] = x[1]
            x = A.dot(np.array([[self.local_rod_x[k]],[self.local_rod_y[k]]]))
            self.global_rod_x[k] = x[0]
            self.global_rod_y[k] = x[1]
        #now move
        self.global_cyl_x = self.r0x + self.global_cyl_x 
        self.global_cyl_y = self.r0y + self.global_cyl_y
        self.global_rod_x = self.r0x + self.global_rod_x 
        self.global_rod_y = self.r0y + self.global_rod_y
        
    def change_length(self, new_length):
        self.length = new_length
        
    def change_thickness(self, new_thickness):
        self.thickness = new_thickness
    def deform(self, delta):
        #first rotate
        A = np.array([[np.cos(self.th),-np.sin(self.th)],
         [np.sin(self.th),np.cos(self.th)]])
        for k in range(0,7):
            x = A.dot(np.array([[self.local_rod_x[k]+delta],[self.local_rod_y[k]]]))
            self.global_rod_x[k] = x[0]
            self.global_rod_y[k] = x[1]
        #now move
        self.global_rod_x = self.r0x + self.global_rod_x 
        self.global_rod_y = self.r0y + self.global_rod_y

class mass:

    a = 10.0
    b = 10.0
    xfactor = 1.
    yfactor = 1.
    
    local_x = np.zeros([])
    local_y = np.zeros([])
    global_x = np.zeros(5)
    global_y = np.zeros(5)
    
    r0x = 0.0
    r0y = 0.0
    th = 0.0    
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
        th0 = np.pi/2.
        
        x0 = self.r0x
        y0 = self.r0y
        x1 = x0 + np.sqrt(2.)*np.cos(th0/2)
        y1 = y0 + np.sqrt(2.)*np.sin(th0/2)
        x2 = x1 + 2.*np.cos(2*th0)
        y2 = y1 + 2.*np.sin(2*th0)
        x3 = x2 + 2.*np.cos(3*th0)
        y3 = y2 + 2.*np.sin(3*th0)
        x4 = x3 + 2.*np.cos(0.)
        y4 = y3 + 2.*np.sin(0.)
        x5 = x4 + 2.*np.cos(th0)
        y5 = y4 + 2.*np.sin(th0)
        
        
        self.local_x = np.array([x1,x2,x3,x4,x5])
        self.local_y = np.array([y1,y2,y3,y4,y5])
        
        self.xfactor = self.a/(x1-x3)
        self.yfactor = self.b/(y5-y4)
        self.local_x = self.local_x*self.xfactor
        self.local_y = self.local_y*self.yfactor
        
    def locate_mass(self, r0x,r0y,th):
        self.r0x = r0x
        self.r0y = r0y
        self.th = th
        #first rotate
        A = np.array([[np.cos(self.th),-np.sin(self.th)],
         [np.sin(self.th),np.cos(self.th)]])
        for k in range(0,5):
            x = A.dot(np.array([[self.local_x[k]],[self.local_y[k]]]))
            self.global_x[k] = x[0]
            self.global_y[k] = x[1]
        #now move
        self.global_x = self.r0x + self.global_x 
        self.global_y = self.r0y + self.global_y
        
    def change_length(self, new_length):
        self.length = new_length
        
    def change_thickness(self, new_thickness):
        self.thickness = new_thickness
    def deform(self, delta):
        #first rotate
        A = np.array([[np.cos(self.th),-np.sin(self.th)],
         [np.sin(self.th),np.cos(self.th)]])
        for k in range(0,5):
            x = A.dot(np.array([[self.local_x[k]+delta],[self.local_y[k]]]))
            self.global_x[k] = x[0]
            self.global_y[k] = x[1]
        #now move
        self.global_x = self.r0x + self.global_x 
        self.global_y = self.r0y + self.global_y