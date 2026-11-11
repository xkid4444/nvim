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
        "cpp",
        "markdown",
        "markdown_inline",
        "rust",
        "ron",
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
      -- Disable for files larger than 200 MB
      disable = function(lang, buf)
        local max_filesize = 200 * 1024 * 1024 -- 200 MB
        local ok, stats = pcall(vim.loop.fs_stat, vim.api.nvim_buf_get_name(buf))
        if ok and stats and stats.size > max_filesize then
          return true
        else
          return "log"
        end
      end,
    },
  },
}
