###############################################################################
# Sample to write content a flowfile from json format
# modified from "https://github.com/BatchIQ/nifi-scripting-samples"
#
# Assumed input json format: 
# { 
#   "tagname": "first",
#   "value": 12345,
#   "message": "Foo"
#   "timesatmp": 1514541007050
#               }
# output
# {
#   "tagname": "first",
#   "value": 152399025,
#   "message": "Hello World"
#   "timesatmp": 1514541007050
#               }
# }
###############################################################################

import json
import sys
import traceback
from datetime import datetime, timedelta, timezone
from java.nio.charset import StandardCharsets
from org.apache.commons.io import IOUtils
from org.apache.nifi.processor.io import StreamCallback
from org.python.core.util import StringUtil


class TransformCallback(StreamCallback):
    def __init__(self):
        pass

    def process(self, inputStream, outputStream):
        try:
            # Read input FlowFile content
            input_text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
            input_obj = json.loads(input_text)

            # Transform content
            output_obj = input_obj
            # Write output content
            outputStream.write(StringUtil.(output_obj['values']))
        except:
            traceback.print_exc(file=sys.stdout)
            raise


flowFile = session.get()
if flowFile != None:
    flowFile = session.write(flowFile, TransformCallback())

    # Finish by transferring the FlowFile to an output relationship
session.transfer(flowFile, REL_SUCCESS)