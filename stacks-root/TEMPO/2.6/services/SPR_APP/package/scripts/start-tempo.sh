export TEMPO_HOME="$(cd "`dirname "$0"`"/..; pwd)"
$TEMPO_HOME/bin/daemon.sh start  $TEMPO_HOME/lib/tempo.jar --server.port=$1
