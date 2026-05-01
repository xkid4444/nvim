-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

-- vim.keymap.set({mode}, {lhs}, {rhs}, {opts})
-- mode: String or table (e.g., 'n' for Normal, 'i' for Insert, 'v' for Visual, { 'n', 'v' } for both).
-- lhs: The key sequence you want to trigger (e.g., <leader>ff).
-- rhs: The command, function, or mapping to execute.
-- opts: A table with options like silent = true (don't show command in command line) or noremap = true

-- ## select all
-- vim.keymap.set("n", "<C-a>", "gg<S-v>G")

-- ## next buffer
vim.keymap.set("n", "<Tab>", ":BufferLineCycleNext<CR>", { noremap = true, silent = true, desc = "Next Tab" })
-- ## prev buffer
vim.keymap.set("n", "<S-Tab>", ":BufferLineCyclePrev<CR>", { noremap = true, silent = true, desc = "Prev Tab" })

-- ## move buffer next
vim.keymap.set("n", "<A-]>", ":BufferLineMoveNext<CR>", { noremap = true, silent = true, desc = "Move tab next" })
-- ## move buffer back
vim.keymap.set("n", "<A-[>", ":BufferLineMovePrev<CR>", { noremap = true, silent = true, desc = "Move tab back" })

-- ## molten keys
vim.keymap.set("n", "<leader>mi", ":MoltenInit<CR>", { silent = true, desc = "Initialize the plugin" })
vim.keymap.set("n", "<leader>md", ":MoltenDeinit<CR>", { silent = true, desc = "De-initialize the plugin" })
vim.keymap.set("n", "<leader>me", ":MoltenEvaluateOperator<CR>", { silent = true, desc = "run operator selection" })
vim.keymap.set("n", "<leader>ml", ":MoltenEvaluateLine<CR>", { silent = true, desc = "evaluate line" })
vim.keymap.set("n", "<leader>mr", ":MoltenReevaluateCell<CR>", { silent = true, desc = "re-evaluate cell" })
vim.keymap.set("n", "<leader>mc", ":MoltenInterrupt<CR>", { silent = true, desc = "Interrupt kernel" })
vim.keymap.set("n", "<leader>m]", ":MoltenNext<CR>", { silent = true, desc = "goto next" })
vim.keymap.set("n", "<leader>m[", ":MoltenPrev<CR>", { silent = true, desc = "goto previous" })
vim.keymap.set(
  "v",
  "<leader>mv",
  ":<C-u>MoltenEvaluateVisual<CR>gv",
  { silent = true, desc = "evaluate visual selection" }
)
vim.keymap.set("n", "<leader>mo", ":noautocmd MoltenEnterOutput<CR>", {
  silent = true,
  desc = "Enter molten output",
})
