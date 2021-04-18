from napari_plugin_engine import napari_hook_implementation
from ._qt import AnimationWidget


@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return (AnimationWidget, {'name': 'Wizard'})