from django.contrib.gis.geos import Point

from voxel_globe.common_tasks import shared_task, VipTask
from voxel_globe.serializers.numpyjson import NumpyAwareJSONEncoder
import voxel_globe.meta.models

import numpy
import json

@shared_task(base=VipTask, bind=True)
def addTiePoint(self, x,y,*args, **kwargs):
  tp = voxel_globe.meta.models.TiePoint(point=Point(x,y), *args, **kwargs)
  tp.service_id = self.request.id
  tp.save()
  return tp.id

def fetchCameraFrustum(imageId, cameraSetId, size=100, output='json', **kwargs):
  from voxel_globe.meta.tools import projectPoint
  from voxel_globe.tools.camera import get_kto
  try:
    image_id = int(imageId)
    camera_set_id = int(cameraSetId)
    size = int(size) #Size in meters
    image = voxel_globe.meta.models.Image.objects.get(id=image_id)

    w = image.image_width
    h = image.image_height
    K, T, llh = get_kto(image, camera_set_id)
    llh1 = projectPoint(K, T, llh, numpy.array([0]), numpy.array([0]), distances=0) 
    llh2 = projectPoint(K, T, llh, numpy.array([0,w,w,0]), numpy.array([0,0,h,h]), distances=size)

    llh2['lon'] = numpy.concatenate((llh1['lon'], llh2['lon']))
    llh2['lat'] = numpy.concatenate((llh1['lat'], llh2['lat']))
    llh2['h']   = numpy.concatenate((llh1['h'],   llh2['h']))

    if output == 'json':
      return json.dumps(llh2, cls=NumpyAwareJSONEncoder)
    elif output == 'kml':
      kml = '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
  <name>KmlFile</name>
  <Style id="s_ylw-pushpin">
    <IconStyle>
      <scale>1.1</scale>
      <Icon>
        <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
      </Icon>
      <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
    </IconStyle>
  </Style>
  <StyleMap id="m_ylw-pushpin">
    <Pair>
      <key>normal</key>
      <styleUrl>#s_ylw-pushpin</styleUrl>
    </Pair>
    <Pair>
      <key>highlight</key>
      <styleUrl>#s_ylw-pushpin_hl</styleUrl>
    </Pair>
  </StyleMap>
  <Style id="s_ylw-pushpin_hl">
    <IconStyle>
      <scale>1.3</scale>
      <Icon>
        <href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
      </Icon>
      <hotSpot x="20" y="2" xunits="pixels" yunits="pixels"/>
    </IconStyle>
  </Style>
  <Placemark>
    <name>Untitled Path</name>
    <styleUrl>#m_ylw-pushpin</styleUrl>
    <LineString>
      <tessellate>1</tessellate>
      <altitudeMode>absolute</altitudeMode>
      <coordinates>'''
      for x in [0,1,0,2,0,3,0,4,3,2,1,4]:
        kml += '%0.12g,%0.12g,%0.12g ' % (llh2['lon'][x], llh2['lat'][x], llh2['h'][x])
      kml += '''      </coordinates>
    </LineString>
  </Placemark>
</Document>
</kml>'''
      return kml
  except voxel_globe.meta.models.Image.DoesNotExist:
    pass

  return ''


def fetchCameraRay(imageId, cameraSetId, height=-100, **kwargs):
  from voxel_globe.meta.tools import projectPoint
  from voxel_globe.tools.camera import get_kto
  try:
    image_id = int(imageId)
    camera_set_id = int(cameraSetId)

    height = int(height) #altitude of death valley :)

    image = voxel_globe.meta.models.Image.objects.get(id=image_id)
    x = int(kwargs.pop('X', image.image_width/2))
    y = int(kwargs.pop('Y', image.image_height/2))

    K, T, llh = get_kto(image, camera_set_id)
    llh1 = projectPoint(K, T, llh, numpy.array([x]), numpy.array([y]), distances=0) 
    llh2 = projectPoint(K, T, llh, numpy.array([x]), numpy.array([y]), zs=numpy.array([height]))

    llh2['lon'] = numpy.concatenate((llh1['lon'], llh2['lon']))
    llh2['lat'] = numpy.concatenate((llh1['lat'], llh2['lat']))
    llh2['h']   = numpy.concatenate((llh1['h'], llh2['h']))

    return json.dumps(llh2, cls=NumpyAwareJSONEncoder)
  except voxel_globe.meta.models.Image.DoesNotExist:
    pass

  return ''
