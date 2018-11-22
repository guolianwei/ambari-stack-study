import sys
import xml.sax
from resource_management import *
from resource_management.core.logger import Logger
class Master(Script):
  def install(self, env):
    import status_params
    env.set_params(status_params)
    test_varembace=status_params.test_varembace;
    print "test_varembace"+test_varembace
    pid_file = format("{test_varembace}/gmetad.pid")
    print pid_file
    Logger.info("geted test_varembrace"+pid_file)
    print 'Install the Sample Srv Master';
  def stop(self, env):
    print 'Stop the Sample Srv Master';
    Logger.info("Stop the Sample Srv Master")
  def start(self, env):
    print 'Start the Sample Srv Master';
    Logger.info("Start the Sample Srv Master")
  def status(self, env):
    print 'Status of the Sample Srv Master';
    Logger.info("Status of the Sample Srv Master")
  def configure(self, env):
    Logger.info("Status of the Sample Srv Master")
    print 'Configure the Sample Srv Master';
if __name__ == "__main__":
  Master().execute()
