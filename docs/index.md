# Plugins  
All plugins:  
* is_visible: boolean  
* in_navigation: boolean  
* bg_color: charfield  
* css_class: charfield
* height: charfield
* width: charfield
* name: charfield
* show_name: boolean

## Example conf
```python
CMSPLUGINS: {
    # Defaults for all cmslugins
    'defaults': {
        'bg_colors': [
            ('', _('---')),
            ('bg-bright', _('bright')),
            ('bg-dark', _('dark')),
        ],
        'css_classes': [
            ('', _('---')),
        ],
        'heights': [
            ('', _('defined by css')),
            ('window-height h-100', _('full window height')),
        ],
        'widths': [
            ('', _('defined by css')),
            ('w-100', _('100%')),
            ('w-50', _('50%')),
        ],
    },
    # cmsplugins.ColumnPlugin configuration
    'ColumnPlugin': {
        'allow_children': True,
        'child_classes': ['ColumnPlugin', 'PicturePlugin'],
        'required_fields': ['bg_color'],
        'fieldsets':
            ('settings', {
                'classes': ['section', 'collapse'],
                'fields': ['is_visible', 'in_navigation'],
            }),
            ('style', {
                'classes': ['section', 'collapse'],
                'fields': ['bg_color', 'css_class', 'width', 'height'],
            }),
            ('title', {
                'classes': ['section', 'title'],
                'fields': ['name', 'show_name'],
            }),
        ),
        'widgets': {
            'bg_color': {
                'widget': 'Select',
                'choices': [('', 'choice 1'), ('choice-2', 'choice 2')],
            },
        }
    },
}
```

## Available Plugins
### Sections  
Module: Layout  
Plugins:  
* WrapPlugin: standard section container  

### Columns  
Module: Layout
Plugins:
* ColumnPlugin: column...  

### Headers  
Module: Content  
Plugins:  
* HeaderPlugin: Intentionaly simple image "mood" plugin. for more complex choices check pictures and sliders  

### Iframes  
Module: Content  
Plugins:  
* IFramePlugin: Simple Iframe Plugin with aspect ratio definition  

### Maps  
Module: Content  
Plugins:  
* GoogleMapPlugin: Advanced google maps plugin, with settings  
* GoogleStreetViewPlugin:  Advanced google street view plugin, with settings  

### Pictures  
Module: Content  
Plugins:  
* GalleryPlugin: Gallery, can only have GalleryPicturePlugin as child  
* PicturePlugin: Picture ...  

### Sliders  
Module: Content  
Plugins:  
* SliderPlugin: Simple slider, can only have SliderSlidePluginPlugin as child  
* SliderSlidePluginPlugin: Slide plugin for SliderPlugin  
* SlideshowPlugin:  !!! TODO !!!  
* SlideshowSlidePluginPlugin: !!! TODO !!!  

### Videos  
Module: Content  
Plugins:  
* VideoPlugin: Youtube & Vimeo video plugin  
