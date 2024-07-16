import numpy as np
import pandas as pd
from scipy.stats import kurtosis, skew
import math
from scipy.stats import entropy

def Equation(acc_x, acc_y, acc_z, gyro_x, gyro_y, gyro_z):
    acc_x_abs = []
    acc_y_abs = []
    acc_z_abs = []
    magnitude_acc = []
    gyro_x_abs = []
    gyro_y_abs = []
    gyro_z_abs = []
    magnitude_gyro = []
    acc_tilt_angle = []
    gyro_tilt_angle = []


    for x_acc,y_acc,z_acc in zip(acc_x, acc_y, acc_z):
        magnitude_acc.append(np.sqrt(x_acc**2 + y_acc**2 + z_acc**2))
        acc_x_abs.append(abs(x_acc))
        acc_y_abs.append(abs(y_acc))
        acc_z_abs.append(abs(z_acc))
        acc_tilt_angle = math.asin(y_acc / np.sqrt(x_acc**2 + y_acc**2 + z_acc**2)) * (180.0 / math.pi)

    for x_gyro,y_gyro,z_gyro in zip(gyro_x, gyro_y, gyro_z):
        magnitude_gyro.append(np.sqrt(x_gyro**2 + y_gyro**2 + z_gyro**2))
        gyro_x_abs.append(abs(x_gyro))
        gyro_y_abs.append(abs(y_gyro))
        gyro_z_abs.append(abs(z_gyro))
        gyro_tilt_angle = math.asin(y_gyro / np.sqrt(x_gyro**2 + y_gyro**2 + z_gyro**2)) * (180.0 / math.pi)
        
    mean_acc_x = np.mean(acc_x)
    mean_acc_y = np.mean(acc_y)
    mean_acc_z = np.mean(acc_z)
    mean_acc_x_abs = np.mean(acc_x_abs)
    mean_acc_y_abs = np.mean(acc_y_abs)
    mean_acc_z_abs = np.mean(acc_z_abs)
    mean_acc_magnitude = np.mean(magnitude_acc)
    mean_acc_TA = np.mean(acc_tilt_angle)


    mean_gyro_x = np.mean(gyro_x)
    mean_gyro_y = np.mean(gyro_y)
    mean_gyro_z = np.mean(gyro_z)
    mean_gyro_x_abs = np.mean(gyro_x_abs)
    mean_gyro_y_abs = np.mean(gyro_y_abs)
    mean_gyro_z_abs = np.mean(gyro_z_abs)
    mean_gyro_magnitude = np.mean(magnitude_gyro)
    mean_gyro_TA = np.mean(gyro_tilt_angle)
    median_acc_x = np.median(acc_x)
    median_acc_y = np.median(acc_y)
    median_acc_z = np.median(acc_z)
    median_acc_x_abs = np.median(acc_x_abs)
    median_acc_y_abs = np.median(acc_y_abs)
    median_acc_z_abs = np.median(acc_z_abs)
    median_acc_magnitude = np.median(magnitude_acc)
    median_acc_TA = np.median(acc_tilt_angle)
    median_gyro_x = np.median(gyro_x)
    median_gyro_y = np.median(gyro_y)
    median_gyro_z = np.median(gyro_z)
    median_gyro_x_abs = np.median(gyro_x_abs)
    median_gyro_y_abs = np.median(gyro_y_abs)
    median_gyro_z_abs = np.median(gyro_z_abs)
    median_gyro_magnitude = np.median(magnitude_gyro)
    median_gyro_TA = np.median(gyro_tilt_angle)

    STD_acc_x = np.std(acc_x)
    STD_acc_y = np.std(acc_y)
    STD_acc_z = np.std(acc_z)
    STD_acc_x_abs = np.std(acc_x_abs)
    STD_acc_y_abs = np.std(acc_y_abs)
    STD_acc_z_abs = np.std(acc_z_abs)
    STD_acc_magnitude = np.std(magnitude_acc)
    STD_gyro_x = np.std(gyro_x)
    STD_gyro_y = np.std(gyro_y)
    STD_gyro_z = np.std(gyro_z)
    STD_gyro_x_abs = np.std(gyro_x_abs)
    STD_gyro_y_abs = np.std(gyro_y_abs)
    STD_gyro_z_abs = np.std(gyro_z_abs)
    STD_gyro_magnitude = np.std(magnitude_gyro)
    kurtosis_acc_x = kurtosis(acc_x)
    kurtosis_acc_y = kurtosis(acc_y)
    kurtosis_acc_z = kurtosis(acc_z)
    kurtosis_acc_x_abs = kurtosis(acc_x_abs)
    kurtosis_acc_y_abs = kurtosis(acc_y_abs)
    kurtosis_acc_z_abs = kurtosis(acc_z_abs)
    kurtosis_acc_magnitude = kurtosis(magnitude_acc)

    kurtosis_gyro_x = kurtosis(gyro_x)
    kurtosis_gyro_y = kurtosis(gyro_y)
    kurtosis_gyro_z = kurtosis(gyro_z)
    kurtosis_gyro_x_abs = kurtosis(gyro_x_abs)
    kurtosis_gyro_y_abs = kurtosis(gyro_y_abs)
    kurtosis_gyro_z_abs = kurtosis(gyro_z_abs)
    kurtosis_gyro_magnitude = kurtosis(magnitude_gyro)
    skewness_acc_x = skew(acc_x)
    skewness_acc_y = skew(acc_y)
    skewness_acc_z = skew(acc_z)
    skewness_acc_x_abs = skew(acc_x_abs)
    skewness_acc_y_abs = skew(acc_y_abs)
    skewness_acc_z_abs = skew(acc_z_abs)
    skewness_acc_magnitude = skew(magnitude_acc)
    skewness_gyro_x = skew(gyro_x)
    skewness_gyro_y = skew(gyro_y)
    skewness_gyro_z = skew(gyro_z)
    skewness_gyro_x_abs = skew(gyro_x_abs)
    skewness_gyro_y_abs = skew(gyro_y_abs)
    skewness_gyro_z_abs = skew(gyro_z_abs)
    skewness_gyro_magnitude = skew(magnitude_gyro)
    min_acc_x = np.min(acc_x)
    min_acc_y = np.min(acc_y)
    min_acc_z = np.min(acc_z)
    min_acc_x_abs = np.min(acc_x_abs)
    min_acc_y_abs = np.min(acc_y_abs)
    min_acc_z_abs = np.min(acc_z_abs)
    min_acc_magnitude = np.min(magnitude_acc)
    min_acc_TA = np.min(acc_tilt_angle)
    min_gyro_x = np.min(gyro_x)
    min_gyro_y = np.min(gyro_y)
    min_gyro_z = np.min(gyro_z)
    min_gyro_x_abs = np.min(gyro_x_abs)
    min_gyro_y_abs = np.min(gyro_y_abs)
    min_gyro_z_abs = np.min(gyro_z_abs)
    min_gyro_magnitude = np.min(magnitude_gyro)
    min_gyro_TA = np.min(gyro_tilt_angle)
    max_acc_x = np.max(acc_x)
    max_acc_y = np.max(acc_y)
    max_acc_z = np.max(acc_z)
    max_acc_x_abs = np.max(acc_x_abs)
    max_acc_y_abs = np.max(acc_y_abs)
    max_acc_z_abs = np.max(acc_z_abs)
    max_acc_magnitude = np.max(magnitude_acc)
    max_acc_TA = np.max(acc_tilt_angle)
    max_gyro_x = np.max(gyro_x)
    max_gyro_y = np.max(gyro_y)
    max_gyro_z = np.max(gyro_z)
    max_gyro_x_abs = np.max(gyro_x_abs)
    max_gyro_y_abs = np.max(gyro_y_abs)
    max_gyro_z_abs = np.max(gyro_z_abs)
    max_gyro_magnitude =np.max(magnitude_gyro)
    max_gyro_TA = np.max(gyro_tilt_angle)
    RMS_acc_x = np.sqrt(np.mean(np.square(acc_x)))
    RMS_acc_y = np.sqrt(np.mean(np.square(acc_y)))
    RMS_acc_z = np.sqrt(np.mean(np.square(acc_z)))
    RMS_acc_x_abs = np.sqrt(np.mean(np.square(acc_x_abs)))
    RMS_acc_y_abs = np.sqrt(np.mean(np.square(acc_y_abs)))
    RMS_acc_z_abs = np.sqrt(np.mean(np.square(acc_z_abs)))
    RMS_acc_magnitude = np.sqrt(np.mean(np.square(magnitude_acc)))
    RMS_acc_TA = np.sqrt(np.mean(np.square(acc_tilt_angle)))

    RMS_gyro_x = np.sqrt(np.mean(np.square(gyro_x)))
    RMS_gyro_y = np.sqrt(np.mean(np.square(gyro_y)))
    RMS_gyro_z = np.sqrt(np.mean(np.square(gyro_z)))
    RMS_gyro_x_abs = np.sqrt(np.mean(np.square(gyro_x_abs)))
    RMS_gyro_y_abs = np.sqrt(np.mean(np.square(gyro_y_abs)))
    RMS_gyro_z_abs = np.sqrt(np.mean(np.square(gyro_z_abs)))
    RMS_gyro_magnitude = np.sqrt(np.mean(np.square(magnitude_gyro)))
    RMS_gyro_TA = np.sqrt(np.mean(np.square(gyro_tilt_angle)))
    fourth_central_moment_acc_x = np.mean((acc_x - mean_acc_x)**4)
    fourth_central_moment_acc_y = np.mean((acc_y - mean_acc_y)**4)
    fourth_central_moment_acc_z = np.mean((acc_z - mean_acc_z)**4)
    fourth_central_moment_acc_x_abs = np.mean((acc_x_abs - mean_acc_x_abs)**4)
    fourth_central_moment_acc_y_abs = np.mean((acc_y_abs - mean_acc_y_abs)**4)
    fourth_central_moment_acc_z_abs = np.mean((acc_z_abs - mean_acc_z_abs)**4)
    fourth_central_moment_acc_magnitude = np.mean((magnitude_acc - mean_acc_magnitude)**4)

    fourth_central_moment_gyro_x = np.mean((gyro_x - mean_gyro_x)**4)
    fourth_central_moment_gyro_y = np.mean((gyro_y - mean_gyro_y)**4)
    fourth_central_moment_gyro_z = np.mean((gyro_z - mean_gyro_z)**4)
    fourth_central_moment_gyro_x_abs = np.mean((gyro_x_abs - mean_gyro_x_abs)**4)
    fourth_central_moment_gyro_y_abs = np.mean((gyro_y_abs - mean_gyro_y_abs)**4)
    fourth_central_moment_gyro_z_abs = np.mean((gyro_z_abs - mean_gyro_z_abs)**4)
    fourth_central_moment_gyro_magnitude = np.mean((magnitude_gyro - mean_gyro_magnitude)**4)
    fifth_central_moment_acc_x =  np.mean((acc_x - mean_acc_x)**5)
    fifth_central_moment_acc_y = np.mean((acc_y - mean_acc_y)**5)
    fifth_central_moment_acc_z = np.mean((acc_z - mean_acc_z)**5)
    fifth_central_moment_acc_x_abs = np.mean((acc_x_abs - mean_acc_x_abs)**5)
    fifth_central_moment_acc_y_abs = np.mean((acc_y - mean_acc_y_abs)**5)
    fifth_central_moment_acc_z_abs = np.mean((acc_z_abs - mean_acc_z_abs)**5)
    fifth_central_moment_acc_magnitude = np.mean((magnitude_acc - mean_acc_magnitude)**5)

    fifth_central_moment_gyro_x = np.mean((gyro_x - mean_gyro_x)**5)
    fifth_central_moment_gyro_y = np.mean((gyro_y - mean_gyro_y)**5)
    fifth_central_moment_gyro_z = np.mean((gyro_z - mean_gyro_z)**5)
    fifth_central_moment_gyro_x_abs = np.mean((gyro_x_abs - mean_gyro_x_abs)**5)
    fifth_central_moment_gyro_y_abs = np.mean((gyro_y_abs - mean_gyro_y_abs)**5)
    fifth_central_moment_gyro_z_abs = np.mean((gyro_z_abs - mean_gyro_z_abs)**5)
    fifth_central_moment_gyro_magnitude = np.mean((magnitude_gyro - mean_gyro_magnitude)**5)
    probability_distribution_acc = np.histogramdd(magnitude_acc, bins=10, density=True)[0].flatten()
    probability_distribution_acc = np.histogramdd(magnitude_gyro, bins=10, density=True)[0].flatten()
    entropy_acc = entropy(probability_distribution_acc)
    entropy_gyro = entropy(magnitude_gyro)
    slope_acc = np.sqrt((max_acc_x - min_acc_x)**2 + (max_acc_y - min_acc_y)**2 + (max_acc_z - min_acc_z)**2 )
    slope_gyro = np.sqrt((max_gyro_x - min_gyro_x)**2 + (max_gyro_y - min_gyro_y)**2 + (max_gyro_z - min_gyro_z)**2)
    # Create a list of values to write to the CSV file
    values = { 
        'mean_acc_x': [mean_acc_x], 'mean_acc_y': [mean_acc_y], 'mean_acc_z': [mean_acc_z],
        'mean_acc_x_abs': [mean_acc_x_abs], 'mean_acc_y_abs': [mean_acc_y_abs], 'mean_acc_z_abs': [mean_acc_z_abs],
        'mean_acc_magnitude': [mean_acc_magnitude], 'mean_acc_TA': [mean_acc_TA], 
        
        'mean_gyro_x': [mean_gyro_x], 'mean_gyro_y': [mean_gyro_y], 'mean_gyro_z': [mean_gyro_z],
        'mean_gyro_x_abs': [mean_gyro_x_abs], 'mean_gyro_y_abs': [mean_gyro_y_abs], 'mean_gyro_z_abs': [mean_gyro_z_abs],
        'mean_gyro_magnitude': [mean_gyro_magnitude], 'mean_gyro_TA': [mean_gyro_TA], 
        'median_acc_x': [median_acc_x], 'median_acc_y': [median_acc_y], 'median_acc_z': [median_acc_z],
        'median_acc_x_abs': [median_acc_x_abs], 'median_acc_y_abs': [median_acc_y_abs], 'median_acc_z_abs': [median_acc_z_abs],
        'median_acc_magnitude': [median_acc_magnitude], 'median_acc_TA': [median_acc_TA],
        
        'median_gyro_x': [median_gyro_x], 'median_gyro_y': [median_gyro_y], 'median_gyro_z': [median_gyro_z],
        'median_gyro_x_abs': [median_gyro_x_abs], 'median_gyro_y_abs': [median_gyro_y_abs], 'median_gyro_z_abs': [median_gyro_z_abs],
        'median_gyro_magnitude': [median_gyro_magnitude], 'median_gyro_TA': [median_gyro_TA], 

        'STD_acc_x': [STD_acc_x], 'STD_acc_y': [STD_acc_y], 'STD_acc_z': [STD_acc_z],
        'STD_acc_x_abs': [STD_acc_x_abs], 'STD_acc_y_abs': [STD_acc_y_abs], 'STD_acc_z_abs': [STD_acc_z_abs],
        'STD_acc_magnitude': [STD_acc_magnitude],  
        
        'STD_gyro_x': [STD_gyro_x], 'STD_gyro_y': [STD_gyro_y], 'STD_gyro_z': [STD_gyro_z],
        'STD_gyro_x_abs': [STD_gyro_x_abs], 'STD_gyro_y_abs': [STD_gyro_y_abs], 'STD_gyro_z_abs': [STD_gyro_z_abs],
        'STD_gyro_magnitude': [STD_gyro_magnitude],  
        
        'kurtosis_acc_x': [kurtosis_acc_x], 'kurtosis_acc_y': [kurtosis_acc_y], 'kurtosis_acc_z': [kurtosis_acc_z],
        'kurtosis_acc_x_abs': [kurtosis_acc_x_abs], 'kurtosis_acc_y_abs': [kurtosis_acc_y_abs], 'kurtosis_acc_z_abs': [kurtosis_acc_z_abs],
        'kurtosis_acc_magnitude': [kurtosis_acc_magnitude], 
        
        'kurtosis_gyro_x': [kurtosis_gyro_x], 'kurtosis_gyro_y': [kurtosis_gyro_y], 'kurtosis_gyro_z': [kurtosis_gyro_z],
        'kurtosis_gyro_x_abs': [kurtosis_gyro_x_abs], 'kurtosis_gyro_y_abs': [kurtosis_gyro_y_abs], 'kurtosis_gyro_z_abs': [kurtosis_gyro_z_abs],
        'kurtosis_gyro_magnitude': [kurtosis_gyro_magnitude],  


        'skewness_acc_x': [skewness_acc_x], 'skewness_acc_y': [skewness_acc_y], 'skewness_acc_z': [skewness_acc_z],
        'skewness_acc_x_abs': [skewness_acc_x_abs], 'skewness_acc_y_abs': [skewness_acc_y_abs], 'skewness_acc_z_abs': [skewness_acc_z_abs],
        'skewness_acc_magnitude': [skewness_acc_magnitude], 

        'skewness_gyro_x': [skewness_gyro_x], 'skewness_gyro_y': [skewness_gyro_y], 'skewness_gyro_z': [skewness_gyro_z],
        'skewness_gyro_x_abs': [skewness_gyro_x_abs], 'skewness_gyro_y_abs': [skewness_gyro_y_abs], 'skewness_gyro_z_abs': [skewness_gyro_z_abs],
        'skewness_gyro_magnitude': [skewness_gyro_magnitude], 


        'min_acc_x': [min_acc_x],'min_acc_y': [min_acc_y],'min_acc_z': [min_acc_z],'min_acc_x_abs': [min_acc_x_abs],
        'min_acc_y_abs': [min_acc_y_abs],'min_acc_z_abs': [min_acc_z_abs], 'min_acc_magnitude': [min_acc_magnitude],
        'min_acc_TA': [min_acc_TA],

        'min_gyro_x': [min_gyro_x],'min_gyro_y': [min_gyro_y],'min_gyro_z': [min_gyro_z],'min_gyro_x_abs': [min_gyro_x_abs],
        'min_gyro_y_abs': [min_gyro_y_abs],'min_gyro_z_abs': [min_gyro_z_abs], 'min_gyro_magnitude': [min_gyro_magnitude],
        'min_gyro_TA': [min_gyro_TA],
        'max_acc_x': [max_acc_x],'max_acc_y': [max_acc_y], 'max_acc_z': [max_acc_z],'max_acc_x_abs': [max_acc_x_abs],
        'max_acc_y_abs': [max_acc_y_abs],'max_acc_z_abs': [max_acc_z_abs],'max_acc_magnitude': [max_acc_magnitude],
        'max_acc_TA': [max_acc_TA], 
        'max_gyro_x': [max_gyro_x],'max_gyro_y': [max_gyro_y], 'max_gyro_z': [max_gyro_z],'max_gyro_x_abs': [max_gyro_x_abs],
        'max_gyro_y_abs': [max_gyro_y_abs],'max_gyro_z_abs': [max_gyro_z_abs],'max_gyro_magnitude': [max_gyro_magnitude],
        'max_gyro_TA': [max_gyro_TA],

        'RMS_acc_x': [RMS_acc_x],'RMS_acc_y': [RMS_acc_y],'RMS_acc_z': [RMS_acc_z],'RMS_acc_x_abs': [RMS_acc_x_abs],
        'RMS_acc_y_abs': [RMS_acc_y_abs],'RMS_acc_z_abs': [RMS_acc_z_abs],'RMS_acc_magnitude': [RMS_acc_magnitude],
        'RMS_acc_TA': [RMS_acc_TA],

        'RMS_gyro_x': [RMS_gyro_x],'RMS_gyro_y': [RMS_gyro_y],'RMS_gyro_z': [RMS_gyro_z],
        'RMS_gyro_x_abs': [RMS_gyro_x_abs],'RMS_gyro_y_abs': [RMS_gyro_y_abs],'RMS_gyro_z_abs': [RMS_gyro_z_abs],'RMS_gyro_magnitude': [RMS_gyro_magnitude],
        'RMS_gyro_TA': [RMS_gyro_TA],


        'fourth_central_moment_acc_x': [fourth_central_moment_acc_x],'fourth_central_moment_acc_y': [fourth_central_moment_acc_y],
        'fourth_central_moment_acc_z': [fourth_central_moment_acc_z],'fourth_central_moment_acc_x_abs': [fourth_central_moment_acc_x_abs],
        'fourth_central_moment_acc_y_abs': [fourth_central_moment_acc_y_abs],
        'fourth_central_moment_acc_z_abs': [fourth_central_moment_acc_z_abs],'fourth_central_moment_acc_magnitude': [fourth_central_moment_acc_magnitude],
        
        
        'fourth_central_moment_gyro_x': [fourth_central_moment_gyro_x],'fourth_central_moment_gyro_y': [fourth_central_moment_gyro_y],
        'fourth_central_moment_gyro_z': [fourth_central_moment_gyro_z], 'fourth_central_moment_gyro_x_abs': [fourth_central_moment_gyro_x_abs],
        'fourth_central_moment_gyro_y_abs': [fourth_central_moment_gyro_y_abs],'fourth_central_moment_gyro_z_abs': [fourth_central_moment_gyro_z_abs],
        'fourth_central_moment_gyro_magnitude': [fourth_central_moment_gyro_magnitude],
        
        

        'fifth_central_moment_acc_x': [fifth_central_moment_acc_x],'fifth_central_moment_acc_y': [fifth_central_moment_acc_y],
        'fifth_central_moment_acc_z': [fifth_central_moment_acc_z],'fifth_central_moment_acc_x_abs': [fifth_central_moment_acc_x_abs],
        'fifth_central_moment_acc_y_abs': [fifth_central_moment_acc_y_abs],'fifth_central_moment_acc_z_abs': [fifth_central_moment_acc_z_abs],
        'fifth_central_moment_acc_magnitude': [fifth_central_moment_acc_magnitude],
        
        
        'fifth_central_moment_gyro_x': [fifth_central_moment_gyro_x],'fifth_central_moment_gyro_y': [fifth_central_moment_gyro_y],
        'fifth_central_moment_gyro_z': [fifth_central_moment_gyro_z],'fifth_central_moment_gyro_x_abs': [fifth_central_moment_gyro_x_abs],
        'fifth_central_moment_gyro_y_abs': [fifth_central_moment_gyro_y_abs],'fifth_central_moment_gyro_z_abs': [fifth_central_moment_gyro_z_abs],
        'fifth_central_moment_gyro_magnitude': [fifth_central_moment_gyro_magnitude],

        'entropy_acc':[entropy_acc],
        'entropy_gyro':[entropy_gyro],
        'slope_acc': [slope_acc], 'slope_gyro': [slope_gyro],
        }
    return pd.DataFrame.from_dict(values)