# Plugins  
All plugins:  
* is_visible: boolean  
* in_navigation: boolean  
* css_class: charfield
* name: charfield
* show_name: boolean

## Sections  
Module: Layout  
Plugins:  
* WrapPlugin: standard section container  

## Columns  
Module: Layout
Plugins:
* ColumnWrapPlugin: section which can only have ColumnPlugin as child  
* ColumnPlugin: column...  

## Headers  
Module: Content  
Plugins:  
* HeaderPlugin: Intentionaly simple image "mood" plugin. for more complex choices use look at pictures and sliders  

## Iframes  
Module: Content  
Plugins:  
* IFramePlugin: Simple Iframe Plugin with aspect ratio definition  

### Maps  
Module: Content  
Plugins:  
* GoogleMapPlugin: Advanced google maps plugin, with settings  
* GoogleStreetViewPlugin:   Advanced google street view plugin, with settings

## Pictures  
Module: Content  
Plugins:  
* GalleryPlugin: Gallery, can only have GalleryPicturePlugin as child  
* PicturePlugin  

## Sliders  
Module: Content  
Plugins:  
* SliderPlugin: Simple slider, can only have SliderSlidePluginPlugin as child  
* SliderSlidePluginPlugin: Slide plugin for SliderPlign  
* SlideshowPlugin:  !!! TODO !!!  
* SlideshowSlidePluginPlugin: !!! TODO !!!  

### Videos  
Module: Content  
Plugins:  
* VideoPlugin: Youtube & Vimeo video plugin  
