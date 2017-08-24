"""
Folium plugins
--------------

Add different objects/effects on a folium map.
"""

from __future__ import (absolute_import, division, print_function)

from folium.plugins.boat_marker import BoatMarker
from folium.plugins.fast_marker_cluster import FastMarkerCluster
from folium.plugins.float_image import FloatImage
from folium.plugins.fullscreen import Fullscreen
from folium.plugins.heat_map import HeatMap
from folium.plugins.image_overlay import ImageOverlay
from folium.plugins.marker_cluster import MarkerCluster
from folium.plugins.measure_control import MeasureControl
from folium.plugins.polyline_text_path import PolyLineTextPath
from folium.plugins.scroll_zoom_toggler import ScrollZoomToggler
from folium.plugins.terminator import Terminator
from folium.plugins.timestamped_geo_json import TimestampedGeoJson
from folium.plugins.timestamped_wmstilelayer import TimestampedWmsTileLayers

__all__ = [
    'BoatMarker',
    'FastMarkerCluster',
    'FloatImage',
    'Fullscreen',
    'HeatMap',
    'ImageOverlay',
    'MarkerCluster',
    'MeasureControl',
    'PolyLineTextPath',
    'ScrollZoomToggler',
    'Terminator',
    'TimestampedGeoJson',
    'TimestampedWmsTileLayers'
    ]
