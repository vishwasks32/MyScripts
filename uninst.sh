#!/bin/sh
input="/root/lnt.txt" #change for different files
while IFS= read -r var
do
        echo "Uninstalling ....."
        echo "$var"
        removepkg $var 
        if [ $? -eq 0 ]; then
                echo "OK"
        else
                echo "FAIL"
        fi
done < "$input"
