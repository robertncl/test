#!/usr/bin/env python

import yaml
import json

with open("input.yaml", "r") as input:
    try:
        #load the yaml input into a dict
        fstab_input = yaml.safe_load(input)
        
        #remove the first level of the input
        fstab_list = list(fstab_input.values())

        output = open("fstab.txt","a")
        
        #iterate through the nested dict inside the list
        for dic in fstab_list:
            for key, val in dic.items():
                
                #first write the device
                output.write(key + " ")
                
                #iterate through the dict and join the value into a string to append into the output
                for i in val.values():
                    listToStr = ''.join(map(str, i))
                    output.write(listToStr)
                    output.write(" ")
                    
                #add newline at the end of the loop
                output.write("\n")
                
        output.close()
        
    except yaml.YAMLError as exc:
        print(exc)
