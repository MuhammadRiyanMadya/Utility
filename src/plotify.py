#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


def plotify(stats:dict, imgTitle):
    
    locs = ('Bulk', 'Utility', 'Pelletizing 1', 'Pelletizing 2', 'BM 1', 'BM 2')
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
    nLabel = 1
    for cluster, clusterNumber in cluster.items():
        p = ax.bar(locs, clusterNumber, width, label=cluster, bottom=bottom, color = color[i])
        bottom += clusterNumber
        i += 1
        nLabel += 1
        
        ax.bar_label(p, label_type='center')

    ##ax.set_title('Troubles')
    ax.legend()
##    plt.show()
    fig.savefig(r'D:\Polytama Propindo\Production - Documents\General\Trouble Report dan Laporan Kejadian\__program\__buffer' + '\\' + imgTitle)

    return

# test

##plotify({'Process':[7,3,6,2,3,4], 'Quality':[7,3,6,2,3,4], 'Safety':[7,3,6,2,3,4]}, '12-12-13.png')
