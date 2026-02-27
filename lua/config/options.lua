-- Options are automatically loaded before lazy.nvim startup
-- Default options that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/options.lua
-- Add any additional options here

-- add yank to clipboard
vim.opt.clipboard = "unnamedplus"

-- add log type to be recognised
vim.filetype.add({
  extension = {
    log = "log",
  },
})

-- open drag and drop files to edit
vim.paste = (function(overridden)
  return function(lines, phase)
    local files = {}

    -- Identify all valid file paths in the pasted lines
    for _, line in ipairs(lines) do
      local path = line:gsub("^%s*(.-)%s*$", "%1") -- Trim whitespace
      if path ~= "" and vim.fn.filereadable(path) == 1 then
        table.insert(files, path)
      end
    end

    -- If files were found, handle them and intercept the paste
    if #files > 0 then
      for i, path in ipairs(files) do
        vim.cmd("edit " .. vim.fn.fnameescape(path))
      end
      return true -- Signal that the paste was handled
    end

    -- Otherwise, proceed with normal paste behavior
    return overridden(lines, phase)
  end
end)(vim.paste)
