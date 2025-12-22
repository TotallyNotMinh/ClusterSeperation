import numpy as np

class Point2D:
    def __init__(self, x, y, var, point_count):
        self.x_cen = x
        self.y_cen = y
        self.var = var
        self.point_count = point_count
        self.nearby_points = [[x, y]]

    def generate_points(self):
        nearby_points = []
        for i in range(1, self.point_count):
            x = np.random.normal(self.x_cen, self.var)
            y = np.random.normal(self.y_cen, self.var)
            nearby_points.append([x, y])
        return nearby_points

class Point3D:
    def __init__(self, x, y, z, var, point_count):
        self.x_cen = x
        self.y_cen = y
        self.z_cen = z
        self.var = var
        self.point_count = point_count

    def generate_points(self):
        nearby_points = []
        for i in range(1, self.point_count):
            x = np.random.normal(self.x_cen, self.var)
            y = np.random.normal(self.y_cen, self.var)
            z = np.random.normal(self.z_cen, self.var)
            nearby_points.append([x, y, z])      
        print(nearby_points)
        return nearby_points



        
    



    
    



    
        
    

