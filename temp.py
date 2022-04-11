import matplotlib.pyplot as plt
import numpy as npy


if __name__ == '__main__':
    
    c = []
    avg = []
    
    with open("/Users/billhu/Documents/Probability/PM project/t4_res.txt") as f:
        data = f.read()
        data = data.replace(" ", "")
        data = data.split(";")
        data.remove(data[-1])
        
        for i in data:
            try:
                # print(i)
                i.replace(" ", "")
                i = i.split(",")
                if i != '':
                    c.append(float(i[0][2:]))
                    avg.append(float(i[1][4:]))
                # print(i[0][2:])
                
            except IndexError:
                print("end!!!")
            
            # print(i)
        # print(data)
        
        # print(c)
        # print(avg)
        
        plt.subplot(111)
        plt.title('Relation of c and final result')
        plt.plot(c, avg, marker='o', markerfacecolor='blue', markersize=3)
        plt.xlim(0, 10);  plt.ylim(3600, 5000)
        plt.xlabel("c");  plt.ylabel("avg final result")
        plt.show()
        
