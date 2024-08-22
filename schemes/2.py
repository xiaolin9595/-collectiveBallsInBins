# #!/usr/bin/env python
# import math
# import sys
# from tabulate import tabulate
# from schemes import *

# def makeRow(name, scheme, tex):
#     comsize = '{:.2f}'.format(round(scheme["comsize"] / 8000.0, 2))
#     encodingsize = '{:.2f}'.format(round(scheme["encodingsymbolsize"] * scheme["encodinglength"] / 8000000.0, 2))
#     commpqsize = '{:.2f}'.format(round(scheme["commpqsize"] / 8000.0, 2))
#     reception = scheme["reception"]
#     encodinglength = scheme["encodinglength"]
#     samples = scheme["samples"]
#     commsize = '{:.2f}'.format(round(scheme["commpqsize"] * samples / 8000000.0, 2))
#     if tex:
#         row = ["\\Inst" + name, comsize, encodingsize, commpqsize, samples, commsize]
#     else:
#         row = [name, comsize, encodingsize, commpqsize, (reception, encodinglength), samples, commsize]
#     return row

# #####################################################################
# opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
# args = [arg for arg in sys.argv[1:] if not opt.startswith("-")]
# if len(args) == 0:
#     print("Missing Argument: Datasize in Megabytes.")
#     print("Hint: To print the table in LaTeX code, add the option -l.")
#     sys.exit(-1)

# datasize = int(args[0]) * 8000000
# tex = False

# # Print to LaTeX
# if "-l" in opts:
#     tex = True

# if tex:
#     table = [["Name", "|com|", "|Encoding|", "Comm. p. Q.", "Reception", "Samples", "Comm Total"]]
# else:
#     table = [["Name", "|com| [KB]", "|Encoding| [MB]", "Comm. p. Q. [KB]", "Reception", "Samples", "Comm Total [MB]"]]

# scheme = makeNaiveScheme(datasize)
# table.append(makeRow("Naive", scheme, tex))
# scheme = makeMerkleScheme(datasize)
# table.append(makeRow("Merkle", scheme, tex))
# scheme = makeKZGScheme(datasize)
# table.append(makeRow("RS", scheme, tex))
# scheme = makeTensorScheme(datasize)
# table.append(makeRow("Tensor", scheme, tex))
# scheme = makeHashBasedScheme(datasize)
# table.append(makeRow("Hash", scheme, tex))
# scheme = makeHomHashBasedScheme(datasize)
# table.append(makeRow("HomHash", scheme, tex))

# if tex:
#     print(tabulate(table, headers='firstrow', tablefmt='latex_raw', disable_numparse=True))
# else:
#     print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))







#!/usr/bin/env python
import math
import sys
from tabulate import tabulate
from schemes import *

def makeRow(name, scheme, tex):
    comsize = '{:.2f}'.format(round(scheme["comsize"] / 8000.0, 2))
    encodingsize = '{:.2f}'.format(round(scheme["encodingsymbolsize"] * scheme["encodinglength"] / 8000000.0, 2))
    commpqsize = '{:.2f}'.format(round(scheme["commpqsize"] / 8000.0, 2))
    reception = scheme["reception"]
    encodinglength = scheme["encodinglength"]
    samples = scheme["samples"]
    commsize = '{:.2f}'.format(round(scheme["commpqsize"] * samples / 8000000.0, 2))
    if tex:
        row = ["\\Inst" + name, comsize, encodingsize, commpqsize, samples, commsize]
    else:
        row = [name, comsize, encodingsize, commpqsize, (reception, encodinglength), samples, commsize]
    return row

####################################################################
opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]
if len(args) == 0:
    print("Missing Argument: Datasize in Megabytes.")
    print("Hint: To print the table in LaTeX code, add the option -l.")
    sys.exit(-1)

datasize = int(args[0]) * 8000000
tex = False

# Print to LaTeX
if "-l" in opts:
    tex = True

if tex:
    table = [["Name", "|com|", "|Encoding|", "Comm. p. Q.", "Reception", "Samples", "Comm Total"]]
else:
    table = [["Name", "|com| [KB]", "|Encoding| [MB]", "Comm. p. Q. [KB]", "Reception", "Samples", "Comm Total [MB]"]]

scheme = makeNaiveScheme(datasize)
table.append(makeRow("Naive", scheme, tex))
scheme = makeMerkleScheme(datasize)
table.append(makeRow("Merkle", scheme, tex))
scheme = makeKZGScheme(datasize)
table.append(makeRow("RS", scheme, tex))
scheme = makeTensorScheme(datasize)
table.append(makeRow("Tensor", scheme, tex))
scheme = makeHashBasedScheme(datasize)
table.append(makeRow("Hash", scheme, tex))
scheme = makeHomHashBasedScheme(datasize)
table.append(makeRow("HomHash", scheme, tex))

if tex:
    print(tabulate(table, headers='firstrow', tablefmt='latex_raw', disable_numparse=True))
else:
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))