#!/usr/bin/python3

from ansible.module_utils.basic import AnsibleModule

def can_reach(module, host, port, timeout):
    nc_path = module.get_bin_path('nc', required=True)
    args = [nc_path, '-z', '-w', str(timeout), host, str(port)]
    (rc, stdout, stderr) = module.run_command(args)
    return rc == 0

def main():
    module = AnsibleModule( 
        argument_spec=dict(
            host=dict(required=True), 
            port=dict(required=True, type='int'),
            timeout=dict(required=False, type='int', default=3) 
        ),
        supports_check_mode=True 
    )
    if module.check_mode: 
        module.exit_json(changed=False) 
    host = module.params['host']
    port = module.params['port']
    timeout = module.params['timeout']
    
    if can_reach(module, host, port, timeout):
        module.exit_json(changed=False)
    else:
        msg = "Could not reach %s:%s" % (host, port)
        module.fail_json(msg=msg)

if __name__ == "__main__":
    main()