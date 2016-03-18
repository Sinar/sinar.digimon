from collective.grok import gs
from sinar.digimon import MessageFactory as _

@gs.importstep(
    name=u'sinar.digimon', 
    title=_('sinar.digimon import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinar.digimon.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
