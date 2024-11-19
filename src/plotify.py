#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from matplotlib.patches import Rectangle


def plotify(stats:dict, imgTitle, latestVal):
    
    locs = ('Bulk', 'Utility', 'PCR 1', 'PCR 2', 'BM 1', 'BM 2')
    cluster = {
        # test
##        'Process': np.array([7, 3, 6,2,3,4]),
##        'Quality': np.array([3, 4, 8,1,3, 5]),
##        'Safety': np.array([7, 3, 5,1,3, 5]),
        'Process': np.array(stats['Process']),
        'Quality': np.array(stats['Quality']),
        'Safety': np.array(stats['Safety']),
    }
    width = 0.4

    color = ["#0288D1", "#CE93D8", "#EF9A9A"]
    labels = ['Safety', 'Quality', 'Process']
    fig, ax = plt.subplots()
    bottom = np.zeros(6)
    i = 0

    for cluster, clusterNumber in cluster.items():
        p = ax.bar(locs, clusterNumber, width, label=cluster, bottom=bottom, color = color[i])
        bottom += clusterNumber
        i += 1
        
##        ax.bar_label(p, label_type='center')

    ax.set_title(r"$\bf{" + '+1' + "}$ at " + latestVal)
    ax.legend()
    
    fig.savefig(r'C:\Users\ssv\AppData\Local\Programs\Python\Python311\InjectionX\__program\__buffer' + '\\' + imgTitle)
    for p in ax.get_children()[:-1]:
        if isinstance(p, Rectangle):
            x, y = p.get_xy()
            w, h = p.get_width(), p.get_height()
            if h > 0:
                ax.text(x + 0.5*w, y + 0.5*h, '%0.0f'%h, va='center', ha='center')

    
##    plt.show()
    return

# test

##plotify({'Process':[7,3,0,0,0,0], 'Quality':[7,3,6,2,3,4], 'Safety':[7,3,6,2,3,4]}, '12-12-13.png', 'Bulk:Quality')
