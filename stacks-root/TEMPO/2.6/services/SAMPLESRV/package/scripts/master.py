import sys
import xml.sax
import pwd
import os
import getpass
from resource_management import *
from resource_management.core.logger import Logger
from resource_management.core.resources.system import Execute
from resource_management.core.exceptions import ComponentIsNotRunning, Fail
status_cmd = "pgrep -f 'tempo.jar'"
class Master(Script):
  def install(self, env):
    import status_params
    env.set_params(status_params)
    test_varembace=status_params.test_varembace;
    print "test_varembace"+test_varembace
    config = self.get_config();
    jdk_location=config['ambariLevelParams']['jdk_location']
    Logger.info("Tempo: geted jdk_location"+jdk_location)
    java64_home = config['ambariLevelParams']['java_home']
    java_exec = format("{java64_home}/bin/java")
    java_version = expect("/ambariLevelParams/java_version", int)
    pid_file = format("{test_varembace}/gmetad.pid")
    print pid_file
    Logger.info("geted test_varembrace"+pid_file)
    print 'Install the Sample Srv Master'
    self.install_packages(env)
  def stop(self, env):
    print 'Stop the Sample Srv Master';
    Logger.info("Stop the Sample Srv Master")
    cmd = ('/opt/tempo/bin/stop-tempo.sh')
    Logger.info("status_cmd is "+status_cmd)
    Execute(cmd,
            logoutput = True,
            only_if = status_cmd,
            sudo = False,
    )
  def start(self, env):
    print 'Start the Sample Srv Master';
    Logger.info("Start the Sample Srv Master")
    user_name= getpass.getuser()
    Logger.info("Current System user:" + user_name)
    javaEnv=self.getJavaEen()
    cmd = ('/opt/tempo/bin/start-tempo.sh', '8081',javaEnv[0])
    Execute(cmd,
            logoutput = True,
            not_if = status_cmd,
            sudo = False,
    )
  def status(self, env):
    try:
      Execute(status_cmd)
    except Fail:
      raise ComponentIsNotRunning()
  def configure(self, env):
    Logger.info("Status of the Sample Srv Master")
    print 'Configure the Sample Srv Master';
  def getJavaEen(self):
    config = self.get_config()
    jdk_location=config['ambariLevelParams']['jdk_location']
    Logger.info("Tempo: geted jdk_location:" + jdk_location)
    java64_home = config['ambariLevelParams']['java_home']
    java_exec = format("{java64_home}/bin/java")
    #java_version = expect("/ambariLevelParams/java_version", int)
    Logger.info("geted test_varembrace"+java64_home+" :: "+java_exec)
    return (java64_home,java_exec)
  
if __name__ == "__main__":
  Master().execute()
