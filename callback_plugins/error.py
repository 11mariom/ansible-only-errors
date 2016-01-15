# 2016, Mariusz 'mariom' Kozakowski

from ansible.plugins.callback.default import CallbackModule as CallbackModule_default
from ansible.utils.color import colorize, hostcolor

class CallbackModule(CallbackModule_default):

    '''
    This callback prints only error and unreachable
    '''

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'error'

    def v2_runner_on_ok(self, result):
        pass

    def v2_runner_on_skipped(self, result):
        pass
    
    def v2_playbook_item_on_skipped(self, result):
        pass

    def v2_playbook_on_stats(self, stats):

        hosts = sorted(stats.processed.keys())
        for h in hosts:
            t = stats.summarize(h)

            if t['unreachable'] > 0 or t['failures'] > 0:
                self._display.banner("PLAY RECAP")
                
                self._display.display(u"%s : %s %s %s %s" % (
                    hostcolor(h, t, False),
                    colorize(u'ok', t['ok'], None),
                    colorize(u'changed', t['changed'], None),
                    colorize(u'unreachable', t['unreachable'], None),
                    colorize(u'failed', t['failures'], None)),
                    screen_only=True
                )

                self._display.display("", screen_only=True)
    
