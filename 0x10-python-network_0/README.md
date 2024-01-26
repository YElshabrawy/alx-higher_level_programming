# 0x10-python-network_0

## `grep` notes:
- `grep -i` is used to perform a case-insensitive search when using the grep command, ignoring distinctions between uppercase and lowercase letters.

## `curl` notes:
- `curl -I` is used to display only the HTTP headers of the response without fetching the actual content when making a request with curl.
- `curl -s` is used to (silence) disable the progress meter in the output
- `curl -L` is used to instruct the curl command to follow HTTP redirects automatically. (lw fyh 301 yredirect automatic w yro7 ll new location)
- `curl -X` used to specify the HTTP request method (e.g., GET, POST, PUT) when making a request with curl.
- `curl -H` is used to include HTTP headers in a key-value string "key: value"

## `awk` notes:
- `awk '{print $2}'` is an awk command that extracts and prints the second field (column) from each line of input, based on the default field separator (whitespace).
	- To change separator use `-F`
	```
	awk -F',' '{print $2}' # separator => ","
	```
