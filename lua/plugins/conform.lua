return {
  "stevearc/conform.nvim",
  optional = true,
  opts = {
    formatters_by_ft = {
      javascript = { "prettier" },
      typescript = { "prettier" },
      -- javascriptreact = { "prettier" },
      -- typescriptreact = { "prettier" },
      -- svelte = { "prettier" },
      css = { "prettier" },
      html = { "prettier" },
      json = { "prettier" },
      yaml = { "prettier" },
      markdown = { "prettier" },
      -- graphql = { "prettier" },
      lua = { "stylua" },
      python = { "isort", "black" },
    },
    default_format_opts = {
      timeout_ms = 5000,
      async = false,
      quiet = false,
      lsp_format = "fallback",
    },
  },

  -- "neovim/nvim-lspconfig",
  -- opts = {
  --   servers = {
  --     ruff_lsp = {
  --       mason = false,
  --       -- You might also want to set autostart to false if it's still being initialized
  --       -- autostart = false,
  --     },
  --   },
  -- },

  -- event = { "BufReadPre", "BufNewFile" },
}
