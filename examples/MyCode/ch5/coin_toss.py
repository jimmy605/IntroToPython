import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

count = 200_000

tosses = [random.randrange(1, 3) for i in range(count)]
values, frequencies = np.unique(tosses,return_counts=True)
title = f'Coin toss for {len(tosses):,} total tosses'
sns.set_style('whitegrid')
axes = sns.barplot(x=values, y=frequencies, palette='bright')

axes.set_title(title)
axes.set(xlabel='Heads = 1 Tails = 2', ylabel='Frequency')

axes.set_ylim(top=max(frequencies) * 1.10)
for bar, frequency in zip(axes.patches, frequencies): 
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(tosses):.3%}' 
    axes.text(text_x, text_y, text,
            fontsize=11, ha='center', va='bottom')

plt.show()