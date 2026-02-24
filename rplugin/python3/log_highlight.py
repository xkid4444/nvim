import pynvim


@pynvim.plugin
class LogHighlighter(object):
    def __init__(self, nvim):
        self.nvim = nvim

    def setup_highlights(self):
        # Using a dictionary to manage your theme
        theme = {
            "logError": {"fg": "#FF0000", "bold": True, "underline": True},
            "logFail": {"fg": "#FF0000", "bold": True},
            "logWarn": {"fg": "#FFA500"},
            "logPass": {"fg": "#22FF22"},
            "logInfo": {"fg": "#00FFFF"},
            "logDate": {"fg": "#8093C4"},
            "logDebug": {"fg": "#FFFF00", "italic": True},
            ## SVT specific
            "logCommandPrefix": {"fg": "#FFAFFF"},
            "logCommand": {"fg": "#FFC500"},
            "logComment": {"fg": "#928374"},
            "logLowExeTime": {"fg": "#22FF22"},
            "logMidExeTime": {"fg": "#FFFF00"},
            "logBigExeTime": {"fg": "#FF5C00"},
        }

        for name, opts in theme.items():
            self.nvim.api.set_hl(0, name, opts)

    @pynvim.autocmd("BufReadPost,BufEnter", pattern="*.log", sync=True)
    def apply_highlights(self):
        self.setup_highlights()

        self.nvim.command(r"syntax match logComment /#.*/")
        self.nvim.command(
            r"syntax match logDate /\v\[\d+:\d{2}:\d{2}\.\d{3}\s(TD|S1)\]/"
        )
        self.nvim.command(r"syntax match logCommandPrefix /\v[A-Z][\<\>]/")
        self.nvim.command(
            r"syntax match logCommand /\v<(SEND|POLL|RECV|VM|RM|VBS|WBS)>/"
        )

        self.nvim.command(
            r"syntax match logLowExeTime /\v\d{1,2}ms/ containedin=logComment"
        )
        self.nvim.command(
            r"syntax match logMidExeTime /\v\d{3,4}ms/ containedin=logComment"
        )
        self.nvim.command(
            r"syntax match logBigExeTime /\v\d{5,8}ms/ containedin=logComment"
        )

        self.nvim.command(
            r"syntax match logDebug /\v\c\bDEBUG\b/ containedin=logComment"
        )
        self.nvim.command(r"syntax match logInfo /\v\c\bINFO\b/ containedin=logComment")
        self.nvim.command(r"syntax match logPass / S\_s*$/ containedin=logComment")
        self.nvim.command(r"syntax match logWarn /\v\c\bWARN\b/ containedin=logComment")
        self.nvim.command(r"syntax match logFail / F\_s*$/ containedin=logComment")
        self.nvim.command(
            r"syntax match logError /\v\c\bERROR\b/ containedin=logComment"
        )


## End of file
