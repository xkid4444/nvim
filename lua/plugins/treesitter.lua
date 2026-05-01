return {
  {
    "nvim-treesitter/nvim-treesitter-context",
    opts = {
      ensure_installed = {
        "bash",
        "html",
        "javascript",
        "json",
        "lua",
        "markdown",
        "markdown_inline",
        "python",
        "query",
        "regex",
        "tsx",
        "typescript",
        "vim",
        "yaml",
      },
      enable = true,
      max_lines = 5,
      multiline_threshold = 10,
      line_numbers = true,
    },
    highlight = {
      enable = true,
      -- Disable for files larger than 100 KB
      disable = function(lang, buf)
        local max_filesize = 80 * 1024 * 1024 -- 80 MB
        local ok, stats = pcall(vim.loop.fs_stat, vim.api.nvim_buf_get_name(buf))
        if ok and stats and stats.size > max_filesize then
          return true
        end
      end,
    },
  },
}
