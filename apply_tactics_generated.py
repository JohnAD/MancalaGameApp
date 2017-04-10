import os
import json
from copy import copy

import tactics
from tactics_generator import SCENARIOS, FILENAMES, PROTO_GENOME

tactics_list = PROTO_GENOME['genes']

with open("tactics_data.py", 'w') as outfile:
    outfile.write('# DO NOT EDIT: autogenerated by "apply_tactics_generated.py"\n\n')
    outfile.write("TDATA = {}\n")
    for index, filename in enumerate(FILENAMES):
        tup = SCENARIOS[index]
        msg = "file missing; repeating content"
        if os.path.exists(filename):
            try:
                with open(filename, 'r') as infile:
                    genome = json.load(infile)
                    tactics_list = copy(genome['genes'])
                    msg = 'pulled from "{}"'.format(filename)
            except Exception as e:
                print e
        outfile.write("# {} :\n".format(msg))
        outfile.write("TDATA[{}] = \\\n".format(tup))
        outfile.write("    {}\n".format(tactics_list))
    outfile.write("\n")
    outfile.write('# DO NOT EDIT: autogenerated by "apply_tactics_generated.py"\n')
