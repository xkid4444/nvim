import pynvim


@pynvim.plugin
class LogFiles(object):
    def __init__(self, nvim: pynvim.Nvim):
        self.nvim = nvim
        self.step = 0
        self.step_lines = {}

        self.window_handler = None
        self.buffer_handler = None

    def get_steps(self):
        """
        Get current step number

        :param self: Description
        """
        self.step_lines = {}
        all_lines = self.nvim.current.buffer[:]
        for ii, line in enumerate(all_lines):
            if line.startswith("#Test") and "- Start" in line:
                self.step_lines[ii] = line

    @pynvim.autocmd("BufEnter", pattern="*", eval="expand('<afile>')", sync=True)
    def display_step(self, filename):
        if self.window_handler is not None:
            try:
                self.nvim.api.win_close(self.window_handler, True)
            except Exception:
                pass
            self.window_handler = None
        if self.buffer_handler is not None:
            self.buffer_handler = None

        if filename.endswith(".log") or filename.endswith(".txt"):
            self.get_steps()
            self.buffer_handler = self.nvim.api.create_buf(False, True)

            line_num = self.nvim.current.window.cursor[0]
            step_line = ""

            for key, val in self.step_lines.items():
                if key > line_num:
                    break
                step_line = val

            self.nvim.api.buf_set_lines(self.buffer_handler, 0, 1, True, [step_line])

            opts = {
                "relative": "win",
                "win": self.nvim.current.window.handle,
                "width": len(step_line) if len(step_line) else 35,
                "height": 1,
                "col": 0,
                "row": 1,
                "anchor": "NW",
                "style": "minimal",
                # "border": ["╔", "═", "╗", "║", "╝", "═", "╚", "║"],
                "focusable": False,
            }

            self.window_handler = self.nvim.api.open_win(
                self.buffer_handler, False, opts
            )

            self.nvim.api.win_set_option(self.window_handler, "winblend", 15)

            self.nvim.api.set_option_value(
                "winhighlight", "Normal:NormalFloat", {"win": self.window_handler}
            )

    @pynvim.autocmd("CursorMoved", sync=False)
    def update_display_step(self):
        if self.buffer_handler is not None:
            line_num = self.nvim.current.window.cursor[0]
            step_line = ""

            for key, val in self.step_lines.items():
                if key > line_num:
                    break
                step_line = val

            self.nvim.api.buf_set_lines(self.buffer_handler, 0, 1, True, [step_line])


# End of file
