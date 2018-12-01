#encoding=utf-8
import sys
from resource_management.core.exceptions import ClientComponentHasNoStatus
from resource_management import *
from resource_management.libraries.script.script import Script
from ambari_commons import OSConst
class SampleClient(Script):
  def install(self, env): 
    import status_params
    env.set_params(status_params)
    config = Script.get_config();
    print 'Install the Sample Srv Client';
    pid_dir = config['configurations']['dsd']['some.test.property']
  def configure(self, env):
    print 'Configure the Sample Srv Client';
  def status(self, env):
    raise ClientComponentHasNoStatus()
if __name__ == "__main__":
  SampleClient().execute()
