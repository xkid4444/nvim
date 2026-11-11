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
      -- markdown = { "prettier" },
      -- graphql = { "prettier" },
      lua = { "stylua" },
      python = { "isort", "black" },
    },
    default_format_opts = {
      timeout_ms = 1000,
      async = false,
      quiet = false,
      lsp_format = "fallback",
    },
    formatters = {
      prettier = {
        extra_args = { "--prose-wrap", "preserve", "--print-width", "80" },
      },
    },
  },
}
