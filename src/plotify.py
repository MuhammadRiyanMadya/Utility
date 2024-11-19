# Create dummy data indexed by month and with multi-columns [product, revenue]
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from matplotlib.patches import Rectangle


def plotify(stats:dict, imgTitle):
    
    locs = ('Bulk', 'Utility', 'Pelletizing 1', 'Pelletizing 2', 'BM 1', 'BM 2')
    cluster = {
##        'Process': np.array([7, 3, 6,2,3,4]),
##        'Quality': np.array([3, 4, 8,1,3, 5]),
##        'Safety': np.array([7, 3, 5,1,3, 5]),
        'Process': np.array(stats['Process']),
        'Quality': np.array(stats['Quality']),
        'Safety': np.array(stats['Safety']),
    }
    width = 0.4  # the width of the bars: can also be len(x) sequence

    color = ["#0288D1", "#CE93D8", "#EF9A9A"]
    labels = ['Safety', 'Quality', 'Process']
    fig, ax = plt.subplots()
    bottom = np.zeros(6)
    i = 0
    nLabel = 1
    for cluster, clusterNumber in cluster.items():
        p = ax.bar(locs, clusterNumber, width, label=cluster, bottom=bottom, color = color[i])
        bottom += clusterNumber
        i += 1
        

    ax.set_title('+1' + 'Bulk: )
    ax.legend()
    
##    fig.savefig(r'C:\Users\mrm\Documents\Eng\Reporting system\__buffer' + '\\' + imgTitle)
    
    for p in ax.get_children()[:-1]:
        if isinstance(p, Rectangle):
            x, y = p.get_xy()
            w, h = p.get_width(), p.get_height()
            if h > 0:
                ax.text(x + 0.5*w, y + 0.5*h, '%0.0f'%h, va='center', ha='center')
        
    plt.show()
    return

# test

plotify({'Process':[7,1,0,0,0,0], 'Quality':[3, 0,0,0,0,0], 'Safety':[0,0,0,0,0,1]}, 'alfa.png')
