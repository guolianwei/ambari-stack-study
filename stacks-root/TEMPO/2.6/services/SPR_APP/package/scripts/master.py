import sys
import xml.sax
from mock_service import mock_service
from resource_management import *
from resource_management.core.logger import Logger
class Master(Script):
  def install(self, env):
    import status_params
    env.set_params(status_params)
    test_varembace=status_params.test_varembace;
    print "test_varembace"+test_varembace
    config = self.get_config();
    jdk_location=config['ambariLevelParams']['jdk_location']
    Logger.info("Tempo: geted jdk_location"+jdk_location)
    pid_file = format("{test_varembace}/gmetad.pid")
    print pid_file
    Logger.info("geted test_varembrace"+pid_file)
    self.install_packages(env)
    print 'Install the Sample Srv Master';
  def stop(self, env):
    print 'Stop the Sample Srv Master';
    Logger.info("Stop the Sample Srv Master")
    mock_service("stop")
  def start(self, env):
    print 'Start the Sample Srv Master';
    Logger.info("Start the Sample Srv Master")
    mock_service("start")
  def status(self, env):
    print 'Status of the Sample Srv Master';
    Logger.info("Status of the Sample Srv Master")
  def configure(self, env):
    Logger.info("Status of the Sample Srv Master")
    print 'Configure the Sample Srv Master';
if __name__ == "__main__":
  Master().execute()
