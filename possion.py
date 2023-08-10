import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import seaborn as sns


default_event_steps = 1
default_lambda_steps = 0.5


def helper_text():
    print("\nUsage:\n\tpython possion.py [START_event] [END_event] [TARGET_event] [lambda_START_val] [lambda_END_val] [lambda_TARGET_val] <discrete_event_steps> <lambda_steps>")
    print("\n\t*Arguments enclosed using [ ] are required, and < > are optional")
    print("\n\t*(START_event < TARGET_event <= END_event) and (lambda_START_val < lambda_TARGET_val <= lambda_END_val)")
    print("\nExample:\n\tpython possion.py 0 20 12 0 10 6.5       -> Setting six required args\n\tpython possion.py 0 20 12 0 10 6.5 1     -> Setting six required args + <discrete_event_steps>\n\tpython possion.py 0 20 12 0 10 6.5 1 0.5 -> Setting six required args + <discrete_event_steps> + <lambda_steps>")
    print("\nThese arguments require descrete (Int) values:\n\t[START_event]\n\t[END_event]\n\t[TARGET_event]")
    print("\nWhile these arguments require quantative (Int/float) values:\n\t[lambda_START_val]\n\t[lambda_END_val]\n\t[lambda_TARGET_val]\n\t<discrete_event_steps>\n\t<lambda_steps>")
    print()



class PossionDistributionFunctions:        
    
    def __init__(self, descrete_START_event, descrete_END_event, descrete_TARGET_event, labmda_START_value, labmda_END_value, labmda_TARGET_value, slider_descrete_event_steps=default_event_steps, slider_labda_steps=default_lambda_steps):
        self.__descrete_START_event = descrete_START_event
        self.__descrete_END_event = descrete_END_event
        self.__descrete_TARGET_event = descrete_TARGET_event
        self.__labmda_START_value = labmda_START_value
        self.__labmda_END_value = labmda_END_value
        self.__labmda_TARGET_value = labmda_TARGET_value
        self.__slider_descrete_event_steps = slider_descrete_event_steps
        self.__slider_labda_steps = slider_labda_steps
    
    def poisson_probability(self, lambda_val, k):
        """
        Calculate the probability of observing 'k' events in a Poisson distribution
        with an average rate of 'lambda_val'.
        """
        return (math.exp(-lambda_val) * lambda_val ** k) / math.factorial(k)
    
    def starter(self):

        def show_values_on_bars(axs):
            '''Adds labels on bar plots on a given axiswith .3f places'''
            def _show_on_single_plot(ax):
                for p in ax.patches:
                    _x = p.get_x() + p.get_width() / 2
                    _y = p.get_y() + p.get_height()
                    value = '{:.3f}'.format(p.get_height())
                    if str(value).split('.')[0] == '1':
                        value = '1'
                    ax.text(_x, _y, value, ha="center", va="center", fontsize=6.5, fontweight='bold', color='red')

            if isinstance(axs, np.ndarray):
                for idx, ax in np.ndenumerate(axs):
                    _show_on_single_plot(ax)
            else:
                _show_on_single_plot(axs)

        
        def update(val):
            '''Calls this funciton whenever any of the slider value changes'''

            # Clearing previous axis
            ax[0].cla()
            ax[1].cla()


            x_events = [x for x in range(0, int(slider_events.val)+1)]

            y_probabilities = [self.poisson_probability(slider_lambda.val, k) for k in x_events]

            

            '''Recreating on the 2 empty axis'''
            fig.suptitle(f'Poisson Probability Distribution\n \nE(X) = μ = λ = {slider_lambda.val:.2f}\nV(X) / σ2 = {slider_lambda.val:.2f}\nSD / σ = {np.sqrt(slider_lambda.val):.2f}', fontsize=16)

            ax[0].set_xlim([-1, x_events[-1]+1])
            ax[1].set_xlim([-1, x_events[-1]+1])

            ax[0].set_ylim([-0.1, 1.1])
            ax[1].set_ylim([-0.1, 1.1])

            ax[0].set_xticks(x_events)
            ax[1].set_xticks(x_events)

            

            ax[0].title.set_text('Probability Mass Function')
            ax[0].set_xlabel('Descrete Value Events')
            ax[0].set_ylabel('Probability')
            ax[0].set_xticks(x_events)
            ax[0].set_yticks(y_ticks)
            y_probabilities = [self.poisson_probability(slider_lambda.val, k) for k in x_events]
            sns.barplot(x=x_events, y=y_probabilities, errorbar=None, ax=ax[0])
            show_values_on_bars(ax[0]) # Show values on top of bar for target axis
            ax[0].plot(x_events, y_probabilities, lw=2, markersize=8, marker=None)

            
            ax[1].title.set_text('Cumulative Distribution Function')
            ax[1].set_xlabel('Descrete Value Events')
            ax[1].set_ylabel('Cumulative Probability')
            ax[1].set_xticks(x_events)
            ax[1].set_yticks(y_ticks)
            cumulative_probabilities = np.cumsum(y_probabilities)
            sns.barplot(x=x_events, y=cumulative_probabilities, errorbar=None, ax=ax[1])
            show_values_on_bars(ax[1]) # Show values on top of bar for target axis
            ax[1].plot(x_events, cumulative_probabilities, lw=2, markersize=8, marker=None)

            ax[0].grid(True)
            ax[1].grid(True)
        
        
        y_ticks = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]  # Create equally spaced tick positions


        fig, ax = plt.subplots(1, 2, figsize=(10, 3))
        fig.canvas.manager.set_window_title('Probability Distribution Function - Simulation') # Set the title for the window

        # Create axes for frequency and amplitude sliders
        ax_events = plt.axes([0.2, 0.05, 0.65, 0.03])
        ax_lambda = plt.axes([0.2, 0.01, 0.65, 0.03])
        slider_events = Slider(
            ax_events, 
            'Events', 
            valmin = self.__descrete_START_event, 
            valmax = self.__descrete_END_event, 
            valinit = self.__descrete_TARGET_event, 
            valstep=self.__slider_descrete_event_steps
        )
        slider_lambda = Slider(ax_lambda,
            'Lambda',
            valmin = self.__labmda_START_value,
            valmax = self.__labmda_END_value,
            valinit = self.__labmda_TARGET_value,
            valstep=self.__slider_labda_steps
        )


        # Adding the main title
        fig.suptitle(f'Poisson Probability Distribution\n \nE(X) = μ = λ = {slider_lambda.val:.2f}\nV(X) / σ2 = {slider_lambda.val:.2f}\nSD / σ = {np.sqrt(slider_lambda.val):.2f}', fontsize=16)


        # Show maximized screen
        figManager = plt.get_current_fig_manager()
        figManager.window.state('zoomed')

        
        # Get current value of slider_event and make the x-axis values
        x_events = [x for x in range(0, int(slider_events.val)+1)]
        



        '''For the --> left subplot/Probabillity Density Function'''
        ax[0].grid(True)
        ax[0].title.set_text('Probability Mass Function')
        ax[0].set_xlabel('Descrete Value Events')
        ax[0].set_ylabel('Probability')
        ax[0].set_ylim([-0.1, 1.1])
        ax[0].set_xticks(x_events)
        ax[0].set_yticks(y_ticks)
        y_probabilities = [self.poisson_probability(slider_lambda.val, k) for k in x_events]

        sns.barplot(x=x_events, y=y_probabilities, errorbar=None, ax=ax[0])
        show_values_on_bars(ax[0]) # Show values on top of bar for target axis

        ax[0].plot(x_events, y_probabilities, lw=2, markersize=8, marker=None)




        '''For the --> right subplot/Cumulative Distribution Function'''
        ax[1].grid(True)
        ax[1].title.set_text('Cumulative Distribution Function')
        ax[1].set_xlabel('Descrete Value Events')
        ax[1].set_ylabel('Cumulative Probability')
        ax[1].set_xticks(x_events)
        ax[1].set_yticks(y_ticks)
        ax[1].set_ylim([-0.1, 1.1])
        cumulative_probabilities = np.cumsum(y_probabilities)

        sns.barplot(x=x_events, y=cumulative_probabilities, errorbar=None, ax=ax[1])
        show_values_on_bars(ax[1]) # Show values on top of bar for target axis

        ax[1].plot(x_events, cumulative_probabilities, lw=2, markersize=8, marker=None)      





        
        # Call update function when slider value is changed
        slider_events.on_changed(update)
        slider_lambda.on_changed(update)


        plt.subplots_adjust(left=0.075, right=0.95, top=0.75, bottom=0.2) # Adjusting the subplots placement


        plt.show()


def main():
    if len(sys.argv) < 7:
        helper_text()
        return

    discrete_START_event = int(sys.argv[1])
    discrete_END_event = int(sys.argv[2])
    discrete_TARGET_event = int(sys.argv[3])
    lambda_START_value = float(sys.argv[4])
    lambda_END_value = float(sys.argv[5])
    lambda_TARGET_value = float(sys.argv[6])

    if len(sys.argv) == 7:
        slider_discrete_event_steps = default_event_steps
        slider_lambda_steps = default_lambda_steps
    else:
        if len(sys.argv) > 9:
            print("\nGiven number of arguments is greater than expected number of arguments.\nPlease run 'possion.py' for help!\n")
        else:
            if len(sys.argv) == 8:
                slider_discrete_event_steps = float(sys.argv[7])
                slider_lambda_steps = default_lambda_steps
            elif len(sys.argv) == 9:
                slider_discrete_event_steps = float(sys.argv[7])
                slider_lambda_steps = float(sys.argv[8])

    # Checking if START_event < TARGET_event <= END_event
    if discrete_START_event < discrete_TARGET_event <= discrete_END_event:

        # Checking if lambda_START_val < lambda_TARGET_val <= lambda_END_val
        if lambda_START_value < lambda_TARGET_value <= lambda_END_value:
            Possion = PossionDistributionFunctions(discrete_START_event, discrete_END_event, discrete_TARGET_event, lambda_START_value, lambda_END_value, lambda_TARGET_value, slider_discrete_event_steps, slider_lambda_steps)
            Possion.starter()

        else:
            print("\n'START_event' should be less than 'TARGET_event', and 'TARGET_event' should be less than or equals to 'END_event'\nRun 'python possion.py' to get help.")

    else:
        print("\n'lambda_START_val' should be less than 'lambda_TARGET_val', and 'lambda_TARGET_val' should be less than or equals to 'lambda_END_val'\nRun 'python possion.py' to get help.")

    

if __name__ == "__main__":
    main()