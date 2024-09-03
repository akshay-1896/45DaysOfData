class College:
    college_name = "IIT" # class variables can be accessed using class name or class objects
    college_city = "Jaipur"
    
    # instance variable constructor
    def __init__(self,cse_hod,ece_hod,e_hod):
        # instance variables
        self.college_cse_hod = cse_hod
        self.college_ece_hod = ece_hod
        self.college_electrical_hod = e_hod
        self.student_marks = [25,35,45,41,42,47,49,38,39,29,46,47]
        self.random_number = [23,34,12,54,64,76,34,54,72,73,82,99,2,56,3,1,8,67,98,94,20,50]
        print("Constructor called")

    # self --> acts as a pointer, as it references address to the object
    
    def display(self):
        print("My College name: ", self.college_name)
        print("MY CSE HOD: ", self.college_cse_hod)
        print("My College city: ", self.college_city)
        
    def average_marks(self):
        marks = self.student_marks
        # print(marks)
        total_sum = 0
        count = 0
        for item in marks:
            total_sum += item
            count += 1
            
        print(total_sum/count)
        
    #method even no and odd no count
    def even_odd_counter(self):
        rn = self.random_number
        e_count = 0
        o_count = 0
        for item in rn:
            if item % 2 == 0 :
                e_count += 1
            else :
                o_count += 1
        
        print(f"Even no: {e_count}")
        print(f"Odd no: {o_count}")
        
    def even_average_finder(self):
        rn = self.random_number
        even = 0
        count = 0
        for item in rn:
            if item % 2 == 0:
                even += item
                count += 1
            
        print(even/count)
        
    def target_finder(self,item):
        rn = self.random_number
        # self.t = item
        t = int(input("Enter the target: "))
        count = 0
        for i in range(len(rn)):
            if t == rn[i]:
                print(f"\nTarget {t} found at {i}")
                count = 1
                
        if count == 0:
            print(f"\nTarget {t} not found or may be not in the list!!")
                
                
obj = College(cse_hod="Manoj Sharma",ece_hod="Uday Pratap",e_hod="Rahul Trivedi")
       
print(f"\n{obj.student_marks}\n")
       
obj.display()      
print(" ")   
obj.even_average_finder()      
print(" ")   
obj.even_odd_counter()    
print(" ")   
obj.average_marks()    
print(" ")   
obj.target_finder(99)    
print(" ")   

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                