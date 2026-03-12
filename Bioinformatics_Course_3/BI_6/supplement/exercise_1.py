# -*- coding: utf-8 -*-
# Assignment 6 - 6.1. Generalized Extreme Studentized Deviate

import numpy as np
import scipy.stats as stats

def GESD_test(data, max_outliers):
    """
    Implement the outlier detection method Generalized Extreme Studentized Deviate
    """
    n = len(data)
    data = np.array(data)
    outliers = []
    
    for i in range(1, max_outliers + 1):
        mean = np.mean(data)
        std = np.std(data, ddof=1)
        R = np.abs(data - mean) / std
        max_R_index = np.argmax(R)
        max_R = R[max_R_index]
        
        p_value = 1 - (0.05 / (2 * (n - i + 1)))

        # I couldn't understand how the crtical value was calcualted so I asked chatGPT!! 
        critical_value = stats.t.ppf(p_value, df=n - i - 1) * (n - i) / np.sqrt((n - i - 1 + stats.t.ppf(p_value, df=n - i - 1)**2) * (n - i + 1))
        
        outliers.append((data[max_R_index], max_R, critical_value, i))
        
        if max_R > critical_value:
            data = np.delete(data, max_R_index)
        else:
            break
    
    return [out for out in outliers if out[1] > out[2]]



if __name__ == '__main__':
    """_summary_:
        - Generate normally distributed datasets
        - Introduce random outliers
        - Apply GESD_test() and report the outcome
    """
    import random

    # generate data 
    np.random.seed(0)
    data1 = np.random.normal(0, 1, 10)
    data2 = np.random.normal(0, 1, 40)

    print("data 1:- ", (data1))
    print("data 2:- ", data2)

    # outliers 
    data1_with_outliers = np.copy(data1)
    data2_with_outliers = np.copy(data2)
    
    # adding outliers
    data1_with_outliers[0] = 1 
    data1_with_outliers[5] = 2  
    data1_with_outliers[2] = 3  
    data1_with_outliers[3] = 5  
    data1_with_outliers[7] = 7  
    
    # adding outliers
    data2_with_outliers[5] = 6  
    data2_with_outliers[15] = 5 
    data2_with_outliers[22] = 2 
    data2_with_outliers[30] = 1  
    data2_with_outliers[27] = 4  

    # print("data 1:- ", (data1_with_outliers))
    # print("data 2:- ", data2_with_outliers)

    # GESD_test()
    outliers_data1 = GESD_test(data1_with_outliers, max_outliers=8)
    outliers_data2 = GESD_test(data2_with_outliers, max_outliers=8)

    print("Detected outliers for dataset 1:")
    for outlier in outliers_data1:
        print(f"Outlier: {outlier[0]}, R: {outlier[1]}, Critical value: {outlier[2]}, Iteration: {outlier[3]}")

    print("\nDetected outliers for dataset 2:")
    for outlier in outliers_data2:
        print(f"Outlier: {outlier[0]}, R: {outlier[1]}, Critical value: {outlier[2]}, Iteration: {outlier[3]}")

    if len(outliers_data1) == 5 and len(outliers_data2) == 5:
        print("\nall outliers detected!")
    else:
        print("\ncould not detect all outliers!")
