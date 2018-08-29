"""import re

# Lets use a regular expression to match a date string. Ignore
# the output since we are just testing if the regex matches.
regex = r"([a-zA-Z]+) (\d+)"
if re.search(regex, "June 24"):
    # Indeed, the expression "([a-zA-Z]+) (\d+)" matches the date string

    # If we want, we can use the MatchObject's start() and end() methods
    # to retrieve where the pattern matches in the input string, and the
    # group() method to get all the matches and captured groups.
    match = re.search(regex, "June 24")

    # This will print [0, 7), since it matches at the beginning and end of the
    # string
    print("Match at index %s, %s" % (match.start(), match.end()))

    # The groups contain the matched values.  In particular:
    #    match.group(0) always returns the fully matched string
    #    match.group(1), match.group(2), ... will return the capture
    #            groups in order from left to right in the input string
    #    match.group() is equivalent to match.group(0)

    # So this will print "June 24"
    print("Full match: %s" % (match.group(0)))
    # So this will print "June"
    print("Month: %s" % (match.group(1)))
    # So this will print "24"
    print("Day: %s" % (match.group(2)))
else:
    # If re.search() does not match, then None is returned
    print("The regex pattern does not match. :(")"""

import re

file1 = open("/home/asm/Downloads/diag.out", "r ")
l1 = []

for line in file1:
	str1 = re.match("----- APmgr info: apmgrinfo -a", line, re.M|re.I)
	if str1:
		for lines in file1:
			l1.append(lines)
			str2 = re.match("----- Disconnected APs: wlaninfo --all-disc-ap -l 3", lines, re.M|re.I)
			if str2:
				break

l2 = []
for x in l1:
    if x == "":
    #s1 = re.match("Model/Serial Num ", x, re.M|re.I)
    #if s1:
        #for x in l1:
            l2.append(x)
#for y in l2:
 #print x
mac = []
for i in l1:
    m = re.search(r'[a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}', i)
    if m:

           print "MAC Address :\t",

    if mac == m:
		       print " mac", mac

for i in l1:
    ip = re.search('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}'
                +'(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))', i)
    if ip:
	    mac == ip
	    print " ip address:\t"  , ip.group()

for i in l1:
 patt = re.search('''^([2][0-5][0-5]|^[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})\.([0-2][0-5][0-5]|[1]{0,1}[0-9]{1,2})$''', i)
 if patt:
		print " ipv4 address:\t"  , patt.group()

for i in l1:
	name =  re.search('[A-ZA-Z0-90-90-90-9][-]+[A-ZA-ZA-Z0-90-90-90-9]]',i)
	if name:
		 print "name:\t", name.group()
		 #re.search('([A-H][A-Z][0-9][0-9][0-9][0-9][0-9])' + '([W-Z][A-Z][0-9][0-9][0-9][0-9])', i)



for i in l1:
	name =  re.search('[A-ZA-Z0-9]+[0-90-90-90-9][-]+[A-ZA-Z0-9]+[0-90-90-90-9]',i)
	if name:
		 print "name:\t", name.group()

for i in l1:
	state = re.search('[R][U][N]',i)
	if state:
		 print "state:\t", state.group()

for i in l1:
	tunnel = re.search('[L][3]',i)
	if tunnel:
		 print "tunnel:\t", tunnel.group()

for i in l1:
	SEC_MODE = re.search('[P][S][K]',i)
	if SEC_MODE:
		 print "SEC_MODE:\t", SEC_MODE.group()

for i in l1:
	MESH_ROLE = re.search('[M][E][S][H]+ [A][P]',i)
	if MESH_ROLE:
		 print "MESH_ROLE:\t", MESH_ROLE.group()

for i in l1:
	psk = re.search('[a-zA-Z0-9]+[~!@#$%^&*()_+{}:"|<>?,./;]+[a-zA-Z0-9]+[~!@#$%^&*()_+{}:"|<>?,./;]+[a-zA-Z0-9]+[~!@#$%^&*()_+{}:"|<>?,./;]+[a-zA-Z0-9]+[~!@#$%^&*()_+{}:"|<>?,./;]+[a-zA-Z0-9]+[~!@#$%^&*()_+{}:"|<>?,./;]+[a-zA-Z0-9]+[~!@#$%^&*()_+{}:"|<>?,./;]+',i)
	if psk:
		 print "PSK:\t", psk.group()

for i in l1:
	timer = re.search('[A-Za-za-za-z]+[a-za-za-za-za-z][,\s]+[a-z]+[a-z\s]+[a-z]+[a-z\s] +[a-z]+ [0-90-9]+ [a-z][a-z][a-z]',i)
	if timer:
		 print "timer:\t", timer.group()

for i in l1:
    hw = re.search('[0-9][0-9]+[.][0-9][.][0-9][.][0-9]', i)
    if hw:
        print "H_version:\t", hw.group()

for i in l1:
    sw = re.search('[0-9]+[.][0-9][.][0-9][.][0-9][.][0-9][0-9][0-9]', i)
    if sw:
        print "S_version:\t", sw.group()

for i in l1:
    model = re.search('[a-z][a-z]+[0-9]+[0-9][0-9][0-9]', i)
    if model:
        print "model:\t", model.group()

for i in l1:
    num = re.search('[0-9]+[0-9]+[0-9]+[0-9]+[0-9]+[0-9][0-9][0-9][0-9]', i)
    if num:
        print "serial_number:\t", num.group()
