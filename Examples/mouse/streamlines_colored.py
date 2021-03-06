"""
    This tutorial shows you how to render efferent mesoscale connectivity
    data from the Allen mouse connectome project as streamlines coloring
    each injection's streamline individually. 

"""

from brainrender.scene import Scene
from brainrender.colors import makePalette


# Start by creating a scene with the allen brain atlas atlas
scene = Scene(title="streamlines")


# Download streamlines data for injections in the CA1 field of the hippocampus
filepaths, data = scene.atlas.download_streamlines_for_region("CA1")


scene.add_brain_regions(["CA1"], use_original_color=True, alpha=0.2)

# you can pass either the filepaths or the data
colors = makePalette(len(data), "salmon", "lightgreen")
scene.add_streamlines(data, color=colors, show_injection_site=False)

scene.render(camera="sagittal", zoom=1)
