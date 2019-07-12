import numpy as np
import glob
import matplotlib.pyplot as plt
import sys
import pandas as pd
from matplotlib.animation import FuncAnimation

data_path = "abm-tut-output"

def plot_location():
    # sample data in data directory
    location_df = pd.read_csv('%s/locations.csv' % data_path, index_col="#name")
    city_names = location_df.index.tolist()
    x = location_df.x
    y = location_df.y
    plt.scatter(x, y, s=300, alpha=0.5)
    # label the points with the city names
    for i, txt in enumerate(city_names):
        plt.annotate(txt, (x[i], y[i]), xytext=(5, 5), textcoords='offset points', fontsize='12')


def read_csv_to_df():
    # Reads data from data directory
    df_list = []
    for file_path in glob.glob('%s/agents*.csv' % data_path):
        dataframe = pd.read_csv(file_path, index_col='#id')
        dataframe.apply(pd.to_numeric)
        df_list.append(dataframe)
    return df_list


def animate(i, df, scat):
    scat.set_offsets(np.c_[df[i].x, df[i].y])
    return scat


def save_animation(anim):
    """
    Requires your host system to have the "ffmpeg" pacakage installed
    For mac use home brew: brew install ffmpeg
    this will install a lot of other dependenies required as well
    """
    # Assumes output directory exists
    anim.save('%s/agent_location.mp4' % data_path)
    print('Animation saved in output directory')


def main():

    if len(sys.argv)>1:
        global data_path
        data_path = sys.argv[1]

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.set(xlim=(-10, 110), ylim=(-10, 110))

    num_files = len(glob.glob('%s/agents*.csv' % data_path))
    scat = ax.scatter([], [])
    plot_location()

    print("# of frames: ",num_files)

    dataframe_list = read_csv_to_df()
    # time between frames can be changed by adjusting the interval param which is in milliseconds
    anim = FuncAnimation(
        fig, animate, interval=1000, frames=range(num_files), fargs=(dataframe_list, scat))

    plt.draw()
    # shows the output on screen
    plt.show()
    # uncomment line below to save as mp4 video file
    # save_animation(anim)


if __name__ == "__main__":
    main()
