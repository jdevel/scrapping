import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')
root = tree.getroot()
root.tag
