-- Autocmds are automatically loaded on the VeryLazy event
-- Default autocmds that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/autocmds.lua
--
-- Add any additional autocmds here
-- with `vim.api.nvim_create_autocmd`
--
-- Or remove existing autocmds by their group name (which is prefixed with `lazyvim_` for the defaults)
-- e.g. vim.api.nvim_del_augroup_by_name("lazyvim_wrap_spell")

-- turn off spelling checks for txt & log files
vim.api.nvim_create_autocmd({ "BufRead", "BufNewFile" }, {
  pattern = { "*.txt", "*.log" },
  command = "setlocal nospell",
})

-- log tree-sitter
vim.api.nvim_create_autocmd("User", {
  pattern = "TSUpdate",
  callback = function()
    require("nvim-treesitter.parsers").log = {
      install_info = {
        -- change path as need (try to use full paths)
        path = "~/parsers/tree-sitter-log",
        -- optional entries
        location = "parser",
        generate = true,
        generate_from_json = false,
        -- queries = "queries/neovim", -- symlink queries from given directory
      },
    }
  end,
})
