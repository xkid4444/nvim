# 💤 LazyVim

## Installation

1. Download and install [Neovim](https://github.com/neovim/neovim)
```bash
git clone https://github.com/neovim/neovim.git

## currently latest release is 0.12
git checkout release-0.12
make CMAKE_BUILD_TYPE=RelWithDebInfo
sudo make install
```

2. Download and install starter template for [LazyVim](https://github.com/LazyVim/LazyVim). Refer to the [documentation](https://lazyvim.github.io/installation) to get started.
```bash
git clone https://github.com/LazyVim/starter ~/.config/nvim
```

3. Download this repo and replace neovim configs with this repository
```bash
mv ~/.config/nvim{,.bak}
git clone git@github.com:neovim/neovim.git ~/.config/nvim
```

----

## Usage

### Blink

Completion suggestion from multiple sources like LSP, buffer, snippet...
Disabled for `.log, .txt` files.

### Colors

Two color schemes I found very useful is `navarasu/onedark.nvim` and `scottmckendry/cyberdream.nvim`.
Cyberdream was edited for python for `@variable.member.python` and `@constant.python` to reduce constant white color for variables and constants.

### Conform

Confirm contains formatters by filetype.
For python, recommend installing isort for system or at least in virtual environment. 

### Flogg

Similar to klogg but a plugin for neovim and not as fast for large files.
`:Flogg` to run flogg or default keymapping is `<leader>bf` and to switch source buffer use `<leader>bs`.

### Log

Log is for custom highlights for files with `.log` extension.

### Mini icons

Attach a custom nerd front character to a filetype.

### Mini pairs

Better way to configure pairs like `()`, `{}`, `[]`, `""`, `''`

### Multicursor

Create multiple cursors to format text across lines and columns.
Custom mapped to different keybindings:
- Add cursor `<C-d>` (vscode equivalent)
- Skip cursor `<C-e>` (probably NOT vscode equivalent)
- Add cursor to all matching `<C-a>` word
- Selectively add or remove cursor `<C-leftmouse>`

### Neogit

To better manage git.
`:Neogit` to open neogit or default mapped to `<leader>gg`.

### Nvim lint

To check formats and styles or to disable linters. 

### Render markdown

Using mini.icons customise markdown views.

### Snacks

Collection of quality of life plugins for neovim.
Customised startup page.

### Treesitter

Added `.log` syntax and max_filesize to <= 200MB.



