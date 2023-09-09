from functions import *
import time
import matplotlib.pyplot as plt
import numpy as np

def main():

    file = open("statistics_15_20.txt", "w")
    #n_fixed_points = 3
    #n_steiner_point = 2
    my_sigma = 0.3
    POP_SIZE = 400
    CXPB = 0.9
    MUTPB = 0.1
    seed = 20
    
    #test_for_steiner_number(n_fixed_points, my_sigma, POP_SIZE, CXPB, MUTPB, seed=seed)

    #before_distance, after_distance, before_connections, after_connections, steiner = steiner_alg(n_fixed_points, n_steiner_point, my_sigma, POP_SIZE, CXPB, MUTPB, seed=None)
    #print("\n")
    #print("MST length = ", before_distance)
    #print("MEStT length = ", after_distance)
    #print("Difference = ", before_distance - after_distance)
    #print("Ratio = ", after_distance/before_distance)
    #print("\n")
    #print("Minumum Spanning Tree of fixed points")
    #grafo_new(before_connections)
    #print("Optimized Steiner Tree of fixed points")
    #grafo_new(after_connections, steiner)


    mean_ratio = []
    mean_difference = []
    mean_time = []

    for num_fix in range (3,6):
      print('Num fixed point: ', num_fix)
      n_fixed_points = num_fix
      n_steiner_point = n_fixed_points -2


      time_run = []
      ratio = []
      difference = []
      for i in range (5):
          print("test ",i)
          start_time = time.time()
          before_distance, after_distance, before_connections, after_connections, steiner = steiner_alg(n_fixed_points, n_steiner_point, my_sigma, POP_SIZE, CXPB, MUTPB, seed=None)

          time_run.append((time.time() - start_time))
          ratio.append(after_distance/before_distance)
          difference.append(before_distance-after_distance)

      mean_ratio.append(np.mean(ratio))
      mean_difference.append(np.mean(difference))
      mean_time.append(np.mean(time_run))
    file.write(str(mean_ratio) + "\n" + str(mean_difference) + "\n" + str(mean_time) + "\n")
    file.close()
    x_axis = list(range(len(mean_time)))
    plt.plot(x_axis, mean_ratio)
    plt.show()
    x_axis = list(range(len(mean_time)))
    plt.plot(x_axis, mean_time, fmt = "-ro")
    plt.show()
if __name__ == '__main__':
  main()