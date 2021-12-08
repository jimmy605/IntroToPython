import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

survey = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

values, frequencies = np.unique(survey,return_counts=True)
title = f'Frequency for each rating. A total of {len(survey):,}'
sns.set_style('whitegrid')
axes = sns.barplot(x=values, y=frequencies, palette='bright')

axes.set_title(title)
axes.set(xlabel='Rating', ylabel='Frequency')

axes.set_ylim(top=max(frequencies) * 1.10)
for bar, frequency in zip(axes.patches, frequencies): 
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(survey):.3%}' 
    axes.text(text_x, text_y, text,
            fontsize=11, ha='center', va='bottom')

plt.show()