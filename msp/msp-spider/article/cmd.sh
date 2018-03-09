#!/usr/bin/env bash

RUN_NAME='run.py'

# PID  代表是PID文件
PID=$RUN_NAME\.pid

#使用说明，用来提示输入参数
usage() {
    echo "Usage: sh 执行脚本.sh [start|stop|restart|status]"
    exit 1
}

#检查程序是否在运行
is_exist(){
  pid=`ps -ef|grep $RUN_NAME|grep -v grep|awk '{print $2}' `
  #如果不存在返回1，存在返回0
  if [ -z "${pid}" ]; then
   return 1
  else
    return 0
  fi
}

#启动方法
start(){
  is_exist
  if [ $? -eq "0" ]; then
    echo ">>> ${RUN_NAME} is already running PID=${pid}"
  else
    nohup python -u $RUN_NAME >out.log 2>&1 &
    echo $! > $PID
    echo ">>> start $RUN_NAME successed PID=$!"
   fi
  }

#停止方法
stop(){
  #is_exist
  pidf=$(cat $PID)
  #echo "$pidf"
  echo ">>> api PID = $pidf begin kill $pidf ..."
  kill $pidf
  rm -rf $PID
  sleep 2
  is_exist
  if [ $? -eq "0" ]; then
    echo ">>> api 2 PID = $pid begin kill -9 $pid  ..."
    kill -9  $pid
    sleep 2
    echo ">>> $RUN_NAME process stopped"
  else
    echo ">>> ${RUN_NAME} is not running"
  fi
}

#输出运行状态
status(){
  is_exist
  if [ $? -eq "0" ]; then
    echo ">>> ${RUN_NAME} is running PID is ${pid}"
  else
    echo ">>> ${RUN_NAME} is not running"
  fi
}

#重启
restart(){
  stop
  start
}

#根据输入参数，选择执行对应方法，不输入则执行使用说明
case "$1" in
  "start")
    start
    ;;
  "stop")
    stop
    ;;
  "status")
    status
    ;;
  "restart")
    restart
    ;;
  *)
    usage
    ;;
esac
exit 0