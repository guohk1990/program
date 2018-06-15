#! /bin/bash

sum=0

function fun(){
    if [ $1 -eq 0 ];then
        echo $sum
    else
        let sum+=$1
        fun $(($1-1))
    fi
}

fun $1
