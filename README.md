# CheckMK Local Check: pfSense Usage per Interface

While the CheckMK agent is able to monitor out of the box every interface, pppoe Interfaces won't be tracked. Therefore I had to write this little Local Check

## Requirements

 - Installed CheckMK Agent into pfsense. Tested on pfsense 2.5.2

## Installation

 - Move python script into the local scripts folder of the Agent.
   Default is `/usr/local/lib/check_mk_agent/local`
 - Edit Variables in line 3 and match it with the interfaces you want to test
 - Make the script exexuteable with `chmod +x`
