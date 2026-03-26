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
  },
}
