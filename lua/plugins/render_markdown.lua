return {
  {
    "MeanderingProgrammer/render-markdown.nvim",
    enabled = true,
    render_modes = { "n", "c", "i" },
    -- dependencies = { "nvim-treesitter/nvim-treesitter", "nvim-mini/mini.nvim" }, -- if you use the mini.nvim suite
    dependencies = { "nvim-treesitter/nvim-treesitter", "nvim-mini/mini.icons" }, -- if you use standalone mini plugins
    -- dependencies = { 'nvim-treesitter/nvim-treesitter', 'nvim-tree/nvim-web-devicons' }, -- if you prefer nvim-web-devicons
    ---@module 'render-markdown'
    ---@type render.md.UserConfig
    opts = {
      heading = {
        -- enabled = true,
        backgrounds = {},
      },
      checkbox = {
        enabled = true,
        render_modes = false,
        bullet = false,
        left_pad = 0,
        right_pad = 1,
        unchecked = {
            icon = '󰄱 ',
            highlight = 'RenderMarkdownUnchecked',
            scope_highlight = nil,
        },
        checked = {
            icon = ' ',
            highlight = 'RenderMarkdownChecked',
            scope_highlight = nil,
        },
        custom = {
            todo = { raw = '[-]', rendered = '󰥔 ', highlight = 'RenderMarkdownTodo', scope_highlight = nil },
            warn = { raw = '[!]', rendered = ' ', highlight = 'RenderMarkdownWarn', scope_highlight = nil },
            dead = { raw = '[/]', rendered = '󰜺 ', highlight = 'RenderMarkdownError', scope_highlight = nil },
            select = { raw = '[#]', rendered = '󰡖 ', highlight = 'RenderMarkdownTodo', scope_highlight = nil },
        },
        scope_priority = nil,
      }
    },
  },
}
