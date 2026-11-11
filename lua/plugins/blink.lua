return {
  "saghen/blink.cmp",
  opts = {
    sources = {
      -- -- Global default: no buffer source, so logs/random strings won't pollute comments.
      -- default = { "lsp", "path", "snippets" },
      --
      -- -- Filetype overrides.
      -- per_filetype = {
      --   python = { "lsp", "path", "snippets" },
      --
      --   -- Disable completions entirely in noisy filetypes.
      --   log = {},
      --   text = {},
      --   gitcommit = {},
      -- },

      -- dont suggest lines from .log, .text, .gitcommit files
      providers = {
        -- Keep buffer source defined, but disabled for noisy filetypes
        -- in case LazyVim or another plugin re-adds it.
        buffer = {
          enabled = function()
            local ft = vim.bo.filetype
            return not vim.tbl_contains({
              "log",
              "text",
              "gitcommit",
            }, ft)
          end,
          min_keyword_length = 4,
          max_items = 5,
        },

        -- Prevent LSP from falling back to buffer when LSP returns no results.
        lsp = {
          fallbacks = {},
        },
      },
    },

    completion = {
      trigger = {
        prefetch_on_insert = false,
        show_on_insert = false,
      },
    },
  },
}
