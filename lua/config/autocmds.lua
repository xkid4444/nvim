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
        path = "C:/Users/ben.lee/AppData/Local/nvim/tree-sitter-log",
        url = "",
        -- optional entries
        -- location = "parser",
        generate = true,
        -- generate_from_json = true,
        queries = "queries", -- symlink queries from given directory
      },
      filetype = "log",
    }
  end,
})

vim.api.nvim_create_autocmd("User", {
  pattern = "TSUpdate",
  callback = function()
    require("nvim-treesitter.config").setup({
      ensure_installed = { "lua", "vim", "query", "markdown", "markdown_inline", "log" },
      highlight = { enable = true },
      textobjects = {
        move = {
          enable = true,
          set_jumps = true,
          goto_next_start = {
            ["]f"] = "@function.outer",
          },
          goto_previous_start = {
            ["[f"] = "@function.outer",
          },
        },
      },
    })
  end,
})

vim.api.nvim_create_autocmd("User", {
  pattern = "MoltenInitPost",
  callback = function()
    vim.api.nvim_set_hl(0, "MoltenVirtualText", { fg = "#FFFF44", bg = "#222222", sp = "#FF0000", italic = true })
  end,
})
