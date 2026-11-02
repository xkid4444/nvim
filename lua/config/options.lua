-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here

-- add yank to clipboard
vim.opt.clipboard = "unnamedplus"
vim.opt.swapfile = false

-- fold options
vim.opt.foldmethod = "expr"
vim.opt.foldexpr = "v:lua.vim.treesitter.foldexpr()"

-- set nowrap
vim.opt.wrap = true

-- auto resizing
vim.o.equalalways = false

-- autoread changes
vim.opt.autoread = true

-- disable animations
vim.g.snacks_animate = false


-- add log type to be recognised
vim.filetype.add({
  extension = {
    log = "log",
  },
})
