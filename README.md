## Demo Control shape manager for Maya
*This repo is used for demonstration purposes, to be followed along with in this blog post*

http://bindpose.com/creating-maya-control-shape-manager

Scroll down for an example GIF.

### Usage
1. Copy the `controlShapeManager` folder to your maya scripts path - typically `C:/Users/username/maya/scripts`.
2. In `__init__.py` change the `SHAPE_LIBRARY_PATH` to the path where you would like to store your control shapes.
3. In `__init__.py` change `SHELF_NAME` to the name of the shelf where you want to create the example button for the manager.
4. Run the following code, which will create a button, containing a dropdown menu, on the specified shelf.
```python
import controlShapeManager
```
5. *(Optional)* To get the colours working you need to get the images from [here](https://www.dropbox.com/sh/osdatp13h01coz7/AAB9pCYP9uBZRaVRjYKqIk--a?dl=1). Then in `__init__.py` change `ICON_PATH` to the path where you've saved them.

### Example
![](http://bindpose.com/wp-content/uploads/2017/05/2017-05-01_08-54-21.gif)



