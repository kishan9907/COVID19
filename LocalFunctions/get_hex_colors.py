import matplotlib
import pandas as pd

def get_hex_colors(df, data_to_color, cmap = matplotlib.cm.Reds, log = False):
    
    '''
    This function takes the following arguments
        1. df:pandas DataFrame with the data.
        2. data_to_color: the column name with data based on which we want to create the color scale.
        3. cmap: colors you want to plot. You can use this to communicate different messages. For example: greens --> good, greys --> deaths.
                default is matplotlib.cm.Reds
                more about colormaps: https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html
        3. log: if data has huge outliers, we can create the color map with a logarithic normalization. This way, the outliers won't "pale" our other data.
                default is False.
        
    '''
    
    cmap = cmap # define the color pallete you want. You can use Reds, Blues, Greens etc
    my_values = df[data_to_color] # get the value you wan to convert to colors
    
    mini = min(my_values) # get the min to normalize
    maxi= max(my_values) # get the max to normalize
    
    LOGMIN = 0.01 # arbitrary lower bound for log scale
    
    if log: 
        norm = matplotlib.colors.LogNorm(vmin=max(mini,LOGMIN), vmax=maxi) # normalize log data
    else:
        norm = matplotlib.colors.Normalize(vmin=mini, vmax=maxi) # create a color range
        
    colors = {value:matplotlib.colors.rgb2hex(cmap(norm(value))[:3]) for value in sorted(list(set(my_values)))} # create a dictionary with the total_infected or deaths as keys and colors as values
    
    return colors