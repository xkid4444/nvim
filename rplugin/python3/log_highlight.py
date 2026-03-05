import pynvim


@pynvim.plugin
class LogHighlighter(object):
    def __init__(self, nvim):
        self.nvim = nvim

    # @pynvim.autocmd("BufRead,BufEnter", pattern="*.txt,*.log", sync=True)
    def log_highlights(self):
        self.nvim.api.set_hl(0, "@timeDef", {"fg": "#FF0000", "italic": True})
        theme = {
            # "logError": {"fg": "#FF0000", "bold": True, "underline": True},
            "@failureType": {"fg": "#FF0000", "bold": True},
            # "logWarn": {"fg": "#FFA500"},
            "@successType": {"fg": "#22FF22"},
            # "logInfo": {"fg": "#00FFFF"},
            "@timeDef": {"fg": "#444474"},
            # "logDebug": {"fg": "#FFFF00", "italic": True},
            ## SVT specific
            "@commandPrefix": {"fg": "#FFD0FF"},
            "@commandDef": {"fg": "#FFC500"},
            "@cmtDef": {"fg": "#928374"},
            "@stepStart": {"fg": "#FF44FF"},
            "@stepEnd": {"fg": "#FF44FF"},
            # "logHex": {"fg": "#AFFF0F"},
            # "logBitstr": {"fg": "#FF0FAF"},
            # "logInt": {"fg": "#0FAFFF"},
            "@intd2Type": {"fg": "#00FF00"},
            "@intd4Type": {"fg": "#FFFF00"},
            "@intdxType": {"fg": "#FF5C00"},
        }

        for name, opts in theme.items():
            self.nvim.api.set_hl(0, name, opts)

    def setup_highlights(self):
        # Using a dictionary to manage your theme
        theme = {
            "logError": {"fg": "#FF0000", "bold": True, "underline": True},
            "logFail": {"fg": "#FF0000", "bold": True},
            "logWarn": {"fg": "#FFA500"},
            "logPass": {"fg": "#22FF22"},
            "logInfo": {"fg": "#00FFFF"},
            "logDate": {"fg": "#444474"},
            "logDebug": {"fg": "#FFFF00", "italic": True},
            ## SVT specific
            "logCommandPrefix": {"fg": "#FFD0FF"},
            "logCommand": {"fg": "#FFC500"},
            "logComment": {"fg": "#928374"},
            "logSteps": {"fg": "#FF44FF"},
            "logHex": {"fg": "#AFFF0F"},
            "logBitstr": {"fg": "#FF0FAF"},
            "logInt": {"fg": "#0FAFFF"},
            "logLowExeTime": {"fg": "#00FF00"},
            "logMidExeTime": {"fg": "#FFFF00"},
            "logBigExeTime": {"fg": "#FF5C00"},
        }

        for name, opts in theme.items():
            self.nvim.api.set_hl(0, name, opts)

    @pynvim.autocmd("BufRead,BufEnter", pattern="*.txt,*.log", sync=True)
    def apply_highlights(self):
        self.setup_highlights()

        self.nvim.command(r"syntax match logComment /#.*/")
        self.nvim.command(
            r"syntax match logSteps /\v#Test\sID\s[0-9]{3,5}\s-\sStep\s[0-9]{1,10}\s-\s(Start|End)/"
        )
        self.nvim.command(
            r"syntax match logDate /\v\[\d+:\d{2}:\d{2}\.\d{3}\s(TD|S1)\]/"
        )

        self.nvim.command(r"syntax match logInt /\v<\d+>/")
        self.nvim.command(r"syntax match logBitstr /\v<[x01]{8,}>/")
        self.nvim.command(r"syntax match logHex /\v<0x[0-9A-Za-z]{1,}>/")

        # gpio_cmd = "MR|PR|RD|AL|WE|WDERR|SPI_ER|SPI_RD|SPI_DN|SSS|"
        # commands = "SEND|POLL|RECV|VM|RM|VBS|WBS|FLUSH|SPICFG|SLEEP|WGPIO|WBSI|NEWBFR|WBFR|SENDX|COPYF2X"
        # self.nvim.command(r"syntax match logCommand /\v[A-Z][\<\>][0-9A-Z]{2,}/")
        self.nvim.command(r"syntax match logCommandPrefix /\v[A-Z][\<\>]/")

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
