#!/bin/bash

su avahi -s /bin/bash -c  "avahi-set-host-name $1"
