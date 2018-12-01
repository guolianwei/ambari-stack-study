usage="Usage: daemon.sh (start|stop) jar_file_path port"
usagestop="Usage: deameon.sh (start|stop)"
sbin="`dirname "$0"`"
sbin="`cd "$sbin"; pwd`"
if [ "$XTKKX_ENETPCL_PID_DIR" = "" ]; then
  MERIT_DATA_CLOUD_ANALYSE_PID_DIR=/tmp
fi
if [ "$MERIT_DATA_CLOUD_ANALYSE_IDENT_STRING" = "" ]; then
  export MERIT_DATA_CLOUD_ANALYSE_IDENT_STRING="$USER"
fi

export HNAME_MERITDATA="$HOSTNAME"

#get log directory
if [ "$MERIT_DATA_CLOUD_ANALYSE_LOG_DIR" = "" ]; then
  export MERIT_DATA_CLOUD_ANALYSE_LOG_DIR="$sbin/mock-logs"
fi
export _XTKKX_ENETPCL_DAEMON_OUT=$MERIT_DATA_CLOUD_ANALYSE_LOG_DIR/mock-$MERIT_DATA_CLOUD_ANALYSE_IDENT_STRING-$HNAME_MERITDATA.log
export _MERIT_DATA_CLOUD_ANALYSE_DAEMON_PIDFILE=$MERIT_DATA_CLOUD_ANALYSE_PID_DIR/mock-$MERIT_DATA_CLOUD_ANALYSE_IDENT_STRING.pid
echo log file is : $_XTKKX_ENETPCL_DAEMON_OUT
# if no args specified, show usage
startStop=$1
if [ $# -lt 3 ]  &&  [ $startStop == "start" ]; then
  echo $usage
  exit 1
elif [ $# -lt 1 ]; then
  echo $usagestop 
fi

# get arguments
case $startStop in
  (start)
    mkdir -p "$MERIT_DATA_CLOUD_ANALYSE_PID_DIR"
    mkdir -p "$MERIT_DATA_CLOUD_ANALYSE_LOG_DIR"
    if [ -f $_MERIT_DATA_CLOUD_ANALYSE_DAEMON_PIDFILE ]; then
      if kill -0 `cat $_MERIT_DATA_CLOUD_ANALYSE_DAEMON_PIDFILE` > /dev/null 2>&1; then
        echo mock running as process `cat $_MERIT_DATA_CLOUD_ANALYSE_DAEMON_PIDFILE`.  Stop it first.
        exit 1
      fi
    fi
    echo starting
    nohup $JAVA_HOME/bin/java -jar $2 $3 >> $_XTKKX_ENETPCL_DAEMON_OUT 2>&1  &
    echo $! > $_MERIT_DATA_CLOUD_ANALYSE_DAEMON_PIDFILE
    echo mock started log writed to $_XTKKX_ENETPCL_DAEMON_OUT
   ;;
  (stop)
    if [ -f $_MERIT_DATA_CLOUD_ANALYSE_DAEMON_PIDFILE ]; then
      if kill -0 `cat $_MERIT_DATA_CLOUD_ANALYSE_DAEMON_PIDFILE` > /dev/null 2>&1; then
        echo stopping jobserver
        kill `cat $_MERIT_DATA_CLOUD_ANALYSE_DAEMON_PIDFILE`
      else
        echo no mock to stop
      fi
    else
      echo no mock to stop
    fi
  ;;
  (*)
    echo $usage
    exit 1
    ;;

esac
