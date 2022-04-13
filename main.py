from tracemalloc import stop
import matplotlib.pyplot as plt
import graph

NUM_ITERATIONS = 1000

if __name__=="__main__":
    width = 500
    height = 500

    graph = graph.Graph('papa', width, height)

    ###########################
    #     initialize plot     #
    ###########################

    ######################################################
    plt.ion()
    figure, ax = plt.subplots(figsize=(20,20), dpi=50)
    ax.set_xlim(- width / 2, width / 2)
    ax.set_ylim(- height / 2, height / 2)
    ax.set_autoscale_on(False)
    plt.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0)
    ######################################################


    for i in range(0, NUM_ITERATIONS):
        
        ###########################
        #     update plot     #
        ###########################

        ######################################################
        xpoints, ypoints = graph.get_coordinates()

        for i in range(0 ,len(xpoints) - 1, 2):
            ax.plot([xpoints[i], xpoints[i + 1]], [ypoints[i], ypoints[i + 1]], marker='o', ms=20)
        
        figure.canvas.flush_events()
        ax.clear()
        ######################################################

        graph.compute_repulsion_forces()

        graph.compute_attraction_forces()

        graph.compute_gravity()

        graph.update_positions()
        