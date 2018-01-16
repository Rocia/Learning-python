import re
import xml.etree.ElementTree as ET

rex = re.compile(r'''(?P<title>Longitude
                       |Latitude
                       |date&time
                       |gsm\s+cell\s+id
                       |Neighboring\s+List-\s+Lac\s+:\s+Cid\s+:\s+RSSI
                     )
                     \s*:?\s*
                     (?P<value>.*)
                     ''', re.VERBOSE)

root = ET.Element('root')
root.text = '\n'    # newline before the celldata element

with open('cell.txt') as f:
    celldata = ET.SubElement(root, 'celldata')
    celldata.text = '\n'    # newline before the collected element
    celldata.tail = '\n\n'  # empty line after the celldata element
    status = 0              # init status of the finite automaton
    for line in f:
        if status == 0:     # lines of the heading expected
            # If the line contains the wanted data, process it.
            m = rex.search(line)
            if m:
                # Fix some problems with the title as it will be used
                # as the tag name.
                title = m.group('title')
                title = title.replace('&', '')
                title = title.replace(' ', '')

                if line.startswith('Neighboring'):
                    neighbours = ET.SubElement(celldata, 'neighbours')
                    neighbours.text = '\n'
                    neighbours.tail = '\n'
                    status = 1  # empty line and then list of neighbours expected
                else:
                    e = ET.SubElement(celldata, title.lower())
                    e.text = m.group('value')
                    e.tail = '\n'
                    # keep the same status

        elif status == 1:   # empty line expected
            if line.isspace():
                status = 2  # list of neighbours must follow
            else:
                raise RuntimeError('Empty line expected. (status == {})'.format(status))
                status = 999 # error status

        elif status == 2:   # neighbour or the empty line as final separator

            if line.isspace():
                celldata = ET.SubElement(root, 'celldata')
                celldata.text = '\n'
                celldata.tail = '\n\n'
                status = 0  # go to the initial status
            else:
                # This is the neighbour item. Split it by colon,
                # and set the attributes of the item element.
                item = ET.SubElement(neighbours, 'item')
                item.tail = '\n'

                lac, cid, rssi = (a.strip() for a in line.split(':'))
                item.attrib['lac'] = lac
                item.attrib['cid'] = cid
                item.attrib['rssi'] = rssi.split()[0] # dBm removed
                # keep the same status

        elif status == 999: # error status -- break the loop
            break

        else:
            raise LogicError('Unexpected status {}.'.format(status))
            break

# Display for debugging
ET.dump(root)

# Include the root element to the tree and write the tree
# to the file.
tree = ET.ElementTree(root)
tree.write('cell.xml', encoding='utf-8', xml_declaration=True)
