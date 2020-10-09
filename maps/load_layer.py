import os
from django.contrib.gis.utils import LayerMapping
from .models import Jalan, Jembatan, Kesehatan, Drainase, Kab_Sidrap
    
jalan_mapping = {
    'geom': 'LINESTRING25D',
}

jalan_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'media', 'Jalan.shp'),
)

jembatan_mapping = {
    'geom': 'POINT25D',
}

jembatan_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'media', 'Jembatan.shp'),
)

kesehatan_mapping = {
    'geom': 'POINT25D',
}

kesehatan_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'media', 'Kesehatan.shp'),
)

drainase_mapping = {
    'geom': 'LINESTRING25D',
}

drainase_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'media', 'Drainase.shp'),
)

kab_sidrap_mapping = {
    'Provinsi': 'PROVINSI',
    'Kecamatan': 'KECAMATAN',
    'Desa': 'DESA',
    'Kabupaten': 'KABKOT',
    'geom': 'MULTIPOLYGON',
}

kab_sidrap_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'media', 'Kab_Sidrap.shp'),
)

def run(verbose=True):
    lm = LayerMapping(Jalan, jalan_shp, jalan_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

def run(verbose=True):    
    lm = LayerMapping(Jembatan, jembatan_shp, jembatan_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

def run(verbose=True): 
    lm = LayerMapping(Kesehatan, kesehatan_shp, kesehatan_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

def run(verbose=True):
    lm = LayerMapping(Drainase, drainase_shp, drainase_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

def run(verbose=True): 
    lm = LayerMapping(Kab_Sidrap, kab_sidrap_shp, kab_sidrap_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


