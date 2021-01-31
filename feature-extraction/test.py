import cv2
import numpy as np 
from matplotlib import pyplot as plt

def increase_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def get_pixel(img, center, x, y): 
      
    new_value = 0
      
    try: 
        # If local neighbourhood pixel  
        # value is greater than or equal 
        # to center pixel values then  
        # set it to 1 
        if img[x][y] >= center: 
            new_value = 1
              
    except BaseException: 
        # Exception is required when  
        # neighbourhood value of a center 
        # pixel value is null i.e. values 
        # present at boundaries. 
        pass
      
    return new_value

# Function for calculating LBP 
def lbp_calculated_pixel(img, x, y): 
   
    center = img[x][y] 
   
    val_ar = [] 
      
    # top_left 
    val_ar.append(get_pixel(img, center, x-1, y-1)) 
      
    # top 
    val_ar.append(get_pixel(img, center, x-1, y)) 
      
    # top_right 
    val_ar.append(get_pixel(img, center, x-1, y + 1)) 
      
    # right 
    val_ar.append(get_pixel(img, center, x, y + 1)) 
      
    # bottom_right 
    val_ar.append(get_pixel(img, center, x + 1, y + 1)) 
      
    # bottom 
    val_ar.append(get_pixel(img, center, x + 1, y)) 
      
    # bottom_left 
    val_ar.append(get_pixel(img, center, x + 1, y-1)) 
      
    # left 
    val_ar.append(get_pixel(img, center, x, y-1)) 
       
    # Now, we need to convert binary 
    # values to decimal 
    power_val = [1, 2, 4, 8, 16, 32, 64, 128] 
   
    val = 0
      
    for i in range(len(val_ar)):
        val += val_ar[i] * power_val[i] 
          
    return val

for leaf in range(21,26):
    path = './dataset/leaf/TB' + str(leaf) + '.bmp'
    img_bgr = cv2.imread(path, 1)
    height, width, _ = img_bgr.shape
    img_bright = increase_brightness(img_bgr, 80)

    alpha = 1.5 # Contrast control (1.0-3.0)
    beta = 0 # Brightness control (0-100)

    adjusted = cv2.convertScaleAbs(img_bright, alpha=alpha, beta=beta)

    img_gray = cv2.cvtColor(adjusted, cv2.COLOR_BGR2GRAY)
    img_lbp = np.zeros((height, width), np.uint8) 

    # Calculating LBP pixel
    for i in range(0, height): 
        for j in range(0, width): 
            img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j) 

    # Create zoning and calculating average
    # make 6x6 zone and calculate average

    plt.imshow(img_lbp, cmap = 'gray')

    div_h_split = 6
    div_w_split = 6

    h_zone = int(height / div_h_split)
    h_mood_zone = height % div_h_split
    w_zone = int(width / div_w_split)
    w_mood_zone = width % div_w_split

    h_list_zone = []
    w_list_zone = []
    h_calc_zone = h_zone
    w_calc_zone = w_zone

    for h in range(0, div_h_split - 1):
        h_list_zone.append(h_calc_zone)
        h_calc_zone += h_zone

    h_list_zone.append(h_calc_zone + h_mood_zone - 1)

    for w in range(0, div_w_split - 1):
        w_list_zone.append(w_calc_zone)
        w_calc_zone += w_zone

    w_list_zone.append(w_calc_zone + w_mood_zone - 1)

    for h_zoning in h_list_zone:
        point1 = [0, h_zoning]
        point2 = [width - 1, h_zoning]

        x_values = [point1[0], point2[0]]
        y_values = [point1[1], point2[1]]

        plt.plot(x_values, y_values, color='red')

    for w_zoning in w_list_zone:
        point1 = [w_zoning, 0]
        point2 = [w_zoning, height-1]

        x_values = [point1[0], point2[0]]
        y_values = [point1[1], point2[1]]

        plt.plot(x_values, y_values, color='green')

    # Calculated average each of zoning
    average_data = []
    for split_number_h in range(div_h_split):
        start_i_index = 0 if split_number_h < 1 else h_list_zone[split_number_h-1] + 1
        end_i_index = h_list_zone[split_number_h]

        for split_number_w in range(div_w_split):
            start_j_index = 0 if split_number_w < 1 else w_list_zone[split_number_w-1] + 1
            end_j_index = w_list_zone[split_number_w]

            # print(split_number_w, start_i_index, end_i_index, start_j_index, end_j_index)
            array_data = []
            for i in range(start_i_index, end_i_index):
                for j in range(start_j_index, end_j_index):
                    array_data.append(img_lbp[i, j])

            average_data.append(np.average(array_data))

    string_data = ';'.join([str(elem) for elem in average_data]) 
    print(string_data.replace('.', ','))

# plt.show()
