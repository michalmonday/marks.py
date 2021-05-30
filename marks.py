# Python3 program which calculates final mark based on previous and potential future marks.
# How to use this program:
# - modify "previous_marks" list (line 18)
# - run the program
# If the program fails to run because of missing libraries, you can run the following command:
# python3 -m pip install matplotlib tk numpy

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


SECOND_YEAR_WEIGHT = 40
M_WEIGHT = 60 / 8           # single module weight (in 3rd year)

previous_marks = [
    # Format: (mark, weight)

    # 2nd year overall mark
    (70,   SECOND_YEAR_WEIGHT), 

    # total module marks
    (70,   M_WEIGHT),          # Some module final mark
    (70,   M_WEIGHT),          # Another module final mark
    (70,   M_WEIGHT),          # And another module final mark

    # module marks with some assessments unmarked yet
    (70,  M_WEIGHT * 0.06),     # This assessment was worth 6% of some module.
    (70,  M_WEIGHT * 0.12),     # This assessment was worth 12% of some module.
    (70,  M_WEIGHT * 0.12),     # This assessment was worth 12% of some module.
    (70,  M_WEIGHT * 0.1),      # This assessment was worth 10% of some module.
    (70,  M_WEIGHT * 0.2),      # This assessment was worth 20% of some module.
    ] 

def stats_so_far(pm):
    achieved = sum(w / 100.0 * m for m,w in pm)
    optimal = sum(w for _,w in pm)
    percentage = 100.0 / optimal * achieved
    # print(f"So far {optimal:.1f}% was assessed, for which I got {percentage:.1f}%")
    # print()
    return achieved, optimal, percentage
    
def calculate_total_mark(exam_mark, pm):
    achieved, optimal, percentage = stats_so_far(pm)
    remaining = 100 - optimal
    return achieved + remaining / 100.0 * exam_mark

def plot_stats(achieved, optimal):
    fig, (ax1, ax2) = plt.subplots(2, 1, sharex=False, sharey=False, gridspec_kw={'height_ratios': [1, 10]})
    ax1.set_title(f'Previous assessments ({achieved:.1f}% out of {optimal:.1f}%)')
    achieved = int(achieved)
    optimal = int(optimal)
    ax1.set_xticks(range(0,101,10))
    ax1.set_xlim([0,100])
    ax1.set_ylim([0,1])
    ax1.tick_params(axis='y', left=False, labelleft=False, which='both')
    ax1.fill_between(np.arange(0, achieved+1, 1), 0, 1, facecolor='g', alpha=1)
    ax1.fill_between(np.arange(achieved, optimal+1, 1), 0, 1, facecolor='red', alpha=0.5)
    ax1.fill_between(np.arange(optimal, 101, 1), 0, 1, facecolor='black', alpha=0.2)
    ax2_min = 30
    total_x = range(ax2_min,101,1)
    total_y = [calculate_total_mark(em, previous_marks) for em in total_x]
    ax2.set_yticks(range(0,101,10))
    ax2.set_ylim([0,100])
    ax2.set_xticks(range(ax2_min,101,10))
    ax2.set_xlim([ax2_min,100])
    ax2.fill_between(total_x, total_y, 100, facecolor='red', alpha=0.5)
    ax2.fill_between(total_x, 0, total_y, facecolor='green', alpha=1)
    lw = 3
    for line_y, clr in [(70,'cyan'), (60, 'yellow'), (50, 'orange'), (40, 'red')]:
        ax2.axhline(y=line_y, color=clr, linestyle='-', linewidth=lw)
    ax2.set_title("End mark prediction")
    ax2.set_ylabel("End mark")
    ax2.set_xlabel("Remaining assessments mark")
    plt.subplots_adjust(hspace=0.5)
    plt.show()

achieved, optimal, percentage = stats_so_far(previous_marks)
plot_stats(achieved, optimal)


