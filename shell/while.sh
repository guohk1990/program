#! /bin/bash

while :
do
    echo -n "输入1 到 5 之间的数字:"
    read num
    case $num in
        1|2|3|4|5) echo "你输入的数字是: $num"
        ;;
        *) echo "你输入的不是1 到 5 之间的数字，游戏结束！";
        break;
        ;;
    esac
done
