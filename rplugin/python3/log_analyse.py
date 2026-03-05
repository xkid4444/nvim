import os
import csv
import pynvim
import threading

from difflib import SequenceMatcher
from AutoLogAnalysis.tools.BlockParser import BlockParser
from AutoLogAnalysis.JiraManager import JiraManager


@pynvim.plugin
class LogFiles(object):
    def __init__(self, nvim: pynvim.Nvim):
        self.nvim = nvim
        self.tcid = 0
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

            if self.buffer_handler:
                self.nvim.api.buf_set_lines(
                    self.buffer_handler, 0, 1, True, [step_line]
                )

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

    def _check_db(self):
        file_path = self.nvim.current.buffer.name
        bug_path = r"C:/Users/ben.lee/Desktop/code/AutoLogAnalysis/data/bugs"

        csv_list = []
        all_list = [
            os.path.join(bug_path, r"03/Bugs.csv"),
            os.path.join(bug_path, r"04/Bugs.csv"),
            os.path.join(bug_path, r"06/Bugs.csv"),
            os.path.join(bug_path, r"08/Bugs.csv"),
            os.path.join(bug_path, r"09/Bugs.csv"),
            os.path.join(bug_path, r"10/Bugs.csv"),
            os.path.join(bug_path, r"13/Bugs.csv"),
            os.path.join(bug_path, r"14/Bugs.csv"),
            os.path.join(bug_path, r"16/Bugs.csv"),
            os.path.join(bug_path, r"17/Bugs.csv"),
            os.path.join(bug_path, r"18/Bugs.csv"),
        ]
        if "HROCM-03" in file_path:
            csv_list.append(all_list[0])
        if "HROCM-04" in file_path:
            csv_list.append(all_list[1])
        if "flex-06" in file_path:
            csv_list.append(all_list[2])
        if "flex-08" in file_path:
            csv_list.append(all_list[3])
        if "flex-09" in file_path:
            csv_list.append(all_list[4])
        if "flex-10" in file_path:
            csv_list.append(all_list[5])
        if "flex-13" in file_path:
            csv_list.append(all_list[6])
        if "flex-14" in file_path or "flex-114" in file_path:
            csv_list.append(all_list[7])
        if "flex-16" in file_path:
            csv_list.append(all_list[8])
        if "flex-17" in file_path:
            csv_list.append(all_list[9])
        if "flex-18" in file_path:
            csv_list.append(all_list[10])

        if len(csv_list) == 0:
            csv_list = all_list

        bug_list = []

        for csv_file in csv_list:
            file = open(csv_file)

            for line in csv.reader(file):
                if line[0] == "BugID":
                    continue

                bug_list.append(line)

            file.close()

        return bug_list

    @pynvim.autocmd("CursorMoved", sync=False)
    def update_display_step(self):
        if self.buffer_handler is not None:
            line_num = self.nvim.current.window.cursor[0]
            step_line = ""
            for key, val in self.step_lines.items():
                if key > line_num:
                    break
                step_line = val

            split_line = step_line.split()

            if len(split_line) == 8:
                try:
                    self.tcid = int(split_line[2])
                except Exception as e:
                    pass

                try:
                    self.step = int(split_line[5])
                except Exception as e:
                    pass

            self.nvim.api.buf_set_lines(self.buffer_handler, 0, 1, True, [step_line])

    @pynvim.command(name="Logbugs", nargs="*", range="", sync=False, allow_nested=True)
    def bug_manager(self, args, range):
        # bm = BugManager(username="ben.lee")
        # bm.GetReleaseNotes()
        # bm.CollectAllBugs()

        info_msg = "Calling pest control...\\n"

        jm = JiraManager(username="ben.lee")
        proj_list = ["GEM", "OOZ"]
        for p in proj_list:
            info_msg += f"    Looking for {p}   󰃤  󰨰\\n"
            jm_thread = threading.Thread(
                target=jm.SearchProject, args=(p,), daemon=True
            )
            jm_thread.start()
            # jm_thread.join(timeout=60) ## blocking

        cmd_msg = 'lua print("' + info_msg + '")'
        self.nvim.command(cmd_msg)

    @pynvim.command(name="Loga", nargs="*", range="", sync=False)
    def analyse_block(self, args, range):
        start, end = range

        if start == end:
            start -= 30
            end += 30

        lines = self.nvim.current.buffer.api.get_lines(start - 1, end, False)
        block = "\n".join(lines)
        # self.nvim.command(f'lua print("DEBUG: lines: {lines}")', async_=True)

        bp = BlockParser()
        parsed = bp.ParseBlock(block=block)
        if len(parsed) == 0:
            self.nvim.command(f'lua print("ERROR: empty parsed block: {parsed}")')
            return
        elif len(parsed[0]) == 0:
            self.nvim.command(f'lua print("ERROR: empty parsed[0] block: {parsed}")')
            return
        else:
            parsed = parsed[0]

        # self.nvim.command(f'lua print("DEBUG: parsed: {parsed}")')

        bug_list = self._check_db()
        # self.nvim.command(f'lua print("DEBUG: bug_list: {bug_list}")')

        if len(bug_list) == 0:
            self.nvim.command(f'lua print("ERROR: empty bug_list: {bug_list}")')
            return

        match_str = f"\\nTC_{self.tcid} - Step {self.step}\\n"
        match_tracker = {}
        for bug in bug_list:
            match_ratio = 0
            worth_checking = False

            """ check tc_id """
            if self.tcid == bug[1]:
                match_ratio += 10
                """ check step num """
                if self.step == bug[2]:
                    match_ratio += 10
                    worth_checking = True  # if same TC & Step failed, worth checking

            """ check failed commands """
            sm = SequenceMatcher(None, parsed[0], bug[3])
            cmd_ratio = sm.ratio()
            match_ratio += cmd_ratio * 40

            """ if failed command ratio < 70%  continue """
            if cmd_ratio < 0.4 and worth_checking is False:
                continue

            """ check failed seq match """
            sm = SequenceMatcher(None, parsed[1], bug[4])
            seq_ratio = sm.ratio()
            match_ratio += seq_ratio * 40

            if match_ratio > 50 or worth_checking:
                if match_tracker.get(bug[0]):
                    if match_ratio > match_tracker[bug[0]]:
                        match_tracker.update({bug[0]: match_ratio})
                else:
                    match_tracker.update({bug[0]: match_ratio})
        if len(match_tracker) > 0:
            match_tracker_sorted = dict(
                sorted(match_tracker.items(), key=lambda item: item[1], reverse=True)
            )
            for bugid, match in match_tracker_sorted.items():
                match_str += (
                    "   Matched: http://jira:8080/browse/"
                    + bugid
                    + f" at {match:.2f}%\\n"
                )
        else:
            match_str += "   unknown"

        cmd_msg = 'lua print("' + match_str + '")'
        self.nvim.command(cmd_msg)


# End of file
