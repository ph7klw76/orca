import matplotlib.pyplot as plt

def draw_energy_levels(singlet_levels, triplet_levels, offset=0.05, text_offset=0.1):
    fig, ax = plt.subplots()

    # Sort the energy levels
    singlet_levels.sort()
    triplet_levels.sort()

    # Function to add small offset to near-degenerate states
    def add_offset(levels):
        new_levels = []
        i = 0
        while i < len(levels):
            level = levels[i]
            count = levels.count(level)
            if count > 1:
                for j in range(count):
                    new_levels.append(level + j * offset - (count - 1) * offset / 2)
                i += count
            else:
                new_levels.append(level)
                i += 1
        return new_levels

    singlet_levels = add_offset(singlet_levels)
    triplet_levels = add_offset(triplet_levels)

    # Draw singlet energy levels
    previous_level = None
    for i, level in enumerate(singlet_levels):
        ax.hlines(level, xmin=0, xmax=1, color='b', linewidth=2, label='Singlet' if i == 0 else "")
        alignment = 'left' if i % 2 == 0 else 'right'
        
        # Adjust the text position to prevent overlap
        x_position = 0.25
        if previous_level is not None and abs(level - previous_level) < text_offset:
            x_position += text_offset if x_position == 0.25 else -text_offset
        
        ax.text(x_position, level, f"$S_{{{i+1}}}$", verticalalignment='bottom', horizontalalignment=alignment, fontsize=12, color='b')
        previous_level = level

    # Draw triplet energy levels
    previous_level = None
    for ii, level in enumerate(triplet_levels):
        ax.hlines(level, xmin=2, xmax=3, color='r', linewidth=2, label='Triplet' if ii == 0 else "")
        alignment = 'left' if ii % 2 == 0 else 'right'
        
        # Adjust the text position to prevent overlap
        x_position = 2.0
        if previous_level is not None and abs(level - previous_level) < text_offset:
            x_position += text_offset if x_position == 2.0 else -text_offset
        
        ax.text(x_position, level, f"$T_{{{ii+1}}}$", verticalalignment='bottom', horizontalalignment=alignment, fontsize=12, color='r')
        previous_level = level

    # Add labels and title
    ax.set_title('Energy Level Diagram', fontsize=16)
    ax.set_xlabel('Energy Levels', fontsize=16)
    ax.set_ylabel('Energy (eV)', fontsize=16)
    ax.yaxis.set_tick_params(labelsize=16)
    
    # Place the legend in the middle
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), fontsize=16)

    # Show the plot
    plt.show()

# Sample singlet and triplet energy levels in eV
singlet_levels = [3.405,3.405,3.453,3.454,3.666,3.743,3.831,3.840,3.919,3.919,4.068,4.109,4.109,4.163,4.164,4.176,4.180,4.230,4.232,4.337]
triplet_levels = [3.108,3.291,3.292,3.371, 3.372,3.401,3.416,3.426,3.478,3.479,3.575,3.576,3.632,3.652,3.697,3.713,3.846,3.847,3.903,3.903]  
draw_energy_levels(singlet_levels, triplet_levels)
