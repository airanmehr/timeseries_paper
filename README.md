# Time-Serie Paper
Guidelines

1.Use `TexStudio`.

2.Go to `Configure TexStudio>Adv Editor>Line Wrapping` then select `Hard` with max of 80 characters, and make sure every line is less than 80 chrs.

3.Create a macro for push and set the trigger to `?close-file`
```
dialog = new UniversalInputDialog()
dialog.setWindowTitle("Git commit")
dialog.add("", "Comment", "comment")
if (dialog.exec() != null) {
    comment = dialog.get("comment")
    buildManager.runCommand("git commit -a -m \"" + comment + "\"", editor.fileName())
    buildManager.runCommand("git push origin master", editor.fileName())
    }
```
you can run it from menu bar.

