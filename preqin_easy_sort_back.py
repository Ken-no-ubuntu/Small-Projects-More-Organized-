import matplotlib.pyplot as plt
import numpy as np

def create_multi_line_graph(data_sets, title="My Graph", x_label="X Axis", y_label="Y Axis", 
                          fig_size=(10, 6), labels=None):
    """
    Create a graph with multiple lines
    
    Parameters:
    -----------
    data_sets : list of tuples
        List containing (x_data, y_data) tuples for each line
    title : str
        Title of the graph
    x_label : str
        Label for x-axis
    y_label : str
        Label for y-axis
    fig_size : tuple
        Size of the figure (width, height)
    labels : list
        List of labels for each line (for legend)
    """
    # Create figure and axis objects
    plt.figure(figsize=fig_size)
    
    # Plot each line
    for i, (x_data, y_data) in enumerate(data_sets):
        label = labels[i] if labels else f"Line {i+1}"
        plt.plot(x_data, y_data, label=label)
    
    # Add title and labels
    plt.title(title, fontsize=14, pad=15)
    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    
    # Add grid and legend
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # Adjust layout
    plt.tight_layout()
    
    # Show the plot
    plt.show()
"""
# Example usage:
if __name__ == "__main__":
    # Generate sample data for multiple lines
    x = np.linspace(0, 20, 60)
    y1 = x      # First line
    y2 = (x+20)    # Second line
    y3 = -x + 10
    y4 = (-x +20) + 20       # Third line
    
    # Create data sets
    data_sets = [
        (x, y1),
        (x, y2),
        (x, y3),
        (x, y4)
    ]
    
    # Create labels for each line
    labels = ["AS Japan", "AS Japan", "AD Japan", "AD outside Japan"]
    
    # Create the multi-line graph
    create_multi_line_graph(
        data_sets=data_sets,
        labels=labels,
        title="AD-AS Analysis",
        x_label="Real Output",
        y_label="Price Level",
        fig_size=(10, 6)
    )

    """

if __name__ == "__main__":
    # Generate sample data for multiple lines
    x = np.linspace(0, 50, 60)
    y1 = np.full_like(x, 20)      # Horizontal line at y=20
    y2 = np.full_like(x, 30)
    y3 = -x + 40       # Third line
    
    # Create data sets
    data_sets = [
        (x, y1),
        (x, y2),
        (x, y3),
    ]
    
    # Create labels for each line
    labels = ["Initial MP", "Post MP", "IS curve"]
    
    # Create the multi-line graph
    create_multi_line_graph(
        data_sets=data_sets,
        labels=labels,
        title="IS-MP model",
        x_label="Output",
        y_label="Interest Rate",
        fig_size=(10, 6)
    )