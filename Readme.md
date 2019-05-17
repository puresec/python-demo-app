
## Installation

* Make sure you have the Serverless framework installed, and use sls deploy

## Usage

* Use this to execute a command (for example `ls`): `curl --header "Content-Type: application/json"  --request POST  --data '{"cmd":"ls"}' API_GATEWAY_URL`
* Use this to print a file's contents (for example `/etc/password`): `curl --header "Content-Type: application/json"  --request POST  --data '{"filename":"/etc/passwd"}' API_GATEWAY_URL`
